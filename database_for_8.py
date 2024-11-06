import sqlite3

class DataBase:
    def __init__(self, db_notes='db_notes.db'):
        self.connect = sqlite3.connect(db_notes)
        self.cursor = self.connect.cursor()
        
    def create_table(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS notes(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                content TEXT NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
    ''')
        
    def add_note(self, add_title, add_content):
        self.cursor.execute("INSERT INTO notes (title, content) VALUES (?, ?)",
                            (add_title, add_content))
        self.connect.commit()
        print("Успешно добавлено")
    
    def review_notes(self):
        self.cursor.execute("SELECT * FROM notes")
        review = self.cursor.fetchall()
        for reviews in review:
                print(
f"ID: {reviews[0]}, Заголовок: {reviews[1]}, Содержание: {reviews[2]}, Дата создание: {reviews[3]},"
        )
     
    def update_note(self, num):
        if num == 1:
            updated_title = input("Ведите обновленный заголовок: ")
            id_note = int(input("Ведите id Заметки: "))
            print("Успешно заменен")
            
            self.cursor.execute("UPDATE notes SET title = ? WHERE id = ?", 
                                (updated_title, id_note))
        elif num == 2:
            updated_content = input("Ведите обновленный содержание: ")
            id_note = id_note = int(input("Ведите id Заметки: "))
            print("Успешно заменен")
            
            self.cursor.execute("UPDATE notes SET content = ? WHERE id = ?", 
                                (updated_content, id_note))   
        elif num == 3:
            updated_title = input("Ведите обновленный заголовок: ")
            updated_content = input("Ведите обновленный содержание: ")
            id_note = id_note = int(input("Ведите id Заметки: "))
            
            self.cursor.execute("UPDATE notes SET title = ?, content = ? WHERE id = ?",
                                (updated_title, updated_content, id_note))
            print("Успешно заменен")
        else:
            print('Не правильно виден цифра: Повторите')
            
            
        self.connect.commit()
        
    def del_note(self, id_note):
        review = self.cursor.execute("SELECT id FROM notes").fetchall()
        for reviews in review:
            reviews
            if id_note in reviews:
                self.cursor.execute("DELETE FROM notes WHERE  id = ?", (id_note,))
                self.connect.commit()
                print('Успешно удалено')
                break
        else:
            print("не имеется")

            
       
    def close_connect(self):
        self.connect.close()