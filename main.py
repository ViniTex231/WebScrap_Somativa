from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from conexao import conexao


# print("[0] - Springer")
# print("[1] - Elgin")
# print("[2] - Gree")
# print("[3] - LG")
# print("[4] - Samsung")
# escolha = int(input("Digite a marca desejada: "))
nome = ["Springer", "Elgin", "Gree", "LG", "Samsung"]
#url_nome = ["U3ByaW5nZXIiXX0=&", "RWxnaW4iXX0=&", "R3JlZSJdfQ==&", "TEciXX0=&", "U2Ftc3VuZyJdfQ==&"]


class Web:
    def __init__(self, marca):
        self.marca = marca
        self.site = f"https://www.kabum.com.br/busca/ar-condicionado-{self.marca}"
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
        self.criar_tabela()
        self.abrir_site()


    def abrir_site(self):
        self.driver.get(self.site)
        sleep(1)
        for i in range(10):
            print(self.driver.find_element(By.XPATH, self.map["ar"]['xpath'].replace('%VARIAVEL%', f'{i+1}')).text)
            marca = self.driver.find_element(By.XPATH, self.map["ar"]['xpath'].replace('%VARIAVEL%', f'{i+1}')).text
            print(self.driver.find_element(By.XPATH, self.map["valor"]['xpath'].replace('%VARIAVEL%', f'{i+1}')).text)
            preco = self.driver.find_element(By.XPATH, self.map["valor"]['xpath'].replace('%VARIAVEL%', f'{i + 1}')).text
            self.inserir_produtos(marca, preco)

    def criar_tabela(self):
        cursor = conexao.cursor()
        cursor.execute(
            f"SELECT * FROM information_schema.tables WHERE table_name = '{self.marca}'")
        list_table = cursor.fetchone()

        if list_table:
            cursor.execute(f"DROP TABLE IF EXISTS {self.marca}")
            create_table = f"create table {self.marca} (marca varchar(255), valor varchar(255))"
            cursor.execute(create_table)
            conexao.commit()

    def inserir_produtos(self, marca, preco):
        inserir_produtos = f'''INSERT INTO {marca}(marca, valor)
        values
        ("{marca}", "{preco}")'''
        cursor = conexao.cursor()
        cursor.execute(inserir_produtos)
        conexao.commit()

