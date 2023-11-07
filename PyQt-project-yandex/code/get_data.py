import requests
from bs4 import BeautifulSoup


def website_request(link,
                    headers={
                        "Accept": "	*/*",
                        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/119.0"
                    }):
    request = requests.get(link)
    src = request.text
    with open("index.html", "w") as f:
        f.write(src)

    return src

def parsing_2():
    headers={
                "user-agent": "Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/119.0",
                "referer": "https://www.banki.ru/products/deposits/?source=menubloks_deposits"
            }
    with open("url_list", "w") as file:
        for page in range(1, 2):
            url = f"https://www.banki.ru/products/deposits/api/group/nizhniy_novgorod/?segmentation_page=deposits_main&amount=0&currency=RUB&period=0&special[]=0&special[]=14&special[]=2&special[]=1&special[]=9&special[]=12&special[]=10&type=All&replenishment=0&partial_withdrawal=0&payment_period_per_month=0&capitalization=0&early_termination_method=0&is_no_additional_expenses=0&hide_growing_rates=0&top_hundred_place=0&is_main_page=1&is_only_bankiru_offer=0&sort=popular&order=desc&page={page}&page_type=MAINPRODUCT_SEARCH"
            request = requests.get(url=url, headers=headers)
            file.write(request.text)
            

def parsing(src):
    request = src
    # Парснг !!! Необходимо в soup добаваить все банки !!!
    soup = BeautifulSoup(request, "lxml")

    chunk_bank = soup.find_all("div", {"class": "lf4cbd87d ld6d46e58 lfd76152f"})
 
    with open("data_bank.txt", "w", encoding="utf8") as f:
        for info_bank in chunk_bank:
            info_bank = list(filter(None, info_bank.text.split('\n')))
            if len(info_bank) > 8:
                info_bank = info_bank[:8]
            f.write(f"{info_bank}\n")
    names_banck = soup.find_all("div", {"class": "text-size-5 text-weight-bold"})

    print("*******************************")
    print("DONE")


def main():
    #src = website_request("https://www.banki.ru/products/deposits/?source=menubloks_deposits")
    #parsing(src)
    parsing_2()


if __name__ == "__main__":
    main()
