from flask import Flask, request, jsonify
import sqlite3
import os

dirname = os.path.dirname(__file__)
DATABASE_FILENAME =  os.path.join(dirname, 'db/startup_bike.db')

app = Flask(__name__)

# usuario
@app.route('/usuarios', methods=['GET'])
def get_usuarios():
    conn = sqlite3.connect(DATABASE_FILENAME)
    cursor = conn.cursor()

    cursor.execute("""SELECT * FROM usuarios""")
    usuarios = cursor.fetchall()

    return jsonify(usuarios), 200


@app.route('/usuarios/<int:id>', methods=['GET'])
def get_usuario_id(id):
    conn = sqlite3.connect(DATABASE_FILENAME)
    cursor = conn.cursor()

    cursor.execute("""SELECT * FROM usuarios WHERE id=?;""",(id,))
    usu_id = cursor.fetchone()

    if not usu_id:
        return {'mensagem': 'usuario não encontrado!'}, 404
    
    return jsonify(usu_id), 200

@app.route('/usuarios', methods=['POST'])
def post_usuario():
    conn = sqlite3.connect(DATABASE_FILENAME)
    cursor = conn.cursor()

    data = request.get_json()

    nome = data["nome"]
    cpf = data["cpf"]
    data_nascimento = data["data_nascimento"]
 
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO usuarios (nome, cpf, data_nascimento)
    VALUES (?, ?, ?)
    """, (nome, cpf, data_nascimento))

    conn.commit()

    return {'mensagem': 'Usuario criado com sucesso!'}, 201


@app.route('/usuarios/<int:id>', methods=['PUT'])
def put_usuario(id):
    conn = sqlite3.connect(DATABASE_FILENAME)
    cursor = conn.cursor()

    cursor.execute("""SELECT * FROM usuarios WHERE ID = ?""",(id,))
    usuario = cursor.fetchone()

    if usuario is None:
        {"error":"usuario não encontrado"},404

    data = request.json

    nome = data["nome"]
    cpf = data["cpf"]
    data_nascimento = data["data_nascimento"]

    cursor.execute("""UPDATE usuarios SET nome=?, cpf=?, data_nascimento=? WHERE ID = ?""", (nome, cpf, data_nascimento,id))

    conn.commit()
    conn.close()
    return {"mensagem":"usuario atualizado"}, 200

@app.route('/usuarios/<int:id>', methods=['DELETE'])
def delete_usuario(id):
    conn = sqlite3.connect(DATABASE_FILENAME)
    cursor = conn.cursor()

    # verificar se o livro existe
    cursor.execute("""
    SELECT * FROM usuarios WHERE id = ?;
    """, (id,))
    usuario = cursor.fetchone()

    if not usuario:
        return {'mensagem': 'Usuario não encontrado!'}, 404

    cursor.execute("""
    DELETE FROM usuarios WHERE id = ?;
    """, (id,))

    conn.commit()

    return {'mensagem': 'Usuario deletado com sucesso!'}, 200



# bicicletas
@app.route('/bikes', methods=['GET'])
def get_bikes():
    conn = sqlite3.connect(DATABASE_FILENAME)
    cursor = conn.cursor()

    cursor.execute("""SELECT * FROM bicicletas""")
    bicicletas = cursor.fetchall()

    return jsonify(bicicletas), 200


@app.route('/bikes/<int:id>', methods=['GET'])
def get_bikes_id(id):
    conn = sqlite3.connect(DATABASE_FILENAME)
    cursor = conn.cursor()

    cursor.execute("""SELECT * FROM bicicletas WHERE id=?;""",(id,))
    bike_id = cursor.fetchone()

    if not bike_id:
        return {'mensagem': 'bike não encontrada!'}, 404
    
    return jsonify(bike_id), 200


@app.route('/bikes', methods=['POST'])
def post_bike():
    conn = sqlite3.connect(DATABASE_FILENAME)
    cursor = conn.cursor()

    data = request.get_json()

    marca = data["marca"]
    modelo = data["modelo"]
    cidade = data["cidade"]
 
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO bicicletas (marca, modelo, cidade)
    VALUES (?, ?, ?)
    """, (marca, modelo, cidade))

    conn.commit()

    return {'mensagem': 'Bike cadastrada com sucesso!'}, 201



@app.route('/bikes/<int:id>', methods=['PUT'])
def put_bike(id):
    conn = sqlite3.connect(DATABASE_FILENAME)
    cursor = conn.cursor()

    cursor.execute("""SELECT * FROM bicicletas WHERE ID = ?""",(id,))
    bicicleta = cursor.fetchone()

    if bicicleta is None:
        {"error":"bicicleta não encontrada"},404

    data = request.json

    marca = data["marca"]
    modelo = data["modelo"]
    cidade = data["cidade"]

    cursor.execute("""UPDATE bicicletas SET marca=?, modelo=?, cidade=? WHERE ID = ?""", (marca, modelo, cidade,id))

    conn.commit()
    conn.close()
    return {"mensagem":"bike atualizada"}, 200


@app.route('/bikes/<int:id>', methods=['DELETE'])
def delete_bike(id):
    conn = sqlite3.connect(DATABASE_FILENAME)
    cursor = conn.cursor()

    # verificar se o livro existe
    cursor.execute("""
    SELECT * FROM bicicletas WHERE id = ?;
    """, (id,))
    bicicleta = cursor.fetchone()

    if not bicicleta:
        return {'mensagem': 'bicicleta não encontrada!'}, 404

    cursor.execute("""
    DELETE FROM bicicletas WHERE id = ?;
    """, (id,))

    conn.commit()

    return {'mensagem': 'bicicleta deletada com sucesso!'}, 200


# emprestimos
@app.route('/emprestimos', methods=['GET'])
def get_emprestimos():
    conn = sqlite3.connect(DATABASE_FILENAME)
    cursor = conn.cursor()

    cursor.execute("""SELECT * FROM emprestimos""")
    emprestimos = cursor.fetchall()

    return jsonify(emprestimos), 200


@app.route('/emprestimos/<int:id>', methods=['DELETE'])
def delete_emprestimo(id):
    conn = sqlite3.connect(DATABASE_FILENAME)
    cursor = conn.cursor()

    # verificar se o livro existe
    cursor.execute("""
    SELECT * FROM emprestimos WHERE id = ?;
    """, (id,))
    emprestimo = cursor.fetchone()

    if not emprestimo:
        return {'mensagem': 'Empréstimo não encontrado!'}, 404

    cursor.execute("""
    DELETE FROM emprestimos WHERE id = ?;
    """, (id,))

    conn.commit()

    return {'mensagem': 'emprestimo deletado com sucesso!'}, 200


if __name__ == '__main__':
    app.run(debug=True)