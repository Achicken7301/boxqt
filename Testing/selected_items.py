from PyQt5.QtWidgets import (QWidget, QListWidget, QVBoxLayout, QApplication)
import sys

class Example(QWidget):

    def __init__(self):
        super().__init__()


        self.l = QListWidget()
        for n in range(10):
            self.l.addItem(str(n))

        self.l.itemSelectionChanged.connect(self.selectionChanged)

        vbox = QVBoxLayout()
        vbox.addWidget(self.l)

        self.setLayout(vbox)
        self.setGeometry(300, 300, 300, 300)
        self.show()

    def selectionChanged(self):
        print("Selected items: ", self.l.selectedItems())


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())