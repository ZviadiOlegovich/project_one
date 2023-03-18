import mysql.connector

# Подключение к базе данных
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Ford2008",
    database="todo",
    port="33306"
)

# Создание курсора для выполнения запросов
cursor = db.cursor()

# Функция добавления задачи
def add_task():
    task = input("Введите название задачи: ")
    query = "INSERT INTO tasks (title) VALUES (%s)"
    values = (task,)
    cursor.execute(query, values)
    db.commit()
    print("Задача добавлена!")

# Функция удаления задачи
def remove_task():
    task_number = input("Введите номер задачи, которую нужно удалить: ")
    query = "SELECT * FROM tasks"
    cursor.execute(query)
    tasks = cursor.fetchall()
    if task_number.isdigit() and int(task_number) <= len(tasks):
        task_id = tasks[int(task_number) - 1][0]
        query = "DELETE FROM tasks WHERE id = %s"
        values = (task_id,)
        cursor.execute(query, values)
        db.commit()
        print("Задача удалена!")
    else:
        print("Неверный номер задачи.")

# Функция вывода списка задач
def show_tasks():
    query = "SELECT * FROM tasks"
    cursor.execute(query)
    tasks = cursor.fetchall()
    if len(tasks) > 0:
        print("Список задач:")
        for i, task in enumerate(tasks):
            print(f"{i+1}. {task[1]}")
    else:
        print("Список задач пуст.")

# Цикл для ввода команд
while True:
    print("Доступные команды: add, remove, show, exit")
    command = input("Введите команду: ")
    if command == "add":
        add_task()
    elif command == "remove":
        remove_task()
    elif command == "show":
        show_tasks()
    elif command == "exit":
        break
    else:
        print("Неверная команда. Попробуйте еще раз.")
