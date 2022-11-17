import pymysql
from .database import Database


class MySQL():
    def __init__(self, host, user, password):
        self.host, self.user, self.password = host, user, password
        self.connection = pymysql.connect(
            host=self.host, user=self.user, password=self.password, charset="utf8mb4", cursorclass=pymysql.cursors.DictCursor)

        self.cursor = self.connection.cursor()
        self.database = None

    def select_database(self, database):
        database_connection = pymysql.connect(
            host=self.host, user=self.user, password=self.password, db=database, charset="utf8mb4", cursorclass=pymysql.cursors.DictCursor)

        self.database = Database(database, database_connection)

    def delete_database(self, name):
        query = f"DROP DATABASE {name}"
        self.cursor.execute(query)

        return

    def get_databases(self):
        query = f"SHOW DATABASES"
        self.cursor.execute(query)

        databases = []

        for result in self.cursor.fetchall():
            database_name = result["Database"]

            if database_name == "information_schema":
                continue

            databases.append(database_name)

        return databases

    def create_database(self, name):
        query = f"CREATE DATABASE {name}"
        self.cursor.execute(query)

        return
