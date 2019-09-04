import sys
from PyQt5.QtWidgets import *


class MyApp(QDialog):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        tabs = QTabWidget()
        tabs.addTab(FirstTab(), '길이')
        tabs.addTab(SecondTab(), '무게')

        buttonbox = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        buttonbox.accepted.connect(self.accept)
        buttonbox.rejected.connect(self.reject)

        vbox = QVBoxLayout()
        vbox.addWidget(tabs)
        vbox.addWidget(buttonbox)

        self.setLayout(vbox)

        self.setWindowTitle('QTabWidget')
        self.setGeometry(300, 300, 400, 300)
        self.show()


class FirstTab(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        name = QLabel('Length Input:')
        nameedit = QLineEdit()

        nameedit.textChanged[str].connect(self.onChanged)
        self.lbl=QLabel('test', self)

        self.num='0'
        
        combo = QComboBox()
        list = ['mm','cm','m','km']
        combo.addItems(list)
        combo.activated[str].connect(self.onActivated)
        
    
        vbox1=QVBoxLayout()
        vbox1.addWidget(name)
        vbox1.addWidget(nameedit)
        vbox1.addWidget(combo)
        vbox1.addWidget(self.lbl)
        vbox1.addStretch()

        self.setLayout(vbox1) 


    def onActivated(self, text):
        if text =='mm':
            num1=float(self.num)
            mmNum=str(num1)+'mm'
            cmNum=str(num1/10)+'cm'
            mNum=str(num1/1000)+'m'
            kmNum=str(num1/1000000)+'km'
            self.lbl.setText(mmNum+'\n'+cmNum+'\n'+mNum+'\n'+kmNum)

        elif text =='cm':
            num1=float(self.num)
            mmNum=str(num1*10)+'mm'
            cmNum=str(num1)+'cm'
            mNum=str(num1/100)+'m'
            kmNum=str(num1/100000)+'km'
            self.lbl.setText(mmNum+'\n'+cmNum+'\n'+mNum+'\n'+kmNum)

        elif text =='m':
            num1=float(self.num)
            mmNum=str(num1*1000)+'mm'
            cmNum=str(num1*100)+'cm'
            mNum=str(num1)+'m'
            kmNum=str(num1/1000)+'km'
            self.lbl.setText(mmNum+'\n'+cmNum+'\n'+mNum+'\n'+kmNum)

        else:
            num1=float(self.num)
            mmNum=str(num1*1000000)+'mm'
            cmNum=str(num1*100000)+'cm'
            mNum=str(num1*1000)+'m'
            kmNum=str(num1)+'km'
            self.lbl.setText(mmNum+'\n'+cmNum+'\n'+mNum+'\n'+kmNum)


    def onChanged(self, text):
        self.num=text


class SecondTab(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        name = QLabel('Weight Input:')
        nameedit = QLineEdit()

        nameedit.textChanged[str].connect(self.onChanged)
        self.lbl=QLabel('test', self)

        self.num='0'

        combo = QComboBox()
        list = ['mg','g','kg','t']
        combo.addItems(list)
        combo.activated[str].connect(self.onActivated)


        vbox1=QVBoxLayout()
        vbox1.addWidget(name)
        vbox1.addWidget(nameedit)
        vbox1.addWidget(combo)
        vbox1.addWidget(self.lbl)
        vbox1.addStretch()

        self.setLayout(vbox1)


    def onActivated(self, text):
        if text =='mg':
            num1=float(self.num)
            mmNum=str(num1)+'mg'
            cmNum=str(num1/1000)+'g'
            mNum=str(num1/1000000)+'kg'
            kmNum=str(num1/1000000000)+'t'
            self.lbl.setText(mmNum+'\n'+cmNum+'\n'+mNum+'\n'+kmNum)

        elif text =='g':
            num1=float(self.num)
            mmNum=str(num1*1000)+'mg'
            cmNum=str(num1)+'g'
            mNum=str(num1/1000)+'kg'
            kmNum=str(num1/1000000)+'t'
            self.lbl.setText(mmNum+'\n'+cmNum+'\n'+mNum+'\n'+kmNum)

        elif text =='kg':
            num1=float(self.num)
            mmNum=str(num1*1000000)+'mg'
            cmNum=str(num1*1000)+'g'
            mNum=str(num1)+'kg'
            kmNum=str(num1/1000)+'t'
            self.lbl.setText(mmNum+'\n'+cmNum+'\n'+mNum+'\n'+kmNum)

        else:
            num1=float(self.num)
            mmNum=str(num1*1000000000)+'mg'
            cmNum=str(num1*1000000)+'g'
            mNum=str(num1*1000)+'kg'
            kmNum=str(num1)+'t'
            self.lbl.setText(mmNum+'\n'+cmNum+'\n'+mNum+'\n'+kmNum)


    def onChanged(self, text):
        self.num=text




if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
