import tkinter as tk
from tkinter import ttk, messagebox, simpledialog
from db import connect_db  # החיבור למסד הנתונים שלך

def create_feedback_window(title, fetch_function):
    """יוצר חלון חדש עם טבלה וטעינת נתונים בעזרת fetch_function."""
    win = tk.Toplevel()
    win.title(title)
    win.geometry("750x450")
    win.configure(bg="#f9f9f9")

    # כותרת בחלון התצוגה
    title_label = tk.Label(win, text=title, font=("Arial", 16, "bold"), bg="#f9f9f9")
    title_label.pack(pady=(10,5))

    # Treeview עם עיצוב
    tree = ttk.Treeview(win, columns=("guest_name", "rating", "date", "description"), show="headings", height=15)
    tree.heading("guest_name", text="שם אורח")
    tree.heading("rating", text="דירוג")
    tree.heading("date", text="תאריך")
    tree.heading("description", text="תיאור")

    # רוחב עמודות מותאם
    tree.column("guest_name", width=150, anchor="center")
    tree.column("rating", width=60, anchor="center")
    tree.column("date", width=120, anchor="center")
    tree.column("description", width=400, anchor="w")

    tree.pack(fill="both", expand=True, padx=15, pady=10)

    fetch_function(tree)

def fetch_all_feedbacks(tree):
    try:
        conn = connect_db()
        cur = conn.cursor()
        cur.execute("""
            SELECT g.name, f.rating, f.description, f.date
            FROM feedback f
            JOIN guest g ON f.gid = g.gid
            ORDER BY f.date DESC;
        """)
        rows = cur.fetchall()
        tree.delete(*tree.get_children())
        for row in rows:
            tree.insert("", "end", values=row)
        cur.close()
        conn.close()
    except Exception as e:
        messagebox.showerror("שגיאה", f"שגיאה בשליפת כל הפידבקים: {e}")

def fetch_low_rating_feedbacks(tree):
    try:
        conn = connect_db()
        cur = conn.cursor()
        cur.execute("""
            SELECT g.name, f.rating, f.description, f.date
            FROM feedback f
            JOIN guest g ON f.gid = g.gid
            WHERE f.rating < 3
            ORDER BY f.date DESC;
        """)
        rows = cur.fetchall()
        tree.delete(*tree.get_children())
        for row in rows:
            tree.insert("", "end", values=row)
        cur.close()
        conn.close()
    except Exception as e:
        messagebox.showerror("שגיאה", f"שגיאה בשליפת פידבקים עם דירוג נמוך: {e}")

def fetch_guest_feedbacks(tree):
    gid = simpledialog.askinteger("בדיקת פידבקים של אורח", "הכנס מספר אורח (GID):")
    if gid is None:
        return
    try:
        conn = connect_db()
        cur = conn.cursor()

        cur.execute("BEGIN;")
        cur.execute("SELECT get_guest_feedbacks(%s);", (gid,))
        cursor_name = cur.fetchone()[0]

        cur.execute(f"FETCH ALL FROM {cursor_name};")
        rows = cur.fetchall()

        cur.execute(f"CLOSE {cursor_name};")
        cur.execute("COMMIT;")
        cur.close()
        conn.close()

        tree.delete(*tree.get_children())
        for rating, date, description in rows:
            tree.insert("", "end", values=("", rating, date, description))

    except Exception as e:
        messagebox.showerror("שגיאה", f"שגיאה בשליפת פידבקים של אורח: {e}")

def run_reward_procedure():
    try:
        conn = connect_db()
        cur = conn.cursor()
        cur.execute("CALL reward_high_rating_guests();")
        conn.commit()
        cur.close()
        conn.close()
        messagebox.showinfo("הצלחה", "נקודות בונוס הוענקו לאורחים עם דירוג גבוה.")
    except Exception as e:
        messagebox.showerror("שגיאה", f"שגיאה בהרצת הפרוצדורה: {e}")

def open_feedback_management():
    root = tk.Tk()
    root.title("ניהול פידבקים")
    root.geometry("450x320")
    root.resizable(False, False)
    root.configure(bg="#f9f9f9")

    # כותרת ראשית
    title_label = tk.Label(root, text="ניהול פידבקים", font=("Arial", 20, "bold"), bg="#f9f9f9", fg="#333333")
    title_label.pack(pady=(30, 20))

    # מסגרת מרכזית לכפתורים, עם מרכזיות ונראות טובה
    frame = tk.Frame(root, bg="#f9f9f9")
    frame.pack()

    btn_style = {
        "width": 30,
        "height": 2,
        "font": ("Arial", 13),
        "bg": "#4a90e2",
        "fg": "white",
        "activebackground": "#357ABD",
        "activeforeground": "white",
        "bd": 0,
        "cursor": "hand2",
        "relief": "ridge",
    }

    tk.Button(frame, text="הצגת כל הפידבקים", command=lambda: create_feedback_window("כל הפידבקים", fetch_all_feedbacks), **btn_style).pack(pady=7)
    tk.Button(frame, text="הצגת פידבקים עם דירוג מתחת ל-3", command=lambda: create_feedback_window("פידבקים עם דירוג נמוך", fetch_low_rating_feedbacks), **btn_style).pack(pady=7)
    tk.Button(frame, text="בדיקת פידבקים של אורח", command=lambda: create_feedback_window("פידבקים של אורח", fetch_guest_feedbacks), **btn_style).pack(pady=7)
    tk.Button(frame, text="הענקת נקודות בונוס", command=run_reward_procedure, **btn_style).pack(pady=7)

    root.mainloop()

if __name__ == "__main__":
    open_feedback_management()
