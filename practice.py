import sqlite3

class DatabaseManager:
    def __init__(self, db_name):
        self.db_name = db_name
        self.connection = None

    def open_connection(self):
        self.connection = sqlite3.connect(self.db_name)

    def close_connection(self):
        if self.connection:
            self.connection.close()

    def find_user_by_name(self, username):
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM users WHERE username = ?", (username,))
        return cursor.fetchone()

class User:
    def __init__(self, db_manager):
        self.db_manager = db_manager

    def create_table(self):
        self.db_manager.connection.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY,
                username TEXT,
                role TEXT
            )
        ''')

    def add_user(self, username, role):
        cursor = self.db_manager.connection.cursor()
        cursor.execute("INSERT INTO users (username, role) VALUES (?, ?)", (username, role))
        self.db_manager.connection.commit()

    def get_user_by_id(self, user_id):
        cursor = self.db_manager.connection.cursor()
        cursor.execute("SELECT * FROM users WHERE id = ?", (user_id,))
        return cursor.fetchone()

class Admin(User):
    def create_table(self):
        self.db_manager.connection.execute('''
            CREATE TABLE IF NOT EXISTS admins (
                id INTEGER PRIMARY KEY,
                username TEXT,
                permissions TEXT
            )
        ''')

    def add_admin(self, username, permissions):
        cursor = self.db_manager.connection.cursor()
        cursor.execute("INSERT INTO admins (username, permissions) VALUES (?, ?)", (username, permissions))
        self.db_manager.connection.commit()

class Customer(User):
    def create_table(self):
        self.db_manager.connection.execute('''
            CREATE TABLE IF NOT EXISTS customers (
                id INTEGER PRIMARY KEY,
                username TEXT,
                email TEXT
            )
        ''')

    def add_customer(self, username, email):
        cursor = self.db_manager.connection.cursor()
        cursor.execute("INSERT INTO customers (username, email) VALUES (?, ?)", (username, email))
        self.db_manager.connection.commit()

db_manager = DatabaseManager("manager.db")
db_manager.open_connection()

user_manager = User(db_manager)
user_manager.create_table()
user_manager.add_user("jamshid", "customer")

admin_manager = Admin(db_manager)
admin_manager.create_table()
admin_manager.add_admin("admin_jamshid", "all_permissions")

customer_manager = Customer(db_manager)
customer_manager.create_table()
customer_manager.add_customer("jamshid", "Zhabibullaev07@gmail.com")
customer_manager.add_customer("ali", "ali@gmaiil.com")
customer_manager.add_customer("farid", "farid@gmail.com")
customer_manager.add_customer("dilsho", "dilshod@gmail.com")

print(user_manager.get_user_by_id(1))
print(db_manager.find_user_by_name("jamshid"))

db_manager.connection.execute("INSERT INTO users (username, role) VALUES (?, ?)", ("amir", "customer"))
db_manager.connection.commit()
db_manager.connection.execute("INSERT INTO users (username, role) VALUES (?, ?)", ("sardor", "admin"))
db_manager.connection.commit()

db_manager.close_connection()