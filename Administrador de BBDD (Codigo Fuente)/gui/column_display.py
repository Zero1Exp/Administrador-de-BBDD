import tkinter as tk
from tkinter import ttk


class ColumnDisplay(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.config(height="250", width="230")

        columns = ["Nombre", "Tipo", "Longitud"]
        self.data_table = ttk.Treeview(self)
        self.data_table['columns'] = tuple(columns)
        self.data_table.column("#0", width=0,  stretch=tk.NO)

        for field in columns:
            self.data_table.column(field, anchor=tk.CENTER, width=80)
            self.data_table.heading(
                field, text=field.upper(), anchor=tk.CENTER)

        self.bind("<<ColumnChange>>", self.refresh)

        self.pack_propagate(0)
        self.data_table.pack(padx=5)

        self.scroll_x = ttk.Scrollbar(
            self, orient=tk.HORIZONTAL, command=self.data_table.xview)
        self.scroll_x.pack(fill=tk.BOTH)
        self.data_table.config(xscrollcommand=self.scroll_x.set)

    def refresh(self, _):
        self.data_table.delete(*self.data_table.get_children())

        if self.parent.columns:
            for index, column_name in enumerate(self.parent.columns):
                column = self.parent.columns[column_name]
                self.data_table.insert(parent='', index='end',
                                       iid=index, values=[column_name, column["type"], column["length"]])
