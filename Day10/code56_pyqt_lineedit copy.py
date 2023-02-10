# 라인 에디트 - textbox

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt

class MyApp(QWidget) :
    def __init__(self) :
        super().__init__()
        self.initUI()

    def initUI(self) :
        self.lblResulk  =QLabel(self)
        self.lblResulk.move(20, 20)

        txtInput = QLineEdit(self)
        txtInput.move(20, 40)
        txtInput.textChanged[str].connect(self.onChanged)
        
        # 필수 설정
        self.setWindowTitle('Line Edit')
        self.setGeometry(300, 300, 300, 300)
        self.show()
    
    def onChanged(self, text):
        self.lblResulk.setText(text)
        self.lblResulk.adjustSize()

if __name__ == '__main__' :
    app =  QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())