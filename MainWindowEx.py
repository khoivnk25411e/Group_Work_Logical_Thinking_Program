from MainWindow import Ui_MainWindow


def ptb2(a,b,c):
    pass


class MainWindowEx(Ui_MainWindow):
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.setupSignalandSlots()
        self.MainWindow=MainWindow
    def setupSignalandSlots(self):
        self.pushButtonClose.clicked.connect(self.process_close)
        self.pushButtonClear.clicked.connect(self.process_clear)
        self.pushButtonSolve.clicked.connect(self.process_solve)
    def ShowWindow(self):
        self.MainWindow.show()
    def process_close(self):
        self.MainWindow.close()
    def process_clear(self):
        self.lineEditA.clear()
        self.lineEditB.clear()
        self.lineEditC.clear()
        self.lineEditResult.clear()
        self.lineEditA.setFocus()
    def process_solve(self):
        a=int(self.lineEditA.text())
        b=int(self.lineEditB.text())
        c=int(self.lineEditC.text())
        value=ptb2(a,b,c)
        pass