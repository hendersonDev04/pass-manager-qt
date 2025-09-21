from PyQt6.QtWidgets import QWidget, QPushButton, QLineEdit, QDateEdit
from PyQt6.QtCore import pyqtSignal, QDate
from PyQt6 import uic   
from models.password_registration_model import PasswordRegistrationModel
from dto.password_dto import PasswordDto
from controller.common_controller import Message

class PasswordRegistrationController(QWidget):

    close_view_signal = pyqtSignal()

    def __init__(self):
        super().__init__()
        uic.loadUi("view/password_registration_view.ui", self)
        self.register_password_instance = PasswordRegistrationModel()
        self.close_btn = self.findChild(QPushButton, "close_btn")
        self.save_btn = self.findChild(QPushButton, "save_btn")
        self.cancel_btn = self.findChild(QPushButton, "cancel_btn")

        self.user_txt = self.findChild(QLineEdit, "user_txt")
        self.pass_txt = self.findChild(QLineEdit, "pass_txt")
        self.social_media_txt = self.findChild(QLineEdit, "social_red_txt")
        self.date_process_dte = self.findChild(QDateEdit, "date_process_dte")

        self.close_btn.clicked.connect(self.close_register_view)
        self.cancel_btn.clicked.connect(self.initialize_controls)
        self.save_btn.clicked.connect(self.save_password_register)

        self.initialize_controls()

    def initialize_controls(self):
        self.set_date_format(self.date_process_dte)
        self.user_txt.clear()
        self.pass_txt.clear()
        self.social_media_txt.clear()
        self.social_media_txt.setFocus()
        
    def set_date_format(self, date : QDateEdit):
        date.setDate(QDate.currentDate())
        date.setCalendarPopup(True)
        date.setDisplayFormat("dd/MM/yyyy")

    def close_register_view(self):
        self.close()
        self.close_view_signal.emit()

    def _set_password(self):
        try:

            password: PasswordDto = PasswordDto(
                date_process = self.date_process_dte.date().toPyDate(),
                social_media = self.social_media_txt.text(),
                user = self.user_txt.text(),
                password = self.pass_txt.text()
            )
            return password
        
        except ValueError as e:
            Message.message_informative(f"Advertencia : {e}")

    def save_password_register(self):

        password : PasswordDto = self._set_password()
        
        if not password:
            return

        try:

            response = self.register_password_instance.save_password_register(password)
            is_OK : bool = Message.message_question("Seguro de guardar?.")
            if not is_OK:
                return
            
            Message.message_informative(response.message)
            self.initialize_controls()

        except Exception as e:
            Message.message_informative(f"Ocurrio un error : {e}")
