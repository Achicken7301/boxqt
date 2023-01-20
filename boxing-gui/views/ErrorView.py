from PyQt5.QtWidgets import QMessageBox

def deviceNotFound(msg:str):
    msgBox = QMessageBox()
    msgBox.setWindowTitle("Error")
    msgBox.setIcon(QMessageBox.Information)
    msgBox.setText(msg)
    # msgBox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
    msgBox.setStandardButtons(QMessageBox.Ok)
    returnValue = msgBox.exec_()