import tkinter as tk
from tkinter import ttk, messagebox
from tkcalendar import DateEntry
import psycopg2
from db import connect_db

def open_new_reservation():
    form = tk.Toplevel()
    form.title("הוספת הזמנה חדשה")
    form.geometry("400x500")

    tk.Label(form, text=":מספר אורח").pack()
    gid_entry = tk.Entry(form)
    gid_entry.pack()

    tk.Label(form, text=":בחר סוג חדר").pack()
    room_type_combo = ttk.Combobox(form, values=["Suite", "Deluxe", "Single", "Double", "Queen", "Family", "Penthouse", "King", "Twin", "Accessible"])
    room_type_combo.pack()

    # מילון להמרת תיאור -> מזהה העדפה
    preference_map = {}

    tk.Label(form, text=":בחר העדפה").pack()
    preferences_combo = ttk.Combobox(form, values=[])
    preferences_combo.pack()

    def load_preferences():
        try:
            conn = connect_db()
            cur = conn.cursor()
            cur.execute("SELECT id, description FROM preference;")
            preferences = cur.fetchall()
            cur.close()
            conn.close()

            # עדכון המילון והקומבובוקס
            for pref_id, desc in preferences:
                preference_map[desc] = pref_id

            preferences_combo['values'] = list(preference_map.keys())
            if preferences:
                preferences_combo.current(0)

        except Exception as e:
            messagebox.showerror("שגיאה", f"שגיאה בטעינת העדפות: {e}")

    load_preferences()

    tk.Label(form, text=":תאריך כניסה").pack()
    checkin_entry = DateEntry(form, date_pattern="yyyy-mm-dd")
    checkin_entry.pack()

    tk.Label(form, text=":תאריך יציאה").pack()
    checkout_entry = DateEntry(form, date_pattern="yyyy-mm-dd")
    checkout_entry.pack()

    tk.Label(form, text=":בחר חדר פנוי").pack()
    available_rooms_combo = ttk.Combobox(form, values=[])
    available_rooms_combo.pack()

    def update_available_rooms():
        room_type = room_type_combo.get()
        check_in = checkin_entry.get()
        check_out = checkout_entry.get()
        if not room_type or not check_in or not check_out:
            messagebox.showwarning("הודעה", "אנא מלא את סוג החדר ואת התאריכים")
            return

        try:
            conn = connect_db()
            cur = conn.cursor()
            cur.execute("BEGIN;")
            cur.execute("SELECT get_available_rooms_by_type(%s, %s, %s);", (room_type, check_in, check_out))
            cursor_name = cur.fetchone()[0]
            cur.execute(f"FETCH ALL FROM {cursor_name};")
            rooms = cur.fetchall()
            cur.execute(f"CLOSE {cursor_name};")
            cur.execute("COMMIT;")
            cur.close()
            conn.close()

            room_numbers = [str(r[0]) for r in rooms]
            available_rooms_combo['values'] = room_numbers

            if not room_numbers:
                messagebox.showinfo("הודעה", "אין חדרים פנויים לטווח זה.")
            else:
                available_rooms_combo.current(0)

        except Exception as e:
            messagebox.showerror("שגיאה", f"שגיאה בשליפת חדרים פנויים: {e}")

    tk.Button(form, text="עדכן רשימת חדרים פנויים", command=update_available_rooms).pack(pady=5)

    def submit_reservation():
        try:
            gid = int(gid_entry.get())
            room = int(available_rooms_combo.get())
            preference_desc = preferences_combo.get()
            preferences = preference_map[preference_desc]
            check_in = checkin_entry.get()
            check_out = checkout_entry.get()

            conn = connect_db()
            cur = conn.cursor()
            cur.execute("CALL add_reservation_with_guest(%s, %s, %s, %s, %s);",
                        (gid, room, preferences, check_in, check_out))
            conn.commit()
            cur.close()
            conn.close()

            messagebox.showinfo("הצלחה", "!ההזמנה נוספה בהצלחה")
            form.destroy()

        except Exception as e:
            messagebox.showerror("שגיאה", f"שגיאה בהוספה: {e}")

    tk.Button(
        form,
        text="אישור הזמנה",
        width=30,
        command=submit_reservation,
        bg="#4CAF50",          # ירוק בוהק
        fg="white",            # טקסט לבן
        font=("Helvetica", 14, "bold"),  # גופן גדול ועבה
        activebackground="#45a049",      # צבע רקע כשלחוצים
        relief="raised",
        bd=4,                  # עובי הגבול
        padx=10, pady=5        # ריווח פנימי אופקי ואנכי
    ).pack(pady=15)
