
class UserDto:

    def __init__(self, user: str, password: str):
        self._user = None
        self._password = None

        self.user = user
        self.password = password

    @property
    def user(self):
        return self._user
    
    @user.setter
    def user(self, value : str):

        if not value.strip():
            raise ValueError("El \"Usuario\" es obligatorio.")
        
        self._user = value

    @property
    def password(self):
        return self._password
    
    @password.setter
    def password(self, value: str):

        if not value.strip():
            raise ValueError("La \"Contrasenia\" es obligatorio.")
        
        self._password = value