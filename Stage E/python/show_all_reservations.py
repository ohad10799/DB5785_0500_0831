import tkinter as tk
from tkinter import ttk, messagebox
import psycopg2
from db import connect_db

def open_view_reservations_by_room_type():
    window = tk.Toplevel()
    window.title("רשימת ההזמנות")
    window.geometry("850x450")

    tk.Label(window, text="רשימת הזמנות", font=("Helvetica", 16, "bold")).pack(pady=10)

    frame = tk.Frame(window, padx=10, pady=10)
    frame.pack(fill=tk.BOTH, expand=True)

    tree = ttk.Treeview(frame, columns=("resid", "roomNumber", "roomType", "check_in", "check_out", "gid"), show="headings")
    tree.heading("resid", text="מספר הזמנה")
    tree.heading("roomNumber", text="מספר חדר")
    tree.heading("roomType", text="סוג חדר")
    tree.heading("check_in", text="תאריך כניסה")
    tree.heading("check_out", text="תאריך יציאה")
    tree.heading("gid", text="מספר אורח")

    tree.column("resid", width=100, anchor="center")
    tree.column("roomNumber", width=100, anchor="center")
    tree.column("roomType", width=150, anchor="w")
    tree.column("check_in", width=120, anchor="center")
    tree.column("check_out", width=120, anchor="center")
    tree.column("gid", width=100, anchor="center")

    scrollbar_y = ttk.Scrollbar(frame, orient="vertical", command=tree.yview)
    scrollbar_y.pack(side=tk.RIGHT, fill=tk.Y)

    scrollbar_x = ttk.Scrollbar(frame, orient="horizontal", command=tree.xview)
    scrollbar_x.pack(side=tk.BOTTOM, fill=tk.X)

    tree.configure(yscrollcommand=scrollbar_y.set, xscrollcommand=scrollbar_x.set)
    tree.pack(fill=tk.BOTH, expand=True)

    try:
        conn = connect_db()
        cur = conn.cursor()

        query = """
            SELECT
                r.resid,
                r."roomNumber",
                rm."roomType",
                cio."check_in_date",
                cio."check_out_date",
                cio."gid"
            FROM reservation r
            JOIN room rm ON r."roomNumber" = rm."roomNumber"
            JOIN check_in_out cio ON r.resid = cio.resid
            ORDER BY rm."roomType", cio."check_in_date";
        """

        cur.execute(query)
        rows = cur.fetchall()

        for row in rows:
            tree.insert("", tk.END, values=row)

        # צבע שורות לסירוגין
        for i, item in enumerate(tree.get_children()):
            if i % 2 == 0:
                tree.item(item, tags=("evenrow",))
            else:
                tree.item(item, tags=("oddrow",))

        tree.tag_configure("evenrow", background="#f9f9ff")
        tree.tag_configure("oddrow", background="white")

        cur.close()
        conn.close()

    except Exception as e:
        messagebox.showerror("שגיאה", f"שגיאה בטעינת ההזמנות: {e}")
