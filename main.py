import sqlite3

conexao = sqlite3.connect('biblioteca.db')
cursor = conexao.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS livros (
    id INTEGER PRIMARY KEY AUTOINCREMENT,)
    titulo TEXT NOT NULL,
    autor TEXT NOT NULL,
    ano_publicacao INTEGER,
    disponivel text NOT NULL CHECK (disponivel IN ('sim', 'nao'))


''')

conexao.commit()


def cadrastar_livro(titulo, autor, ano):
    cursor.execute('''
    INSERT INTO livros (titulo, autor, ano_publicacao, disponivel)
    VALUES (?, ?, ?, 'sim')
    ''', (titulo, autor, ano))
    conexao.commit()
    print(f'Livro "{titulo}" cadastrado com sucesso!')  




