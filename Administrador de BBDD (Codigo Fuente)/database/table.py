class Table():
    def __init__(self, name, cursor):
        self.name = name
        self.cursor = cursor

        self.columns = self.get_columns()
        self.rows = self.get_rows()

    def get_columns(self):
        query = f"DESCRIBE `{self.name}`"
        self.cursor.execute(query)

        columns = {}

        for result in self.cursor.fetchall():
            column_name = result['Field']
            column_type = result["Type"].split("(")[0]
            type_length = None

            if "(" in result["Type"]:
                type_length = result["Type"].split("(")[1].replace(")", "")

            columns[column_name] = {
                "type": column_type,
                "length": type_length,
            }

        return columns

    def get_rows(self):
        query = f"SELECT * FROM `{self.name}`"
        self.cursor.execute(query)

        rows = []

        for result in self.cursor.fetchall():
            parsed_result = []

            for key in result:
                parsed_result.append(result[key])

            rows.append(parsed_result)

        return rows

    def add_column(self, column):
        query = f"ALTER TABLE `{self.name}` ADD {column}"
        self.cursor.execute(query)

        self.columns = self.get_columns()
        self.rows = self.get_rows()

    def delete_column(self, column_name):
        query = f"ALTER TABLE {self.name} DROP COLUMN {column_name}"
        self.cursor.execute(query)

        self.columns = self.get_columns()
        self.rows = self.get_rows()

    def insert_row(self, data):
        query = f"INSERT INTO {self.name} ({','.join(column for column in self.columns)}) VALUES {data}"
        print(query)
        self.cursor.execute(query)

        self.columns = self.get_columns()
        self.rows = self.get_rows()

    def delete_row(self, condition):
        query = f"DELETE FROM {self.name} WHERE {condition}"
        self.cursor.execute(query)

        self.columns = self.get_columns()
        self.rows = self.get_rows()

    def update_row(self, data, condition):
        query = f"UPDATE {self.name} set {data} WHERE {condition}"
        self.cursor.execute(query)

        self.columns = self.get_columns()
        self.rows = self.get_rows()
