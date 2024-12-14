import tkinter as tk
from tkinter import simpledialog, messagebox
import mysql.connector

# MySQL connection (adjust your credentials accordingly)
try:
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",  # Update if needed
        database="customer_db"
    )
    cursor = mydb.cursor()
except mysql.connector.Error as err:
    messagebox.showerror("Database Error", f"Error: {err}")
    exit()

orders = []  # Ensure orders can be dynamically updated


class App:
    def __init__(self, root):
        self.root = root
        self.root.geometry("800x600")
        self.center_window()
        self.root.title("Role Selection")
        self.root.configure(bg="black")
        self.create_widgets()

    def center_window(self):
        self.root.update_idletasks()
        width = self.root.winfo_width()
        height = self.root.winfo_height()
        x = (self.root.winfo_screenwidth() // 2) - (width // 2)
        y = (self.root.winfo_screenheight() // 2) - (height // 2)
        self.root.geometry(f'{width}x{height}+{x}+{y}')

    def create_widgets(self):
        font_family = "Arial"
        font_size = 14

        self.role_label = tk.Label(self.root, text="Choose your role:", bg="#add8e6", font=(font_family, font_size))
        self.role_label.pack(pady=10)

        self.role_var = tk.StringVar(value="Customer")
        self.admin_radio = tk.Radiobutton(self.root, text="Admin", variable=self.role_var, value="Admin",
                                          bg="#add8e6", font=(font_family, font_size))
        self.customer_radio = tk.Radiobutton(self.root, text="Customer", variable=self.role_var, value="Customer",
                                             bg="#add8e6", font=(font_family, font_size))
        self.admin_radio.pack(pady=5)
        self.customer_radio.pack(pady=5)

        self.proceed_button = tk.Button(self.root, text="Proceed", command=self.proceed,
                                        font=(font_family, font_size))
        self.proceed_button.pack(pady=10)

    def proceed(self):
        role = self.role_var.get()
        if role == "Admin":
            self.admin_login()
        elif role == "Customer":
            self.customer_login()
        else:
            messagebox.showerror("Error", "Invalid User Type")

    def admin_login(self):
        self.clear_window()
        self.create_login_window("Admin")

    def customer_login(self):
        self.clear_window()
        self.create_login_window("Customer")

    def create_login_window(self, role):
        font_family = "Arial"
        font_size = 14

        tk.Label(self.root, text=f"{role} Login", bg="#add8e6", font=(font_family, font_size, "bold")).pack(pady=10)
        self.email_label = tk.Label(self.root, text="Username:", bg="#add8e6", font=(font_family, font_size))
        self.email_label.pack(pady=5)
        self.email_entry = tk.Entry(self.root, font=(font_family, font_size))
        self.email_entry.pack(pady=5)

        self.password_label = tk.Label(self.root, text="Password:", bg="#add8e6", font=(font_family, font_size))
        self.password_label.pack(pady=5)
        self.password_entry = tk.Entry(self.root, show="*", font=(font_family, font_size))
        self.password_entry.pack(pady=5)

        self.login_button = tk.Button(self.root, text="Login", command=lambda: self.login(role))
        self.login_button.pack(pady=10)

    def login(self, role):
        username = self.email_entry.get()
        password = self.password_entry.get()

        if not username or not password:
            messagebox.showerror("Error", "Username and Password are required")
            return

        try:
            cursor.execute(
                "SELECT username, password FROM users WHERE username = %s AND password = %s",
                (username, password)
            )
            user = cursor.fetchone()

            if user:
                if role == "Admin":
                    self.admin_dashboard()
                elif role == "Customer":
                    self.customer_dashboard()
            else:
                messagebox.showerror("Error", "Invalid Credentials")
        except mysql.connector.Error as err:
            messagebox.showerror("Database Error", f"Error: {err}")

    def admin_dashboard(self):
        self.clear_window()
        tk.Label(self.root, text="Admin Dashboard", font=("Arial", 16, "bold")).pack(pady=20)

        self.product_button = tk.Button(self.root, text="Manage Products", command=self.product_page)
        self.product_button.pack(pady=10)

        self.orders_button = tk.Button(self.root, text="Display Orders", command=self.display_orders)
        self.orders_button.pack(pady=10)

        self.logout_button = tk.Button(self.root, text="Logout", command=self.logout)
        self.logout_button.pack(pady=10)

    def product_page(self):
        # Clear the current window
        self.clear_window()

        # Add UI elements for adding a new product
        tk.Label(self.root, text="Manage Products", font=("Arial", 16)).pack(pady=20)

        # Input for product name
        self.product_name_label = tk.Label(self.root, text="Product Name:", font=("Arial", 12))
        self.product_name_label.pack(pady=5)
        self.product_name_entry = tk.Entry(self.root, font=("Arial", 12))
        self.product_name_entry.pack(pady=5)

        # Input for product price
        self.product_price_label = tk.Label(self.root, text="Product Price:", font=("Arial", 12))
        self.product_price_label.pack(pady=5)
        self.product_price_entry = tk.Entry(self.root, font=("Arial", 12))
        self.product_price_entry.pack(pady=5)

        # Add button to add product
        add_button = tk.Button(self.root, text="Add Product", command=self.add_product)
        add_button.pack(pady=10)

        # Button to view product list
        view_button = tk.Button(self.root, text="View Products", command=self.display_product_list)
        view_button.pack(pady=5)

        # Back button to return to the admin dashboard
        back_button = tk.Button(self.root, text="Back", command=self.admin_dashboard)
        back_button.pack(pady=10)

    def add_product(self):
        name = self.product_name_entry.get()
        price = self.product_price_entry.get()

        if not name or not price:
            messagebox.showerror("Error", "Both product name and price are required")
            return

        try:
            cursor.execute("INSERT INTO product (pro_name, unit_price) VALUES (%s, %s)", (name, price))
            mydb.commit()
            messagebox.showinfo("Success", "Product added successfully")
            self.display_product_list()  # Refresh the list to show the new product
        except mysql.connector.Error as err:
            messagebox.showerror("Database Error", f"Error: {err}")

    def remove_product(self):
        product_name = simpledialog.askstring("Input", "Enter the product name to remove:")
        if product_name:
            # Remove product from the database
            cursor.execute("DELETE FROM product WHERE pro_name = %s", (product_name,))
            mydb.commit()
            messagebox.showinfo("Success", f"Product '{product_name}' removed successfully.")
            self.product_page()

    def display_product_list(self):
        try:
            cursor.execute("SELECT pro_name, unit_price FROM product")
            products = cursor.fetchall()
            if products:
                for product in products:
                    tk.Label(self.root, text=f"Product: {product[0]} | Price: ${product[1]:.2f}").pack(pady=5)
            else:
                tk.Label(self.root, text="No products available").pack(pady=5)
        except mysql.connector.Error as err:
            messagebox.showerror("Database Error", f"Error: {err}")

    def display_orders(self):
        self.clear_window()
        tk.Label(self.root, text="Display Orders", font=("Arial", 16, "bold")).pack(pady=20)

        # Dummy orders
        global orders
        orders = ["Order 1: Smartphone", "Order 2: Laptop", "Order 3: Tablet"]
        for order in orders:
            tk.Label(self.root, text=order).pack(pady=5)

        back_button = tk.Button(self.root, text="Back", command=self.admin_dashboard)
        back_button.pack(pady=10)

    def customer_dashboard(self):
        self.clear_window()
        tk.Label(self.root, text="Customer Dashboard", font=("Arial", 16)).pack(pady=20)

        # Display product list with prices
        self.display_product_list()

        # Button to view and place an order
        self.place_order_button = tk.Button(self.root, text="Place Order", command=self.place_order)
        self.place_order_button.pack(pady=10)

        # Button to cancel the order
        self.cancel_order_button = tk.Button(self.root, text="Cancel Order", command=self.cancel_order)
        self.cancel_order_button.pack(pady=10)

        # Button to logout
        self.logout_button = tk.Button(self.root, text="Logout", command=self.logout)
        self.logout_button.pack(pady=5)

    def add_to_order(self, product):
        # Add product to the order list
        product_id = product[0]
        product_name = product[1]
        product_price = product[2]

        # Add the product to the orders list (this is a simple representation, you may want to store it in a database)
        orders.append({"id": product_id, "name": product_name, "price": product_price})
        messagebox.showinfo("Success", f"{product_name} added to your order")

    def display_product_list(self):
        try:
            cursor.execute(
                "SELECT pro_id, pro_name, unit_price FROM product")  # Ensure column names match your database schema
            products = cursor.fetchall()
            if products:
                for product in products:
                    product_text = f"Product: {product[1]} | Price: ${product[2]:.2f}"
                    tk.Label(self.root, text=product_text).pack(pady=5)

                    # Button to add the product to the order
                    add_button = tk.Button(self.root, text="Add to Order",
                                           command=lambda p=product: self.add_to_order(p))
                    add_button.pack(pady=5)
            else:
                tk.Label(self.root, text="No products available").pack(pady=5)
        except mysql.connector.Error as err:
            messagebox.showerror("Database Error", f"Error: {err}")

    def add_to_order(self, product):
                # Add product to the order list
        product_id = product[0]
        product_name = product[1]
        product_price = product[2]

                # Add the product to the orders list (this is a simple representation, you may want to store it in a database)
        orders.append({"id": product_id, "name": product_name, "price": product_price})
        messagebox.showinfo("Success", f"{product_name} added to your order")

    def place_order(self):
        if not orders:
            messagebox.showerror("Error", "No items in your order")
            return


    # Reset the order list
    orders.clear()

    def cancel_order(self):
        if not orders:
            messagebox.showerror("Error", "No order to cancel")
            return

        # Clear the orders list
        orders.clear()
        messagebox.showinfo("Success", "Your order has been canceled")

    def logout(self):
        self.clear_window()
        self.create_widgets()

    def clear_window(self):
        for widget in self.root.winfo_children():
            widget.destroy()


# Run the application
root = tk.Tk()
app = App(root)
root.mainloop()
