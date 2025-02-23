import sqlite3
import threading
from typing import Optional

class DatabaseConnection:
    _instance = None
    _lock = threading.Lock()
    _local = threading.local()

    def __new__(cls):
        if cls._instance is None:
            with cls._lock:
                if cls._instance is None:
                    cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        self.database_path = 'imoveis.db'

    def get_connection(self) -> sqlite3.Connection:
        if not hasattr(self._local, 'connection'):
            self._local.connection = sqlite3.connect(self.database_path)
        return self._local.connection

    def get_cursor(self) -> sqlite3.Cursor:
        if not hasattr(self._local, 'cursor'):
            self._local.cursor = self.get_connection().cursor()
        return self._local.cursor

    def commit(self):
        if hasattr(self._local, 'connection'):
            self._local.connection.commit()

    def close(self):
        if hasattr(self._local, 'cursor'):
            self._local.cursor.close()
            delattr(self._local, 'cursor')
        if hasattr(self._local, 'connection'):
            self._local.connection.close()
            delattr(self._local, 'connection')

# Criar instância do gerenciador de conexão
db = DatabaseConnection()

# Criar tabela se não existir
with db.get_connection() as conn:
    conn.execute('''CREATE TABLE IF NOT EXISTS imoveis (
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