import sys
import filling_in_db
from PyQt5.QtSql import QSqlDatabase, QSqlQuery
from PyQt5.QtWidgets import (
    QWidget,
    QPushButton,
    QApplication,
    QMainWindow,
    QMessageBox,
    QTableWidget,
    QTableWidgetItem,
)
class Contacts(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        if not createConnection():
            sys.exit(1)
        self.setWindowTitle("Банковские вклады")
        self.resize(1250, 800)

        self.view = QTableWidget(self)
        self.view.move(200, 200)
        self.view.resize(200,200)
        self.view.setColumnCount(6)
        self.view.setHorizontalHeaderLabels(["id", "bank_name", "deposit_name", "persentages", "amount", "term", "link"])
        query = QSqlQuery("SELECT * FROM data_bank")

        while query.next():
            rows = self.view.rowCount()
            self.view.setRowCount(rows + 1)
            self.view.setItem(rows, 0, QTableWidgetItem(str(query.value(0))))
            self.view.setItem(rows, 1, QTableWidgetItem(query.value(1)))
            self.view.setItem(rows, 2, QTableWidgetItem(query.value(2)))
            self.view.setItem(rows, 3, QTableWidgetItem(query.value(3)))
            self.view.setItem(rows, 4, QTableWidgetItem(query.value(4)))
            self.view.setItem(rows, 5, QTableWidgetItem(query.value(5)))
            self.view.setItem(rows, 6, QTableWidgetItem(query.value(6)))


        self.view.resizeColumnsToContents()
        self.setCentralWidget(self.view)
def createConnection():
    con = QSqlDatabase.addDatabase("QSQLITE")
    con.setDatabaseName("database/banking_statistics.sql")
    if not con.open():
        QMessageBox.critical(
            None,
            "QTableView Example - Error!",
            "Database Error: %s" % con.lastError().databaseText(),
        )
        return False
    return True
def update(self):
        try:
            self.btn_update.setText('Привет')
        except:
            pass


def main():
    app = QApplication(sys.argv)
    ex = Contacts()
    ex.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = Contacts()
    win.show()
    sys.exit(app.exec_())