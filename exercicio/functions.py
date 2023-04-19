import sqlite3

from database import conn, c

def inserir_dados(tipo_negociacao, status, endereco, tipo_imovel, caracteristicas, preco, condicoes, observacoes):
    dados = (tipo_negociacao, status, endereco, tipo_imovel, caracteristicas, preco, condicoes, observacoes)
    c.execute('''INSERT INTO imoveis (tipo_negociacao, status, endereco,
                                      tipo_imovel, caracteristicas, preco,
                                      condicoes, observacoes)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?)''', dados)

    conn.commit()