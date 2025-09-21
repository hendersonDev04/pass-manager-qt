from PyQt6.QtGui import QStandardItem
from PyQt6.QtCore import Qt
from connection.connection_db import ConnectionDB

class PasswordDisplayModel:

    def __init__(self):
        self.db_connection : ConnectionDB = ConnectionDB()

    def get_list_passwords(self):
        
        list_passwords : list[list[QStandardItem]] = []

        with self.db_connection.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT id, fecha_registro, pagina, usuario, password FROM Password")
            rows = cursor.fetchall()

        for row in rows:
            item_password : list[QStandardItem] = [
                    QStandardItem(str(row["id"])),
                    QStandardItem(str(row["fecha_registro"])),
                    QStandardItem(str(row["pagina"])),
                    QStandardItem(str(row["usuario"])),
                    QStandardItem(str(row["password"]))
                ]

            list_passwords.append(item_password)
        
        return list_passwords
    
