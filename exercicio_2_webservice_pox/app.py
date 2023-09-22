from flask import Flask, jsonify, request
import sqlite3
# get relative path to find file db/produtos.db no matter where you execute from the python command
import os
dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, 'db/cardapio.db')


# ATENÇÃO: NÃO ALTERE ESTE ARQUIVO
# ATENÇÃO: NÃO ALTERE ESTE ARQUIVO
# ATENÇÃO: NÃO ALTERE ESTE ARQUIVO
# ATENÇÃO: NÃO ALTERE ESTE ARQUIVO

app = Flask(__name__)

def query_db(query, args=(), one=False):
    con = sqlite3.connect(filename)
    cur = con.cursor().execute(query, args)
    rv = cur.fetchall()
    cur.connection.close()
    return (rv[0] if rv else None) if one else rv


# ATENÇÃO: NÃO ALTERE ESTE ARQUIVO
# ATENÇÃO: NÃO ALTERE ESTE ARQUIVO
# ATENÇÃO: NÃO ALTERE ESTE ARQUIVO
# ATENÇÃO: NÃO ALTERE ESTE ARQUIVO

@app.route('/inserir_prato', methods=['POST'])
def inserir_prato():
    data = request.json
    titulo = data['titulo']
    descricao = data['descricao']
    categoria = data['categoria']
    preco = data['preco']
    
    con = sqlite3.connect(filename)
    cursor = con.cursor()
    cursor.execute("INSERT INTO pratos (titulo, descricao, categoria, preco) VALUES (?, ?, ?, ?)", (titulo, descricao, categoria, preco))
    con.commit()
    con.close()

    return jsonify({"status": "Prato inserido com sucesso!"}), 201


# ATENÇÃO: NÃO ALTERE ESTE ARQUIVO
# ATENÇÃO: NÃO ALTERE ESTE ARQUIVO
# ATENÇÃO: NÃO ALTERE ESTE ARQUIVO
# ATENÇÃO: NÃO ALTERE ESTE ARQUIVO

@app.route('/buscar_item', methods=['GET'])
def buscar_item():
    prato_id = request.args.get('id')
    prato = query_db('SELECT * FROM pratos WHERE id = ?', [prato_id], one=True)
    if prato:
        return jsonify({"id": prato[0], "titulo": prato[1], "descricao": prato[2], "categoria": prato[3], "preco": prato[4]})
    return jsonify({"error": "Prato não encontrado"}), 404


# ATENÇÃO: NÃO ALTERE ESTE ARQUIVO
# ATENÇÃO: NÃO ALTERE ESTE ARQUIVO
# ATENÇÃO: NÃO ALTERE ESTE ARQUIVO
# ATENÇÃO: NÃO ALTERE ESTE ARQUIVO

@app.route('/buscar_todos', methods=['GET'])
def buscar_todos():
    pratos = query_db('SELECT * FROM pratos')
    pratos_list = []
    for prato in pratos:
        prato_dict = {
            "id": prato[0],
            "titulo": prato[1],
            "descricao": prato[2],
            "categoria": prato[3],
            "preco": prato[4]
        }
        pratos_list.append(prato_dict)
    return jsonify(pratos_list)


# ATENÇÃO: NÃO ALTERE ESTE ARQUIVO
# ATENÇÃO: NÃO ALTERE ESTE ARQUIVO
# ATENÇÃO: NÃO ALTERE ESTE ARQUIVO
# ATENÇÃO: NÃO ALTERE ESTE ARQUIVO

@app.route('/deletar_item', methods=['DELETE'])
def deletar_item():
    prato_id = request.args.get('id')
    con = sqlite3.connect(filename)
    cursor = con.cursor()
    cursor.execute("DELETE FROM pratos WHERE id = ?", [prato_id])
    con.commit()
    con.close()

    return jsonify({"status": "Prato deletado com sucesso!"}), 200

if __name__ == "__main__":
    app.run(debug=True)


# ATENÇÃO: NÃO ALTERE ESTE ARQUIVO
# ATENÇÃO: NÃO ALTERE ESTE ARQUIVO
# ATENÇÃO: NÃO ALTERE ESTE ARQUIVO
# ATENÇÃO: NÃO ALTERE ESTE ARQUIVO