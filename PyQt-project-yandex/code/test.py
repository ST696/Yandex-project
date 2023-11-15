import sys
from deposit_calculator import result
from PyQt5.QtWidgets import QApplication, QTableWidget, QTableWidgetItem, QWidget, QPushButton
import sqlite3
import filling_in_db

class MyWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 300, 300)
        self.setFixedSize(450, 300)
        self.setWindowTitle('Банковские вклады')
        

       

    def update(self):
        try:
            self.btn.setText('Привет')
        except:
            pass
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())








    elif capitalization == "Ежеквартальная":
                if tip_replenishment == "ежедневно":
                    add_maney = sum_replenishment * 93
                    blok_add_maney = 1

                elif tip_replenishment == "ежемесячно":
                    add_maney = sum_replenishment * 3
                    blok_add_maney = 1

                elif tip_replenishment == "ежеквартально":
                    add_maney = sum_replenishment
                    blok_add_maney = 1

                elif tip_replenishment == "ежегодно":
                    add_maney = sum_replenishment
                    blok_add_maney = 4
                else:
                    add_maney = 0
                for quarter in range(1, days//93 + 1):
                    S=start_sum * (1+ (prosent/100)/4)**quarter
                    iteration += 1
                    time_file.write(f"период:{iteration};всего:{round(S, 2)};прибыль:{round(start_sum * ( 1 + (prosent/100)/12)**quarter - start_sum, 2)};пополнение:{sum_replenishment}\n")
                    if blok_add_maney == unblok_add_maney:
                        start_sum += add_maney
                        unblok_add_maney = 0
                    unblok_add_maney += 1

                print(f"итого: {round(S, 2)}")
                return(round(S, 2))



            elif capitalization == "Ежегодная":
                if tip_replenishment == "ежедневно":
                    add_maney = sum_replenishment * 365
                    blok_add_maney = 1

                elif tip_replenishment == "ежемесячно":
                    add_maney = sum_replenishment * 12
                    blok_add_maney = 1

                elif tip_replenishment == "ежеквартально":
                    add_maney = sum_replenishment * 4
                    blok_add_maney = 1

                elif tip_replenishment == "ежегодно":
                    add_maney = sum_replenishment
                    blok_add_maney = 1
                else:
                    add_maney = 0
                for year in range(1, days//365 + 1):
                    S=start_sum * (1+ (prosent/100))**year
                    iteration += 1
                    time_file.write(f"период:{iteration};всего:{round(S, 2)};прибыль:{round(start_sum * ( 1 + (prosent/100)/12)**year - start_sum, 2)};пополнение:{sum_replenishment}\n")
                    if blok_add_maney == unblok_add_maney:
                        start_sum += add_maney
                        unblok_add_maney = 0
                    unblok_add_maney += 1
                print(f"итого: {round(S, 2)}")
                return(round(S, 2))


            elif capitalization == "Ежедневная":
                if tip_replenishment == "ежедневно":
                    add_maney = sum_replenishment 
                    blok_add_maney = 1

                elif tip_replenishment == "ежемесячно":
                    add_maney = sum_replenishment
                    blok_add_maney = 31

                elif tip_replenishment == "ежеквартально":
                    add_maney = sum_replenishment
                    blok_add_maney = 93

                elif tip_replenishment == "ежегодно":
                    add_maney = sum_replenishment
                    blok_add_maney = 365
                else:
                    add_maney = 0
                for day in range(1, days + 1):
                    S = start_sum * (1 + (prosent/100) / 365)**day
                    iteration += 1
                    time_file.write(f"период:{iteration};всего:{round(S, 2)};прибыль:{round(start_sum * ( 1 + (prosent/100)/12)**day - start_sum, 2)};пополнение:{sum_replenishment}\n")
                    if blok_add_maney == unblok_add_maney:
                        start_sum += add_maney
                        unblok_add_maney = 0
                    unblok_add_maney += 1