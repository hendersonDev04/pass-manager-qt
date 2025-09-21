import sys
from PyQt6.QtWidgets import QApplication
from app_manager import AppManager

if __name__ == '__main__':
    app = QApplication([])
    manager = AppManager(app)
    sys.exit(app.exec())

