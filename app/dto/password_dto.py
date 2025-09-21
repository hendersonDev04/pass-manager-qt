from datetime import date

class PasswordDto():

    def __init__(self, date_process : date, social_media : str, user : str, password : str, id : int = None):
        self._id : int = None
        self._date_process : date = None
        self._social_media : str = None
        self._user : str = None
        self._password : str = None

        self.id = id
        self.date_process = date_process
        self.social_media = social_media
        self.user = user
        self.password = password

    @property
    def id(self):
        return self._id
    
    @id.setter
    def id(self, value: int):
        if not value:
            return self._id
        
        self._id = value

    @property
    def date_process(self):
        return self._date_process
    
    @date_process.setter
    def date_process(self, value: date):

        if value > date.today():
            raise ValueError("La fecha registro no puede se mayor a la actual.")
        
        self._date_process = value

    @property
    def social_media(self):
        return self._social_media
    
    @social_media.setter
    def social_media(self, value : str):

        if not value.strip():
            raise ValueError("El dato \"social media\" es obligatorio.")
        
        self._social_media = value

    @property
    def user(self):
        return self._user
    
    @user.setter
    def user(self, value : str):

        if not value.strip():
            raise ValueError("El dato \"usuario\" es obligatorio.")
        
        self._user = value

    @property
    def password(self):
        return self._password
    
    @password.setter
    def password(self, value : str):

        if not value.strip():
            raise ValueError("El dato \"password\" es obligatorio.")
        
        self._password = value