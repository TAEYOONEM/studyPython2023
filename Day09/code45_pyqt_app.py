import sys
from PyQt5.QtWidgets import QApplication, QWidget

class MyApp(QWidget) :
    
    def __init__(self) :
        super().__init__()
        # GUI 화면 설정
        self.initUI()

    def initUI(self) :
        self.setWindowTitle('simple window')
        # self.move(1500,300)
        self.resize(400,200)
        self.show()

if __name__ == '__main__' :
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
    
