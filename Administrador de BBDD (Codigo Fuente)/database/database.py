from .table import Table


class Database():
    def __init__(self, name, connection):
        self.name = name
        self.connection = connection
        self.cursor = connection.cursor()

        self.tables = self.inyect_tables()

    def inyect_tables(self):
        query = f"SHOW TABLES"
        self.cursor.execute(query)

        tables = {}

        for result in self.cursor.fetchall():
            table_name = result[f"Tables_in_{self.name}"]
            tables[table_name] = Table(table_name, self.cursor)

        return tables

    def create_table(self, name):
        query = f"CREATE TABLE `{name}` (`id` INT NOT NULL AUTO_INCREMENT , PRIMARY KEY (`id`))"

        self.cursor.execute(query)

        self.tables = self.inyect_tables()

        return

    def delete_table(self, name):
        query = f"DROP TABLE `{name}`"
        self.cursor.execute(query)

        self.tables = self.inyect_tables()

        return

    def truncate_table(self, name):
        query = f"TRUNCATE TABLE `{name}`"
        self.cursor.execute(query)

        self.tables = self.inyect_tables()
