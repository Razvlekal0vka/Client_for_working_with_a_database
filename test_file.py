import sqlite3  # импортируем библиотеку для работы с SQLite

conn = sqlite3.connect('example.db')  # создаем соединение с базой данных
cur = conn.cursor()  # получаем курсор для выполнения запросов

cur.execute(''' CREATE TABLE IF NOT EXISTS example (
                id integer PRIMARY KEY, 
                name text, 
                age integer
              ) ''')  # создаем таблицу "example" в базе данных
conn.commit()  # сохраняем изменения

entries = [
    {'name': 'Alice', 'age': 18},
    {'name': 'Bob', 'age': 20}
]

for entry in entries:
    cur.execute(f''' INSERT INTO example (name, age) 
                     VALUES ({entry['name']}, {entry['age']}) ''')
    conn.commit()

result = cur.execute('SELECT * FROM example').fetchall()  # выбираем все записи из таблицы
for row in result:
    print(row)

cur.close()  # закрываем курсор
conn.close()  # закрываем соединение
