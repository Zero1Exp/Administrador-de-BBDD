import tkinter as tk
from gui.application import Application
from gui.login import Login
from database.mysql import MySQL


class GUI(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Administrador de BBDD")
        self.resizable(False, False)
        self.geometry("700x400")
        self.admin = None
        self.iconbitmap("./icon.ico")

        self.content = Login(self)
        self.content.pack(expand=True, anchor=tk.CENTER)

    def connect_to_database(self, host, user, password):
        self.admin = MySQL(host, user, password)

        self.content.destroy()
        self.content = Application(self, self.admin)
        self.content.pack()

    def render(self):
        self.mainloop()
