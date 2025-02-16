import tkinter as tk
import psycopg2
from tkinter import messagebox, ttk
'''
root = Tk()
root.title('GUI for groupwork')
root.geometry("500x550")
'''

class ProductManager:
    def __init__(self, root):
        self.root = root
        self.root.title("Manage Products, Warehouses and Suppliers")

        #self.background_image = tk.PhotoImage(file= "/Users/nooraalikirri/Documents/Basics of database systems/groupwork/GUI Tkinter/pexel.png")
        #self.background_label = tk.Label(self.root, image=self.background_image)
        #self.background_label.place(relwidth=1, relheight=1)

        self.conn = psycopg2.connect(database = "postgres", 
                            user = "postgres", 
                            host= 'localhost',
                            password = "thz111",
                            port = 5432)
        self.createGUIproduct()

        #root = tkinter.Tk()
    #create GUI
    def createGUIproduct(self):
        #Styling
        #style = ttk.Style()
        #style.configure("TLabel", padding=(0, 0), font=('Georgia', 10))
        #style.configure("TButton", padding=(0, 0), font=('Georgia', 10))
        #style.configure("TEntry", padding=(0, 0), font=('Georgia', 10))

        # Labels
        Product_info = tk.Label(self.root, text="Edit Products")
        productID_label = tk.Label(self.root, text='ProductID')
        productName_label = tk.Label(self.root, text='Product Name')
        price_label = tk.Label(self.root, text='Price')
        warehouseID_product_label = tk.Label(self.root, text = "Warehouse ID")
        warehouseID_label = tk.Label(self.root, text='WarehouseID')
        amountOfProduct_label = tk.Label(self.root, text = "Amount of product in warehouses")
        Warehouse_info = tk.Label(self.root, text="Edit Warehouses")
        warehouseAddress_label = tk.Label(self.root, text='Warehouse City')
        supplier_info = tk.Label(self.root, text="Edit Suppliers")
        supplierID_label = tk.Label(self.root, text='SupplierID')
        supplierName_label = tk.Label(self.root, text='Supplier Name')
        supplierProduct_label = tk.Label(self.root, text="Supplier's productID")
        supplierNumber_laber = tk.Label(self.root, text='Supplier Phone Number')

        #entry widgets
        self.entry_productID = tk.Entry(self.root)
        self.entry_productName = tk.Entry(self.root)
        self.entry_price = tk.Entry(self.root)
        self.entry_warehouseID_product = tk.Entry(self.root)
        self.entry_amountOfProduct = tk.Entry(self.root)
        self.entry_warehouseID = tk.Entry(self.root)
        self.entry_warehouseAddress = tk.Entry(self.root)
        self.entry_supplierID = tk.Entry(self.root)
        self.entry_supplierName = tk.Entry(self.root)
        self.entry_supplierProduct = tk.Entry(self.root)
        self.entry_supplierNumber = tk.Entry(self.root)

        #buttons
        submit_addNewProduct = tk.Button(self.root, text= "Add new product", command = self.submit_NewProduct)
        submit_UpdatingProduct = tk.Button(self.root, text= "Update product", command = self.submit_UpdateProduct)
        submit_RemoveProduct = tk.Button(self.root, text= "Remove product", command = self.submit_RemoveProduct)
        submit_addNewWarehouse = tk.Button(self.root, text= "Add new Warehouse", command = self.submit_newWarehouse)
        submit_UpdatingWarehouse = tk.Button(self.root, text= "Update Warehouse", command = self.submit_updateWarehouse)
        submit_RemoveWarehouse = tk.Button(self.root, text= "Remove Warehouse", command = self.delete_Warehouse)
        submit_addNewSupplier = tk.Button(self.root, text= "Add new Supplier", command = self.add_Supplier)
        submit_UpdatingSupplier = tk.Button(self.root, text= "Update Supplier", command= self.update_Supplier)
        submit_RemoveSupplier = tk.Button(self.root, text= "Remove Supplier", command = self.delete_Supplier)

        #GRID LAYOUT

        Product_info.grid(row=0, column=0, columnspan=2, padx=5, pady= 5)
        productID_label.grid(row=1, padx=10)
        self.entry_productID.grid(row=1, column=1, padx=10)
        productName_label.grid(row=2, padx=10)
        self.entry_productName.grid(row=2, column=1, padx=10)
        price_label.grid(row=3,padx=10)
        self.entry_price.grid(row=3, column=1, padx=10)
        warehouseID_product_label.grid(row=4, padx=10)
        self.entry_warehouseID_product.grid(row=4, column=1, padx=10)
        amountOfProduct_label.grid(row =5, padx = 10)
        self.entry_amountOfProduct.grid(row = 5, column = 1, padx = 10)
        submit_addNewProduct.grid(row = 6, column= 1, pady = 0, padx = 10)
        submit_UpdatingProduct.grid(row = 7, column= 1, pady = 0, padx = 10)
        submit_RemoveProduct.grid(row = 8, column= 1, pady = 0, padx = 10)
        Warehouse_info.grid(row=9, column=0, columnspan=2, padx=10, pady=5)
        warehouseID_label.grid(row=10,padx=10)
        self.entry_warehouseID.grid(row=10, column=1, padx=10)
        warehouseAddress_label.grid(row=11, padx=10)
        self.entry_warehouseAddress.grid(row=11, column=1, padx=10)
        submit_addNewWarehouse.grid(row = 12, column= 1, pady = 0, padx = 10)
        submit_UpdatingWarehouse.grid(row = 13, column= 1, pady = 0, padx = 10)
        submit_RemoveWarehouse.grid(row = 14, column= 1, pady = 0, padx = 10)
        supplier_info.grid(row=15, column=0, columnspan=2, pady=5, padx=10,)
        supplierID_label.grid(row=16, padx=10)
        self.entry_supplierID.grid(row=16, column=1, padx=10)
        supplierName_label.grid(row=17, padx=10)
        self.entry_supplierName.grid(row=17, column=1, padx=10)
        supplierProduct_label.grid(row= 18, padx=10)
        self.entry_supplierProduct.grid(row=18, column=1, padx=10)
        supplierNumber_laber.grid(row=19, padx=10)
        self.entry_supplierNumber.grid(row=19, column=1, padx = 10)
        submit_addNewSupplier.grid(row=20, column =1, pady = 0, padx =10)
        submit_UpdatingSupplier.grid(row=21, column =1, pady = 0, padx =10)
        submit_RemoveSupplier.grid(row=22, column =1, pady = 0, padx =10)

        listbox_products_label = tk.Label(self.root, text = "All products (scroll down to see more)")
        listbox_products_label.grid(row=0, column= 3, columnspan=5)
        listbox_products = tk.Listbox(self.root, width= 40)
        listbox_products.grid(row = 1, rowspan= 7, column = 3, columnspan = 5, padx = 10)

        listbox_warehouses_label = tk.Label(self.root, text = "All warehouses (scroll down to see more)")
        listbox_warehouses_label.grid(row=9, column= 3, columnspan=5)
        listbox_warehouses = tk.Listbox(self.root, width= 40)
        listbox_warehouses.grid(row = 10, rowspan= 5, column = 3, columnspan = 5, padx = 10)


        listbox_suppliers_label = tk.Label(self.root, text = "All suppliers (scroll down to see more)")
        listbox_suppliers_label.grid(row=15, column= 3, columnspan=5)
        listbox_suppliers = tk.Listbox(self.root, width= 40)
        listbox_suppliers.grid(row = 16, rowspan= 7, column = 3, columnspan = 5, padx = 10)
    

        #printing proudcts in listbox
        c = self.conn.cursor()
        c.execute("SELECT * FROM product") 
        products = c.fetchall()
        #create loop to insert data into listbox
        for product in products:
            self.productID = product[0]
            self.productName = product[1]
            self.price = product[2]
            self.warehouseID = product[3]
            self.amountofproduct = product[4]
            listbox_products.insert(tk.END, f"{self.productID}: {self.productName}, {self.price} €, {self.warehouseID}, {self.amountofproduct} pcs")

        #printing warehouses in listbox
        c.execute("SELECT * FROM warehouse") 
        warehouses = c.fetchall()
        #create loop to insert data into listbox
        for warehouse in warehouses:
            self.warehouseID = warehouse[0]
            self.warehouse_city = warehouse[1]
            listbox_warehouses.insert(tk.END, f"{self.warehouseID}: {self.warehouse_city}")
            
    
    #printing suppliers in listbox
        c.execute("SELECT * FROM supplier") 
        suppliers = c.fetchall()
        #create loop to insert data into listbox
        for supplier in suppliers:
            self.supplierID = supplier[0]
            self.supplierName = supplier[1]
            self.productID = supplier[2]
            self.supplierContactNumber = supplier[3]
            listbox_suppliers.insert(tk.END, f"{self.supplierID}: {self.supplierName}, {self.productID} , {self.supplierContactNumber}")


    #create function for adding a new product   
    def submit_NewProduct(self):
        p_ID = self.entry_productID.get()
        p_name = self.entry_productName.get()
        p_price= self.entry_price.get()
        p_warehouseID= self.entry_warehouseID_product.get()
        p_amount= self.entry_amountOfProduct.get()
        if p_ID and p_name and p_price and p_warehouseID and p_amount:
            try: 
                c = self.conn.cursor()
                check_query = "SELECT productID FROM product WHERE productID = (%s)"
                c.execute(check_query, (p_ID,))
                fetched_ID = (c.fetchone())
                fetched_ID = str(fetched_ID)

                if fetched_ID == 'None':
                    c.execute("INSERT INTO product (productID, productName, price, warehouseID, amountofproduct) VALUES (%s, %s, %s, %s, %s)" ,
                        (p_ID,p_name,p_price, p_warehouseID, p_amount,))
                    messagebox.showinfo("Success", f"New product {p_ID} added succesfully!")

                else:
                    messagebox.showwarning("Warning",f"ID {p_ID} already exists!")
            except Exception as e:
                    messagebox.showerror("Error!", f"Error adding order: {e}")
        else:
            messagebox.showwarning("Warning!", "Please enter all the information.")

        #delete records from display
        self.entry_productID.delete(0, tk.END)   
        self.entry_productName.delete(0, tk.END)
        self.entry_price.delete(0, tk.END)
        self.entry_warehouseID.delete(0, tk.END)
        self.entry_amountOfProduct.delete(0,tk.END)

       

        self.conn.commit()
        self.createGUIproduct()


    #function for updating a product
    def submit_UpdateProduct(self):
        try:
            c = self.conn.cursor()
            check_query = "SELECT productID FROM product WHERE productID = (%s)"
            c.execute(check_query, (self.entry_productID.get(),))
            fetched_ID = (c.fetchone())
            fetched_ID = str(fetched_ID)

            if fetched_ID == 'None':
                messagebox.showwarning("Warning",f"Error: ID {self.entry_productID.get()} not found!")
                
            else:
                c.execute("UPDATE product SET productName = (%s), price = (%s), warehouseID = (%s), amountofproduct = (%s) WHERE productID = (%s)",
                    (self.entry_productName.get(), self.entry_price.get(), self.entry_warehouseID_product.get(), self.entry_amountOfProduct.get(), self.entry_productID.get(),))
                messagebox.showinfo("Success!",f"Product {self.entry_productID.get()} updated succesfully!")

            #delete records from display
            self.conn.commit()
            self.entry_productID.delete(0, tk.END)   
            self.entry_productName.delete(0, tk.END)
            self.entry_price.delete(0, tk.END)  
            self.entry_warehouseID_product.delete(0, tk.END)
            self.entry_amountOfProduct.delete(0,tk.END)
            

            self.createGUIproduct()

        except Exception as e:
            messagebox.showerror("Error", f"Error updating product: {e}")

    #delete product
    def submit_RemoveProduct(self):
        p_ID = self.entry_productID.get()

        if p_ID:
            try:
                c = self.conn.cursor()
                check_query = "SELECT productID FROM product WHERE productID = (%s)"
                c.execute(check_query, (p_ID,))
                fetched_ID = c.fetchone()
                fetched_ID = str(fetched_ID)
                
                if fetched_ID == 'None':
                    messagebox.showwarning("Warning",f"Error: ID {p_ID} not found!")
                else:    
                    c.execute("DELETE FROM product WHERE productID = (%s)", (p_ID,))
                    messagebox.showinfo("Success", "Product deleted successfully!")
            except Exception as e:
                messagebox.showerror("Error", f"Error deleting product: {e}")
        else:
            messagebox.showwarning("Warning", "Please enter the Product ID to delete.")
        
        self.conn.commit()
        self.entry_productID.delete(0, tk.END)   
        self.entry_productName.delete(0, tk.END)
        self.entry_price.delete(0, tk.END)  
        self.entry_warehouseID_product.delete(0, tk.END)
        self.entry_amountOfProduct.delete(0,tk.END)

        self.createGUIproduct()
    
        
    #Add new warehouse
    def submit_newWarehouse(self):
        w_ID = self.entry_warehouseID.get()
        w_Address = self.entry_warehouseAddress.get()
        if w_ID and w_Address:
            try:
                c = self.conn.cursor()
                c.execute("INSERT INTO warehouse (\"WarehouseID\", warehouse_city) VALUES (%s, %s)" ,
                (self.entry_warehouseID.get(), self.entry_warehouseAddress.get()))
                
                messagebox.showinfo("Success!", "Warehouse added successfully!")
            except Exception as e:
                messagebox.showerror("Error!", f"Error adding warehouse: {e}")
        else:
            messagebox.showwarning("Warning!", "Please enter all the information.")
    
        self.conn.commit()
        #delete records from display
        self.entry_warehouseID.delete(0, tk.END)   
        self.entry_warehouseAddress.delete(0, tk.END)  
        
        self.createGUIproduct()

    #update Warehouse
    def submit_updateWarehouse(self):
        w_ID = self.entry_warehouseID.get()
        w_Address = self.entry_warehouseAddress.get()

        if w_ID and w_Address:
            try:
                c = self.conn.cursor()
                check_query = "SELECT \"WarehouseID\" FROM warehouse WHERE \"WarehouseID\" = (%s) "
                c.execute(check_query, (w_ID,))
                fetched_ID = (c.fetchone())
                fetched_ID = str(fetched_ID)

                if fetched_ID == 'None':
                    messagebox.showerror("Error",f"Error: ID {w_ID} not found!")
                
                else:
                    c.execute("UPDATE warehouse SET warehouse_city = (%s) WHERE \"WarehouseID\" = (%s) ",
                        (w_Address, w_ID,))
                    messagebox.showinfo("Success!",f"Warehouse {w_ID} updated succesfully!")
            
            except Exception as e:
                messagebox.showerror("Error!", f"Error updating warehouse: {e}")
        
        else: 
            messagebox.showwarning("Warning!", "Please enter all the information.")

        self.conn.commit()    
        self.entry_warehouseID.delete(0, tk.END)   
        self.entry_warehouseAddress.delete(0, tk.END)

        self.createGUIproduct()  
    
    #delete warehouse

    def delete_Warehouse(self):
        w_ID = self.entry_warehouseID.get()
        if w_ID:
            try:
                c = self.conn.cursor()
                check_query = "SELECT \"WarehouseID\" FROM warehouse WHERE \"WarehouseID\"= (%s)"
                c.execute(check_query, (w_ID,))
                fetched_ID = (c.fetchone())
                fetched_ID = str(fetched_ID)

                if fetched_ID == 'None':
                    messagebox.showerror("Error",f"Error: ID {w_ID} not found!")
                
                else:
                    c.execute("DELETE FROM warehouse WHERE \"WarehouseID\" = (%s)",
                        (w_ID,))
                    messagebox.showinfo("Success!",f"Warehouse {w_ID} deleted succesfully!")
            
            except Exception as e:
                messagebox.showerror("Error!", f"Error deleting warehouse: {e}")
        else: 
            messagebox.showwarning("Warning!", "Please enter all the information.")

        self.conn.commit()          
        self.entry_warehouseID.delete(0, tk.END)   
        self.entry_warehouseAddress.delete(0, tk.END)

        self.createGUIproduct()  

    #add supplier
    
    def add_Supplier(self):
        s_ID = self.entry_supplierID.get()
        s_name = self.entry_supplierName.get()
        p_ID = self.entry_supplierProduct.get()
        s_number = self.entry_supplierNumber.get()


        if s_ID and s_name and p_ID:
            try:
                c = self.conn.cursor()
                c.execute("INSERT INTO supplier (\"SupplierID\", \"SupplierName\", \"ProductID\", \"SupplierContactNumber\") VALUES (%s, %s, %s, %s)" ,
                    (s_ID, s_name, p_ID, s_number,))
                messagebox.showinfo("Success!", "Supplier added successfully!")
            except Exception as e:
                messagebox.showerror("Error!", f"Error adding supplier: {e}")
                print(e)
        else:
            messagebox.showwarning("Warning!", "Please enter all the information.")
    
        self.conn.commit()
        #delete records from display
        self.entry_supplierID.delete(0, tk.END)  
        self.entry_supplierName.delete(0, tk.END)  
        self.entry_supplierProduct.delete(0, tk.END)  
        self.entry_supplierNumber.delete(0, tk.END)  

        self.createGUIproduct()

    def update_Supplier(self):
        s_ID = self.entry_supplierID.get()
        s_name = self.entry_supplierName.get()
        p_ID = self.entry_supplierProduct.get()
        s_number = self.entry_supplierNumber.get()

        if s_ID and s_name and p_ID and s_number:
            try:
                c = self.conn.cursor()
                c.execute("UPDATE supplier SET \"SupplierName\" = (%s), \"ProductID\" = (%s), \"SupplierContactNumber\"= (%s) WHERE \"SupplierID\" = (%s)" ,
                (s_name, p_ID, s_number,s_ID,))
                messagebox.showinfo("Success!", "Supplier updated successfully!")
            except Exception as e:
                messagebox.showerror("Error!", f"Error updating supplier: {e}")
        else:
            messagebox.showwarning("Warning!", "Please enter all the information.")
        
        self.conn.commit()  
        self.entry_supplierID.delete(0, tk.END)  
        self.entry_supplierName.delete(0, tk.END)  
        self.entry_supplierProduct.delete(0, tk.END)  
        self.entry_supplierNumber.delete(0, tk.END)  

        self.createGUIproduct()

    def delete_Supplier(self):
        s_ID = self.entry_supplierID.get()

        if s_ID:
            try:
                c = self.conn.cursor()
                check_query = "SELECT \"SupplierID\" FROM supplier WHERE \"SupplierID\"= (%s)"
                c.execute(check_query, (s_ID,))
                fetched_ID = (c.fetchone())
                fetched_ID = str(fetched_ID)

                if fetched_ID == 'None':
                    messagebox.showerror("Error",f"Error: ID {s_ID} not found!")
                
                else:
                    c.execute("DELETE FROM supplier WHERE \"SupplierID\" = (%s)",
                        (s_ID,))
                    messagebox.showinfo("Success!",f"Supplier {s_ID} deleted succesfully!")
            
            except Exception as e:
                messagebox.showerror("Error!", f"Error deleting supplier: {e}")
            
        self.conn.commit()  
        self.entry_supplierID.delete(0, tk.END)  
        self.entry_supplierName.delete(0, tk.END)  
        self.entry_supplierProduct.delete(0, tk.END)  
        self.entry_supplierNumber.delete(0, tk.END)  
    
        self.createGUIproduct()

    def runSelf(self):
        self.root.mainloop()

if __name__ == "__main__":
    root = tk.Tk()
    app = ProductManager(root)
    app.runSelf()







