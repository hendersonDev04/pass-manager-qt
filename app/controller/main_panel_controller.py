from PyQt6.QtWidgets import QMainWindow, QPushButton, QStackedWidget, QWidget
from PyQt6 import uic

from controller.password_registration_controller import PasswordRegistrationController
from controller.password_display_controller import PasswordDisplayController
from controller.password_update_controller import PasswordUpdateController
from dto.password_dto import PasswordDto
from controller.common_controller import Message

class MainPanelController(QMainWindow):

    def __init__(self):
        super().__init__()
        uic.loadUi("view/main_panel_view.ui", self)
        self.setFixedSize(680, 460)

        self.exit_btn = self.findChild(QPushButton, "exit_btn")
        self.register_btn = self.findChild(QPushButton, "register_btn")
        self.show_btn = self.findChild(QPushButton, "show_btn")

        self.display_widget_stack = self.findChild(QStackedWidget, "display_stack")
        self.delete_default_widgets()

        self.exit_btn.clicked.connect(self.exit_program)
        self.register_btn.clicked.connect(self.load_register_pass_view)
        self.show_btn.clicked.connect(self.load_show_pass_view)

        self.empty_widget_instance : QWidget = None
        self.password_registration_instance : QWidget = None
        self.password_display_instance : QWidget = None

    def exit_program(self):
        is_OK : bool = Message.message_question("El programa cerrará. Dese continuar?")
        if not is_OK:
            return
        
        self.close()

    def delete_default_widgets(self):
        while self.display_widget_stack.count() > 0:
            current_widget : QWidget = self.display_widget_stack.widget(0)
            self.display_widget_stack.removeWidget(current_widget)
            current_widget.deleteLater()

        self.empty_widget_instance = QWidget()
        self.display_widget_stack.addWidget(self.empty_widget_instance)

    def load_register_pass_view(self):
        if self.password_registration_instance is None:
            self.password_registration_instance = PasswordRegistrationController()
            self.display_widget_stack.addWidget(self.password_registration_instance)
            self.password_registration_instance.close_view_signal.connect(self.load_empty_widget)
            
        self.display_widget_stack.setCurrentWidget(self.password_registration_instance)
        self.password_registration_instance.initialize_controls()

    def load_empty_widget(self):
        self.display_widget_stack.setCurrentIndex(0)

    def load_show_pass_view(self):
        if self.password_display_instance is None:
            self.password_display_instance = PasswordDisplayController()
            self.display_widget_stack.addWidget(self.password_display_instance)
            self.password_display_instance.close_view_signal.connect(self.load_empty_widget)
            self.password_display_instance.send_password_signal.connect(self.upload_password_to_update)

        self.display_widget_stack.setCurrentWidget(self.password_display_instance)
        self.password_display_instance.initialize_controls()

    def upload_password_to_update(self, password : PasswordDto):
        
        password_update_instance : PasswordUpdateController = PasswordUpdateController(self, password)
        password_update_instance.reload_password_tbl_signal.connect(self.load_show_pass_view)
        password_update_instance.exec()