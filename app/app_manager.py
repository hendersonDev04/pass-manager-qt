from connection.connection_db import ConnectionDB
from controller.login_panel_controller import LoginPanelController
from controller.main_panel_controller import MainPanelController

class AppManager:

    def __init__(self, app):
        self.app = app
        self.login_panel_instance : LoginPanelController = None
        self.main_panel_instance : MainPanelController = None
        self.db_connection_instance: ConnectionDB = ConnectionDB()
        self.db_connection_instance.init_db()
        self.show_login_view()

    def show_login_view(self):
        self.login_panel_instance = LoginPanelController()
        self.login_panel_instance.login_successfully_signal.connect(self.show_main_panel_view)
        self.login_panel_instance.show()

    def show_main_panel_view(self):
        self.main_panel_instance = MainPanelController()
        self.main_panel_instance.show()