import requests
from bs4 import BeautifulSoup


def get_source_html(link):
    # ("https://www.banki.ru/products/deposits/?source=menubloks_deposits")
    responce = requests.get(link)


def herni():
    responce = requests.get("https://www.banki.ru/products/deposits/?source=menubloks_deposits")
    soup = BeautifulSoup(responce.text, features="html.parser")
    chank_bank = soup.find_all("div", {"class": "lf4cbd87d ld6d46e58 lfd76152f"})
    with open("data_bank.txt", "w", encoding="utf8") as f:
        for info_bank in chank_bank:
            info_bank = list(filter(None, info_bank.text.split('\n')))
            if len(info_bank) > 8:
                info_bank = info_bank[:8]
            f.write(f"{info_bank}\n")
    names_banck = soup.find_all("div", {"class": "text-size-5 text-weight-bold"})

    print("*******************************")
    count = 0
    print("DONE")

def main():
    herni()


if __name__ == "__main__":
    main()
