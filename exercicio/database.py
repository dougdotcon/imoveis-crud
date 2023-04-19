import sqlite3

conn = sqlite3.connect('imoveis.db')

c = conn.cursor()

c.execute('''CREATE TABLE IF NOT EXISTS imoveis (
                id INTEGER PRIMARY KEY,
                tipo_negociacao TEXT NOT NULL,
                status TEXT NOT NULL,
                endereco TEXT NOT NULL,
                tipo_imovel TEXT NOT NULL,
                caracteristicas TEXT NOT NULL,
                preco REAL,
                condicoes TEXT,
                observacoes TEXT
            )''')

conn.commit()