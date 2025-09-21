from connection.connection_db import ConnectionDB
from dto.user_dto import UserDto
from dto.response_dto import ResponseDto

class LoginModel:
    
    def __init__(self):
        self.db_connection_instance : ConnectionDB = ConnectionDB()

    def get_access_login(self, user : UserDto):

        has_access : bool = False
        with self.db_connection_instance.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT usuario, password FROM User")
            rows= cursor.fetchall()

        for row in rows:
            if user.user == row["usuario"] and user.password == row["password"]:
                has_access = True
                break
        
        return has_access
    
    def check_user_exists(self):

        exist_user : bool = False
        with self.db_connection_instance.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT Usuario FROM User")
            row = cursor.fetchall()

        if len(row) != 0:
            exist_user = True
            return exist_user
        
        return exist_user

