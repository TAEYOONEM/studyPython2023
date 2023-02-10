# 레이아웃 절대적 배치

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QComboBox
from PyQt5.QtCore import Qt

class MyApp(QWidget) :
    def __init__(self) :
        super().__init__()
        self.initUI()

    def initUI(self) :
        self.lblOption = QLabel('선택값: ',self)
        self.lblOption.move(20,20)

        cbOption = QComboBox(self)
        cbOption.addItem('Option1')
        cbOption.addItem('Option2')
        cbOption.addItem('Option3')
        cbOption.addItem('Option4')
        cbOption.move(20,40)
        
        cbOption.activated[str].connect(self.onActivated)
        
    
        # 필수 설정
        self.setWindowTitle('Combo Box')
        self.setGeometry(300, 300, 300, 300)
        self.show()
    
    def onActivated(self, text) :
        self.lblOption.setText('선택값: ' +text)
        self.lblOption.adjustSize()


if __name__ == '__main__' :
    app =  QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())