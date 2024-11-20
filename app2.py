import tkinter as tk
from tkinter import messagebox
import mysql.connector  # For MySQL; replace with pyodbc for MS SQL
# import pyodbc

# Database Connection
def connect_to_db():
    return mysql.connector.connect(
        host="localhost",
        user="your_username",
        password="your_password",
        database="customer_db"
    )

# Register User
def register_user(role):
    def register():
        username = entry_username.get()
        password = entry_password.get()

        conn = connect_to_db()
        cursor = conn.cursor()
        try:
            cursor.execute("INSERT INTO users (username, password, role) VALUES (%s, %s, %s)",
                           (username, password, role))
            conn.commit()
            messagebox.showinfo("Success", f"{role.capitalize()} registered successfully!")
            register_window.destroy()
        except Exception as e:
            messagebox.showerror("Error", f"Error during registration: {str(e)}")
        finally:
            cursor.close()
            conn.close()

    register_window = tk.Toplevel(root)
    register_window.title(f"{role.capitalize()} Registration")

    tk.Label(register_window, text="Username").grid(row=0, column=0)
    entry_username = tk.Entry(register_window)
    entry_username.grid(row=0, column=1)

    tk.Label(register_window, text="Password").grid(row=1, column=0)
    entry_password = tk.Entry(register_window, show="*")
    entry_password.grid(row=1, column=1)

    tk.Button(register_window, text="Register", command=register).grid(row=2, column=1)

# Login User
def login():
    username = entry_username.get()
    password = entry_password.get()

    conn = connect_to_db()
    cursor = conn.cursor()
    cursor.execute("SELECT role FROM users WHERE username = %s AND password = %s", (username, password))
    result = cursor.fetchone()

    if result:
        user_role = result[0]
        messagebox.showinfo("Success", f"Logged in as {user_role}")
        login_window.destroy()
        show_product_view()
    else:
        messagebox.showerror("Error", "Invalid credentials")

    cursor.close()
    conn.close()

# View Products
def show_product_view():
    conn = connect_to_db()
    cursor = conn.cursor()
    cursor.execute("SELECT product_name, price FROM products")
    products = cursor.fetchall()
    cursor.close()
    conn.close()

    product_window = tk.Toplevel(root)
    product_window.title("Product List")

    tk.Label(product_window, text="Product Name").grid(row=0, column=0)
    tk.Label(product_window, text="Price").grid(row=0, column=1)

    for i, (product_name, price) in enumerate(products, start=1):
        tk.Label(product_window, text=product_name).grid(row=i, column=0)
        tk.Label(product_window, text=f"${price:.2f}").grid(row=i, column=1)

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
