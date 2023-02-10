#  다이얼로그

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap

class MyApp(QWidget) :
    def __init__(self) :
        super().__init__()
        self.initUI()

    def initUI(self) :
        self.btnDlg = QPushButton('이름',self)
        self.btnDlg.move(30, 30)
        self.btnDlg.clicked.connect(self.onClicked)
        
        self.txtInput =QLineEdit(self)
        self.txtInput.move(30, 60)

        


        # 필수 설정
        self.setWindowTitle('다이얼로그')
        self.setGeometry(300, 300, 300, 300)
        self.show()
    
    def onClicked(self) :
        text, ok = QInputDialog.getText(self, '인풋 다이얼로그', '이름을 입력하시오:')
        if ok:
            self.txtInput.setText(text)

if __name__ == '__main__' :
    app =  QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())