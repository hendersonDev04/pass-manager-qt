from PyQt6.QtWidgets import QWidget, QStackedWidget, QVBoxLayout
from PyQt6.QtCore import pyqtSignal, Qt
from PyQt6 import uic

from controller.login_controller import LoginController
from controller.user_controller import UserController

class LoginPanelController(QWidget):

    login_successfully_signal = pyqtSignal()
    def __init__(self):
        super().__init__()
        uic.loadUi("view/login_panel_view.ui", self)
        self.setFixedSize(680, 460)
        self.login_instance : QWidget = None
        self.display_login_stack = self.findChild(QStackedWidget, "display_login_stack")
        self.delete_default_widgets()

    def load_login_view(self):

        if self.login_instance is None:
            self.login_instance = LoginController()
            self.display_login_stack.addWidget(self.login_instance)
            self.login_instance.has_user_signal.connect(self.load_user_view)
            self.login_instance.exit_login_signal.connect(self.close_program)
            self.login_instance.login_successful_signal.connect(self.send_login_signal)

        self.display_login_stack.setCurrentWidget(self.login_instance)
        self.login_instance.initialize_controls()

    def close_program(self):
        self.close()

    def delete_default_widgets(self):
        while self.display_login_stack.count() > 0:
            current_widget : QWidget = self.display_login_stack.widget(0)
            self.display_login_stack.removeWidget(current_widget)
            current_widget.deleteLater()

        self.load_login_view()

    def load_user_view(self, exist_user : bool):
        
        if not exist_user:
            user_instance : UserController = UserController()
            self.display_login_stack.addWidget(user_instance)
            user_instance.save_sucsessful_signal.connect(self.load_login_view)

        self.display_login_stack.setCurrentIndex(1)
        
    def send_login_signal(self):
        self.login_successfully_signal.emit()
        self.close_program()