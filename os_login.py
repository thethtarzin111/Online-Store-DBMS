import tkinter as tk
from tkinter import ttk, messagebox
import subprocess

class Login:
    def __init__(self, root):
        self.root = root
        self.root.title("Login")

        style = ttk.Style()
        style.configure("TLabel", padding=(10, 5), font=('Georgia', 20))
        style.configure("TEntry", padding=(5, 5), font=('Georgia', 13))
        style.configure("TButton", padding=(10, 5), font=('Georgia', 13))

        

        label_title = ttk.Label(self.root, text="Log in to verify your access")
        label_title.grid(row=0, column=0, pady=10, padx=10, sticky="w")

        label_username = ttk.Label(self.root, text="Username:")
        label_username.grid(row=1, column=0, pady=0, padx=10, sticky="e")

        self.entry_username = ttk.Entry(self.root)
        self.entry_username.grid(row=1, column=1, pady=10, padx=10, sticky="w")

        label_password = ttk.Label(self.root, text="Password:")
        label_password.grid(row=2, column=0, pady=10, padx=10, sticky="e")

        self.entry_password = ttk.Entry(self.root, show="*")
        self.entry_password.grid(row=2, column=1, pady=10, padx=10, sticky="w")

        button_login = ttk.Button(self.root, text="Login", command=self.check_login)
        button_login.grid(row=3, column=1, pady=20, padx=10, sticky="w")

    def check_login(self):
        
        if self.entry_username.get() == "noora" and self.entry_password.get() == "na123" or self.entry_username.get() == "thet" and self.entry_password.get() == "thz456":
            self.root.destroy()
            self.open_customer()
        else:
            messagebox.showerror("Login Failed!", "Invalid username or password! Please try again.")


    def open_customer(self):
        subprocess.run(["python3", "os_main.py"])

    # ... (rest of your open functions)

if __name__ == "__main__":
    root = tk.Tk()
    app = Login(root)
    root.mainloop()
