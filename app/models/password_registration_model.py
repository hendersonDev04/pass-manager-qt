from connection.connection_db import ConnectionDB
from dto.password_dto import PasswordDto
from dto.response_dto import ResponseDto

class PasswordRegistrationModel:

    def __init__(self):
        self.db_connection_instance : ConnectionDB = ConnectionDB()

    def save_password_register(self, password : PasswordDto):

        try:

            with self.db_connection_instance.get_connection() as conn:
                cursor = conn.cursor()
                cursor.execute("""
                    INSERT INTO Password (fecha_registro, pagina, usuario, password)
                    VALUES (?, ?, ?, ?)
                """, (password.date_process.strftime("%Y-%m-%d"), 
                    password.social_media, 
                    password.user, 
                    password.password))
                conn.commit()

                response : ResponseDto = ResponseDto(
                    id_response = 1,
                    message = "Registro correcto."
                )

                return response
            
        except Exception as e:
            raise Exception(f"funcion save_password_register : {str(e)}")
    
    def update_password_register(self, password : PasswordDto):

        try:

            with self.db_connection_instance.get_connection() as conn:
                cursor = conn.cursor()
                cursor.execute("""
                    UPDATE Password
                        SET password = ?
                    WHERE id = ?
                """,(password.password, password.id))
                conn.commit()

                response : ResponseDto = ResponseDto(
                    id_response = 1,
                    message = "Actualizacion correcta."
                )

                return response
        
        except Exception as e:
            raise Exception(f"funcion update_password_register; {str(e)}")