from PyQt6.QtWidgets import QWidget, QPushButton, QLineEdit
from PyQt6.QtCore import pyqtSignal
from PyQt6 import uic

from models.login_model import LoginModel
from dto.user_dto import UserDto
from controller.common_controller import Message

class LoginController(QWidget):

    has_user_signal = pyqtSignal(bool)
    exit_login_signal = pyqtSignal()
    login_successful_signal = pyqtSignal()

    def __init__(self):
        super().__init__()

        uic.loadUi("view/login_view.ui", self)
        self.login_model_instance : LoginModel = LoginModel()
        self.exit_btn = self.findChild(QPushButton, "exit_btn")
        self.login_btn = self.findChild(QPushButton, "login_btn")
        self.user_txt = self.findChild(QLineEdit, "user_txt")
        self.password_txt = self.findChild(QLineEdit, "password_txt")
        #Actions
        self.exit_btn.clicked.connect(self.close_view)
        self.login_btn.clicked.connect(self.login)

    def initialize_controls(self):
        self.user_txt.clear()
        self.password_txt.clear()
        self.user_txt.setFocus()

    def close_view(self):
        self.close()
        self.exit_login_signal.emit()

    def check_user_exists(self):
        exist_user : bool = self.login_model_instance.check_user_exists()   
        return exist_user
    
    def set_user(self):
        try:

            user : UserDto = UserDto(
                user = self.user_txt.text(),
                password = self.password_txt.text()
            )
            return user
        except Exception as e:
            Message.message_informative(f"Advertencia : {e}")

    def login(self):    

        if not self.check_user_exists():
            Message.message_informative("No existe ningun usuario, por favor registre uno.")
            self.has_user_signal.emit(False)
            return
        
        user = self.set_user()

        if not user:
            return
        
        has_access : bool = self.login_model_instance.get_access_login(user)
        if not has_access:
            Message.message_informative("Credenciales incorrectas.")
            return
        
        self.login_successful_signal.emit()


