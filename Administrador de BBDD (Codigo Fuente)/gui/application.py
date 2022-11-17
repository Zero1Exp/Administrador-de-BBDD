import tkinter as tk
from gui.db_list import DatabaseList
from gui.table_list import TableList
from gui.data_display import DataDisplay
from gui.forms import Forms


class Application(tk.Frame):
    def __init__(self, gui, admin):
        super().__init__(gui)
        self.admin = admin

        self.db_list = DatabaseList(self)
        self.table_list = TableList(self)
        self.data_display = DataDisplay(self)
        self.forms = Forms(self)

        self.grid_rowconfigure(0, weight=0)
        self.grid_rowconfigure(1, weight=0)
        self.grid_columnconfigure(0, weight=0)
        self.grid_columnconfigure(1, weight=0)
        self.grid_rowconfigure(2, weight=0)

        self.db_list.grid(row=0, column=0, padx=5, pady=5)
        self.table_list.grid(row=0, column=1, padx=5, pady=5)
        self.data_display.grid(row=0, column=2, padx=5, pady=5)
        self.forms.grid(row=1, column=0, columnspan=3,
                        sticky=tk.NSEW, padx="50")

        self.bind("<<DatabaseChange>>", self.on_database_change)
        self.bind("<<TableChange>>", self.on_table_change)
        self.bind("<<DatabaseUpdate>>", self.db_list.refresh)
        self.bind("<<TableUpdate>>", self.table_list.refresh)
        self.bind("<<ColumnUpdate>>", self.data_display.refresh)
        self.bind("<<RowUpdate>>", self.data_display.refresh)
        self.bind("<<TableTruncate>>", self.data_display.refresh)

    def on_table_change(self, event):
        self.data_display.refresh(event)
        self.forms.on_table_change(event)

    def on_database_change(self, event):
        self.table_list.refresh(event)
        self.forms.on_db_change(event)

    def render(self):
        self.mainloop()
