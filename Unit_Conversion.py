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

        self.setWindowTitle('Unit Conversion')
        self.setGeometry(300, 300, 400, 300)
        self.show()


class FirstTab(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        name = QLabel('Length Input:')
        self.nameedit = QLineEdit()

        self.nameedit.textChanged[str].connect(self.onActivated)
        self.lbl=QLabel('', self)

        
        
        self.combo = QComboBox()
        list = ['mm','cm','m','km']
        self.combo.addItems(list)
        self.combo.activated[str].connect(self.onActivated)
        
        vbox1=QVBoxLayout()
        vbox1.addWidget(name)
        vbox1.addWidget(self.nameedit)
        vbox1.addWidget(self.combo)
        vbox1.addWidget(self.lbl)
        vbox1.addStretch()

        self.setLayout(vbox1) 


    def onActivated(self):
        num1=float(self.nameedit.text())
        text=self.combo.currentText()
        if text =='mm':
            mmNum=str(num1)+'mm'
            cmNum=str(num1/10)+'cm'
            mNum=str(num1/1000)+'m'
            kmNum=str(num1/1000000)+'km'

        elif text =='cm':
            mmNum=str(num1*10)+'mm'
            cmNum=str(num1)+'cm'
            mNum=str(num1/100)+'m'
            kmNum=str(num1/100000)+'km'

        elif text =='m':
            mmNum=str(num1*1000)+'mm'
            cmNum=str(num1*100)+'cm'
            mNum=str(num1)+'m'
            kmNum=str(num1/1000)+'km'

        elif text =='km':
            mmNum=str(num1*1000000)+'mm'
            cmNum=str(num1*100000)+'cm'
            mNum=str(num1*1000)+'m'
            kmNum=str(num1)+'km'

        self.lbl.setText(mmNum+'\n'+cmNum+'\n'+mNum+'\n'+kmNum)


# def onChanged(self, text):
#       self.num=text
#       self.onActivated()



class SecondTab(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        name = QLabel('Weight Input:')
        self.nameedit = QLineEdit()

        self.nameedit.textChanged[str].connect(self.onActivated)
        self.lbl=QLabel('', self)


        self.combo = QComboBox()
        list = ['mg','g','kg','t']
        self.combo.addItems(list)
        self.combo.activated[str].connect(self.onActivated)


        vbox1=QVBoxLayout()
        vbox1.addWidget(name)
        vbox1.addWidget(self.nameedit)
        vbox1.addWidget(self.combo)
        vbox1.addWidget(self.lbl)
        vbox1.addStretch()

        self.setLayout(vbox1)


    def onActivated(self, text):

        num1=float(self.nameedit.text())
        text=self.combo.currentText()
        if text =='mg':
            mmNum=str(num1)+'mg'
            cmNum=str(num1/1000)+'g'
            mNum=str(num1/1000000)+'kg'
            kmNum=str(num1/1000000000)+'t'

        elif text =='g':
            mmNum=str(num1*1000)+'mg'
            cmNum=str(num1)+'g'
            mNum=str(num1/1000)+'kg'
            kmNum=str(num1/1000000)+'t'

        elif text =='kg':
            mmNum=str(num1*1000000)+'mg'
            cmNum=str(num1*1000)+'g'
            mNum=str(num1)+'kg'
            kmNum=str(num1/1000)+'t'

        elif text =='t':
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
