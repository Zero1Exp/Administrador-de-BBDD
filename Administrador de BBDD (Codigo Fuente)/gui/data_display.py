import tkinter as tk
from tkinter import ttk
from gui.column_display import ColumnDisplay
from gui.row_display import RowDisplay


class DataDisplay(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.admin = self.parent.admin
        self.columns = []

        self.notebook = ttk.Notebook(self)
        self.column_display = ColumnDisplay(self)
        self.row_display = RowDisplay(self)

        self.notebook.add(self.column_display, text="Columnas")
        self.notebook.add(self.row_display, text="Filas")

        self.notebook.pack(padx=5, pady=5)

    def refresh(self, event):

        self.selected_table = event.widget.table_list.listbox.get(tk.ANCHOR)

        if self.selected_table in self.parent.admin.database.tables:
            self.columns = self.parent.admin.database.tables[self.selected_table].columns

            self.column_display.event_generate("<<ColumnChange>>")
            self.row_display.event_generate("<<RowChange>>")
