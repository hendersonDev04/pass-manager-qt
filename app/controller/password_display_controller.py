from datetime import datetime
from PyQt6.QtWidgets import QWidget, QPushButton, QTableView, QHeaderView
from PyQt6.QtGui import QStandardItemModel, QStandardItem
from PyQt6 import uic
from PyQt6.QtCore import pyqtSignal, QModelIndex
from models.password_display_model import PasswordDisplayModel
from dto.password_dto import PasswordDto

class PasswordDisplayController(QWidget):

    close_view_signal = pyqtSignal(bool)
    send_password_signal = pyqtSignal(object)

    def __init__(self):
        super().__init__()
        uic.loadUi("view/password_display_view.ui", self)

        self.show_pass_instance : PasswordDisplayModel = PasswordDisplayModel()

        self.close_btn = self.findChild(QPushButton, "close_btn")
        self.close_btn.clicked.connect(self.close_view)
        self.password_data_tbl = self.findChild(QTableView, "pass_data_tbl")
        self.password_data_model: QStandardItemModel = QStandardItemModel(self)

        self.password_data_tbl.doubleClicked.connect(self.send_password_to_update)
        self.config_table()
        self.initialize_controls()

    def initialize_controls(self):
        self.password_data_model.setRowCount(0)
        self.load_password_data_model()

    def config_table(self):
        self.password_data_model.setHorizontalHeaderLabels(["ID","FECHA REGISTRO","PAGINA","USUARIO","PASSWORD"])
        self.password_data_tbl.setSelectionMode(QTableView.SelectionMode.SingleSelection)
        self.password_data_tbl.setSelectionBehavior(QTableView.SelectionBehavior.SelectRows)
        self.password_data_tbl.setEditTriggers(QTableView.EditTrigger.NoEditTriggers)
        self.password_data_tbl.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Interactive)
        self.password_data_tbl.setModel(self.password_data_model)

    def close_view(self):
        self.close()
        self.close_view_signal.emit(True)

    def load_password_data_model(self):

        list_passwords : list[list[QStandardItem]] = self.show_pass_instance.get_list_passwords()
        for password in list_passwords:
            self.password_data_model.appendRow(password)

    def send_password_to_update(self, index_of_model : QModelIndex):
        
        row : int = index_of_model.row()

        password_dto : PasswordDto = PasswordDto(
            id = int(self.password_data_model.item(row, 0).text()),
            date_process = datetime.strptime(self.password_data_model.item(row, 1).text(), "%Y-%m-%d").date(),
            social_media = self.password_data_model.item(row, 2).text(),
            user = self.password_data_model.item(row, 3).text(),
            password = self.password_data_model.item(row, 4).text()
        )

        self.send_password_signal.emit(password_dto)
        
