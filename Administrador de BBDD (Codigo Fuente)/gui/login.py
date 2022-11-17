import tkinter as tk


class Login(tk.Frame):
    def __init__(self, gui):
        super().__init__(gui)

        self.host = tk.StringVar(value="localhost")
        self.user = tk.StringVar(value="root")
        self.password = tk.StringVar(value="")

        tk.Label(self, text='Host').pack(anchor=tk.W)
        tk.Entry(self, textvariable=self.host).pack()
        tk.Label(self, text='Usuario').pack(anchor=tk.W)
        tk.Entry(self, textvariable=self.user).pack()
        tk.Label(self, text='Contraseña').pack(anchor=tk.W)
        tk.Entry(self, textvariable=self.password).pack()
        tk.Button(self, text='Confirmar', command=lambda: gui.connect_to_database(
            self.host.get(), self.user.get(), self.password.get())).pack(pady=15)
