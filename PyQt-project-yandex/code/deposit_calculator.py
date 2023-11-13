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

    """
    A = P * (1 + r/n)**(n*t)


    A – общая сумма денег (тело вклада + проценты), которую вы получите после того, как срок вклада закончится.
    P – стартовая сумма, которую вы кладете на счет вклада.
    r – процентная ставка по вкладу.
    n – количество расчетов прибыль в году, для ежедневной капитализации – 365 или 366, для ежемесячной – 12 и так далее.
    t – количество лет вклада. 6 месяцев – это 0.5 года.
    """
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
                for mounth in range(1, days//31 + 1):
                    S = start_sum * (1 + (prosent/100)/12)**mounth
                    iteration += 1
                    time_file.write(f"период:{iteration};всего:{round(S, 2)};прибыль:{round(start_sum * ( 1 + (prosent/100)/12)**mounth - start_sum, 2)};пополнение:{sum_replenishment}\n")

                    
                """
                mounth – количество проведенных операций перевода процентов в тело вклада на протяжении полного срока действия договора (то есть месяцев вклада);

                S – сумма вклада на дату окончания действия депозита, которую вкладчик получит на руки;

                start_sum – изначально внесенная сумма на депозит с возможностью капитализации;

                prosent - % ставка (годовая).
                """
                print(f"итого: {round(S, 2)}")
                return(round(S, 2))

            elif capitalization == "Ежеквартальная":
                for quarter in range(1, days//93 + 1):
                    S=start_sum * (1+ (prosent/100)/4)**quarter
                    iteration += 1
                    time_file.write(f"период:{iteration};всего:{round(S, 2)};прибыль:{round(start_sum * ( 1 + (prosent/100)/12)**quarter - start_sum, 2)};пополнение:{sum_replenishment}\n")

                """
                S - получаемый в конце срока доход (тело вклада + проценты);

                start_sum – изначально размещенная сумма на депозите;

                prosent - годовой %;

                quarter – количество кварталов, на протяжении которых открыт вклад.
                """
                print(f"итого: {round(S, 2)}")
                return(round(S, 2))



            elif capitalization == "Ежегодная":
                for year in range(1, days//365 + 1):
                    S=start_sum * (1+ (prosent/100))**year
                    iteration += 1
                    time_file.write(f"период:{iteration};всего:{round(S, 2)};прибыль:{round(start_sum * ( 1 + (prosent/100)/12)**year - start_sum, 2)};пополнение:{sum_replenishment}\n")

                """
                S - получаемый в конце срока доход (тело вклада + проценты);

                start_sum – изначально размещенная сумма на депозите;

                prosent - годовой %;

                quarter – количество кварталов, на протяжении которых открыт вклад.
                """
                print(f"итого: {round(S, 2)}")
                return(round(S, 2))


            elif capitalization == "Ежедневная":
                for day in range(1, days + 1):
                    S = start_sum * (1 + (prosent/100) / 365)**day
                    iteration += 1
                    time_file.write(f"период:{iteration};всего:{round(S, 2)};прибыль:{round(start_sum * ( 1 + (prosent/100)/12)**day - start_sum, 2)};пополнение:{sum_replenishment}\n")

                    """
                    S – суммарный доход (тело вклада + проценты);

                    start_sum – внесенная при заключении договора сумма;

                    prosent – годовая % ставка;

                    К – 365 или 366 дней;

                    day – кол-во дней, на которые открыт депозит.
                    """   
    except Exception as ex:

        print(ex)
    else:
        raise

delta = datetime.timedelta
variables = {
    "sum_start_deposit": 100000,
    "iterest_rate": 2,
    "capitalization": "Ежемесячная",
    "data_tip": "лет",
    "sum_replenishment": 10000,
    "tip_replenishment": "ежемесячно",
    "term_deposit": 15
}
if __name__ == "__main__":
     result(variables)