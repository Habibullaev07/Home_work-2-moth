import sqlite3
import time

def connect_database():
    return sqlite3.connect("library.db")

def create_table():
    with connect_database() as connect:
        connect.execute('''
            CREATE TABLE IF NOT EXISTS books (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT UNIQUE NOT NULL,
                author TEXT NOT NULL,
                year INTEGER NOT NULL       
        )
    ''')
  
def add_books():
    try:
        user_add_title = input("Добавьте название книги: ")
        user_add_author = input("Добавьте автора: ")
        user_add_year = int(input("Добавьте год выпуска: "))
        
        with connect_database() as connect:
            connect.execute("INSERT INTO books (title, author, year) VALUES (?, ?, ?)",
                (user_add_title, user_add_author, user_add_year))
            print("Успешно добавлен")
    except sqlite3.IntegrityError:
        print("Ошибка: книга с таким названием существует")
    except BaseException:
        print("Ошибка\n\tПишите цифры: на год выпуска")


def find_book_by_title():
    user_find_title = input("Ведите название книги для поиска: ")
    with connect_database() as connect:
        book = connect.execute("SELECT * FROM books WHERE title = ?",(user_find_title,)).fetchone()
        if book:
            print(f"Название: {book[1]} Автор: {book[2]} Год выпуска: {book[3]}")
        else:
            print(f"Такой книги: '{user_find_title}' Не найдено")
            
def update_book_year():
    try:
        user_wr_title_book = (input("Ведите название книги:"))
        user_update_year = int(input("Ведите обновленное значение: "))
        with connect_database() as connect:
            view_books = connect.execute("SELECT * FROM books WHERE title = ?",
                                        (user_wr_title_book,)).fetchall()
            if not view_books:
                print(f"Не правильно веден: название книги '{user_wr_title_book}' Не существует") 
            else:
                connect.execute("UPDATE books SET year = ? WHERE title = ?",
                    (user_update_year, user_wr_title_book))
                print("Успешно обновлен")
    except BaseException:
        print("Ошибка\n\tПишите цифры: на год выпуска")
        
def delete_book_by_title():
    user_delete_book = input("Ведите название книги для удаление: ")
    with connect_database() as connect:
        view_books = connect.execute("SELECT * FROM books WHERE title = ?",
                                     (user_delete_book,)).fetchone()
        if view_books is None:
            print(f"Не правильно веден:\n\tназвание книги '{user_delete_book}' Повторите попытку")
        else: 
            connect.execute("DELETE FROM books WHERE title = ?", (user_delete_book,))
            print("Успешно удален")
     
def view_all_books():
    with connect_database() as connect:
        view_all = connect.execute("SELECT * FROM books").fetchall()
        for all_books in view_all:
            print(f"Название: {all_books[1]} Автор: {all_books[2]} Год выпуска: {all_books[3]}")
        

def menu():
    create_table()
    all_func = {
        '1': add_books,
        '2': find_book_by_title,
        '3': update_book_year,     
        '4': delete_book_by_title,    
        '5': view_all_books,
           
    }
    while True:
        time.sleep(2)
        print(
            "\n1. Добавлять книгу.\n"
            "2. Искать книгу по названию.\n"
            "3. Обновлять год издания книги.\n"
            "4. Удалять книгу по названию.\n"
            "5. Просмотр всех книг.\n"
            "6. Выход из программы.\n"
        )

        user_choice = input("Выберите действие: ")
        if user_choice in all_func:
            all_func[user_choice]()
        elif user_choice == '6':
            print("Выход из программы")
            break
        else:
            print(f"Не правильно веден {user_choice} Попробуйте снова")
        
    
# create_table()
# add_books()
# find_book_by_title()
# update_book_year()
# delete_book_by_title()
menu()