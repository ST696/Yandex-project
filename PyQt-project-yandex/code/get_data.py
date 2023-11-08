import requests
from bs4 import BeautifulSoup
           
# f"https://www.banki.ru/products/deposits/?source=menubloks_deposits&page={page}&is_main_page=1"
def get_data_with_raquests(url):
    for page in range(1, 8):
        with open("data_bank.txt", "a", encoding="utf8") as f:
            request = requests.get(f"https://www.banki.ru/products/deposits/?source=menubloks_deposits&page={page}&is_main_page=1")
            soup = BeautifulSoup(request.text, "lxml")
            chunk_bank = soup.find_all("div", {"class": "lf4cbd87d ld6d46e58 lfd76152f"})
            for info_bank in chunk_bank:
                info_bank = list(filter(None, info_bank.text.split('\n')))
                if len(info_bank) > 8:
                    info_bank = info_bank[:8]
                f.write(f"{info_bank}\n")

        

    print("*******************************")
    print("DONE")


def main():
    #get_data_with_raquests("https://www.banki.ru/products/deposits/?source=menubloks_deposits")
    count = set()
    with open("data_bank.txt", "r") as file:
        for bank in file.readlines():
            bank = bank.replace("[", '').replace(']', '').split("'")
            bank = list(filter(lambda x: x != "," and x != "" and x != ", ", bank))
            bank_name = bank[0]
            print(bank_name)
            count.add(bank_name)
        print(count)



if __name__ == "__main__":
    main()
