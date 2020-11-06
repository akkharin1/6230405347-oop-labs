import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        btn =  QPushButton('Quit', self)
        btn.clicked.connect(QApplication)
        label = QLabel('My name is Golf', self)
        label.move(100, 75)
        btn.setToolTip('click to exit')
        btn.resize(btn.sizeHint())
        btn.move(100, 100)

        self.setGeometry(300, 300, 300, 300)
        self.setWindowTitle('Exercise 1')
        self.show()

    def closeEvent(self, event):
        reply = QMessageBox.question(self, 'message',
                                     "Are you sure to quit?",
                                     QMessageBox.Yes |QMessageBox.No,
                                     QMessageBox.No
                                     )
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = Example()
    sys.exit(app.exec_())
