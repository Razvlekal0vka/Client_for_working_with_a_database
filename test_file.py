import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QHBoxLayout, QPushButton, QWidget, QTableWidget, QVBoxLayout


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Мое оконное приложение")
        self.resize(960, 540)  # Установка размеров окна
        self.move(100, 100)  # Установка положения окна

        # Создание горизонтального контейнера для кнопок
        # layout = QHBoxLayout()  # Хз что это делает, тк это есть в коде только для таблиц,
        # но вроде это отвечает за расположение и какую-то там сетку

        """Создание кнопок"""
        button_add = QPushButton("Добавить", self)
        button_edit = QPushButton("Редактировать", self)
        button_delete = QPushButton("Удалить", self)

        # Настройка размеров кнопок
        button_add.setFixedSize(100, 30)
        button_edit.setFixedSize(100, 30)
        button_delete.setFixedSize(100, 30)

        # Настройка расположения кнопок
        button_add.move(10, 10)
        button_edit.move(120, 10)
        button_delete.move(230, 10)

        """Создание таблицы"""
        table = QTableWidget(10, 5)  # Создание таблицы с 10 строками и 5 столбцами

        table.setFixedSize(960, 400)  # Установка фиксированного размера таблицы
        # table.move(200, 400) - не работает

        # Создание вертикального контейнера для таблицы
        layout = QVBoxLayout()
        layout.addWidget(table)

        # Создание основного виджета и установка в него контейнера
        widget = QWidget()
        widget.setLayout(layout)

        # Установка основного виджета в главное окно
        self.setCentralWidget(widget)

        self.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
