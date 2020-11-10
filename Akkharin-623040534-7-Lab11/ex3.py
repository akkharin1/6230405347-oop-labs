import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import QtWidgets, QtCore, QtGui


class FormLayout(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):


        label_name = QLabel("Name")
        self.edit_name = QLineEdit(self)

        fbox = QFormLayout()

        fbox.addRow(label_name, self.edit_name)


        hbox = QHBoxLayout()
        self.pyqt = QCheckBox("PyQt")
        self.pygame = QCheckBox("PyGame")
        self.pytorch = QCheckBox("PyTorch")
        hbox.addWidget(self.pyqt)
        hbox.addWidget(self.pygame)
        hbox.addWidget(self.pytorch)
        hbox.addStretch()
        fbox.addRow(QLabel("library"), hbox)
        self.pyqt.stateChanged.connect(lambda state=self.pyqt.isChecked(), no= "PyQt": self.selectBooks(state, no))
        self.pygame.stateChanged.connect(lambda state=self.pygame.isChecked(), no="PyGame": self.selectBooks(state, no))
        self.pytorch.stateChanged.connect(lambda state=self.pytorch.isChecked(), no="PyTorch": self.selectBooks(state, no))

        hbox = QHBoxLayout()
        hbox.addStretch(1)
        submit = QPushButton("Submit")
        submit.clicked.connect(self.sumit)
        hbox.addWidget(submit)
        hbox.addWidget(QPushButton("Cancael"))
        fbox.addRow(hbox)

        self.setLayout(fbox)
        self.setWindowTitle("Problem3")
        self.show()

    def selectBooks(self, toggle, no):
        if toggle == QtCore.Qt.Checked:
            print(str(no) + 'is selected ')
        else:
            print(str(no) + 'is deselected')

    def sumit(self):
        print("Name is {}".format(self.edit_name.text()))

def main():
    app = QApplication(sys.argv)
    form_layout = FormLayout()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()