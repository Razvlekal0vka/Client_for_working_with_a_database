import pymysql

# Подключение к базе данных
connection = pymysql.connect(
    host='хост_базы_данных',
    user='имя_пользователя',
    password='пароль',
    database='имя_базы_данных'
)

# Создание объекта "курсор" для выполнения SQL-запросов
cursor = connection.cursor()


# Отображение содержимого таблицы
def show_table():
    query = "SELECT * FROM название_таблицы"
    cursor.execute(query)
    result = cursor.fetchall()

    for row in result:
        print(row)


# Добавление данных в таблицу
def add_data(name, age):
    query = f"INSERT INTO название_таблицы (name, age) VALUES ('{name}', {age})"
    cursor.execute(query)
    connection.commit()
    print("Данные успешно добавлены.")


# Редактирование данных в таблице
def edit_data(id, new_name):
    query = f"UPDATE название_таблицы SET name = '{new_name}' WHERE id = {id}"
    cursor.execute(query)
    connection.commit()
    print("Данные успешно обновлены.")


# Удаление данных из таблицы
def delete_data(id):
    query = f"DELETE FROM название_таблицы WHERE id = {id}"
    cursor.execute(query)
    connection.commit()
    print("Данные успешно удалены.")


# Пример использования функций
show_table()

add_data("Иван", 25)
show_table()

edit_data(1, "Петр")
show_table()

delete_data(2)
show_table()

# Закрытие соединения с базой данных
connection.close()
