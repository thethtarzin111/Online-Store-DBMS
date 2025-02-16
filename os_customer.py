import tkinter as tk
from tkinter import ttk, messagebox,PhotoImage
import psycopg2


class CustomerManager:
    def __init__(self, root):
        self.root = root
        self.root.title("Manage Customers")

        #self.background_image = PhotoImage(file=rf"C:\Users\hp\Downloads\Wallpaper-House.com_476125.png")
        #self.background_label = tk.Label(self.root, image=self.background_image)
        #self.background_label.place(relwidth=1, relheight=1)
        
        # Database connection
        self.conn = psycopg2.connect(database="postgres", user="postgres",password="thz111", host="localhost",port="5432")
           
        # Create GUI components
        self.createGUI()

    def createGUI(self):
        #Styling
        style = ttk.Style()
        style.configure("TLabel", padding=(5, 5), font=('Georgia', 10))
        style.configure("TButton", padding=(10, 5), font=('Georgia', 10))
        style.configure("TEntry", padding=(5, 5), font=('Georgia', 10))
        
        # Labels
        label_ID = ttk.Label(self.root, text= "Customer ID:")
        label_fname = ttk.Label(self.root, text="First Name:")
        label_lname = ttk.Label(self.root, text="Last Name:")
        label_straddress = ttk.Label(self.root, text="Street Address:")
        label_cityaddress = ttk.Label(self.root, text="City Address:")
        label_phnumber = ttk.Label(self.root, text="Phone Number:")

        # Entry widgets
        self.entry_ID = ttk.Entry(self.root)
        self.entry_fname = ttk.Entry(self.root)
        self.entry_lname = ttk.Entry(self.root)
        self.entry_straddress = ttk.Entry(self.root)
        self.entry_cityaddress = ttk.Entry(self.root)
        self.entry_phnumber = ttk.Entry(self.root)

        # Buttons
        button_add_customer = ttk.Button(self.root, text="Add Customer", command=self.add_customer)
        button_delete_customer = ttk.Button(self.root, text="Delete Customer", command=self.delete_customer)
        button_show_customer = ttk.Button(self.root, text="Show Existing Customers", command=self.show_customer)
        
        # Grid layout
        label_ID.grid(row=0, column=0, padx=10, pady=10, sticky="w")
        label_fname.grid(row=1, column=0, padx=10, pady=10, sticky="w")
        label_lname.grid(row=2, column=0, padx=10, pady=10, sticky="w")
        label_straddress.grid(row=3, column=0, padx=10, pady=10, sticky="w")
        label_cityaddress.grid(row=4, column=0, padx=10, pady=10, sticky="w")
        label_phnumber.grid(row=5, column=0, padx=10, pady=10, sticky="w")
        
        self.entry_ID.grid(row=0, column=1, padx=10, pady=10)
        self.entry_fname.grid(row=1, column=1, padx=10, pady=10)
        self.entry_lname.grid(row=2, column=1, padx=10, pady=10)
        self.entry_straddress.grid(row=3, column=1, padx=10, pady=10)
        self.entry_cityaddress.grid(row=4, column=1, padx=10, pady=10)
        self.entry_phnumber.grid(row=5, column=1, padx=10, pady=10)
        button_add_customer.grid(row=6, column=0, columnspan=2, pady=10)
        button_delete_customer.grid(row=7, column=0, columnspan=2, pady=10)
        button_show_customer.grid(row=8, column=0, columnspan=2, pady=10)

    def add_customer(self):
        ID = self.entry_ID.get()
        fname = self.entry_fname.get()
        lname = self.entry_lname.get()
        straddress = self.entry_straddress.get()
        cityaddress = self.entry_cityaddress.get()
        phnumber = self.entry_phnumber.get()

        if ID and fname and lname and straddress and cityaddress and phnumber:
            try:
                cursor = self.conn.cursor()
                sql = "INSERT INTO customer(\"CustomerID\",\"CustomerFirstName\",\"CustomerLastName\", \"CustomerStreetAddress\", \"CustomerCityAddress\", \"CustomerPhoneNumber\")VALUES (%s, %s, %s, %s, %s, %s)"
                cursor.execute(sql, (ID, fname, lname, straddress, cityaddress, phnumber))
                self.conn.commit()
                messagebox.showinfo("Success!", "Customer added successfully!")
            except Exception as e:
                messagebox.showerror("Error!", f"Error adding customer: {e}")
        else:
            messagebox.showwarning("Warning!", "Please enter all the information.")

    def delete_customer(self):
        ID = self.entry_ID.get()

        if ID:
            try:
                cursor = self.conn.cursor()
                cursor.execute("DELETE FROM customer WHERE \"CustomerID\"=%s", (ID,))
                self.conn.commit()
                messagebox.showinfo("Success", "Customer deleted successfully!")
            except Exception as e:
                messagebox.showerror("Error", f"Error deleting customer: {e}")
        else:
            messagebox.showwarning("Warning", "Please enter the Customer ID to delete.")

    def show_customer(self):
        cursor = self.conn.cursor()
        sql = "SELECT * FROM customer"
        
        # Retrieve customer data from the database
        cursor.execute(sql)
        customers = cursor.fetchall()
        
        customers_window = tk.Toplevel(root)
        customers_window.title("Existing Customers")

        # Display customer data in the new window
        customers_label = tk.Label(customers_window, text="Existing Customers:\n")
        customers_label.pack()

        for customer in customers:
            customer_info = (
                f"ID: {customer[0]}\n"
                f"First Name: {customer[1]}\n"
                f"Last Name: {customer[2]}\n"
                f"Phone Number: {customer[3]}\n"
                f"Street Address: {customer[4]}\n"
                f"City Address: {customer[5]}\n"
            )
            customer_label = tk.Label(customers_window, text=customer_info)
            customer_label.pack()

        
    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    root = tk.Tk()
    app = CustomerManager(root)
    app.run()
