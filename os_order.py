import tkinter as tk
from tkinter import ttk, messagebox,PhotoImage
import psycopg2

class OrderManager:
    def __init__(self, root):
        self.root = root
        self.root.title("Manage Orders")

        #self.background_image = PhotoImage(file=rf"C:\Users\hp\Downloads\Wallpaper-House.com_476125.png")
        #self.background_label = tk.Label(self.root, image=self.background_image)
        #self.background_label.place(relwidth=1, relheight=1)
        
        # Database connection
        self.conn = psycopg2.connect(database="postgres", user="postgres",password="thz111", host="localhost",port="5432")
           
        # Create GUI components
        self.createGUI_order()

    def createGUI_order(self):
        #Styling
        style = ttk.Style()
        style.configure("TLabel", padding=(5, 5), font=('Georgia', 10))
        style.configure("TButton", padding=(10, 5), font=('Georgia', 10))
        style.configure("TEntry", padding=(5, 5), font=('Georgia', 10))

       
         # Labels
        order_info = tk.Label(self.root, text="Edit Orders")
        orderID_label = tk.Label(self.root, text='Order ID')
        customerID_label = tk.Label(self.root, text='Customer ID')
        orderDate_label = tk.Label(self.root, text='Order date (yyyy-mm-dd)')
        productID_label = tk.Label(self.root, text='Product ID')
        productAmount_label = tk.Label(self.root, text='Amount of product')

        #entry widgets
        self.entry_orderID = tk.Entry(self.root)
        self.entry_customerID = tk.Entry(self.root)
        self.entry_orderDate = tk.Entry(self.root)
        self.entry_productID = tk.Entry(self.root)
        self.entry_productAmount = tk.Entry(self.root)

        #buttons
        submit_addNewOrder = tk.Button(self.root, text= "Add new order", command= self.addOrder)
        submit_deleteOrder = tk.Button(self.root, text= "Delete order", command= self.removeOrder)
        submit_showOrder = tk.Button(self.root, text = "Find an order", command = self.showOrder)
        submit_orderByDate = tk.Button(self.root, text = "Orders by date", command = self.orderByDate)

         #GRID LAYOUT

        order_info.grid(row=0, column=0, columnspan=2, padx=5, pady=5)
        orderID_label.grid(row=1, padx=10)
        self.entry_orderID.grid(row=1, column=1, padx=10)
        customerID_label.grid(row=2, column=0, padx=10)
        self.entry_customerID.grid(row=2, column=1, padx=10)
        orderDate_label.grid(row=3, column=0, padx=10)
        self.entry_orderDate.grid(row=3, column=1, padx=10)
        productID_label.grid(row=4, column=0, padx=10)
        self.entry_productID.grid(row=4, column=1, padx=10)
        productAmount_label.grid(row=5, column=0, padx=10)
        self.entry_productAmount.grid(row=5, column=1, padx=10)
        submit_addNewOrder.grid(row = 6, column= 1, pady = 5, padx = 10)
        submit_deleteOrder.grid(row = 8, column= 1, pady = 5, padx = 10)
        submit_showOrder.grid(row = 9, column= 1, pady = 5, padx = 10)
        submit_orderByDate.grid(row = 9, column = 4, padx = 10, pady = 5)

        listbox_orders_label = tk.Label(self.root, text = "All orders (scroll down to see more)")
        listbox_orders_label.grid(row=0, column= 3, columnspan=5)
        self.listbox_orders = tk.Listbox(self.root, width= 50)
        self.listbox_orders.grid(row = 1, rowspan= 8, column = 3, columnspan = 5, padx = 10)


        #printing proudcts in listbox
        c = self.conn.cursor()
        c.execute("SELECT \"order\".orderID, \"order\".customerID, \"order\".orderDate, productorder.productID, productorder.\"productAmount\" FROM \"order\" LEFT JOIN productorder ON \"order\".orderID = productorder.orderID") 
        orders = c.fetchall()
        #create loop to insert data into listbox
        self.listbox_orders.insert(tk.END,"OrderID: CustomerID, Order date, ProductID, Product amount")
        for order in orders:
            self.orderID = order [0]
            self.customerID = order [1]
            self.orderDate = order [2]
            self.productID = order[3]
            self.productAmount = order[4]
            self.listbox_orders.insert(tk.END, f"{self.orderID}: {self.customerID}, {self.orderDate},{self.productID}, {self.productAmount}")
    
    def orderByDate(self):
        c = self.conn.cursor()
        self.listbox_orders.delete(0, tk.END)
        c.execute("SELECT \"order\".orderID, \"order\".customerID, \"order\".orderDate, productorder.productID, productorder.\"productAmount\" FROM \"order\" LEFT JOIN productorder ON \"order\".orderID = productorder.orderID ORDER BY \"order\".orderDate ") 
        orders = c.fetchall()
        #create loop to insert data into listbox
        self.listbox_orders.insert(tk.END,"OrderID: CustomerID, Order date, ProductID, Product amount")
        for order in orders:
            self.orderID = order [0]
            self.customerID = order [1]
            self.orderDate = order [2]
            self.productID = order[3]
            self.productAmount = order[4]
            self.listbox_orders.insert(tk.END, f"{self.orderID}: {self.customerID}, {self.orderDate},{self.productID}, {self.productAmount}")
  


    def showOrder(self):
        o_ID = self.entry_orderID.get()
        if o_ID:
            try:
                c = self.conn.cursor()
                productlist = []
                c.execute("SELECT orderID, customerID, orderDate  FROM \"order\"  WHERE orderID=(%s) ",
                        (o_ID,)) 
                order = c.fetchone()
                c.execute("Select orderID, productID,\"productAmount\" FROM productorder WHERE orderID =(%s) ",
                        (o_ID,))
                productsInOrder = c.fetchall()
                productlist.append(order)
                for product in productsInOrder:
                        self.productID = product[1]
                        self.productAmount = product[2]
                        productlist.append(self.productID)
                        productlist.append(self.productAmount)
                thisorder = productlist[0]
                theseproducts = productlist[1:]
                self.conn.commit()
                messagebox.showinfo("Order",f"Order: {thisorder}, contains the following products: {theseproducts}")
            except Exception as e:
                messagebox.showerror("Error!", f"Error finding the order: {e}")
        else:
            messagebox.showwarning("Warning!", "Please enter the order ID.")
    
        self.entry_orderID.delete(0, tk.END)   
        self.entry_customerID.delete(0, tk.END)
        self.entry_orderDate.delete(0, tk.END)
        self.entry_productID.delete(0, tk.END)
        self.entry_productAmount.delete(0, tk.END)

    def addOrder(self):
        o_ID = self.entry_orderID.get()
        o_ID_po = self.entry_orderID.get()
        c_ID = self.entry_customerID.get()
        orderD = self.entry_orderDate.get()
        p_ID = self.entry_productID.get()
        p_amount = self.entry_productAmount.get()

        if o_ID and c_ID and orderD and p_ID and p_amount:
            try:
                c = self.conn.cursor()
                check_query = "SELECT orderID FROM \"order\" WHERE orderID = (%s)"
                c.execute(check_query, (o_ID,))
                fetched_ID = (c.fetchone())
                fetched_ID = str(fetched_ID)

                if fetched_ID == 'None':
                    c.execute ("INSERT INTO \"order\" (orderID, customerID, orderDate) VALUES (%s, %s, %s)" ,
                    (o_ID, c_ID, orderD,))
                    c.execute ("INSERT INTO productorder (orderID, productID, \"productAmount\") VALUES (%s, %s, %s)" ,
                    (o_ID_po, p_ID, p_amount,))
                    self.conn.commit()
                    messagebox.showinfo("Success!", "Order added successfully!")                    
                else:
                    messagebox.showwarning("Warning",f"ID {o_ID} already exists!")
            
            except Exception as e:
                messagebox.showerror("Error!", f"Error adding order: {e}")
        else:
            messagebox.showwarning("Warning!", "Please enter all the information.")

         #delete records from display
        self.entry_orderID.delete(0, tk.END)   
        self.entry_customerID.delete(0, tk.END)
        self.entry_orderDate.delete(0, tk.END)
        self.entry_productID.delete(0, tk.END)
        self.entry_productAmount.delete(0, tk.END)

        self.createGUI_order()

        #add update order (let's skip this, for orders it's only possible to add, find or remove an order)
        #delete order
    def removeOrder(self):
        o_ID = self.entry_orderID.get()

        if o_ID:
            try:
                c = self.conn.cursor()
                check_query = "SELECT orderID FROM \"order\" WHERE orderID = (%s)"
                c.execute(check_query, (o_ID,))
                fetched_ID = (c.fetchone())
                fetched_ID = str(fetched_ID)

                if fetched_ID == 'None':
                    messagebox.showerror("Error",f"Error: ID {o_ID} not found!")
                    
                else:
                    c.execute("DELETE FROM productorder WHERE orderID = (%s)",
                        (o_ID,))
                    c.execute("DELETE FROM \"order\" WHERE orderID = (%s) ",
                        (o_ID,))
                    messagebox.showinfo("Success!",f"Order {o_ID} deleted succesfully!")
            
            except Exception as e:
                messagebox.showerror("Error!", f"Error deleting order: {e}")    

        self.conn.commit()

        self.entry_orderID.delete(0, tk.END)   
        self.entry_customerID.delete(0, tk.END)
        self.entry_orderDate.delete(0, tk.END)
        self.entry_productID.delete(0, tk.END)
        self.entry_productAmount.delete(0, tk.END)

        self.createGUI_order()



    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    root = tk.Tk()
    app = OrderManager(root)
    app.run()
