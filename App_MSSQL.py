import tkinter as tk
from tkinter import messagebox
import pyodbc  # For connecting to MS SQL Server


# Function to connect to MS SQL Server
def connect_to_db():
    try:
        conn = pyodbc.connect(
            "DRIVER={SQL Server};"
            "SERVER=YourServerName;"  # Replace with your server name
            "DATABASE=YourDatabaseName;"  # Replace with your database name
            "UID=YourUsername;"  # Replace with your username
            "PWD=YourPassword;"  # Replace with your password
        )
        return conn
    except Exception as e:
        messagebox.showerror("Database Error", f"Failed to connect to the database: {e}")
        return None


# Function to handle login
def login():
    username = entry_username.get()
    password = entry_password.get()

    if not username or not password:
        messagebox.showwarning("Input Error", "Please fill in all fields")
        return

    conn = connect_to_db()
    if conn:
        try:
            cursor = conn.cursor()
            cursor.execute(
                "SELECT * FROM Users WHERE Username = ? AND Password = ?",
                (username, password)
            )
            user = cursor.fetchone()
            if user:
                messagebox.showinfo("Success", f"Welcome {username}!")
            else:
                messagebox.showerror("Error", "Invalid Username or Password")
        except Exception as e:
            messagebox.showerror("Database Error", f"Error querying the database: {e}")
        finally:
            conn.close()


# Function to handle registration
def register_user(role):
    messagebox.showinfo("Info", f"Registration for {role} is not implemented yet")


# Main Window Setup
root = tk.Tk()
root.title("City Electronics Management System")

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
