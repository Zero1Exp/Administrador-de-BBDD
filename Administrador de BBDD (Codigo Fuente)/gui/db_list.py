import tkinter as tk


class DatabaseList(tk.LabelFrame):
    def __init__(self, parent):
        super().__init__(parent, text="Bases de Datos")
        self.parent = parent
        self.config(height="275", width="175")

        self.listbox = tk.Listbox(self)

        self.listbox.insert(0, *parent.admin.get_databases())

        self.pack_propagate(0)
        self.listbox.pack(padx=5)
        self.listbox.config(height="15", width="30")

        self.listbox.bind('<<ListboxSelect>>', self.on_select)

    def refresh(self, _):
        self.listbox.delete(0, tk.END)
        self.listbox.insert(0, *self.parent.admin.get_databases())

    def on_select(self, event):
        self.parent.admin.select_database(event.widget.get(tk.ANCHOR))
        self.parent.event_generate("<<DatabaseChange>>")
