from PyQt5 import QtGui, QtCore, QtWidgets
import sys
from views.MainWindow import MainWindow
from utils.sensor import stopGetData


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.setWindowTitle("Boxing App")
    window.show()

    # app theme
    # qss = "boxing-gui/Ubuntu.qss"
    # with open(qss, "r") as fh:
    #     app.setStyleSheet(fh.read())

    # set app icon
    app_icon = QtGui.QIcon()
    app_icon.addFile("boxing-gui/icons/logo.png", QtCore.QSize(64, 64))
    app.setWindowIcon(app_icon)

    return_value = app.exec_()
    if return_value == 0:
        print("Exiting program...")
        stopGetData()

    sys.exit(return_value)
