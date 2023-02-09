# 레이아웃 절대적 배치

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt

class MyApp(QWidget) :
    def __init__(self) :
        super().__init__()
        self.initUI()

    def initUI(self) :
        cbShowTitle = QCheckBox('Show title', self)    
        cbShowTitle.move(20, 20)
        cbShowTitle.toggle()
        cbShowTitle.stateChanged.connect(self.changeTitle)
        
        # 필수 설정
        self.setWindowTitle('QCheckBox')
        self.setGeometry(300, 300, 400, 200)
        self.show()
    def changeTitle(self, state):
        if state == Qt.Checked:
            self.setWindowTitle('QCheckBox')
        else:
            self.setWindowTitle(' ')



if __name__ == '__main__' :
    app =  QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())