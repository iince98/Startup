from PySide2 import QtWidgets, QtGui, QtCore 
import frontend

class Myfrontend (frontend.Ui_MainWindow, QtWidgets.QMainWindow):
    def __init__(self):
        super(Myfrontend, self). __init__()
        self.setupUi(self)
        self.showMaximized()

if __name__ == "__main__":
    app = QtWidgets.QApplication()
    tr = Myfrontend()
    tr.show()
    app.exec_()
