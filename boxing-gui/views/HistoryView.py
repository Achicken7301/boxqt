from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QWidget, QFileSystemModel
import pandas as pd
from ui.Ui_history import Ui_HistoryDialog


class HistoryViewDialog(QtWidgets.QDialog):
    def __init__(self, parent: QWidget, dir_path) -> None:
        super().__init__(parent)
        self.ui = Ui_HistoryDialog()
        self.ui.setupUi(self)

        self.root_path = dir_path

        self.model = QFileSystemModel()
        self.model.setRootPath(self.root_path)

        self.ui.treeView.setModel(self.model)
        self.ui.treeView.setRootIndex(self.model.index(self.root_path))
        self.ui.treeView.clicked.connect(self.onClick)
        self.ui.treeView.doubleClicked.connect(self.ondoubleClicked)

    def onClick(self, index):
        file_info = self.model.fileInfo(index)
        if file_info.isFile():
            file_name = file_info.fileName()
            print("Selected file name:", file_name)

        self.ui.acel_chart.clear()

        self.buff_acel = pd.read_csv(self.root_path + "\\" + file_name)
        # print(self.buff_acel['ax'])
        self.ui.acel_chart.plot(
            self.buff_acel["ax"],
            pen={"color": "b", "width": 2},
            name="ax",
        )

    def ondoubleClicked(self) -> pd.DataFrame:
        self.accept()
        return self.buff_acel
