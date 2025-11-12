from PyQt6.QtWidgets import QApplication, QMainWindow

app=QApplication([])
myWindow= MainWindowEx()
myWindow.setupUi(QMainWindow())
myWindow.show()
app.exec()