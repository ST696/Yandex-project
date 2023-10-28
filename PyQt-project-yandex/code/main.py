import sys

from PyQt5 import uic  # Импортируем uic
from PyQt5.QtWidgets import QApplication, QMainWindow


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('file_ui/untitled.ui', self)  # Загружаем дизайн
        # Обратите внимание: имя элемента такое же как в QTDesigner
        self.button_save.clicked.connect(self.save_table)
        self.button_clear.clicked.connect(self.clear_table)
        self.button_start.clicked.connect(self.start)

    def start(self):
        print("start OK")

    def clear_table(self):
        print("clear table OK")

    def save_table(self):
        print("save OK")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())