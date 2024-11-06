from database_for_8 import DataBase

def menu():
    database = DataBase()
    database.create_table()
    all_func = {
        '1': lambda: database.add_note(
            input("Ведите заголовок заметки: "),
            input("Ведите содержание заметки: ")
            ),
        '2': database.review_notes,
        '3': lambda: database.update_note(
            int(input('''\n1. Изменить заголовок\n2. Изменить содержание
3. Изменить заголовок и содержание \n\nВыберите еще одно действие: '''))
            ),
        '4': lambda: database.del_note(int(input("Ведите id Заметки: ")))
    }
    
    while True:
        print(
            "\n1. Добавить заметку.\n"
            "2. Посмотреть все заметки.\n"
            "3. Редактировать заметку.\n"
            "4. Удалить заметку.\n"
            "5. Выйти.\n"
        )
        choice = input("Выберите действия: ")
        if choice in all_func:
            all_func[choice]()
        elif choice == '5':
            print("Выход из программы")
            break
        else:
            print("Неверно веден, повторите")
            
    database.close_connect()
menu()
        
        