import requests
from bs4 import BeautifulSoup

class Get_Deposit_Interest():
    def __init__(self):

        self.responce = requests.get("https://www.banki.ru/products/deposits/?source=menubloks_deposits")
        self.soup = BeautifulSoup(self.responce.text, features="html.parser")
        class_find = self.soup.find_all("div", {"class": "lbb023d8c l40cb8252"})
        names_banck = self.soup.find_all("div", {"class": "text-size-5 text-weight-bold"})
        for name in names_banck:
            print(name.text)
        #find_map = class_find.find("span")[0].text
        print("*******************************")
        count = 0

        for bunck in class_find:
            if len(bunck) != 0:
                if bunck.find('div').text == "Эффективная ставка":
                    print(f"{count}:{bunck.find('div').text} ::: {bunck.find('span').text}")
                elif bunck.find('div').text == "Сумма":
                    print(f"{count}:{bunck.find('div').text} ::: {bunck.find('span').text}")
                elif bunck.find('div').text == "Срок":
                    print(f"{count}:{bunck.find_all('div')[0].text} ::: {bunck.find_all('div')[1].text}")
            count += 1

        print("DONE")

x = Get_Deposit_Interest()