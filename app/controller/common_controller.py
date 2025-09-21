from PyQt6.QtWidgets import QMessageBox

class Message:

    @staticmethod
    def message_informative(message : str):
       alert : QMessageBox = QMessageBox(QMessageBox.Icon.Information, "Mensaje informativo", message, QMessageBox.StandardButton.Ok)
       alert.exec()

    @staticmethod
    def message_question(message : str):
        isOK : bool = True
        alert : QMessageBox = QMessageBox(QMessageBox.Icon.Question, "Mensaje informativo", message, 
                                          QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
        
        if (QMessageBox.StandardButton.Yes != alert.exec()):
            isOK = False
            return isOK
        
        return isOK
