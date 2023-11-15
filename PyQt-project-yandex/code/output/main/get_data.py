import requests
from bs4 import BeautifulSoup
           
# f"https://www.banki.ru/products/deposits/?source=menubloks_deposits&page={page}&is_main_page=1"
def get_data_with_raquests():
    headers = {
    }
    with open("data_bank.txt", "w", encoding="utf8") as f:
        try:
            for page in range(1, 8):
                request = requests.get(f"https://www.banki.ru/products/deposits/?source=menubloks_deposits&page={page}&is_main_page=1", headers=headers)
                soup = BeautifulSoup(request.text, "lxml")
                chunk_bank = soup.find_all("div", {"class": "lf4cbd87d ld6d46e58 lfd76152f"})
                for info_bank in chunk_bank:
                    info_bank = list(filter(None, info_bank.text.split('\n')))
                    if len(info_bank) > 8:
                        info_bank = info_bank[:8]
                    f.write(f"{info_bank}\n")
            print("*******************************")
            print("DONE")
            return True
        except:
            return False




def main():
    get_data_with_raquests()



if __name__ == "__main__":
    main()
