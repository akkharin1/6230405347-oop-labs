import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *


class Problem1(QWidget):

    def __init__(self):
        super().__init__()
        self.init_value = 50
        self.slider1 = QSlider(Qt.Horizontal, self)
        self.slider2 = QSlider(Qt.Horizontal, self)
        self.value1 = QLabel(self)
        self.value2 = QLabel(self)
        self.add = QPushButton("Add", self)
        self.subtract = QPushButton("Subtract", self)
        self.multiply = QPushButton("Multiply", self)
        self.divide = QPushButton("Divide", self)
        self.ans = QLineEdit(self)
        self.initUI()

    def initUI(self):
        self.slider1.setMaximum(0)
        self.slider1.setMaximum(100)
        self.slider1.setValue(50)
        self.slider1.setTickPosition(QSlider.TicksBelow)
        self.slider1.valueChanged[int].connect(self.change_value)

        self.value1.setText(str(self.init_value))
        self.value1.setFont(QFont("Arial", 20))
        self.value1.setStyleSheet("color: blue")

        self.slider2.setMaximum(0)
        self.slider2.setMaximum(100)
        self.slider2.setValue(50)
        self.slider2.setTickPosition(QSlider.TicksBelow)
        self.slider2.valueChanged[int].connect(self.change_value)

        self.value2.setText(str(self.init_value))
        self.value2.setFont(QFont("Arial", 20))
        self.value2.setStyleSheet("color: blue")

        self.add.clicked[bool].connect(lambda: self.set_pressed())
        self.subtract.clicked[bool].connect(lambda: self.set_pressed())
        self.multiply.clicked[bool].connect(lambda: self.set_pressed())
        self.divide.clicked[bool].connect(lambda: self.set_pressed())

        self.slider1.valueChanged.connect(lambda: self.calculate(self.value1.text(), self.value2.text()))
        self.slider2.valueChanged.connect(lambda: self.calculate(self.value1.text(), self.value2.text()))
        self.add.setCheckable(True)
        self.subtract.setCheckable(True)
        self.multiply.setCheckable(True)
        self.divide.setCheckable(True)

        result_lab = QLabel("Result", self)
        self.ans.setEnabled(True)
        self.ans.setMinimumWidth(100)
        self.ans.setMinimumHeight(25)
        self.ans.setStyleSheet("background-color: grey;color:yellow")
        self.ans.setText(None)


        hbox1 = QHBoxLayout()
        hbox1.addWidget(self.value1)
        hbox1.addWidget(self.slider1)

        hbox2 = QHBoxLayout()
        hbox2.addWidget(self.value2)
        hbox2.addWidget(self.slider2)

        hbox3 = QHBoxLayout()
        hbox3.addWidget(self.add)
        hbox3.addWidget(self.subtract)
        hbox3.addWidget(self.multiply)
        hbox3.addWidget(self.divide)

        hbox4 = QHBoxLayout()
        hbox4.addWidget(result_lab)
        hbox4.addWidget(self.ans)

        vbox = QVBoxLayout()
        vbox.addLayout(hbox1)
        vbox.addLayout(hbox2)
        vbox.addLayout(hbox3)
        vbox.addLayout(hbox4)

        self.setLayout(vbox)
        self.adjustSize()
        self.setWindowTitle("Simple Calculator")
        self.show()

    def change_value(self, value):
        updated_value = value
        sender_slider = self.sender()
        if sender_slider == self.slider1:
            self.value1.setText(str(updated_value))
        elif sender_slider == self.slider2:
            self.value2.setText(str(updated_value))

    def calculate(self, a, b):
        value1 = int(a)
        value2 = int(b)
        if self.add.isChecked() :
            answer = value1 + value2
        elif self.subtract.isChecked():
            answer = value1 - value2
        elif self.multiply.isChecked():
            answer = value1 * value2
        elif self.divide.isChecked():
            try:
                answer = value1 / value2
            except ZeroDivisionError:
                answer = "Error"
        else:
            answer = "no operation"
        self.ans.setText(str(answer))

    def set_pressed(self):
        sender = self.sender()
        if sender.text() == "Add":
            self.add.setChecked(True)
            self.subtract.setChecked(False)
            self.multiply.setChecked(False)
            self.divide.setChecked(False)
        elif sender.text() == "Subtract":
            self.add.setChecked(False)
            self.subtract.setChecked(True)
            self.multiply.setChecked(False)
            self.divide.setChecked(False)
        elif sender.text() == "Multiply":
            self.add.setChecked(False)
            self.subtract.setChecked(False)
            self.multiply.setChecked(True)
            self.divide.setChecked(False)
        elif sender.text() == "Divide":
            self.add.setChecked(False)
            self.subtract.setChecked(False)
            self.multiply.setChecked(False)
            self.divide.setChecked(True)





def main():
    app = QApplication(sys.argv)
    ex = Problem1()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()