from PyQt5 import QtWidgets
from ui.Ui_about_this_app_dialog import Ui_AboutThisAppDialog

class AboutThisAppDialog(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_AboutThisAppDialog()
        self.ui.setupUi(self)