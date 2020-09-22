#pyside2-uic frontend.ui > frontend.py
#pyinstaller --onefile frontend_main.py

from PySide2 import QtWidgets, QtGui, QtCore, QtSql
from PySide2.QtGui import QStandardItemModel
from PySide2.QtCore import QDateTime, Qt, QRect, QSize
from PySide2.QtGui import QPainter 
from PySide2.QtWidgets import (QWidget, QHeaderView, QHBoxLayout, QTableView,
                               QSizePolicy, QTableWidget, QLabel, QAction, QDockWidget,
                                QFrame, QAbstractItemView, QMdiArea, QMdiSubWindow, QScrollArea,
                                QMessageBox)
from PySide2.QtCharts import QtCharts
import frontend
import pandas as pd
import numpy as np
import pyqtgraph as pg
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg, NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure
import sys
import matplotlib.pyplot as plt
#matplotlib.use('Qt5Agg')


class MplCanvas(FigureCanvasQTAgg):

    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)
        super(MplCanvas, self).__init__(fig)

class Myfrontend (frontend.Ui_MainWindow, QtWidgets.QMainWindow):
    def __init__(self):
        super(Myfrontend, self). __init__()
        self.setupUi(self)
        self.showMaximized()
        global filename, column_names
        filename = "/Users/macpro/Downloads/DS-Demo-Log.txt"
        column_names =[]
        

        ######### Create MENU
        bar = self.menuBar()

        file = bar.addMenu("Create Component")
        file.addAction("Component_1")
        file.addAction("Component_2")
        file.addAction("Component_3")
        file.triggered[QAction].connect(self.combo_box_selectionchange)
        
        
        self.tableWidget = QTableWidget()
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setGeometry(QRect(50, 6, 100, 50))
        self.tableWidget.resizeColumnsToContents()
        self.tableWidget.resizeRowsToContents()
        self.tableWidget.itemSelectionChanged.connect(self.draw_graph)
        
        #self.tablewidget_2.itemSelectionChanged.connect(self.fill_table)
        #self.tableWidget.setSelectionBehavior(QTableWidget.SelectRows)

        self.mdi = QMdiArea(self.tab_2)
        self.mdi.tileSubWindows()
        self.mdi_width = self.tabWidget.width()
        self.mdi_height = self.tabWidget.height()
        self.mdi.setGeometry(QRect(0,0, self.mdi_width,self.mdi_height))
        #self.tableWidget.selectionChanged.connect(self.on_customContextMenuRequested)
        #self.tableWidget.customContextMenuRequested.connect(self.on_customContextMenuRequested)
        #self.tableWidget.SelectedClicked.connect(self.on_customContextMenuRequested)
        ######### Create MENU

        sub = QMdiSubWindow()
        self.sub_combo = QtWidgets.QComboBox()
        report_list =[" ", "Report 27","Report 33", "Report 35", "Report 37", "Report 39", "Report 41"]
        for i in report_list:
            self.sub_combo.addItem(i)
        sub_layout = QtWidgets.QVBoxLayout()

        sub_layout.addWidget(self.gb_Ablesevorgang)
        sub_layout.addWidget(self.sub_combo)
        sub_layout.addWidget(self.tableWidget)
        sub_widget= QtWidgets.QWidget()
        sub_widget.setLayout(sub_layout)

        sub.setWindowTitle("Reports")
        sub.setWidget(sub_widget)
        self.mdi.addSubWindow(sub)
        
        self.btn_asc_lesen_2.clicked.connect(self.read_data)
        self.sub_combo.currentIndexChanged.connect(self.fill_table)
        self.cb_modul.currentIndexChanged.connect(self.cbmodul_selectionchange)
        
        #self.cb_modul.currentIndexChanged.connect(self.createDB)
        #self.createDB()


        
        global sc
        sc = MplCanvas(self, width=5, height=4, dpi=100)
  
        self.tableWidget.clear()
    
       
       
        #### SUB1 Graph area creation
        sub1 = QMdiSubWindow()
        toolbar = NavigationToolbar(sc, self)
        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(toolbar)
        layout.addWidget(sc)
        widget = QtWidgets.QWidget()
        widget.setLayout(layout)
        sub1.setWidget(widget)
        self.mdi.addSubWindow(sub1)

    
    def read_data (self):
        #filename = QtWidgets.QFileDialog.getOpenFileName(self, "Open File",  "/Users/macpro/Downloads/")[0]
        global filename
        filename = "/Users/macpro/Downloads/Log_demo2.txt"

        self.tabWidget.setCurrentWidget(self.tab_2)

    

    def fill_table(self):
        dataset=pd.read_csv(filename, delimiter="\t")
        column_name_type = self.sub_combo.currentText()
        #print(column_name_type)
        new = dataset["    file"].str.split(" ", n = 1, expand = True) 

        dataset["number"] = new[0]
        dataset["value"] = new[1]
        all_report_types = list(new[0])
        report_list =[]
        ### Remove blanks
        while "" in all_report_types:
            all_report_types.remove("")
        #### Remove non suitable report types(ending with "-")
        for i in all_report_types:
            if i[0] =="0" and i[-1]!="-":
                report_list.append(i)
        ### Remove duplicates
        global report_list_ready
        report_list_ready =list(dict.fromkeys(report_list)) 
        group = dataset.groupby("number")
        
        col_name_pd = pd.read_excel("column_names_ONLY.xlsx", index_col="number")
        for col in col_name_pd.columns:
            col_name_pd[col]= col_name_pd[col].replace("\n", "") 
            col_name_pd[col]= col_name_pd[col].replace(np.nan, "")
        global column_names
        column_names = col_name_pd.loc[int(column_name_type.split(" ")[1])]
        group_to_be_selected = "0"+column_name_type.split(" ")[1]
        #print(group_to_be_selected)
        try:
            group_selected=group.get_group(group_to_be_selected)
        except:
            QMessageBox.about(self, "Warning", "There is no {} in the file selected".format(column_name_type))
        #print(group_selected.shape)

        group_selected = group_selected.iloc[:,2:-2]
        group_selected.dropna(inplace=True, axis=1)
        

        ### Clean the Dataframe
        for i in range(group_selected.shape[0]):
            for j in range(group_selected.shape[1]):
                #print(group_selected.iloc[i,j])
                try:
                    if group_selected.iloc[i,j].count(".") >= 2:
                        v = group_selected.iloc[i,j].split(".")
                        v1 = v[0]
                        v2 = v[1]
                        num = float("{}.{}".format(v1, v2))
                        # print(num)
                        num = round(num, 2)
                        group_selected.iloc[i,j] = num
                    else:
                        num = float(group_selected.iloc[i,j])
                        num = round(num, 2)
                        group_selected.iloc[i,j] = num
                except:
                    print(group_selected.iloc[i,j], "Fail")
    

       
        self.r_number = group_selected.shape[0]
        self.col_number = group_selected.shape[1]
        self.label.setText("Datenspalten ausgelesen: {}".format(self.col_number))
        self.label_2.setText("Datenszeilen ausgelesen: {}".format(self.r_number))
        self.tableWidget.setColumnCount(self.col_number)
        self.tableWidget.setRowCount(self.r_number)
        self.tableWidget.setRowCount(0)
        self.tableWidget.setHorizontalHeaderLabels(column_names)
        #self.tableWidget.horizontalHeader().setDefaultAlignment(QtCore.Qt.AlignCenter | QtCore.Qt.TextWordWrap)
        self.tableWidget.horizontalHeader().setResizeMode(QtGui.QHeaderView.ResizeToContents)
        #self.chart = QtCharts.QChart()
        #self.chart.setAnimationOptions(QtCharts.QChart.AllAnimations)
        #self.add_series("Magnitude (Column 1)", [0, 1])
        #print(self.r_number, self.col_number)
        
        for i in range (self.r_number):
            self.tableWidget.insertRow(i)
            for j in range(self.col_number):
                
                self.tableWidget.setItem(i, j, QtWidgets.QTableWidgetItem(str(group_selected.iloc[i,j])))
        self.tableWidget.scrollToBottom()
        



    def draw_graph(self):
        indexes_ =[]
        indexes_text =[]
        for selectionRange in self.tableWidget.selectedRanges():
            indexes_.extend(range(selectionRange.topRow(), selectionRange.bottomRow()+1))
        indexes_ = list(map(int, indexes_))
        #print ("indexes", indexes_, type(indexes_))      # indexes is a list like [0, 2] of selected rows
        #print(self.tableWidget.selectedRanges())
        #print(self.tableWidget.item(self.tableWidget.currentRow(), self.tableWidget.currentColumn()).text()) 
        indexes_text = [float(self.tableWidget.item(i, self.tableWidget.currentColumn()).text()) for i in indexes_]
        #sc.resize(400,400)
        
        x_axes = [float(self.tableWidget.item(i, 0).text()) for i in indexes_]

        sc.axes.plot(x_axes, indexes_text)
        sc.axes.set_xlabel("Zeit")
        #column_names[tableWidget.currentColumn()]
        sc.axes.set_ylabel(column_names[self.tableWidget.currentColumn()+1])
        sc.draw()
        
        #sc.show()
        #mytable.cellWidget(i, j).currentText()


    def combo_box_selectionchange(self, q):
        my_dock_widget = QDockWidget (str(q.text()), self.mdi)
        my_dock_widget.setAllowedAreas(Qt.LeftDockWidgetArea | Qt.TopDockWidgetArea | Qt.BottomDockWidgetArea | Qt.RightDockWidgetArea)
        self.addDockWidget(Qt.LeftDockWidgetArea, my_dock_widget)
        my_dock_widget.move(100,100)
        my_dock_widget.setWindowTitle(q.text())
        #icon = QtGui.QIcon()
        #icon.addPixmap(QtGui.QPixmap("ukraine.png",QtGui.QIcon.Normal, QtGui.QIcon.On))
        #topleftwindow.windowIcon(icon)
        my_dock_widget.show()
 
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
        # Create QLineSeries
        self.series = QtCharts.QLineSeries()
        self.series.setName(name)

        # Filling QLineSeries
        for i in range(self.model.rowCount()):
            # Getting the data
            t = self.model.index(i, 0).data()
            date_fmt = "yyyy-MM-dd HH:mm:ss.zzz"

            x = QDateTime().fromString(t, date_fmt).toSecsSinceEpoch()
            y = float(self.model.index(i, 1).data())

            if x > 0 and y > 0:
                self.series.append(x, y)

        self.chart.addSeries(self.series)

        # Setting X-axis
        self.axis_x = QtCharts.QDateTimeAxis()
        self.axis_x.setTickCount(10)
        self.axis_x.setFormat("dd.MM (h:mm)")
        self.axis_x.setTitleText("Date")
        self.chart.addAxis(self.axis_x, Qt.AlignBottom)
        self.series.attachAxis(self.axis_x)
        # Setting Y-axis
        self.axis_y = QtCharts.QValueAxis()
        self.axis_y.setTickCount(10)
        self.axis_y.setLabelFormat("%.2f")
        self.axis_y.setTitleText("Magnitude")
        self.chart.addAxis(self.axis_y, Qt.AlignLeft)
        self.series.attachAxis(self.axis_y)

        # Getting the color from the QChart to use it on the QTableView
        self.model.color = "{}".format(self.series.pen().color().name())
      

if __name__ == "__main__":
    app = QtWidgets.QApplication()
    tr = Myfrontend()
    tr.show()
    app.exec_()
