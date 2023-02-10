#  다이얼로그 + 메세지 박스

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon

class MyApp(QMainWindow) :
    def __init__(self) :
        super().__init__()
        self.initUI()

    def initUI(self) :
        self.textEdit = QTextEdit()
        self.setCentralWidget(self.textEdit)
        self.statusBar()
        
        openFile = QAction(QIcon('./Day10/cow.png'), 'Open', self)
        openFile.setShortcut('Ctrl+O')
        openFile.setStatusTip('파일 열기')
        openFile.triggered.connect(self.showDialog)
        
        menubar = self.menuBar()
        menubar.setNativeMenuBar(False)
        fileMenu = menubar.addMenu('&File')
        fileMenu.addAction(openFile)

        # 필수 설정
        self.setWindowTitle('파일 다이얼로그')
        self.setGeometry(300, 300, 300, 300)
        self.show()

    def showDialog(self):
        fname = QFileDialog.getOpenFileName(self, 'Open file', './')
        if fname[0]: # 파일을 선택했다면
            f = open(fname[0], 'rt',encoding='utf-8') 
            with f: 
                data = f.read()
                self.textEdit.setText(data)
            f.close()
    
    def closeEvent(self, event):
        reply = QMessageBox.question(self, '종료', '종료하시겠습니까?',
                                    QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()
        
        QMessageBox.about(self,'성공','로드했습니다.')

if __name__ == '__main__' :
    app =  QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())