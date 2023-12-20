from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem

# Создание приложения
app = QApplication([])
window = QMainWindow()

# Создание виджета таблицы
table = QTableWidget(window)

# Установка количества строк и столбцов
table.setRowCount(3)  # Здесь можно указать нужное количество строк
table.setColumnCount(4)  # Здесь можно указать нужное количество столбцов

# Заполнение таблицы данными
table.setItem(0, 0, QTableWidgetItem("Ячейка 1"))
table.setItem(0, 1, QTableWidgetItem("Ячейка 2"))
table.setItem(0, 2, QTableWidgetItem("Ячейка 3"))
table.setItem(0, 3, QTableWidgetItem("Ячейка 4"))

# Отображение таблицы
table.resizeColumnsToContents()
window.setCentralWidget(table)
window.show()

# Запуск приложения
app.exec_()
