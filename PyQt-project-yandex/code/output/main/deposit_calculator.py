import sqlite3
import datetime

def result(variables):
    start_sum = variables["sum_start_deposit"]
    prosent = variables["iterest_rate"]
    capitalization = variables["capitalization"]
    tip_term_deposit = variables["data_tip"]
    term_deposit = variables["term_deposit"]
    tip_replenishment = variables["tip_replenishment"]
    sum_replenishment = variables["sum_replenishment"]

    
    term = {
        "лет": term_deposit * 365,
        "месяцев": term_deposit * 30,
        "дней": term_deposit 
    } 
    days = term[tip_term_deposit]
    try:
        iteration = 0
        with open("time_file/time_res.txt", "w") as time_file:
            if capitalization == "Ежемесячная":

                if tip_replenishment == "ежедневно":
                    sum_replenishment *= 31
                    for mounth in range(1, days//31 + 1):
                        S = start_sum * (1 + (prosent/100)/12)**mounth
                        iteration += 1
                        time_file.write(f"период:{iteration};всего:{round(S, 2)};прибыль:{round(start_sum * ( 1 + (prosent/100)/12)**mounth - start_sum, 2)};пополнение:{sum_replenishment}\n")
                        start_sum += sum_replenishment

                elif tip_replenishment == "ежемесячно":
                    for mounth in range(1, days//31 + 1):
                        S = start_sum * (1 + (prosent/100)/12)**mounth
                        iteration += 1
                        time_file.write(f"период:{iteration};всего:{round(S, 2)};прибыль:{round(start_sum * ( 1 + (prosent/100)/12)**mounth - start_sum, 2)};пополнение:{sum_replenishment}\n")
                        start_sum += sum_replenishment

                elif tip_replenishment == "ежеквартально":
                    for mounth in range(1, days//31 + 1):
                        add_sum = sum_replenishment
                        S = start_sum * (1 + (prosent/100)/12)**mounth
                        iteration += 1
                        if mounth % 4 == 0:
                            time_file.write(f"период:{iteration};всего:{round(S, 2)};прибыль:{round(start_sum * ( 1 + (prosent/100)/12)**mounth - start_sum, 2)};пополнение:{add_sum}\n")
                            start_sum += add_sum
                        else:
                            add_sum = 0
                            time_file.write(f"период:{iteration};всего:{round(S, 2)};прибыль:{round(start_sum * ( 1 + (prosent/100)/12)**mounth - start_sum, 2)};пополнение:{add_sum}\n")

                elif tip_replenishment == "ежегодно":
                    for mounth in range(1, days//31 + 1):
                        add_sum = sum_replenishment
                        S = start_sum * (1 + (prosent/100)/12)**mounth
                        iteration += 1
                        if mounth % 12 == 0:
                            time_file.write(f"период:{iteration};всего:{round(S, 2)};прибыль:{round(start_sum * ( 1 + (prosent/100)/12)**mounth - start_sum, 2)};пополнение:{add_sum}\n")
                            start_sum += add_sum
                        else:
                            add_sum = 0
                            time_file.write(f"период:{iteration};всего:{round(S, 2)};прибыль:{round(start_sum * ( 1 + (prosent/100)/12)**mounth - start_sum, 2)};пополнение:{add_sum}\n")


                print(f"итого: {round(S, 2)}")
                return(round(S, 2))
            elif capitalization == "Ежеквартальная":
                if tip_replenishment == "ежедневно":
                    sum_replenishment *= 93
                    for mounth in range(1, days//31 + 1):
                        S = start_sum * (1 + (prosent/100)/12)**mounth
                        iteration += 1
                        time_file.write(f"период:{iteration};всего:{round(S, 2)};прибыль:{round(start_sum * ( 1 + (prosent/100)/12)**mounth - start_sum, 2)};пополнение:{sum_replenishment}\n")
                        start_sum += sum_replenishment

                elif tip_replenishment == "ежемесячно":
                    sum_replenishment *= 4
                    for mounth in range(1, days//31 + 1):
                        S = start_sum * (1 + (prosent/100)/12)**mounth
                        iteration += 1
                        time_file.write(f"период:{iteration};всего:{round(S, 2)};прибыль:{round(start_sum * ( 1 + (prosent/100)/12)**mounth - start_sum, 2)};пополнение:{sum_replenishment}\n")
                        start_sum += sum_replenishment

                elif tip_replenishment == "ежеквартально":
                    for mounth in range(1, days//31 + 1):
                        S = start_sum * (1 + (prosent/100)/12)**mounth
                        iteration += 1
                        time_file.write(f"период:{iteration};всего:{round(S, 2)};прибыль:{round(start_sum * ( 1 + (prosent/100)/12)**mounth - start_sum, 2)};пополнение:{sum_replenishment}\n")
                        start_sum += sum_replenishment

                elif tip_replenishment == "ежегодно":
                    for mounth in range(1, days//31 + 1):
                        add_sum = sum_replenishment
                        S = start_sum * (1 + (prosent/100)/12)**mounth
                        iteration += 1
                        if mounth % 4 == 0:
                            time_file.write(f"период:{iteration};всего:{round(S, 2)};прибыль:{round(start_sum * ( 1 + (prosent/100)/12)**mounth - start_sum, 2)};пополнение:{add_sum}\n")
                            start_sum += add_sum
                        else:
                            add_sum = 0
                            time_file.write(f"период:{iteration};всего:{round(S, 2)};прибыль:{round(start_sum * ( 1 + (prosent/100)/12)**mounth - start_sum, 2)};пополнение:{add_sum}\n")


                print(f"итого: {round(S, 2)}")
                return(round(S, 2))
            elif capitalization == "Ежегодная":
                if tip_replenishment == "ежедневно":
                    sum_replenishment *= 365
                    for mounth in range(1, days//31 + 1):
                        S = start_sum * (1 + (prosent/100)/12)**mounth
                        iteration += 1
                        time_file.write(f"период:{iteration};всего:{round(S, 2)};прибыль:{round(start_sum * ( 1 + (prosent/100)/12)**mounth - start_sum, 2)};пополнение:{sum_replenishment}\n")
                        start_sum += sum_replenishment

                elif tip_replenishment == "ежемесячно":
                    sum_replenishment *= 12
                    for mounth in range(1, days//31 + 1):
                        S = start_sum * (1 + (prosent/100)/12)**mounth
                        iteration += 1
                        time_file.write(f"период:{iteration};всего:{round(S, 2)};прибыль:{round(start_sum * ( 1 + (prosent/100)/12)**mounth - start_sum, 2)};пополнение:{sum_replenishment}\n")
                        start_sum += sum_replenishment

                elif tip_replenishment == "ежеквартально":
                        start_sum *= 4
                        for mounth in range(1, days//31 + 1):
                            S = start_sum * (1 + (prosent/100)/4)**mounth
                            iteration += 1
                            time_file.write(f"период:{iteration};всего:{round(S, 2)};прибыль:{round(start_sum * ( 1 + (prosent/100)/12)**mounth - start_sum, 2)};пополнение:{sum_replenishment}\n")
                            start_sum += sum_replenishment

                elif tip_replenishment == "ежегодно":
                    for mounth in range(1, days//31 + 1):
                        S = start_sum * (1 + (prosent/100)/12)**mounth
                        iteration += 1
                        time_file.write(f"период:{iteration};всего:{round(S, 2)};прибыль:{round(start_sum * ( 1 + (prosent/100)/12)**mounth - start_sum, 2)};пополнение:{sum_replenishment}\n")
                        start_sum += sum_replenishment
                print(f"итого: {round(S, 2)}")
                return(round(S, 2))
            elif capitalization == "Ежедневная":
                if tip_replenishment == "ежедневно":
                    for mounth in range(1, days//31 + 1):
                        S = start_sum * (1 + (prosent/100)/12)**mounth
                        iteration += 1
                        time_file.write(f"период:{iteration};всего:{round(S, 2)};прибыль:{round(start_sum * ( 1 + (prosent/100)/12)**mounth - start_sum, 2)};пополнение:{sum_replenishment}\n")
                        start_sum += sum_replenishment

                elif tip_replenishment == "ежемесячно":
                    for mounth in range(1, days//31 + 1):
                        add_sum = sum_replenishment
                        S = start_sum * (1 + (prosent/100)/12)**mounth
                        iteration += 1
                        if mounth % 31 == 0:
                            time_file.write(f"период:{iteration};всего:{round(S, 2)};прибыль:{round(start_sum * ( 1 + (prosent/100)/12)**mounth - start_sum, 2)};пополнение:{add_sum}\n")
                            start_sum += add_sum
                        else:
                            add_sum = 0
                            time_file.write(f"период:{iteration};всего:{round(S, 2)};прибыль:{round(start_sum * ( 1 + (prosent/100)/12)**mounth - start_sum, 2)};пополнение:{add_sum}\n")


                elif tip_replenishment == "ежеквартально":
                        for mounth in range(1, days//31 + 1):
                            add_sum = sum_replenishment
                            S = start_sum * (1 + (prosent/100)/12)**mounth
                            iteration += 1
                            if mounth % 93 == 0:
                                time_file.write(f"период:{iteration};всего:{round(S, 2)};прибыль:{round(start_sum * ( 1 + (prosent/100)/12)**mounth - start_sum, 2)};пополнение:{add_sum}\n")
                                start_sum += add_sum
                            else:
                                add_sum = 0
                                time_file.write(f"период:{iteration};всего:{round(S, 2)};прибыль:{round(start_sum * ( 1 + (prosent/100)/12)**mounth - start_sum, 2)};пополнение:{add_sum}\n")


                elif tip_replenishment == "ежегодно":
                    for mounth in range(1, days//31 + 1):
                        add_sum = sum_replenishment
                        S = start_sum * (1 + (prosent/100)/12)**mounth
                        iteration += 1
                        if mounth % 365 == 0:
                            time_file.write(f"период:{iteration};всего:{round(S, 2)};прибыль:{round(start_sum * ( 1 + (prosent/100)/12)**mounth - start_sum, 2)};пополнение:{add_sum}\n")
                            start_sum += add_sum
                        else:
                            add_sum = 0
                            time_file.write(f"период:{iteration};всего:{round(S, 2)};прибыль:{round(start_sum * ( 1 + (prosent/100)/12)**mounth - start_sum, 2)};пополнение:{add_sum}\n")


                
            
    except Exception as ex:
        print(ex)

variables = {
    "sum_start_deposit": 100000,
    "iterest_rate": 2,
    "capitalization": "Ежегодная",
    "data_tip": "лет",
    "sum_replenishment": 10000,
    "tip_replenishment": "ежемесячно",
    "term_deposit": 15
}
if __name__ == "__main__":
     result(variables)


     """
    A = P * (1 + r/n)**(n*t)


    A – общая сумма денег (тело вклада + проценты), которую вы получите после того, как срок вклада закончится.
    P – стартовая сумма, которую вы кладете на счет вклада.
    r – процентная ставка по вкладу.
    n – количество расчетов прибыль в году, для ежедневной капитализации – 365 или 366, для ежемесячной – 12 и так далее.
    t – количество лет вклада. 6 месяцев – это 0.5 года.
    """