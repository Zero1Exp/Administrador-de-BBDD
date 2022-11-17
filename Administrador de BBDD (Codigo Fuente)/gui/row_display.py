import tkinter as tk
from tkinter import ttk


class RowDisplay(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.config(height="250", width="230")
        self.bind("<<RowChange>>", self.refresh)

        self.data_table = ttk.Treeview(self)

        self.pack_propagate(0)
        self.data_table.pack(padx=5)

        self.scroll_x = ttk.Scrollbar(
            self, orient=tk.HORIZONTAL, command=self.data_table.xview)
        self.scroll_x.pack(fill=tk.BOTH)
        self.data_table.config(xscrollcommand=self.scroll_x.set)

    def refresh(self, _):
        self.data_table.delete(*self.data_table.get_children())

        columns = [column.upper() for column in self.parent.columns]
        self.data_table['columns'] = tuple(columns)
        self.data_table.column("#0", width=0,  stretch=tk.NO)

        for field in columns:
            self.data_table.column(
                field, anchor=tk.CENTER, stretch=tk.NO, width=50)
            self.data_table.heading(
                field, text=field.upper(), anchor=tk.CENTER)

        if self.parent.columns:
            for index, row in enumerate(self.parent.admin.database.tables[self.parent.selected_table].rows):
                self.data_table.insert(parent='', index='end',
                                       iid=index, values=row)
