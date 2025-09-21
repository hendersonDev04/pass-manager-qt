from PyQt6.QtWidgets import QDialog, QPushButton, QLineEdit, QDateEdit, QGroupBox
from PyQt6.QtCore import QDate, Qt, pyqtSignal, QRect
from PyQt6 import uic   

from models.password_registration_model import PasswordRegistrationModel
from dto.password_dto import PasswordDto
from controller.common_controller import Message

class PasswordUpdateController(QDialog):

    reload_password_tbl_signal : pyqtSignal = pyqtSignal()

    def __init__(self, parent = None, password_data : PasswordDto = None):
        super().__init__()
        self.parent_main = parent
        self.password_data = password_data
        uic.loadUi("view/password_update_view.ui", self)
        self.password_model_instance : PasswordRegistrationModel = PasswordRegistrationModel()
        self.setWindowFlag(Qt.WindowType.FramelessWindowHint | Qt.WindowType.Dialog)
        self.setFixedSize(300,280)
        self.set_center_view()

        self.save_btn = self.findChild(QPushButton, "save_btn")
        self.cancel_btn = self.findChild(QPushButton, "cancel_btn")

        self.id_txt = self.findChild(QLineEdit, "id_txt")
        self.password_txt = self.findChild(QLineEdit, "pass_txt")
        self.date_process_dte = self.findChild(QDateEdit, "date_process_dte")

        self.cancel_btn.clicked.connect(self.close_register_view)
        self.save_btn.clicked.connect(self.update_password_register)

        self.initialize_controls()

    def initialize_controls(self):
        self.id_txt.setHidden(True)
        self.password_txt.setFocus()
        self.date_process_dte.setEnabled(False)

        self.set_password_register()

    def set_password_register(self):
        date_from_py_date : QDate = QDate(self.password_data.date_process.year, 
                                  self.password_data.date_process.month, 
                                  self.password_data.date_process.day
                                )

        self.date_process_dte.setDate(date_from_py_date)
        self.set_date_format(self.date_process_dte)
        self.id_txt.setText(str(self.password_data.id))
        self.password_txt.setText(self.password_data.password)

    def set_date_format(self, date : QDateEdit):
        date.setCalendarPopup(True)
        date.setDisplayFormat("dd/MM/yyyy")

    def close_register_view(self):
        self.close()

    def _set_password(self):
        try:

            password: PasswordDto = PasswordDto(
                id = int(self.id_txt.text()),
                date_process = self.date_process_dte.date().toPyDate(),
                social_media = self.password_data.social_media,
                user = self.password_data.password,
                password = self.password_txt.text()
            )
            return password
        
        except Exception as e:
            Message.message_informative(f"Error : {e}")

    def update_password_register(self):

        password : PasswordDto = self._set_password()

        if not password:
            return
        
        try:

            response = self.password_model_instance.update_password_register(password)
            Message.message_informative(response.message)
            self.close_register_view()
            self.reload_password_tbl_signal.emit()

        except Exception as e:
            Message.message_informative(f"Error al actualizar registro: {e}")

    def set_center_view(self):
        
        if self.parent_main:
            geometry : QRect = self.geometry()
            x_axis = self.parent_main.geometry().x() + (self.parent_main.width() - geometry.width()) // 2
            y_axis = self.parent_main.geometry().y() + (self.parent_main.height() - geometry.height()) // 2
            self.move(x_axis, y_axis)

