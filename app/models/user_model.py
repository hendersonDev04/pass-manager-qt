from connection.connection_db import ConnectionDB
from dto.user_dto import UserDto
from dto.response_dto import ResponseDto

class UserModel:

    def __init__(self):
         self.db_connection_instance : ConnectionDB = ConnectionDB()

    def save_user(self, user : UserDto):
        
        try:

            with self.db_connection_instance.get_connection() as conn:
                cursor = conn.cursor()
                cursor.execute("""
                    INSERT INTO User (usuario, password)
                    VALUES (?, ?)
                """, (user.user, user.password))
                conn.commit()

                response : ResponseDto = ResponseDto(
                    id_response = 1,
                    message = "Registro correcto."
                )

                return response
            
        except Exception as e:
            raise Exception(f"funcion save_user: {str(e)}")