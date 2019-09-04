import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QGridLayout, QLabel, QLineEdit, QTextEdit, QPushButton)

class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()
#    self.old=''
        self.new = '0'
#       self.operator = ''
#    self.new=''

      
        self.num1=QPushButton('1')
        self.num1.clicked.connect(self.btn1)

    def btn1(self):
        print("test 1")
        print(self.num1.text())

    def initUI(self):


# num1 = QPushButton('1')
        
#      self.num1.clicked.connect(self.btn1)
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
        equal_btn=QPushButton('=')


        grid = QGridLayout()
        self.setLayout(grid)
        self.label = QLabel()
#       self.label.setText('<p align="right"><font size=30><b>' + self.new + '</b></font></p>')
        
#   self.label.setText()
        grid.addWidget(self.label, 0, 0, 1, 4)
# grid.addWidget(QLabel('Result:'), 0, 0)
#        result=self.new
        grid.addWidget(QLineEdit(),0,1)

        grid.addWidget(num7, 1, 0)

        grid.addWidget(num8, 1, 1)
        
        grid.addWidget(num9, 1, 2)
    
        grid.addWidget(minus_btn,1,4)
        
        grid.addWidget(num4, 2, 0)
        grid.addWidget(num5, 2, 1)
        grid.addWidget(num6, 2, 2)
        
        grid.addWidget(plus_btn,2,4)


        grid.addWidget(self.num1, 3, 0)
        grid.addWidget(num2, 3, 1)
        grid.addWidget(num3, 3, 2)

        grid.addWidget(equal_btn,3,4)

        grid.addWidget(num0,4,0)
        grid.addWidget(del_btn,4,2)

        
        self.setWindowTitle('QGridLayout')
        self.setGeometry(300, 300, 300, 200)
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())

