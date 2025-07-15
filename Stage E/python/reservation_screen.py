import tkinter as tk
from tkinter import messagebox
from new_reservation_screen import open_new_reservation
from delete_reservation_screen import open_delete_reservation
from show_all_reservations import open_view_reservations_by_room_type

def open_reservation_menu():
    window = tk.Toplevel()
    window.title("ניהול הזמנות")
    window.geometry("400x400")
    window.resizable(False, False)
    window.configure(bg="#f0f4f8")

    tk.Label(window, text=":בחר פעולה", font=("Helvetica", 16, "bold"), bg="#f0f4f8", fg="#333").pack(pady=(30, 20))

    btn_style = {
        "width": 30,
        "height": 2,
        "font": ("Helvetica", 14, "bold"),
        "bg": "#4a90e2",
        "fg": "white",
        "activebackground": "#357ABD",
        "activeforeground": "white",
        "bd": 0,
        "relief": "flat",
        "cursor": "hand2"
    }

    tk.Button(window, text="יצירת הזמנה", command=open_new_reservation, **btn_style).pack(pady=10)
    tk.Button(window, text="מחיקת הזמנה", command=open_delete_reservation, **btn_style).pack(pady=10)
    tk.Button(window, text="הצגת כל ההזמנות", command=open_view_reservations_by_room_type, **btn_style).pack(pady=10)
