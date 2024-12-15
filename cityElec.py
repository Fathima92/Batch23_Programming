import tkinter as tk
from tkinter import messagebox
import mysql.connector

def connect_to_db():
    return mysql.connector.connect(
        host="localhost",
        user="your_username",
        password="your_password",
        database="customer_db")

def center_window(window, width, height):
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x_coordinate = (screen_width // 10) - (width // 10)
    y_coordinate = (screen_height // 10) - (height // 10)
    window.geometry(f"{width}x{height}+{x_coordinate}+{y_coordinate}")

def admin_login_window():
    admin_window = tk.Toplevel(root)
    admin_window.title("Admin Login")
    admin_window.configure(bg='#282C34')
    center_window(admin_window, 600, 400)

    admin_frame = tk.Frame(admin_window , bg='#282C34')
    admin_frame.pack(expand=True)

    tk.Label(admin_frame, text="Admin Login", font=("Times New Roman", 18, "bold") , bg='#282C34', fg='#61DAFB').grid(row=0, column=0, columnspan=2, pady=20)
    tk.Label(admin_frame, text="Username:", font=("Times New Roman", 15, "bold"), bg='#282C34', fg='#FFFFFF').grid(row=1, column=0, padx=10, pady=5, sticky="e")
    entry_username = tk.Entry(admin_frame)
    entry_username.grid(row=1, column=1, padx=10, pady=5)

    tk.Label(admin_frame, text="Password:", font=("Times New Roman", 12, "bold"), bg='#282C34', fg='#FFFFFF').grid(row=2, column=0, padx=10, pady=5, sticky="e")
    entry_password = tk.Entry(admin_frame, show="*")
    entry_password.grid(row=2, column=1, padx=10, pady=5)

    tk.Button(admin_frame, text="Login", font=("Times New Roman", 13, "bold"), bg='#61DAFB', fg='#282C34', command=lambda: admin_login(entry_username, entry_password)).grid(row=3, column=0, columnspan=2, pady=20)

def customer_login_window():
    customer_window = tk.Toplevel(root)
    customer_window.title("Customer Login")
    customer_window.configure(bg='#282C34')
    center_window(customer_window, 600, 400)

    customer_frame = tk.Frame(customer_window , bg='#282C34')
    customer_frame.pack(expand=True)

    tk.Label(customer_frame, text="Customer Login", font=("Times New Roman", 18, "bold") , bg='#282C34', fg='#61DAFB').grid(row=0, column=0, columnspan=2, pady=20)
    tk.Label(customer_frame, text="Username:", font=("Times New Roman", 15, "bold") , bg='#282C34', fg='#FFFFFF').grid(row=1, column=0, padx=10, pady=5, sticky="e")
    entry_username = tk.Entry(customer_frame)
    entry_username.grid(row=1, column=1, padx=10, pady=5)

    tk.Label(customer_frame, text="Password:", font=("Times New Roman", 15, "bold") , bg='#282C34', fg='#FFFFFF').grid(row=2, column=0, padx=10, pady=5, sticky="e")
    entry_password = tk.Entry(customer_frame, show="*")
    entry_password.grid(row=2, column=1, padx=10, pady=5)

    tk.Button(customer_frame, text="Login", font=("Times New Roman", 16, "bold"), bg='#61DAFB', fg='#282C34' , command=lambda: customer_login(entry_username, entry_password)).grid(row=3, column=0, columnspan=2, pady=20)

def admin_login(entry_username, entry_password):
    username = entry_username.get()
    password = entry_password.get()

    if username == "" or password == "":
        messagebox.showinfo("", "Blank are not Allowed")
    elif username == "Riffath" and password == "2004":
        messagebox.showinfo("", "Succesfully Login")
        open_admin_dashboard()
    else:
        messagebox.showinfo("", "Incorrect username and password")

def customer_login(entry_username, entry_password):
    username = entry_username.get()
    password = entry_password.get()

    if username == "" or password == "":
        messagebox.showinfo("", "Blank are not Allowed")
    elif username == "Sefa" and password == "0527":
        messagebox.showinfo("", "Successfully login")
        open_customer_dashboard()
    else:
        messagebox.showinfo("", "Incorrect username and password")

def open_admin_dashboard():
    admin_dashboard = tk.Toplevel(root)
    admin_dashboard.title("Admin Dashboard")
    admin_dashboard.configure(bg='#282C34')
    center_window(admin_dashboard, 600, 400)

    tk.Label(admin_dashboard, text="Admin Dashboard", font=("Times New Roman", 18, "bold") , bg='#282C34', fg='#61DAFB').pack(pady=20)

    tk.Button(admin_dashboard, text="Add Admins", font=("Times New Roman", 15, "bold"), bg='#61DAFB', fg='#282C34', command=open_add_admins_window).pack(pady=5)
    tk.Button(admin_dashboard, text="Add Products", font=("Times New Roman", 15, "bold"), bg='#61DAFB', fg='#282C34', command=lambda: messagebox.showinfo("Add Products","Add Products functionality to be implemented")).pack(pady=5)
    tk.Button(admin_dashboard, text="Modify Product", font=("Times New Roman", 15, "bold"), bg='#61DAFB', fg='#282C34', command=lambda: messagebox.showinfo("Modify Product", "Modify Product functionality to be implemented")).pack(pady=5)
    tk.Button(admin_dashboard, text="Customize Orders", font=("Times New Roman", 15, "bold"), bg='#61DAFB', fg='#282C34', command=lambda: messagebox.showinfo("Customize Orders", "Customize Orders functionality to be implemented")).pack(pady=5)

def open_add_admins_window():
    add_admins_window = tk.Toplevel(root)
    add_admins_window.title("Add Admins")
    add_admins_window.configure(bg='#282C34')
    center_window(add_admins_window, 600, 400)

    add_admins_frame = tk.Frame(add_admins_window , bg='#282C34')
    add_admins_frame.pack(expand=True)

    tk.Label(add_admins_frame, text="ID:", font=("Times New Roman", 18, "bold") , bg='#282C34', fg='#FFFFFF').grid(row=0, column=0, padx=10, pady=5, sticky="e")
    entry_admin_id = tk.Entry(add_admins_frame)
    entry_admin_id.grid(row=0, column=1, padx=10, pady=5)

    tk.Label(add_admins_frame, text="Name:", font=("Times New Roman", 18, "bold") ,bg='#282C34', fg='#FFFFFF' ).grid(row=1, column=0, padx=10, pady=5, sticky="e")
    entry_admin_name = tk.Entry(add_admins_frame)
    entry_admin_name.grid(row=1, column=1, padx=10, pady=5)

    tk.Label(add_admins_frame, text="Password:", font=("Times New Roman", 18, "bold"), bg='#282C34', fg='#FFFFFF' ).grid(row=2, column=0, padx=10, pady=5, sticky="e")
    entry_admin_password = tk.Entry(add_admins_frame, show="*")
    entry_admin_password.grid(row=2, column=1, padx=10, pady=5)

    tk.Button(add_admins_frame, text="Add Admin", font=("Times New Roman", 16, "bold"),bg='#61DAFB', fg='#282C34', command=lambda: add_admin(entry_admin_id, entry_admin_name, entry_admin_password)).grid(row=3, column=0, columnspan=2, pady=20)

def add_admin(entry_id, entry_name, entry_password):
    id = entry_id.get()
    name = entry_name.get()
    password = entry_password.get()

    if id == "" or name == "" or password == "":
        messagebox.showinfo("", "All fields are required")
    else:
        conn = connect_to_db()
        cursor = conn.cursor()
        try:
            cursor.execute("INSERT INTO admins (admin_id, admin_name, admin_password) VALUES (%s, %s, %s)", (id, name, password))
            conn.commit()
            messagebox.showinfo("Success", "Admin added successfully")
        except mysql.connector.Error as err:
            messagebox.showerror("Error", f"Error: {err}")
        finally:
            cursor.close()
            conn.close()

def open_customer_dashboard():
    customer_dashboard = tk.Toplevel(root)
    customer_dashboard.title("Customer Dashboard")
    center_window(customer_dashboard, 600, 400)

    tk.Label(customer_dashboard, text="Customer Dashboard", font=("Times New Roman", 18, "bold")).pack(pady=20)

    tk.Button(customer_dashboard, text="Place Order", font=("Times New Roman", 15, "bold"), command=lambda: messagebox.showinfo("Place Order", "Place Order functionality to be implemented")).pack(pady=5)
    tk.Button(customer_dashboard, text="View Orders", font=("Times New Roman", 15, "bold"), command=lambda: messagebox.showinfo("View Orders", "View Orders functionality to be implemented")).pack(pady=5)
    tk.Button(customer_dashboard, text="View Products", font=("Times New Roman", 15, "bold"), command=lambda: messagebox.showinfo("View Products", "View Products functionality to be implemented")).pack(pady=5)

root = tk.Tk()
root.title("City Electronics Management System")
root.configure(bg='#ADD8E6')

window_width = 600
window_height = 400

center_window(root, window_width, window_height)

login_frame = tk.Frame(root)
login_frame.pack(pady=20)

login_label = tk.Label(login_frame, text="Welcome to City Electronics Login", font=("Arial", 18, "bold"))
login_label.pack(pady=10)

register_frame = tk.Frame(root)
register_frame.pack(pady=20)

admin_register_button = tk.Button(register_frame, text="Register as Admin", font=("Times New Roman", 15, "bold"), command=admin_login_window)
admin_register_button.pack(pady=5)

customer_register_button = tk.Button(register_frame, text="Register as Customer", font=("Times New Roman", 15, "bold"), command=customer_login_window)
customer_register_button.pack(pady=10)

root.mainloop()
