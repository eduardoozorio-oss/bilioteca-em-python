import sqlite3
conexao = sqlite3.connect("biblioteca.db")
cursor = conexao.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS livros (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    titulo TEXT NOT NULL,
    autor TEXT NOT NULL,
    ano INTEGER,
    disponivel TEXT CHECK(disponivel IN ('Sim', 'Não')) NOT NULL
)
""")
conexao.commit()

# Etapa 2 - Função de cadastro

def cadastrar_livro(titulo, autor, ano):
    cursor.execute("""
        INSERT INTO livros (titulo, autor, ano, disponivel)
        VALUES (?, ?, ?, 'Sim')
    """, (titulo, autor, ano))
    conexao.commit()
    print(f"\n Livro '{titulo}' cadastrado com sucesso!")











