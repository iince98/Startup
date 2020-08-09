#pyside2-uic frontend.ui > frontend.py
#pyinstaller --onefile frontend_main.py

from PySide2 import QtWidgets, QtGui, QtCore, QtSql 

import frontend

class Myfrontend (frontend.Ui_MainWindow, QtWidgets.QMainWindow):
    def __init__(self):
        super(Myfrontend, self). __init__()
        self.setupUi(self)
        self.showMaximized()

        self.cb_modul.currentIndexChanged.connect(self.cbmodul_selectionchange)
        #self.cb_modul.currentIndexChanged.connect(self.createDB)
        #self.createDB()

    def cbmodul_selectionchange(self):
        self.lineEdit_3.setText (self.cb_modul.currentText())
        if self.cb_modul.currentText() == "Modul 1":
            self.cb_versuchart.setEnabled(False)
        else:
            self.cb_versuchart.setEnabled(True)


    ######## Create DATABASE 
    def createDB(self):
        db = QtSql.QSqlDatabase.addDatabase('QSQLITE')
        db.setDatabaseName('sports.db')
            
        if not db.open():
            QtGui.QMessageBox.critical(None, QtGui.qApp.tr("Cannot open database"),
                QtGui.qApp.tr("Unable to establish a database connection.\n"
                    "This example needs SQLite support. Please read "
                    "the Qt SQL driver documentation for information "
                    "how to build it.\n\n" "Click Cancel to exit."),
                QtGui.QMessageBox.Cancel)
                    
            return False
                
        query = QtSql.QSqlQuery()
            
        query.exec_("create table sportsmen(id int primary key, "
            "firstname varchar(20), lastname varchar(20))")
                
        query.exec_("insert into sportsmen values(101, 'Ibrahim', 'Federer')")
        query.exec_("insert into sportsmen values(102, 'Christiano', 'Ronaldo')")
        query.exec_("insert into sportsmen values(103, 'Ussain', 'Bolt')")
        query.exec_("insert into sportsmen values(104, 'Sachin', 'Tendulkar')")
        query.exec_("insert into sportsmen values(105, 'Saina', 'Nehwal')")
        query.exec_("insert into sportsmen values(106, 'Ibrahim', 'Ince')")
        return True
        ###### DATABASE ############################################

if __name__ == "__main__":
    app = QtWidgets.QApplication()
    tr = Myfrontend()
    tr.show()
    app.exec_()
