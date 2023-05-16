from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from conexao import conexao


print("[0] - Springer")
print("[1] - Elgin")
print("[2] - Gree")
print("[3] - LG")
print("[4] - Samsung")
escolha = int(input("Digite a marca desejada: "))
nome = ["SPRINGER", "ELGIN", "GREE", "LG", "SAMSUNG"]
url_nome = ["U3ByaW5nZXIiXX0=&", "RWxnaW4iXX0=&", "R3JlZSJdfQ==&", "TEciXX0=&", "U2Ftc3VuZyJdfQ==&"]


class Web:
    def __init__(self, url_nome):
        self.url_nome = url_nome
        self.site = "https://www.kabum.com.br/ar-e-ventilacao/ar-condicionado/ar-condicionado-split?page_number=1&page_size=20&facet_filters=eyJtYW51ZmFjdHVyZXIiOlsi[%MARCA%]sort=most_searched"
        self.map = {
            "ar": {
                'xpath': '/html/body/div[1]/div[1]/div[3]/div/div/div[2]/div/main/div[%VARIAVEL%]/a/div/button/div/h2/span'

            },
            "valor": {
                'xpath': '/html/body/div[1]/div[1]/div[3]/div/div/div[2]/div/main/div[%VARIAVEL%]/a/div/div/span[2]'
            }
        }
        options = webdriver.ChromeOptions()
        options.add_argument("--headless")
        self.driver = webdriver.Chrome(options=options)
        self.driver.maximize_window()

    def abrir_site(self):
        self.driver.get(self.site.replace('[%MARCA%]', self.url_nome))
        sleep(1)
        self.criar_tabela(nome[escolha])
        for i in range(10):
            print(self.driver.find_element(By.XPATH, self.map["ar"]['xpath'].replace('%VARIAVEL%', f'{i+1}')).text)
            marca = self.driver.find_element(By.XPATH, self.map["ar"]['xpath'].replace('%VARIAVEL%', f'{i+1}')).text
            print(self.driver.find_element(By.XPATH, self.map["valor"]['xpath'].replace('%VARIAVEL%', f'{i+1}')).text)
            preco = self.driver.find_element(By.XPATH, self.map["valor"]['xpath'].replace('%VARIAVEL%', f'{i + 1}')).text
            self.inserir_produtos(marca, preco, nome[escolha])

    def criar_tabela(self,tabela):
        create_table = f"create table {tabela} (marca varchar(255), valor varchar(255))"
        cursor = conexao.cursor()
        cursor.execute(create_table)
        conexao.commit()

    def inserir_produtos(self, marca, preco, tabela):
        inserir_produtos = f'''INSERT INTO {tabela}(marca, valor)
        values
        ("{marca}", "{preco}")'''
        cursor = conexao.cursor()
        cursor.execute(inserir_produtos)
        conexao.commit()


start = Web(url_nome[escolha])
start.abrir_site()
