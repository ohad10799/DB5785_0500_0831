import tkinter as tk
from tkinter import messagebox
import psycopg2
from db import connect_db

def open_delete_reservation():
    form = tk.Toplevel()
    form.title("מחיקת הזמנה")
    form.geometry("300x200")

    tk.Label(form, text="הכנס מספר הזמנה (resID):").pack(pady=10)
    resid_entry = tk.Entry(form)
    resid_entry.pack()

    def delete_reservation():
        try:
            resid = int(resid_entry.get())

            # הודעת אישור מהמשתמש
            confirm = messagebox.askyesno("אישור מחיקה", f"האם אתה בטוח שברצונך למחוק את ההזמנה מספר {resid}?")
            if not confirm:
                return  # המשתמש בחר לא להמשיך

            conn = connect_db()
            cur = conn.cursor()

            cur.execute("CALL delete_reservation(%s);", (resid,))
            conn.commit()

            cur.close()
            conn.close()

            messagebox.showinfo("הצלחה", f"ההזמנה מספר {resid} נמחקה בהצלחה.")
            form.destroy()

        except Exception as e:
            messagebox.showerror("שגיאה", f"שגיאה במחיקה: {e}")

    tk.Button(
        form,
        text="מחק הזמנה",
        width=25,
        command=delete_reservation,
        bg="#d9534f",          # אדום בולט
        fg="white",            # טקסט לבן
        font=("Helvetica", 14, "bold"),
        activebackground="#c9302c",
        relief="raised",
        bd=4,
        padx=10, pady=5
    ).pack(pady=20)
