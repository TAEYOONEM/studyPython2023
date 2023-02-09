import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, qApp, QDesktopWidget
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QDate,QTime

class MyApp(QMainWindow) :
    
    def __init__(self) :
        super().__init__()
        self.initUI()

    def initUI(self) :
        # 메뉴바
        actExit = QAction(QIcon('./Day09/exit.png'),'exit',self)
        actExit.setShortcut('Ctrl+Q')
        actExit.setStatusTip('앱종료')
        actExit.triggered.connect(qApp.quit)

        actSave = QAction(QIcon('./Day09/save.png'),'save',self)
        actSave.setShortcut("Ctrl+S")
        actSave.setStatusTip('저장')

        menubar = self.menuBar()
        menubar.setNativeMenuBar(False)
        filemenu = menubar.addMenu('&File')
        filemenu.addAction(actExit)
        filemenu.addAction(actSave)

        # 툴바
        toolbar = self.addToolBar('toolbar')
        toolbar.addAction(actExit)
        toolbar.addAction(actSave)

        # 상태바
        now = QDate.currentDate()
        time = QTime.currentTime()
        self.statusBar().showMessage(now.toString('yyyy-MM-dd') +' '+time.toString())
        self.setWindowIcon(QIcon('./Day09/iot.png'))

        # GUI 화면 설정
        self.setWindowTitle('bar window')
        # self.move(1500,300)
        self.resize(400,200)
        self.setCenter()
        self.show()

    # 화면 중심 셋팅
    def setCenter(self) :
        qr = self.frameGeometry() # 창의 위치값
        cp =QDesktopWidget().availableGeometry().center() # 화면 중심 파악
        qr.moveCenter(cp) # 직사각형 위치를 중심으로
        self.move(qr.topLeft()) #창을 직사각형 위치로

if __name__ == '__main__' :
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
    
