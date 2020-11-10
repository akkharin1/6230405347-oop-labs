from PyQt5 import QtWidgets, QtCore, QtGui
import sys

class window_gui(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.checkOne = QtWidgets.QCheckBox('one')
        self.checkTwo = QtWidgets.QCheckBox('two')
        self.vlayout = QtWidgets.QVBoxLayout()
        self.vlayout.addWidget(self.checkOne)
        self.vlayout.addWidget(self.checkTwo)
        self.setLayout(self.vlayout)
        self.checkOne.stateChanged.connect(lambda state=self.checkOne.isChecked(), no=1: self.selectBooks(state, no))
        self.checkTwo.stateChanged.connect(lambda state=self.checkTwo.isChecked(), no=2: self.selectBooks(state, no))

    def selectBooks(self, toggle, no):
        if toggle == QtCore.Qt.Checked:
            print('checked '+str(no))
        else:
            print('unchecked '+str(no))

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    w = window_gui()
    w.show()
    app.exec()