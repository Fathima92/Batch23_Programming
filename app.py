import tkinter as tk
from tkinter import messagebox
import mysql.connector  # For MySQL; replace with pyodbc for MS SQL

# Main Window Setup
root = tk.Tk()
root.title("City Electronics Managment System")

# Login Window
login_window = tk.Frame(root)
login_window.grid(row=0, column=0, padx=20, pady=20)

tk.Label(login_window, text="Login").grid(row=0, column=1)

tk.Label(login_window, text="Username").grid(row=1, column=0)
entry_username = tk.Entry(login_window)
entry_username.grid(row=1, column=1)

tk.Label(login_window, text="Password").grid(row=2, column=0)
entry_password = tk.Entry(login_window, show="*")
entry_password.grid(row=2, column=1)

tk.Button(login_window, text="Login", command=login).grid(row=3, column=1)

# Registration Buttons
tk.Button(root, text="Register as Admin", command=lambda: register_user("admin")).grid(row=1, column=0, pady=10)
tk.Button(root, text="Register as Customer", command=lambda: register_user("customer")).grid(row=2, column=0)

root.mainloop()
