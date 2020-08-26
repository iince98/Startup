#pyside2-uic frontend.ui > frontend.py
#pyinstaller --onefile frontend_main.py

from PySide2 import QtWidgets, QtGui, QtCore, QtSql
from PySide2.QtGui import QStandardItemModel
from PySide2.QtCore import QDateTime, Qt, QRect, QSize
from PySide2.QtGui import QPainter
from PySide2.QtWidgets import (QWidget, QHeaderView, QHBoxLayout, QTableView,
                               QSizePolicy, QTableWidget, QLabel, QAction, QDockWidget, QFrame)
from PySide2.QtCharts import QtCharts

import frontend
import pandas as pd


class Myfrontend (frontend.Ui_MainWindow, QtWidgets.QMainWindow):
    def __init__(self):
        super(Myfrontend, self). __init__()
        self.setupUi(self)
        self.showMaximized()

        self.cb_modul.currentIndexChanged.connect(self.cbmodul_selectionchange)
        #self.cb_modul.currentIndexChanged.connect(self.createDB)
        #self.createDB()

        self.btn_asc_lesen_2.clicked.connect(self.bring_data)
        #self.tableWidget.CurrentChanged.connect(self.label_write)
        #self.tableview.setModel(tablemodel)
        #self.tableview.clicked.connect(self.viewClicked)
        
        ######### Create MENU
        bar = self.menuBar()

        file = bar.addMenu("Create Component")
        file.addAction("Component_1")
        file.addAction("Component_2")
        file.addAction("Component_3")
        file.triggered[QAction].connect(self.combo_box_selectionchange)

        ######### Create MENU
    


    



    
    def combo_box_selectionchange(self, q):
        my_dock_widget = QDockWidget (str(q.text()), self.tab_2)
        my_dock_widget.setAllowedAreas(Qt.LeftDockWidgetArea | Qt.TopDockWidgetArea | Qt.BottomDockWidgetArea | Qt.RightDockWidgetArea)
        self.addDockWidget(Qt.LeftDockWidgetArea, my_dock_widget)
        my_dock_widget.move(100,100)
        my_dock_widget.setWindowTitle(q.text())
        #icon = QtGui.QIcon()
        #icon.addPixmap(QtGui.QPixmap("ukraine.png",QtGui.QIcon.Normal, QtGui.QIcon.On))
        #topleftwindow.windowIcon(icon)
        my_dock_widget.show()
    # def viewClicked(self):
    #     self.label_cell = QLabel(self.tab_2)
    #     self.label_cell.setObjectName(self.tableview.currentIndex())

    #     self.tableWidget.setCurrentCell ="10"
    
    def label_write (self):
        pass
    
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

    def bring_data(self):
        print("Hi")
        #### Create TableWidget 

        self.dock_for_table = QDockWidget(self.tab_2)
        self.tableWidget = QTableWidget(self.dock_for_table)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setGeometry(QRect(50, 6, 431, 650))
        #sizePolicy.setHeightForWidth(self.tableWidget.sizePolicy().hasHeightForWidth())
        #self.tableWidget.setSizePolicy(sizePolicy)
        #self.tableWidget.setFrameShape(QFrame.WinPanel)
        #self.tableWidget.setFrameShadow(QFrame.Raised)
        #self.tableWidget.setLineWidth(4)
        #self.tableWidget.setMidLineWidth(7)


        ##### Read the File
        self.tableWidget.clear()

        filename = QtWidgets.QFileDialog.getOpenFileName(self, "Open File",  "/Users/macpro/Downloads/")[0]
        print(filename)
        dataset=pd.read_csv(filename,delimiter="\t")
        new = dataset["    file"].str.split(" ", n = 1, expand = True) 
        dataset["number"] = new[0]
        dataset["value"] = new[1]
        group = dataset.groupby("number")
        group_35=group.get_group ("035")
        print(len(group_35))

        
    
        ####### Create QtableWidget in 
        #self.tableWidget.setFixedWidth(800)
        #self.tableWidget.setFixedHeight(600)

        self.r_number = group_35.shape[0]
        self.col_number = group_35.shape[1]
        self.tableWidget.setColumnCount(self.col_number)
        self.tableWidget.setRowCount(self.r_number)
        self.tableWidget.setRowCount(0)
        self.tableWidget.setHorizontalHeaderLabels(group_35.columns)
        self.tableWidget.horizontalHeader().setDefaultAlignment(QtCore.Qt.AlignCenter | QtCore.Qt.TextWordWrap)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)

        #self.chart = QtCharts.QChart()
        #self.chart.setAnimationOptions(QtCharts.QChart.AllAnimations)
        #self.add_series("Magnitude (Column 1)", [0, 1])

        for i in range (self.r_number):
            self.tableWidget.insertRow(i)
            for j in range(self.col_number):
                self.tableWidget.setItem(i, j, QtWidgets.QTableWidgetItem(str(group_35.iloc[i,j])))

        


if __name__ == "__main__":
    app = QtWidgets.QApplication()
    tr = Myfrontend()
    tr.show()
    app.exec_()
