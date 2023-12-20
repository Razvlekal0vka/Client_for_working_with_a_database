import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QTableWidget
from PyQt5 import QtCore


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Мое оконное приложение")
        self.resize(960, 540)  # Установка размеров окна
        self.move(100, 100)  # Установка положения окна

        """Создание таблицы"""
        table = QTableWidget(10, 5)  # Создание таблицы с 10 строками и 5 столбцами
        table.setFixedSize(600, 200)  # Установка фиксированного размера таблицы

        # Создание вертикального контейнера для таблицы
        layout = QVBoxLayout()
        layout.addWidget(table)
        layout.setAlignment(QtCore.Qt.AlignBottom)  # Подвинуть таблицу вниз

        # Создание основного виджета и установка в него контейнера с таблицей
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
