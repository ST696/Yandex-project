import sqlite3


class operationDatabase():
    def input_new_data_in_using_db():
        with open("data_bank/data_bank.txt", "r", encoding="utf8") as file:
            id = 1
            for bank in file.readlines():
                con = sqlite3.connect("database/banking_statistics.sql")
                cur = con.cursor()

                bank = bank.replace("[", '').replace(']', '').split("'")
                bank = list(filter(lambda x: x != "," and x != "" and x != ", ", bank))
                bank_name = bank[0]
                deposit_name = bank[1]
                percentages = bank[3]
                amount = bank[5]
                term = bank[7]
                cur.execute(
                    "INSERT INTO data_bank(id, bank_name, deposit_name, percentages, amount, term) VALUES(?, ?, ?, ?, ?, ?)",(id, bank_name, deposit_name, percentages, amount, term))
                id += 1
                con.commit()

    def delete_db(self):
        con = sqlite3.connect("database/banking_statistics.sql")
        cur = con.cursor()
        cur.execute("""DELETE FROM data_bank""")
        con.commit()


def main():
    oper = operationDatabase
    oper.input_new_data_in_using_db()


if __name__ == "__main__":
    main()
