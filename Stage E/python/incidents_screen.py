import tkinter as tk
from tkinter import ttk, messagebox
from db import connect_db

def open_incident_management():
    window = tk.Toplevel()
    window.title("ניהול תלונות")
    window.geometry("850x500")
    window.resizable(True, True)

    # מסגרת ראשית עם רווח פנימי
    main_frame = tk.Frame(window, padx=15, pady=15)
    main_frame.pack(fill="both", expand=True)

    # כותרת בולטת ומרווחה
    tk.Label(main_frame, text="ניהול תלונות", font=("Arial", 20, "bold")).pack(pady=(0,15))

    # מסגרת לטבלה + גלילות
    table_frame = tk.Frame(main_frame)
    table_frame.pack(fill="both", expand=True)

    tree = ttk.Treeview(table_frame, columns=("gid", "description", "report_date", "status"), show="headings")
    tree.heading("gid", text="מספר אורח (GID)")
    tree.heading("description", text="תיאור התקרית")
    tree.heading("report_date", text="תאריך דיווח")
    tree.heading("status", text="סטטוס")

    # רוחב עמודות
    tree.column("gid", width=100, anchor="center")
    tree.column("description", width=350, anchor="w")
    tree.column("report_date", width=130, anchor="center")
    tree.column("status", width=100, anchor="center")

    # סרגלי גלילה
    scrollbar_y = ttk.Scrollbar(table_frame, orient="vertical", command=tree.yview)
    scrollbar_y.pack(side="right", fill="y")

    scrollbar_x = ttk.Scrollbar(table_frame, orient="horizontal", command=tree.xview)
    scrollbar_x.pack(side="bottom", fill="x")

    tree.configure(yscrollcommand=scrollbar_y.set, xscrollcommand=scrollbar_x.set)
    tree.pack(fill="both", expand=True)

    # סגנון כפתורים
    btn_style = {
        "height": 2,
        "font": ("Arial", 12, "bold"),
        "bg": "#4a90e2",
        "fg": "white",
        "activebackground": "#357ABD",
        "activeforeground": "white",
        "bd": 0,
        "cursor": "hand2",
        "relief": "ridge",
    }

    # מסגרת לכפתורים, מיושרת במרכז עם ריווח
    buttons_frame = tk.Frame(main_frame)
    buttons_frame.pack(pady=15)

    btn_load = tk.Button(buttons_frame, text="טען תקריות", width=22, **btn_style)
    btn_load.grid(row=0, column=0, padx=10)

    btn_delete = tk.Button(buttons_frame, text="מחק תקריות שקיימות מעל שנה", width=22, **btn_style)
    btn_delete.grid(row=0, column=1, padx=10)

    btn_resolve = tk.Button(buttons_frame, text="סגור תקריות פתוחות מעל 30 יום", width=26, **btn_style)
    btn_resolve.grid(row=0, column=2, padx=10)

    # פונקציות כפתורים

    def load_incident_dates():
        try:
            conn = connect_db()
            cur = conn.cursor()

            cur.execute("""
                SELECT g.gid, i.description, i.report_date,
                       CASE WHEN i.status THEN 'פתוחה' ELSE 'סגורה' END AS status
                FROM incidentreport i
                JOIN guest g ON i."incidentId" = g."incidentId"
                ORDER BY i.report_date DESC;
            """)

            rows = cur.fetchall()
            tree.delete(*tree.get_children())
            for row in rows:
                tree.insert("", "end", values=row)

            cur.close()
            conn.close()
        except Exception as e:
            messagebox.showerror("שגיאה", f"שגיאה בטעינת התלונות: {e}")

    def delete_old_incidents():
        try:
            conn = connect_db()
            cur = conn.cursor()
            cur.execute("""
                DELETE FROM incidentreport
                WHERE report_date < CURRENT_DATE - INTERVAL '1 year';
            """)
            conn.commit()
            cur.close()
            conn.close()
            messagebox.showinfo("הצלחה", "תקריות ישנות נמחקו בהצלחה.")
            load_incident_dates()
        except Exception as e:
            messagebox.showerror("שגיאה", f"שגיאה במחיקה: {e}")

    def resolve_old_incidents():
        try:
            conn = connect_db()
            cur = conn.cursor()
            cur.execute("CALL resolve_old_incidents();")
            conn.commit()
            cur.close()
            conn.close()
            messagebox.showinfo("הצלחה", "תקריות של מעל 30 יום עודכנו עם הערה!.")
            load_incident_dates()
        except Exception as e:
            messagebox.showerror("שגיאה", f"שגיאה בעדכון תקריות: {e}")

    # חיבור הכפתורים לפונקציות
    btn_load.config(command=load_incident_dates)
    btn_delete.config(command=delete_old_incidents)
    btn_resolve.config(command=resolve_old_incidents)

    # טעינה ראשונית
    load_incident_dates()
