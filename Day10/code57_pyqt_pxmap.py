#  이미지 처리 위젯

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap

class MyApp(QWidget) :
    def __init__(self) :
        super().__init__()
        self.initUI()

    def initUI(self) :
        pixmap = QPixmap('./Day10/cow.png')

        lblImage = QLabel(self)
        lblImage.setPixmap(pixmap)

        lblSize = QLabel(str(pixmap.width()) +'x'+str(pixmap.height()))
        lblSize.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        vbox = QVBoxLayout(self)
        vbox.addWidget(lblImage)
        vbox.addWidget(lblSize)
        self.setLayout(vbox)
        
        # 필수 설정
        self.setWindowTitle('이미지 위젯')
        self.setGeometry(300, 300, 300, 300)
        self.show()


if __name__ == '__main__' :
    app =  QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())