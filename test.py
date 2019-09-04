import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QTabWidget, QVBoxLayout, QLabel, QLineEdit)


class MyApp(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        self.lbl=QLabel(self)
        self.lbl.move(60,40)

        qle=QLineEdit(self)
        qle.move(60,100)
        qle.textChanged[str].connect(self.onChanged)
        
        tab1 = QWidget()
#tab1 = qle()
        tab2 = QWidget()

        tabs = QTabWidget()
        tabs.addTab(tab1, '길이')
        tabs.addTab(tab2, '무게')

        
        vbox = QVBoxLayout()
        vbox.addWidget(tabs)

        
        self.setLayout(vbox)

        self.setWindowTitle('QTabWidget')
        self.setGeometry(300, 300, 300, 200)
        self.show()

    def onChanged(self, text):
        self.lbl.setText(text)
        self.lbl.adjustSize()
if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
