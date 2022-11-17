import tkinter as tk
from tkinter import ttk


class Forms(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent

        self.db_name = tk.StringVar()
        self.table_name = tk.StringVar()
        self.column_entry = tk.StringVar()
        self.row_entry = tk.StringVar()

        # MODIFICAR BASES DE DATOS
        modify_db = tk.LabelFrame(self, text="Bases de Datos")
        tk.Entry(modify_db, textvariable=self.db_name).grid(
            row=0, column=0, columnspan=2, padx=3, pady=3)
        tk.Button(modify_db, text="Agregar", command=lambda: self.modify_db(
            "CREATE")).grid(row=1, column=0, padx=2, pady=2)
        tk.Button(modify_db, text="Eliminar", command=lambda: self.modify_db(
            "DELETE")).grid(row=1, column=1, padx=2, pady=2)

        modify_db.grid(row=0, column=0, padx=5, pady=5)

        # MODIFICAR TABLAS
        modify_table = tk.LabelFrame(self, text="Tablas")
        tk.Entry(modify_table, textvariable=self.table_name).grid(
            row=0, column=0, columnspan=3, padx=2, pady=2)
        tk.Button(modify_table, text="Agregar", command=lambda: self.modify_table(
            "CREATE")).grid(row=1, column=0, padx=2, pady=3)
        tk.Button(modify_table, text="Eliminar", command=lambda: self.modify_table(
            "DELETE")).grid(row=1, column=1, padx=2, pady=2)
        tk.Button(modify_table, text="Vaciar", command=lambda: self.modify_table(
            "TRUNCATE")).grid(row=1, column=2, padx=2, pady=2)

        modify_table.grid(row=0, column=1, padx=5, pady=5)

        # MODIFICAR COLUMNAS
        # NO TERMINADO
        modify_column = tk.LabelFrame(self, text="Columnas")
        tk.Entry(modify_column, textvariable=self.column_entry).grid(
            row=0, column=0, columnspan=4, padx=2, pady=2)
        tk.Button(modify_column, text="Agregar", command=lambda: self.modify_column(
            "CREATE")).grid(row=1, column=0, padx=2, pady=3)
        tk.Button(modify_column, text="Eliminar", command=lambda: self.modify_column(
            "DELETE")).grid(row=1, column=1, padx=2, pady=2)

        modify_column.grid(row=0, column=2, padx=5, pady=5)

        # MODIFICAR FILAS
        # NO TERMINADO
        modify_row = tk.LabelFrame(self, text="Filas")
        tk.Entry(modify_row, textvariable=self.row_entry).grid(
            row=0, column=0, columnspan=5, padx=2, pady=2)
        tk.Button(modify_row, text="Agregar", command=lambda: self.modify_row("CREATE")).grid(
            row=1, column=0, padx=2, pady=3)
        tk.Button(modify_row, text="Eliminar", command=lambda: self.modify_row("DELETE")).grid(
            row=1, column=1, padx=2, pady=2)

        modify_row.grid(row=0, column=3, padx=5, pady=5)

    def on_table_change(self, event):
        self.table_name.set(event.widget.table_list.listbox.get(tk.ANCHOR))

    def on_db_change(self, event):
        self.db_name.set(event.widget.db_list.listbox.get(tk.ANCHOR))

    def modify_row(self, type):
        if type == "CREATE":
            values = tuple(self.row_entry.get().split(","))
            self.parent.admin.database.tables[self.table_name.get()].insert_row(
                values)
        elif type == "DELETE":
            self.parent.admin.database.tables[self.table_name.get()].delete_row(
                self.row_entry.get())

        self.parent.event_generate("<<RowUpdate>>")

    def modify_column(self, type):
        if type == "CREATE":
            self.parent.admin.database.tables[self.table_name.get()].add_column(
                self.column_entry.get())
        elif type == "DELETE":
            self.parent.admin.database.tables[self.table_name.get()].delete_column(
                self.column_entry.get())

        self.parent.event_generate("<<ColumnUpdate>>")

    def modify_table(self, type):
        if type == "CREATE":
            self.parent.admin.database.create_table(self.table_name.get())
        elif type == "DELETE":
            self.parent.admin.database.delete_table(self.table_name.get())
        elif type == "TRUNCATE":
            self.parent.admin.database.truncate_table(self.table_name.get())
            return self.parent.event_generate("<<TableTruncate>>")

        self.parent.event_generate("<<TableUpdate>>")

    def modify_db(self, type):
        if type == "CREATE":
            self.parent.admin.create_database(self.db_name.get())
        elif type == "DELETE":
            self.parent.admin.delete_database(self.db_name.get())

        self.parent.event_generate("<<DatabaseUpdate>>")
