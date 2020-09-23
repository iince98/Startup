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
        #filename = "/Users/macpro/Downloads/DS-Demo-Log.txt"
        

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
        self.sub_combo_report = QtWidgets.QComboBox()
        report_list =[" ","Report 33", "Report 35", "Report 37", "Report 39"]
        for i in report_list:
            self.sub_combo_report.addItem(i)

        self.sub_combo_calculation = QtWidgets.QComboBox()
        global calculation_list
        calculation_list =["","Spannung_1\nkN/mm2","Spannung_2\nkN/mm2",	"Spannung_3\nkN/mm2",	"V0\nmm3",	"Volumen\nl/m3"]
        for i in calculation_list:
            self.sub_combo_calculation.addItem(i)
        
        sub_layout = QtWidgets.QVBoxLayout()
        sub_layout.addWidget(self.gb_Ablesevorgang)
        sub_layout.addWidget(self.sub_combo_report)
        sub_layout.addWidget(self.sub_combo_calculation)
        sub_layout.addWidget(self.tableWidget)
        sub_widget= QtWidgets.QWidget()
        sub_widget.setLayout(sub_layout)

        sub.setWindowTitle("Reports")
        sub.setWidget(sub_widget)
        self.mdi.addSubWindow(sub)
        
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


        self.btn_asc_lesen_2.clicked.connect(self.read_data)
        #self.sub_combo_report.currentIndexChanged.connect(self.fill_table)
        self.sub_combo_calculation.currentIndexChanged.connect(self.fill_table)
        self.cb_modul.currentIndexChanged.connect(self.cbmodul_selectionchange)
        #self.cb_modul.currentIndexChanged.connect(self.createDB)
        #self.createDB()
        #self.multiple_check.stateChanged.connect(multiple_check_state)
        #legend_check.stateChanged.connect(self.legend_check_state)
    
    #def multiple_check_state (self, state):
    def legend_check_state(self, state):
        global legend_state
        legend_state = state


    def read_data (self):
        global filename

        #filename = QtWidgets.QFileDialog.getOpenFileName(self, "Open File",  "/Users/macpro/Downloads/")[0]
        filename = "/Users/macpro/Downloads/Log_demo2.txt"

        self.tabWidget.setCurrentWidget(self.tab_2)

    

    def fill_table(self):
        dataset=pd.read_csv(filename, delimiter="\t")
        report_type = self.sub_combo_report.currentText()
        calculation_type = self.sub_combo_calculation.currentText()
        #print(type(calculation_type), calculation_type)
        columns_list =[["33",["Zeit\ns",	"Vertikale Kraft\nkN",	"Vertikale Position\nmm",	"delta h\nmm",	"sig3\nkN/m2", 	"u\nkN/m2",	"u gesteuert\nkN/m2",	"Vertikale Spannung iso\nkN/m2",	"Dev iso\nkN/m2",	"Vertikale Stauchung (Position)\n%",	"Vertikale Spannung aniso\nkN/m2",	"Dev aniso\nkN/m2",	"P0\nN",	"delta V\nml", "P-Volumenänderung\nml",	"Z-Volumenänderung gemessen\nml",	"Probenhöhe\nmm",	"P-Volumen\nml",	"Probenfläche iso\nmm2",	"Durchmesser iso\nmm",	"Anfängeliche Fläche aniso\nmm2",	"Anfängliche Höhe aniso\nmm",	"Verformung aniso\nmm",	"Probenfläche aniso\nmm2",	"Spannung_1\nkN/mm2","Spannung_2\nkN/mm2",	"Spannung_3\nkN/mm2",	"V0\nmm3",	"Volumen\nl/m3"]],
                        ["35",["Zeit\ns",	"Vertikale Kraft\nkN",	"Vertikale Position\nmm",	"u gesteuert\nkN/m2",	"P0\nN",	"Vertikale Spannung iso\nkN/m2",	"Dev iso\nkN/m2",	"Vertikale Stauchung (Position)\n%",	"delta h\nmm",	"Vertikale Spannung aniso\nkN/m2",	"Dev aniso\nkN/m2",	"P-Volumenänderung\nml",	"u\nkN/m2",	"delta V\nml",	"Z-Volumenänderung gemessen\nml",	"sig3\nkN/m2",	"Probenhöhe\nmm",	"Probenfläche aniso\nmm2",	"Probenhöhe aniso\nmm",	"Anfängeliche Fläche aniso\nmm2",	"Anfängliche Höhe aniso\nmm",	"Probendurchmesser aniso\nmm",	"P-Volumen\nml",	"Probenfläche iso\nmm2",	"Durchmesser iso\nmm",	"Verformung aniso\nmm","Spannung_1\nkN/mm2","Spannung_2\nkN/mm2",	"Spannung_3\nkN/mm2",	"V0\nmm3",	"Volumen\nl/m3"]],
                        ["37",["Zeit\ns",	"Vertikale Kraft\nkN",	"Vertikale Position\nmm",	"delta h\nmm",	"sig3\nkN/m2",	"u\nkN/m2",	"u gesteuert\nkN/m2",	"Vertikale Spannung iso\nkN/m2",	"Dev iso\nkN/m2",	"Vertikale Stauchung (Position)\n%",	"Vertikale Spannung aniso\nkN/m2",	"Dev aniso\nkN/m2",	"P0\nN",	"delta V\nml",	"P-Volumenänderung\nml",	"Z-Volumenänderung gemessen\nml",	"Probenhöhe\nmm",	"P-Volumen\nml",	"Probenfläche iso\nmm2",	"Durchmesser iso\nmm",	"Anfängeliche Fläche aniso\nmm2",	"Anfängliche Höhe aniso\nmm",	"Verformung aniso\nmm",	"Probenfläche aniso\nmm2", "Spannung_1\nkN/mm2","Spannung_2\nkN/mm2",	"Spannung_3\nkN/mm2",	"V0\nmm3",	"Volumen\nl/m3"]],
                        ["39",["Zeit\ns",	"Vertikale Kraft\nkN",	"Vertikale Position\nmm",	"delta h\nmm",	"sig3\nkN/m2",	"u\nkN/m2",	"u gesteuert\nkN/m2",	"Vertikale Spannung iso\nkN/m2",	"Dev iso\nkN/m2",	"Vertikale Stauchung (Position)\n%",	"Vertikale Spannung aniso\nkN/m2",	"Dev aniso\nkN/m2",	"P0\nN",	"delta V\nml",	"P-Volumenänderung\nml",	"Z-Volumenänderung gemessen\nml",	"Probenhöhe\nmm",	"P-Volumen\nml",	"Probenfläche iso\nmm2",	"Durchmesser iso\nmm",	"Anfängeliche Fläche aniso\nmm2",	"Anfängliche Höhe aniso\nmm",	"Verformung aniso\nmm",	"Probenfläche aniso\nmm2",	"Spannung_1\nkN/mm2","Spannung_2\nkN/mm2",	"Spannung_3\nkN/mm2",	"V0\nmm3",	"Volumen\nl/m3"]]]
        new = dataset["    file"].str.split(" ", n = 1, expand = True) 

        dataset["number"] = new[0]
        dataset["value"] = new[1]
        
        # all_report_types = list(new[0])
        # report_list =[]
        # ### Remove blanks
        # while "" in all_report_types:
        #     all_report_types.remove("")
        # #### Remove non suitable report types(ending with "-")
        # for i in all_report_types:
        #     if i[0] =="0" and i[-1]!="-":
        #         report_list.append(i)
        ### Remove duplicates
        #global report_list_ready
        #report_list_ready =list(dict.fromkeys(report_list)) 
        group = dataset.groupby("number")
        
        # col_name_pd = pd.read_excel("column_names_ONLY.xlsx", index_col="number")
        # for col in col_name_pd.columns:
        #     col_name_pd[col]= col_name_pd[col].replace("\n", "") 
        #     col_name_pd[col]= col_name_pd[col].replace(np.nan, "")
        global column_names
        # column_names_all = col_name_pd.loc[int(report_type.split(" ")[1])]
        group_to_be_selected = "0"+report_type.split(" ")[1]
        for i in range (len(columns_list)):
            if columns_list[i][0] == report_type.split(" ")[1]:
                column_names = columns_list[i][1]
        #print(column_names) 
        #print(group_to_be_selected)
        try:
            group_selected=group.get_group(group_to_be_selected)
        except:
            QMessageBox.about(self, "Warning", "There is no {} in the file selected".format(report_type))
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
        
       
     
       

         #### 5 CALCULATIONS
        #print(group_selected.iloc[:,2], group_selected.iloc[:,17])
        if report_type.split(" ")[1] =="35":
            group_selected["Spannung_1"] = group_selected.iloc[:,2] * 1000000 / group_selected.iloc[:,17] #0,025
            group_selected["Spannung_2"] = (group_selected["Spannung_1"] - group_selected.iloc[:,17]*1000000) / 2
            group_selected["Spannung_3"] = (group_selected["Spannung_1"] + group_selected.iloc[:,17]*1000000) / 2
            group_selected["V0"] = group_selected.iloc[:,16] * (group_selected.iloc[:,21] /2) * (group_selected.iloc[:,21] /2) * float(3.14)
            group_selected["Volumen"] = group_selected.iloc[:,13] / (group_selected["V0"]/1000000)

        if report_type.split(" ")[1] =="33" or report_type.split(" ")[1] =="37" or report_type.split(" ")[1] =="39":
            group_selected["Spannung_1"] = group_selected.iloc[:,2] * 1000000 / group_selected.iloc[:,23] #0,025
            group_selected["Spannung_2"] = (group_selected["Spannung_1"] - group_selected.iloc[:,23]*1000000) / 2
            group_selected["Spannung_3"] = (group_selected["Spannung_1"] + group_selected.iloc[:,23]*1000000) / 2
            group_selected["V0"] = group_selected.iloc[:,16] * (group_selected.iloc[:,19] /2) * (group_selected.iloc[:,19] /2) * float(3.14)
            group_selected["Volumen"] = group_selected.iloc[:,13] / (group_selected["V0"]/1000000)


        group_selected.columns = column_names 
        for i in calculation_list[1:]:
            if i != calculation_type:
                
                #print(len(i), i, len(calculation_type), calculation_type)
                column_names.remove(i)
                #gapminder_ocean.drop(['pop'], axis=1)
                #group_selected.drop([i], axis=1)        
                group_selected.drop([i], inplace =True, axis=1)
        
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
        


        for i in range (self.r_number):
            self.tableWidget.insertRow(i)
            for j in range(self.col_number):
                
                self.tableWidget.setItem(i, j, QtWidgets.QTableWidgetItem(str(group_selected.iloc[i,j])))
        #self.tableWidget.scrollToItem(self.tableWidget.itemAt(100,25))
        #self.tableWidget.scrollToTop()



    def draw_graph(self):
        #sc.axes.clear() 

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
        #self.axes.cla()
        sc.axes.plot(x_axes, indexes_text, label=column_names[self.tableWidget.currentColumn()])
        sc.axes.set_xlabel("Zeit")
        #column_names[tableWidget.currentColumn()]
        sc.axes.set_ylabel(column_names[self.tableWidget.currentColumn()])
        sc.axes.legend(loc='upper right', frameon=True)
    

        
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
