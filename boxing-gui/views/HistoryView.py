from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtWidgets import QWidget

from ui.Ui_history import Ui_Dialog


class HistoryViewDialog(QtWidgets.QDialog):
    def __init__(self, parent: QWidget) -> None:
        super().__init__(parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
