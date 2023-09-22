import sqlite3

conn = sqlite3.connect('produtos.db')
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE produtos (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    preco REAL NOT NULL,
    quantidade INTEGER NOT NULL
);
""")

# Inserindo produtos de exemplo
cursor.execute("""
INSERT INTO produtos (nome, preco, quantidade) VALUES 
('Produto A', 20.5, 10),
('Produto B', 0, 5),
('Produto C', 15.0, 0);
""")

conn.commit()
conn.close()
