from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep


class Web:
    def __init__(self):
        self.site = "https://lista.mercadolivre.com.br/acessorios-veiculos/pneus/novo/pneus-e-acessorios_NoIndex_True#DEAL_ID=MLB2138&S=landingHubacessorios-para-veiculos&V=6&T=Special-normal&L=PNEU&deal_print_id=80975240-ee6d-11ed-80b1-a3981728d4e1&c_id=special-normal&c_element_order=1&c_campaign=PNEU&c_uid=80975240-ee6d-11ed-80b1-a3981728d4e1"
        self.map = {
            "smartphone": {
                'xpath': '/html/body/main/div/div[2]/section/ol/li[%VARIAVEL%]/div/div/div[2]/div[1]/a/h2'

            },
            'valor': {
                'xpath': '/html/body/main/div/div[2]/section/ol/li[%VARIA%]/div/div/div[2]/div[2]/div[1]/div[1]/div/div/div/span[1]/span[2]'
            }
        }
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

    def abrir_site(self):
        self.driver.get(self.site)
        sleep(5)
        k = 0
        for i in range(10):
            print(self.driver.find_element(By.XPATH, self.map["smartphone"]['xpath'].replace('%VARIAVEL%', f'{i+1}')).text)
            for j in range(1):
                print(self.driver.find_element(By.XPATH, self.map["valor"]['xpath'].replace('%VARIA%', f'{k+1}')).text, end="  ")
                k += 1
            print("")


start = Web()
# start.abrir_site()







# from bs4 import BeautifulSoup
# import requests
#
# URL = "https://www.lojadomecanico.com.br/busca?q=smartphone"
#
# headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36"}
#
# site = requests.get(URL, headers=headers)
#
# soup = BeautifulSoup(site.content, "html.parser")
#
# for i in range(5):
#     title = soup.find('h3', class_ = "product-description")
#     print(title)
