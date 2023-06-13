from conexao import cursor


# LE O MODELO DOS AR CONDICIONADOS NO BANCO DE DADOS
def modelo(tabela):
    sql = f'SELECT marca FROM {tabela}'
    cursor.execute(sql)
    resultado = cursor.fetchall()
    return resultado

# LE O VALOR DOS AR CONDICIONADOS NO BANCO DE DADOS
def preco(tabela):
    sql = f'SELECT valor FROM {tabela}'
    cursor.execute(sql)
    resultado = cursor.fetchall()
    return resultado
