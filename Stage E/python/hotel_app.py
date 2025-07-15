from reservation_screen import *
from incidents_screen import *
from feedback_screen import *
import tkinter as tk

# main menu
def open_main_window():
    root = tk.Tk()
    root.title("Hotel Management System")
    root.geometry("400x400")
    root.resizable(False, False)
    root.configure(bg="#f0f4f8")  # צבע רקע בהיר ונעים

    # כותרת ברוכה הבאה
    welcome_label = tk.Label(root, text="!JCT ברוכים הבאים למלון",
                             font=("Helvetica", 20, "bold"),
                             bg="#f0f4f8", fg="#333")
    welcome_label.pack(pady=(40, 30))

    # מסגרת לכפתורים
    frame = tk.Frame(root, bg="#f0f4f8")
    frame.pack()

    btn_style = {
        "width": 30,
        "height": 2,
        "font": ("Helvetica", 14, "bold"),
        "bg": "#4a90e2",         # כחול נעים
        "fg": "white",
        "activebackground": "#357ABD",
        "activeforeground": "white",
        "bd": 0,
        "relief": "flat",
        "cursor": "hand2"
    }

    # כפתורים עם ריווח בין כפתור לכפתור
    tk.Button(frame, text="ניהול הזמנות", command=open_reservation_menu, **btn_style).pack(pady=10)
    tk.Button(frame, text="ניהול תלונות", command=open_incident_management, **btn_style).pack(pady=10)
    tk.Button(frame, text="ניהול פידבקים", command=open_feedback_management, **btn_style).pack(pady=10)

    root.mainloop()


# הפעלת האפליקציה
if __name__ == "__main__":
    open_main_window()
