import sqlite3
from typing import List, Dict, Optional

from database import db

def inserir_dados(
    tipo_negociacao: str,
    status: str,
    endereco: str,
    tipo_imovel: str,
    caracteristicas: str,
    preco: str,
    condicoes: str,
    observacoes: str
) -> int:
    """Insere um novo imóvel no banco de dados e retorna seu ID"""
    dados = (
        tipo_negociacao,
        status,
        endereco,
        tipo_imovel,
        caracteristicas,
        preco,
        condicoes,
        observacoes,
    )
    
    cursor = db.get_cursor()
    cursor.execute('''INSERT INTO imoveis (
        tipo_negociacao, status, endereco,
        tipo_imovel, caracteristicas, preco,
        condicoes, observacoes
    ) VALUES (?, ?, ?, ?, ?, ?, ?, ?)''', dados)
    
    db.commit()
    return cursor.lastrowid

def buscar_imoveis(
    filtro: Optional[Dict] = None
) -> List[Dict]:
    """Busca imóveis com filtros opcionais"""
    query = "SELECT * FROM imoveis"
    params = []
    
    if filtro:
        conditions = []
        for key, value in filtro.items():
            if value:
                conditions.append(f"{key} LIKE ?")
                params.append(f"%{value}%")
        
        if conditions:
            query += " WHERE " + " AND ".join(conditions)
    
    cursor = db.get_cursor()
    cursor.execute(query, params)
    
    colunas = [description[0] for description in cursor.description]
    resultados = []
    
    for row in cursor.fetchall():
        resultado = dict(zip(colunas, row))
        resultados.append(resultado)
    
    return resultados

def atualizar_imovel(
    id: int,
    tipo_negociacao: str,
    status: str,
    endereco: str,
    tipo_imovel: str,
    caracteristicas: str,
    preco: str,
    condicoes: str,
    observacoes: str
) -> bool:
    """Atualiza um imóvel existente"""
    try:
        dados = (
            tipo_negociacao,
            status,
            endereco,
            tipo_imovel,
            caracteristicas,
            preco,
            condicoes,
            observacoes,
            id
        )
        
        cursor = db.get_cursor()
        cursor.execute('''UPDATE imoveis SET
            tipo_negociacao = ?,
            status = ?,
            endereco = ?,
            tipo_imovel = ?,
            caracteristicas = ?,
            preco = ?,
            condicoes = ?,
            observacoes = ?
            WHERE id = ?''', dados)
        
        db.commit()
        return True
    except sqlite3.Error:
        return False

def excluir_imovel(id: int) -> bool:
    """Exclui um imóvel pelo ID"""
    try:
        cursor = db.get_cursor()
        cursor.execute("DELETE FROM imoveis WHERE id = ?", (id,))
        db.commit()
        return True
    except sqlite3.Error:
        return False

def buscar_imovel_por_id(id: int) -> Optional[Dict]:
    """Busca um imóvel específico pelo ID"""
    cursor = db.get_cursor()
    cursor.execute("SELECT * FROM imoveis WHERE id = ?", (id,))
    resultado = cursor.fetchone()
    
    if not resultado:
        return None
    
    colunas = [description[0] for description in cursor.description]
    return dict(zip(colunas, resultado)) 