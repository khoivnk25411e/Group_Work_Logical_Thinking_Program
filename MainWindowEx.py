<<<<<<< Updated upstream
<<<<<<< Updated upstream
class MainWindowEx(Ui_MainWindow):
=======
=======
>>>>>>> Stashed changes
from MainWindow import Ui_MainWindow


class MainWindowEx(Ui_MainWindow):
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.setupSignalandSlots()
    def setupSignalandSlots(self):
        self.pushButtonClose.clicked.connect(self.process_close)
        self.pushButtonClear.clicked.connect(self.process_clear)
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
<<<<<<< Updated upstream
    
>>>>>>> Stashed changes
=======
    
>>>>>>> Stashed changes
