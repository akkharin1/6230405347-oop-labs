import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *


class FormLayout(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        sam = QLabel("Sample Form", self)
        sam.setStyleSheet("color: blue")
        sam.setFont(QFont("Arial", 18))
        sam.adjustSize()

        label_name = QLabel("Name")
        edit_name = QLineEdit(self)

        fbox = QFormLayout()
        fbox.addRow(sam, sam)
        fbox.addRow(label_name, edit_name)

        hbox = QHBoxLayout()
        radio_male = QRadioButton("Male")
        radio_female = QRadioButton("Female")
        hbox.addWidget(radio_male)
        hbox.addWidget(radio_female)
        hbox.addStretch()
        fbox.addRow(QLabel("Gender"), hbox)

        hbox = QHBoxLayout()
        hbox.addStretch(1)
        hbox.addWidget(QPushButton("Submit"))
        hbox.addWidget(QPushButton("Cancael"))
        fbox.addRow(hbox)

        self.setLayout(fbox)
        self.setWindowTitle("Problem1")
        self.show()

def main():
    app = QApplication(sys.argv)
    form_layout = FormLayout()
    sys.exit(app.exec_())



if __name__ == '__main__':
    main()