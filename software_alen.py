# importing necessary packages

from PySide2 import QtWidgets, QtGui, QtCore, QtSql
from PySide2.QtGui import QStandardItemModel
from PySide2.QtCore import QDateTime, Qt, QRect, QSize
from PySide2.QtGui import QPainter
from PySide2.QtWidgets import (QWidget, QHeaderView, QHBoxLayout, QTableView,
                               QSizePolicy, QTableWidget, QLabel, QAction, QDockWidget,
                                QFrame, QAbstractItemView, QMdiArea, QMdiSubWindow,
                                QMessageBox, QFileDialog
                                )
from PySide2.QtCharts import QtCharts

import pandas as pd

import openpyxl
book = openpyxl.load_workbook("Triax CR stress.xlsx")
sheet = book.active
value = sheet.cell(2,2).value
print(value)



class Ui_Dialog(object):
    def setupUi(self, Dialog):
        '''
        This method will setup the GUI of the software. All the elements of the software GUI are
        made in this Method of UI_Dialog class.
        Elements Added are:
        1) Push Buttons
        2) Line Edits
        3) Labels

        :param Dialog:
        :return:
        '''
        Dialog.setObjectName("Dialog")
        Dialog.resize(996, 758)
        self.comboBox = QtWidgets.QComboBox(Dialog)
        self.comboBox.setGeometry(QtCore.QRect(60, 90, 141, 21))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox_2 = QtWidgets.QComboBox(Dialog)
        self.comboBox_2.setGeometry(QtCore.QRect(230, 90, 141, 21))
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(60, 40, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(230, 40, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")

        font_1 = QtGui.QFont()
        font_1.setPointSize(6)

        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(70, 200, 111, 31))
        self.label_3.setObjectName("label_3")
        self.label_3.setFont(font_1)

        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(190, 200, 111, 31))
        self.label_4.setObjectName("label_4")
        self.label_4.setFont(font_1)

        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(310, 200, 111, 31))
        self.label_5.setObjectName("label_5")
        self.label_5.setFont(font_1)

        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(550, 200, 131, 31))
        self.label_6.setObjectName("label_6")
        self.label_6.setFont(font_1)

        self.label_8 = QtWidgets.QLabel(Dialog)
        self.label_8.setGeometry(QtCore.QRect(430, 200, 111, 31))
        self.label_8.setObjectName("label_8")
        self.label_8.setFont(font_1)

        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(70, 240, 81, 22))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_2.setGeometry(QtCore.QRect(190, 240, 81, 22))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_3.setGeometry(QtCore.QRect(310, 240, 81, 22))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_4.setGeometry(QtCore.QRect(430, 240, 81, 22))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit_5 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_5.setGeometry(QtCore.QRect(550, 240, 81, 22))
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.lineEdit_6 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_6.setGeometry(QtCore.QRect(430, 280, 81, 22))
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.lineEdit_7 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_7.setGeometry(QtCore.QRect(190, 280, 81, 22))
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.lineEdit_8 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_8.setGeometry(QtCore.QRect(310, 280, 81, 22))
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.lineEdit_9 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_9.setGeometry(QtCore.QRect(550, 280, 81, 22))
        self.lineEdit_9.setObjectName("lineEdit_9")
        self.lineEdit_10 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_10.setGeometry(QtCore.QRect(70, 280, 81, 22))
        self.lineEdit_10.setObjectName("lineEdit_10")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(550, 320, 111, 41))
        self.pushButton.setObjectName("pushButton")

        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(400, 70, 111, 41))
        self.pushButton_2.setObjectName("pushButton")

        self.label_7 = QtWidgets.QLabel(Dialog)
        self.label_7.setGeometry(QtCore.QRect(70, 330, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.label_9 = QtWidgets.QLabel(Dialog)
        self.label_9.setGeometry(QtCore.QRect(70, 360, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.lineEdit_11 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_11.setGeometry(QtCore.QRect(160, 340, 91, 22))
        self.lineEdit_11.setObjectName("lineEdit_11")
        self.lineEdit_12 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_12.setGeometry(QtCore.QRect(160, 370, 91, 22))
        self.lineEdit_12.setObjectName("lineEdit_12")
        self.label_10 = QtWidgets.QLabel(Dialog)
        self.label_10.setGeometry(QtCore.QRect(710, 50, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(Dialog)
        self.label_11.setGeometry(QtCore.QRect(710, 80, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(Dialog)
        self.label_12.setGeometry(QtCore.QRect(710, 140, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(Dialog)
        self.label_13.setGeometry(QtCore.QRect(710, 110, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        self.label_14 = QtWidgets.QLabel(Dialog)
        self.label_14.setGeometry(QtCore.QRect(710, 200, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_14.setFont(font)
        self.label_14.setObjectName("label_14")
        self.label_15 = QtWidgets.QLabel(Dialog)
        self.label_15.setGeometry(QtCore.QRect(710, 170, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_15.setFont(font)
        self.label_15.setObjectName("label_15")
        self.label_16 = QtWidgets.QLabel(Dialog)
        self.label_16.setGeometry(QtCore.QRect(710, 260, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_16.setFont(font)
        self.label_16.setObjectName("label_16")
        self.label_17 = QtWidgets.QLabel(Dialog)
        self.label_17.setGeometry(QtCore.QRect(710, 230, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_17.setFont(font)
        self.label_17.setObjectName("label_17")
        self.lineEdit_13 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_13.setGeometry(QtCore.QRect(810, 50, 113, 22))
        self.lineEdit_13.setObjectName("lineEdit_13")
        self.lineEdit_14 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_14.setGeometry(QtCore.QRect(810, 80, 113, 22))
        self.lineEdit_14.setObjectName("lineEdit_14")
        self.lineEdit_15 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_15.setGeometry(QtCore.QRect(810, 140, 113, 22))
        self.lineEdit_15.setObjectName("lineEdit_15")
        self.lineEdit_16 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_16.setGeometry(QtCore.QRect(810, 110, 113, 22))
        self.lineEdit_16.setObjectName("lineEdit_16")
        self.lineEdit_17 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_17.setGeometry(QtCore.QRect(810, 200, 113, 22))
        self.lineEdit_17.setObjectName("lineEdit_17")
        self.lineEdit_18 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_18.setGeometry(QtCore.QRect(810, 170, 113, 22))
        self.lineEdit_18.setObjectName("lineEdit_18")
        self.lineEdit_19 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_19.setGeometry(QtCore.QRect(810, 260, 113, 22))
        self.lineEdit_19.setObjectName("lineEdit_19")
        self.lineEdit_20 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_20.setGeometry(QtCore.QRect(810, 230, 113, 22))
        self.lineEdit_20.setObjectName("lineEdit_20")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        # Connecting the buttons with the methods of the class
        self.pushButton_2.clicked.connect(self.openFileNameDialog)
        self.pushButton.clicked.connect(self.check_file)

        self.col_labels = [self.label_3, self.label_4, self.label_5,
                           self.label_8, self.label_6]

    def openFileNameDialog(self):
        '''
        This Method will allow the user to choose the file from the file dialog and loads everything from
        the text file and saves the file in a form of DataFrame for the future use after Cleaning the data
        from the file. This method also shows the total number of rows and columns from the file.


        :return:
        '''
        try:
            options = QFileDialog.Options()
            options |= QFileDialog.DontUseNativeDialog
            fileName, _ = QFileDialog.getOpenFileName(None, "Choose File", "",
                                                      "Text Files (*.txt)", options=options)
            if fileName:
                # Removing pre written data from fields
                self.label_3.setText("Column 1")
                self.label_4.setText("Column 2")
                self.label_5.setText("Column 3")
                self.label_6.setText("Column 5")
                self.label_8.setText("Column 4")

                self.lineEdit_10.clear()
                self.lineEdit_7.clear()
                self.lineEdit_8.clear()
                self.lineEdit_6.clear()
                self.lineEdit_9.clear()

                # fetching the name of the file
                self.file_path = fileName

                # self.file_name = fileName.split("/")[-1]

                file = open(self.file_path)
                self.cols = file.readline().split("\t")
                self.units = file.readline().split("\t")

                # saving all the rows
                self.rows = []
                for row in file.readlines():
                    row = row.split("\t")
                    self.rows.append(row)

                self.cols[0] = "first"
                self.cols[1] = "second"

                # creating the data frame
                df = pd.DataFrame(self.rows,columns=self.cols)
                for i in range(len(df.columns)):
                    try:
                        df.iloc[:,i] = df.iloc[:,i].map(self.change_val)
                    except:
                        print("Un Clean DATA!!!")

                self.df = df

                # showing the rows and columns
                r,c = self.df.shape
                self.lineEdit_11.setText(str(r))
                self.lineEdit_12.setText(str(c))

        except Exception as e:
            print(e)

    @staticmethod
    def change_val(val):
        '''
        This method will take the value from the text file and convert the value into the correct format by rounding
        after cleaning and removing the redundant decimal points

        :param val:
        :return: cleaned value
        '''

        val = val.replace("\n","")
        try:
            if val.count(".") >= 2:
                v = val.split(".")
                v1 = v[0]
                v2 = v[1]
                num = float("{}.{}".format(v1, v2))
                # print(num)
                num = round(num, 2)
                return num
            else:
                num = float(val)
                num = round(num, 2)
                return num
        except Exception as e:
            return val

    def check_file(self):
        '''
        This method will read all the column numbers from the fields and put the right column names
        on the labels so that user can see the column names. After the column names this method will fetch the
        top values from each column and show those values in the GUI.

        :return:
        '''
        try:
            self.col_fields = [self.lineEdit,self.lineEdit_2,self.lineEdit_3,
                           self.lineEdit_4,self.lineEdit_5]

            self.val_fields = [self.lineEdit_10,self.lineEdit_7,self.lineEdit_8,
                               self.lineEdit_6,self.lineEdit_9]

            for idx,i in enumerate(self.col_fields):
                if i.text().strip() != "":

                    col_number = int(i.text().strip())
                    try:
                        col_name = self.cols[col_number+1]
                        self.col_labels[idx].setText(col_name)
                        col_val = self.df.iloc[:,col_number+1].values[0]
                        self.val_fields[idx].setText(str(col_val))

                    except Exception as e:
                        print("Check the Column Number again")
                        print(e)


        except Exception as e:
            print(e)

    def retranslateUi(self, Dialog):
        '''
        This method will put all the default values in the GUI elements.

        :param Dialog:
        :return:
        '''
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.comboBox.setItemText(0, _translate("Dialog", "Empty"))
        self.comboBox.setItemText(1, _translate("Dialog", "Triax"))
        self.comboBox.setItemText(2, _translate("Dialog", "Permeability"))
        self.comboBox.setItemText(3, _translate("Dialog", "Ultrasonic\n"
""))
        self.comboBox_2.setItemText(0, _translate("Dialog", "Empty"))
        self.comboBox_2.setItemText(1, _translate("Dialog", "UU 17-8"))
        self.comboBox_2.setItemText(2, _translate("Dialog", "CD 17-9\n"
""))
        self.label.setText(_translate("Dialog", "Module choice"))
        self.label_2.setText(_translate("Dialog", "Standard choice"))
        self.label_3.setText(_translate("Dialog", "Column 1"))
        self.label_4.setText(_translate("Dialog", "Column 2"))
        self.label_5.setText(_translate("Dialog", "Column 3"))
        self.label_6.setText(_translate("Dialog", "Column 5"))
        self.label_8.setText(_translate("Dialog", "Column 4"))
        self.pushButton.setText(_translate("Dialog", "Check File"))
        self.pushButton_2.setText(_translate("Dialog", "Choose File"))
        self.label_7.setText(_translate("Dialog", "Rows:"))
        self.label_9.setText(_translate("Dialog", "Column:"))
        self.label_10.setText(_translate("Dialog", "Box 1"))
        self.label_11.setText(_translate("Dialog", "Box 2"))
        self.label_12.setText(_translate("Dialog", "Box 4"))
        self.label_13.setText(_translate("Dialog", "Box 3"))
        self.label_14.setText(_translate("Dialog", "Box 6"))
        self.label_15.setText(_translate("Dialog", "Box 5"))
        self.label_16.setText(_translate("Dialog", "Box 8"))
        self.label_17.setText(_translate("Dialog", "Box 7"))


if __name__ == "__main__":
    # create the object of the Dialog and show the GUI window
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
