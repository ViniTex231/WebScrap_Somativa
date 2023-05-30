from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from conexao import conexao


nome = ["Springer", "Elgin", "Gree", "LG", "Samsung"]

class Web:
    def __init__(self, marca):
        self.marca = marca
        self.site = f"https://www.kabum.com.br/busca/ar-condicionado-{self.marca}"
        self.map = {
            "ar": {
                'xpath': '/html/body/div[1]/div[%VARIA%]/div[3]/div/div/div[2]/div/main/div[%VARIAVEL%]/a/div/button/div/h2/span'

            },
            "valor": {
                'xpath': '/html/body/div[1]/div[%VARIA%]/div[3]/div/div/div[2]/div/main/div[%VARIAVEL%]/a/div/div/span[2]'
            }
        }
        options = webdriver.ChromeOptions()
        options.add_argument("--headless")
        self.driver = webdriver.Chrome(options=options)
        self.criar_tabela()
        self.abrir_site()

    def abrir_site(self):
        print("abriu o site")
        self.driver.get(self.site)
        sleep(5)
        if self.marca == "springer" or self.marca == "gree":
            index = "1"
        else:
            index = "2"

        for i in range(1, 11):
            marca = self.driver.find_element(By.XPATH, self.map["ar"]['xpath'].replace('%VARIA%', f'{index}').replace('%VARIAVEL%', f'{i+1}')).text
            preco = self.driver.find_element(By.XPATH, self.map["valor"]['xpath'].replace('%VARIA%', f'{index}').replace('%VARIAVEL%', f'{i+1}')).text
            print(marca)
            print(preco)
            self.inserir_produtos(marca, preco)

    def criar_tabela(self):
        cursor = conexao.cursor()
        cursor.execute(f"DROP TABLE IF EXISTS {self.marca}")
        cursor.execute(f"create table {self.marca} (marca varchar(255), valor varchar(255))")
        conexao.commit()

    def inserir_produtos(self, marca, preco):
        inserir_produtos = f'''
            INSERT INTO {self.marca} (marca, valor)
            VALUES ('{marca}', '{preco}')
        '''
        cursor = conexao.cursor()
        cursor.execute(inserir_produtos)
        conexao.commit()
