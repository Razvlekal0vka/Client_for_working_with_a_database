import tkinter as tk
from tkinter import ttk

# Создание окна
root = tk.Tk()
root.title("Пример таблицы")

# Создание виджета Treeview (таблицы)
tree = ttk.Treeview(root)




# Определение колонок
tree["columns"] = ("Name", "Age", "Gender")

# Настройка заголовков колонок
tree.heading("#0", text="ID")
tree.heading("Name", text="Имя")
tree.heading("Age", text="Возраст")
tree.heading("Gender", text="Пол")

# Добавление данных в таблицу
tree.insert(parent="", index="end", text="1", values=("Alice", 25, "Female"))
tree.insert(parent="", index="end", text="2", values=("Bob", 30, "Male"))
tree.insert(parent="", index="end", text="3", values=("Charlie", 28, "Male"))
tree.insert(parent="", index="end", text="4", values=("Diana", 22, "Female"))

# Отображение таблицы
tree.pack()
tree.place(x=10, y=10, width=400, height=200)

# Запуск основного цикла
root.mainloop()


#def init():
#    window = tk.Tk()
#    window.geometry("200x480")
#    window.title("DB Client")