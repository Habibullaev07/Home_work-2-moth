import sqlite3

class DatabaseManager:
    def init(self, db_name):
        self.db_name = db_name
        self.connection = None

    def open_connection(self):

        if self.connection is None:
            self.connection = sqlite3.connect(self.db_name)
        return self.connection

    def close_connection(self):

        if self.connection:
            self.connection.close()
            self.connection = None

    def find_user_by_name(self, username):

        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM users WHERE name = ?", (username,))
        return cursor.fetchone()

class User:
    def init(self, db_manager, name, email):
        self.db_manager = db_manager
        self.name = name
        self.email = email

    def add_user(self):
        cursor = self.db_manager.open_connection().cursor()
        cursor.execute("INSERT INTO users (name, email) VALUES (?, ?)", (self.name, self.email))
        self.db_manager.connection.commit()

    def get_user_by_id(self, user_id):
    
        cursor = self.db_manager.open_connection().cursor()
        cursor.execute("SELECT * FROM users WHERE id = ?", (user_id,))
        return cursor.fetchone()

    def delete_user(self, user_id):
        cursor = self.db_manager.open_connection().cursor()
        cursor.execute("DELETE FROM users WHERE id = ?", (user_id,))
        self.db_manager.connection.commit()

class Admin(User):
    def init(self, db_manager, name, email, privileges):
        super().init(db_manager, name, email)
        self.privileges = privileges

    def add_admin(self):

        cursor = self.db_manager.open_connection().cursor()
        cursor.execute("INSERT INTO admins (name, email, privileges) VALUES (?, ?, ?)", 
                       (self.name, self.email, self.privileges))
        self.db_manager.connection.commit()

class Customer(User):
    def init(self, db_manager, name, email, address):

        super().init(db_manager, name, email)
        self.address = address

    def add_customer(self):
        cursor = self.db_manager.open_connection().cursor()
        cursor.execute("INSERT INTO customers (name, email, address) VALUES (?, ?, ?)", 
                       (self.name, self.email, self.address))
        self.db_manager.connection.commit()

db_manager = DatabaseManager('example.db')
db_manager.open_connection()


with db_manager.connection:
    cursor = db_manager.connection.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT, email TEXT)")
    cursor.execute("CREATE TABLE IF NOT EXISTS admins (id INTEGER PRIMARY KEY, name TEXT, email TEXT, privileges TEXT)")
    cursor.execute("CREATE TABLE IF NOT EXISTS customers (id INTEGER PRIMARY KEY, name TEXT, email TEXT, address TEXT)")

