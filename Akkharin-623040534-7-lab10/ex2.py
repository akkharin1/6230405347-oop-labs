import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QToolTip, QPushButton, QMessageBox, QLabel)
from PyQt5.QtCore import QCoreApplication, Qt
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon


class Window(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.initUI()

    def initUI(self):
        layout = QGridLayout()
        self.setLayout(layout)
        menubar = QMenuBar()
        layout.addWidget(menubar, 0, 0)
        actionFile = menubar.addMenu("File")
        add_new = actionFile.addAction("New")
        add_edit = actionFile.addMenu("Edit")
        add_edit.addAction("Copy")
        add_edit.addAction("Paste")
        add_save = actionFile.addAction("Save")
        add_save.setShortcut("Ctrl+s")
        actionFile.addSeparator()
        exitButton = QAction(QIcon('joystick_game_3819.png'), 'Exit', self)
        exitButton.setShortcut('Ctrl+q')
        exitButton.setStatusTip('Exit application')
        exitButton.triggered.connect(self.close)
        actionFile.addAction(exitButton)

        self.setGeometry(300, 300, 300, 300)


def Main():
    app = QApplication(sys.argv)
    screen = Window()
    screen.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    Main()