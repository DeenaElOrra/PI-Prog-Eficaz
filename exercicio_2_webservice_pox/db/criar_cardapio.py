import sqlite3

def criar_base_dados():
    conn = sqlite3.connect("db/cardapio.db")
    cursor = conn.cursor()
    
    cursor.execute("DROP TABLE IF EXISTS Usuarios")
    cursor.execute("DROP TABLE IF EXISTS Produtos")
    cursor.execute("DROP TABLE IF EXISTS Classificacoes")
    
    cursor.execute("""
    CREATE TABLE Pratos(
        id INTEGER PRIMARY KEY,
        titulo TEXT NOT NULL,
        descricao TEXT NOT NULL
        categoria TEXT NOT NULL,
        preco INTEGER NOT NULL
    )
    """)
                   
    pratos = [
        (1, "entrada", "arroz e feijao", "principal", 12),
        (2, "sobremesa", "creme brulle", "sobremesa", 45),
    ]

    cursor.executemany("INSERT INTO Pratos VALUES (?, ?, ?, ?,?)", pratos)
    

    conn.commit()
    conn.close()


criar_base_dados()