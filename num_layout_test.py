import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QGridLayout, QLabel, QLineEdit, QTextEdit, QPushButton)


class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        num1 = QPushButton('1')
        num2 = QPushButton('2')
        num3 = QPushButton('3')
        num4 = QPushButton('4')
        num5 = QPushButton('5')
        num6 = QPushButton('6')
        num7 = QPushButton('7')
        num8 = QPushButton('8')
        num9 = QPushButton('9')
       
        num0 = QPushButton('0')
        del_btn=QPushButton('del')
        plus_btn=QPushButton('+')
        minus_btn=QPushButton('-')

        grid = QGridLayout()
        self.setLayout(grid)
# grid.addWidget(QLabel('Title:'), 0, 0)
#       grid.addWidget(QLabel('Author:'), 1, 0)
#       grid.addWidget(QLabel('Review:'), 2, 0)
        grid.addWidget(num7, 0, 0)
        grid.addWidget(QLineEdit(), 1, 1)
        grid.addWidget(QTextEdit(), 2, 1)
        self.setWindowTitle('QGridLayout')
        self.setGeometry(300, 300, 300, 200)
        self.show()
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
