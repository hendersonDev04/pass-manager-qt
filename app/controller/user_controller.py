from PyQt6.QtWidgets import QWidget, QPushButton, QLineEdit
from PyQt6.QtCore import pyqtSignal
from PyQt6 import uic

from dto.user_dto import UserDto
from controller.common_controller import Message
from models.user_model import UserModel

class UserController(QWidget):

    save_sucsessful_signal = pyqtSignal()

    def __init__(self):
        super().__init__()
        self.user_instance : UserModel = UserModel()
        uic.loadUi("view/user_view.ui", self)

        self.save_btn = self.findChild(QPushButton, "save_btn")
        self.return_btn = self.findChild(QPushButton, "return_btn")

        self.user_txt = self.findChild(QLineEdit, "user_txt")
        self.password_txt = self.findChild(QLineEdit, "password_txt")

        self.save_btn.clicked.connect(self.save_user)
        self.return_btn.clicked.connect(self.close_view)

    def initialize_controls(self):
        self.user_txt.clear()
        self.password_txt.clear()
        self.user_txt.setFocus()

    def close_view(self):
        self.close()

    def set_user(self):

        try:

            user : UserDto = UserDto(
                user = self.user_txt.text(),
                password = self.password_txt.text()
            )

            return user
        except Exception as e:
            Message.message_informative(f"Advertencia : {e}")
            return None
        
    def save_user(self):

        user : UserDto = self.set_user()

        if not user:
           return
       
        try:
           
           is_ok : bool = Message.message_question("Se procedera a guardar, continuar?.")
           if not is_ok:
               return
           
           response = self.user_instance.save_user(user)
           Message.message_informative(response.message)
           self.save_sucsessful_signal.emit()

        except Exception as e:
           Message.message_informative(f"Ocurrio un error : {e}")