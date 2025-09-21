import sqlite3
from pathlib import Path

DB_NAME = "pass_manager_db.db"

class ConnectionDB:

    def __init__(self):
        self.path_db = Path(__file__).parent.parent / DB_NAME

    def get_connection(self):
        conn = sqlite3.connect(self.path_db)
        conn.row_factory = sqlite3.Row
        return conn
    
    def init_db(self):

        with self.get_connection() as cnn:
            cursor = cnn.cursor()
            cursor.execute("""
            CREATE TABLE IF NOT EXISTS Password (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                fecha_registro TEXT NOT NULL,
                pagina TEXT NOT NULL,
                usuario TEXT NOT NULL,
                password TEXT NOT NULL
            )
            """)

            cursor.execute("""                   
            CREATE TABLE IF NOT EXISTS User (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                usuario TEXT NOT NULL,
                password TEXT NOT NULL
            )
            """)
            cnn.commit()