import tkinter as tk
from tkinter import ttk, messagebox
import subprocess

class navigation:
    def __init__(self, root):
        self.root = root
        self.root.title("Navigation Menu")

        style = ttk.Style()
        style.configure("TLabel", padding=(5, 5), font=('Georgia', 20))
        style.configure("TButton", padding=(10, 5), font=('Georgia', 13))
        
        label_title = ttk.Label(self.root, text= "Choose an option")
        label_title.grid(row=0, column=1, pady=10, padx=10, sticky="w")
        
        # Create buttons for navigation
        button_customer = ttk.Button(self.root, text="Manage Customers", command=self.open_customer)
        button_customer.grid(row=1, column=0, columnspan=2, pady=50, padx=50)
        
        button_order = ttk.Button(self.root, text="Manage Orders", command=self.open_order)
        button_order.grid(row=2, column=0, columnspan=2, pady=50, padx=50)

        button_product = ttk.Button(self.root, text="Manage Products", command=self.open_product)
        button_product.grid(row=1, column=5, columnspan=2, pady=50, padx=50)
        
        button_supplier = ttk.Button(self.root, text="Manage Suppliers", command=self.open_supplier)
        button_supplier.grid(row=2, column=5, columnspan=2, pady=50, padx=50)

    
        button_warehouse = ttk.Button(self.root, text="Manage Warehouses", command=self.open_warehouse)
        button_warehouse.grid(row=3, column=0, columnspan=2, pady=50, padx=50)

        
        
    def open_customer(self):
        subprocess.run(["python3", "os_customer.py"])

    def open_order(self):
        subprocess.run(["python3", "os_order.py"])

    def open_product(self):
        subprocess.run(['python3', 'os_product.py'])
        
    def open_supplier(self):
        subprocess.run(["python3", 'os_product.py'])
        
    def open_warehouse(self):
        subprocess.run(["python3", 'os_product.py'])

if __name__ == "__main__":
    root = tk.Tk()
    app = navigation(root)
    root.mainloop()
