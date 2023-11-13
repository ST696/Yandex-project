import sys
from deposit_calculator import result
from PyQt5 import uic
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidget,QTableWidgetItem


class MyWidget(QMainWindow):
    def __init__(self):
        try:
            super().__init__()
            
            uic.loadUi('file_ui/untitled_2.ui', self)
            self.button_save.clicked.connect(self.save_table)
            self.button_clear.clicked.connect(self.clear_table)
            self.button_start.clicked.connect(self.start)
            self.button_choose_deposite.clicked.connect(self.choose_deposite)
            if self.sum_start_deposit.text() == '':
                self.sum_start_deposit.setText('0')
            if self.iterest_rate.text() == '':
                self.iterest_rate.setText('0')
            if self.sum_replenishment.text() == '':
                self.sum_replenishment.setText('0')
            if self.deposite_date.text() == '':
                self.deposite_date.setText('0')
            dialog = QFileDialog(self)
            dialog.setFileMode(QFileDialog.AnyFile)
            # create table
            
            self.rows_table = 10
            self.COLUMNS_TABLES = 10
            self.table_res = QTableWidget(10, 4, self)
            self.table_res.move(25, 220)
            self.table_res.resize(700, 470)
        except Exception as ex:
            print(ex)
    

    def choose_deposite(self):
        print("choose OK")


    def start(self):
        try:
            if self.sum_start_deposit.text() == '':
                self.sum_start_deposit.SetText('0')
            if self.iterest_rate.text() == '':
                self.iterest_rate.SetText('0')
            if self.sum_replenishment.text() == '':
                self.sum_replenishment.SetText('0')
            if self.deposite_date.text() == '':
                self.deposite_date.SetText('0')
                   
            variables = {
                "sum_start_deposit": int(self.sum_start_deposit.text()),
                "iterest_rate": int(self.iterest_rate.text()),
                "capitalization": self.capitalization.currentText(),
                "data_tip": self.date_tip_deposit.currentText(),
                "sum_replenishment": int(self.sum_replenishment.text()),
                "tip_replenishment": self.replenishment_period.currentText(),
                "term_deposit": int(self.deposite_date.text())
            }
            res = result(variables)
            print(F"***********{res}***********")

            with open("time_file/time_res.txt", "r") as time_file:
                res = time_file.read().split('\n')
                newItem1 = QTableWidgetItem(res[0].split(";")[0].split(':')[0])
                newItem2 = QTableWidgetItem(res[0].split(";")[1].split(':')[0])
                newItem3 = QTableWidgetItem(res[0].split(";")[2].split(':')[0])
                newItem4 = QTableWidgetItem(res[0].split(";")[3].split(':')[0])

                self.table_res.setItem(0, 0, newItem1)
                self.table_res.setItem(0, 1, newItem2)
                self.table_res.setItem(0, 2, newItem3)
                self.table_res.setItem(0, 3, newItem4)

                for row in range(1, len(res) - 1):
                    for column in range(self.COLUMNS_TABLES):
                        newItem = QTableWidgetItem(res[row - 1].split(";")[column].split(':')[1])
                        self.table_res.setItem(row, column, newItem)


        except Exception as ex:
            print(ex)
            print("******************какая-то ошибка******************")

        print("start OK")

    def clear_table(self):
        row_count = 10
        for row in range(row_count):
            for column in range(self.COLUMNS_TABLES):
                newItem = QTableWidgetItem("")
                self.table_res.setItem(row, column, newItem)
        print("clear table OK")

    def save_table(self):
        print("save OK")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())