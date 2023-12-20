import tkinter as tk
from tkinter import ttk

# Создание окна
root = tk.Tk()
root.title("Пример таблицы")

# Создание виджета Treeview (таблицы)
tree = ttk.Treeview(root)

tree.grid(row=0, column=0)
tree.configure(width=400, height=300)
tree.configure(width=("chars", 50), height=("lines", 20))


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

# Запуск основного цикла
root.mainloop()
