import tkinter as tk
from tkinter import ttk
from Controller import Controller

class Login(tk.Tk):
    def __init__(self, controller):
        super().__init__()

        self.controller = controller

        self.title("SNMP Watcher Login")
        self.geometry("300x200")
        self.resizable(0,0)

        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)

        #default theme -- we can retrieve here from db too
        source_path = "../include/Azure-ttk-theme/azure.tcl"
        self.tk.call("source", source_path)
        self.tk.call("set_theme", "dark")

        self.create_login_window()
        self.mainloop()
        
    def create_login_window(self):


        self.title_label = ttk.Label(self, text="SNMPv3 Credentials:", width=20)
        self.title_label.grid(column=0, row=0, columnspan=2, padx=5, pady=5)

        self.username_label = ttk.Label(self, text="Username:")
        self.username_label.grid(column=0, row=1, sticky=tk.E, padx=5, pady=5)

        self.username_entry = ttk.Entry(self)
        self.username_entry.grid(column=1, row=1, sticky=tk.W, padx=5, pady=5)

        self.password_label = ttk.Label(self, text="Password:", )
        self.password_label.grid(column=0, row=2, sticky=tk.E, padx=5, pady=5)

        self.password_entry = ttk.Entry(self, show="*")
        self.password_entry.grid(column=1, row=2, sticky=tk.W, padx=5, pady=5)

        self.login_button = ttk.Button(self, text="Login", width=10, command=lambda:self.loginButtonPressed(username_entry.get(), password_entry.get())
        self.login_button.grid(column=0, row=3, columnspan=2, padx=5, pady=5)
        
    def loginButtonPressed(self, username, password):
        sucess = self.controller.LoginSetUserCredentials(username, password)
        
        if sucess == True:
            self.controller.createAppView()
            self.destroy()
        else:
            self.username_entry.config({"background": "Red"})
            self.password_entry.config({"background": "Red"})
            print("Wrong credentials")