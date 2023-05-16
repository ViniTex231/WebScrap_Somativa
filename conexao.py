import mysql.connector

conexao = mysql.connector.connect(host="localhost", database="kabum", user="root", password="")

cursor = conexao.cursor()