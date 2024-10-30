from datetime import datetime
import sqlite3

def connect_db():
    return sqlite3.connect('database_tasks.db')

def create_table():
    with connect_db() as connect:
        connect.execute("""
            CREATE TABLE IF NOT EXISTS tasks (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                description TEXT NOT NULL,
                status TEXT NOT NULL CHECK (status IN ('выполняется', 'завершена')),
                created TEXT NOT NULL
            )
        """)
    print("Таблица 'tasks' готова.")

def add_task(description):
    created = datetime.now().strftime('%Y-%m-%d %H:%M')
    with connect_db() as connect:
        connect.execute("INSERT INTO tasks (description, status, created) VALUES (?, 'выполняется', ?)",
                        (description, created))
    print("Задача успешно добавлена.")

def task_update_status(task_id, new_status):
    if new_status not in ('выполняется', 'завершена'):
        print("Ошибка: допустимые статусы - 'выполняется' или 'завершена'.")
        return
    with connect_db() as connect:
        connect.execute("UPDATE tasks SET status = ? WHERE id = ?", (new_status, task_id))
    print(f"Статус задачи с ID {task_id} обновлен.")

def del_task_with_id(del_task_id):
    with connect_db() as connect:
        connect.execute("DELETE FROM tasks WHERE id = ?", (del_task_id,))
    print(f"Задача с ID {del_task_id} удалена.")

def delete_all_task():
    with connect_db() as connect:
        connect.execute("DELETE FROM tasks")
    print("Все задачи удалены.")

def delete_table():
    with connect_db() as connect:
        connect.execute("DROP TABLE IF EXISTS tasks")
    print("Таблица 'tasks' удалена.")

def view_all_tasks():
    with connect_db() as connect:
        tasks = connect.execute("SELECT * FROM tasks ORDER BY created").fetchall()
        if tasks:
            print("\nСписок всех задач:")
            for task in tasks:
                print(f"ID: {task[0]}, Описание: {task[1]}, Статус: {task[2]}, Дата: {task[3]}")
        else:
            print("Задачи отсутствуют.")

def search_task_status(status):
    with connect_db() as connect:
        tasks = connect.execute("SELECT * FROM tasks WHERE status = ?", (status,)).fetchall()
        if tasks:
            print(f"\nЗадачи со статусом '{status}':")
            for task in tasks:
                print(f"ID: {task[0]}, Описание: {task[1]}, Дата: {task[3]}")
        else:
            print(f"Задачи со статусом '{status}' не найдены.")

def search_task_id(search_id):
    with connect_db() as connect:
        task = connect.execute("SELECT * FROM tasks WHERE id = ?", (search_id,)).fetchone()
        if task:
            print(f"\nЗадача с ID {task[0]}:\nОписание: {task[1]}, Статус: {task[2]}, Дата: {task[3]}")
        else:
            print(f"Задача с ID {search_id} не найдена.")

def main():
    create_table()
    actions = {
        '1': create_table,
        '2': lambda: add_task(input("Введите описание задачи: ")),
        '3': lambda: task_update_status(
            int(input("Введите ID задачи: ")),
            input("Введите новый статус (выполняется/завершена): ")
        ),
        '4': lambda: del_task_with_id(int(input("Введите ID задачи для удаления: ")) ),
        '5': delete_all_task,
        '6': delete_table,
        '7': view_all_tasks,
        '8': lambda: search_task_status(input("Введите статус для поиска (выполняется/завершена): ")),
        '9': lambda: search_task_id(int(input("Введите ID для поиска: "))),
    }

    while True:
        print(
            "\n1. Создать саму таблицу\n"
            "2. Добавить задачу\n"
            "3. Обновить статус задачи\n"
            "4. Удалить задачу по ID\n"
            "5. Удалить все задачи\n"
            "6. Удалить саму таблицу\n"
            "7. Посмотреть все задачи\n"
            "8. Поиск по статусу\n"
            "9. Поиск по ID\n"
            "10. Выход"
        )
        choice = input("Выберите действие: ")
        if choice in actions:
            actions[choice]()
        elif choice == '10':
            print('Выход из программы.')
            break
        else:
            print('Неверный вели, попробуйте снова.')

main()
