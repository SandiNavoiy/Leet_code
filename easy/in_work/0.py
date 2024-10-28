# Создайте классы Database MySQLDatabase и PostgreSQLDatabase
from abc import ABC, abstractmethod


class Database(ABC):
    @abstractmethod
    def connect(self):
        pass

    @abstractmethod
    def execute(self, query):
        pass

    @abstractmethod
    def disconnect(self):
        pass

class MySQLDatabase(Database):

    def connect(self):
        print("Connecting to MySQL database...")


    def execute(self, query):
        print(f"Executing query '{query}' in MySQL database...")


    def disconnect(self):
        print("Disconnecting from MySQL database...")

class PostgreSQLDatabase(Database):

    def connect(self):
        print("Connecting to PostgreSQL database...")


    def execute(self, query):
        print(f"Executing query '{query}' in PostgreSQL database...")


    def disconnect(self):
        print("Disconnecting from PostgreSQL database...")

# Код для проверки

mysql_db = MySQLDatabase()
postgresql_db = PostgreSQLDatabase()

mysql_db.connect()
mysql_db.execute(
    "SELECT * FROM customers;")
mysql_db.disconnect()

postgresql_db.connect()
postgresql_db.execute(
    "SELECT * FROM customers;")
postgresql_db.disconnect()