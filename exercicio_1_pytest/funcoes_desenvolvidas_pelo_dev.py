# Arquivo desenvolvido pelo desenvolvedor descuidado!
import requests
import sqlite3

# get relative path to find file db/produtos.db no matter where you execute from the python command
import os
dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, 'db/produtos.db')

# ATENÇÃO: NÃO ALTERE ESTE ARQUIVO
# ATENÇÃO: NÃO ALTERE ESTE ARQUIVO
# ATENÇÃO: NÃO ALTERE ESTE ARQUIVO
# ATENÇÃO: NÃO ALTERE ESTE ARQUIVO

def consulta_cep(cep):
    if not isinstance(cep, str):
        return False
    if len(cep) > 8:
        return False
    if len(cep) < 8:
        raise Exception("CEP inválido")

    url = f"https://viacep.com.br/ws/{cep}/json/"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data.get("uf")
    else:
        return None

# ATENÇÃO: NÃO ALTERE ESTE ARQUIVO
# ATENÇÃO: NÃO ALTERE ESTE ARQUIVO
# ATENÇÃO: NÃO ALTERE ESTE ARQUIVO
# ATENÇÃO: NÃO ALTERE ESTE ARQUIVO


def verifica_disponibilidade(produto_nome):
    conn = sqlite3.connect(filename)
    cursor = conn.cursor()
    
    cursor.execute("SELECT preco, quantidade FROM produtos WHERE nome=?", (produto_nome,))
    data = cursor.fetchone()
    conn.close()
    
    if data:
        preco, quantidade = data
        if preco <= 0:
            return False
        if quantidade == 0:
            return False
        return True
    return False

# ATENÇÃO: NÃO ALTERE ESTE ARQUIVO
# ATENÇÃO: NÃO ALTERE ESTE ARQUIVO
# ATENÇÃO: NÃO ALTERE ESTE ARQUIVO
# ATENÇÃO: NÃO ALTERE ESTE ARQUIVO