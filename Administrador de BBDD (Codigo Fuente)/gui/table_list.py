import tkinter as tk


class TableList(tk.LabelFrame):
    def __init__(self, parent):
        super().__init__(parent, text="Tablas")
        self.parent = parent
        self.config(height="275", width="175")

        self.listbox = tk.Listbox(self)

        if self.parent.admin.database:
            self.listbox.insert(
                0, *[table for table in self.parent.admin.database.tables])

        self.pack_propagate(0)
        self.listbox.pack(padx=5)
        self.listbox.config(height="15", width="30")

        self.listbox.bind('<<ListboxSelect>>', self.on_select)

    def refresh(self, _):
        self.listbox.delete(0, tk.END)
        if self.parent.admin.database:
            self.listbox.insert(
                0, *[table for table in self.parent.admin.database.tables])

    def on_select(self, _):
        self.parent.event_generate("<<TableChange>>")
