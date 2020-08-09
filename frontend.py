# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'frontend.ui'
##
## Created by: Qt User Interface Compiler version 5.15.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QDate, QDateTime, QMetaObject,
    QObject, QPoint, QRect, QSize, QTime, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter,
    QPixmap, QRadialGradient)
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1066, 747)
        self.actionOpen = QAction(MainWindow)
        self.actionOpen.setObjectName(u"actionOpen")
        self.actionCopy = QAction(MainWindow)
        self.actionCopy.setObjectName(u"actionCopy")
        self.actionSave = QAction(MainWindow)
        self.actionSave.setObjectName(u"actionSave")
        self.actionSave_as = QAction(MainWindow)
        self.actionSave_as.setObjectName(u"actionSave_as")
        self.actionPaste = QAction(MainWindow)
        self.actionPaste.setObjectName(u"actionPaste")
        self.actionCut = QAction(MainWindow)
        self.actionCut.setObjectName(u"actionCut")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_5 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(-1, -1, -1, 60)
        self.vl_modul = QVBoxLayout()
        self.vl_modul.setObjectName(u"vl_modul")
        self.gb_modul = QGroupBox(self.centralwidget)
        self.gb_modul.setObjectName(u"gb_modul")
        self.verticalLayout_3 = QVBoxLayout(self.gb_modul)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.cb_modul = QComboBox(self.gb_modul)
        self.cb_modul.addItem("")
        self.cb_modul.addItem("")
        self.cb_modul.addItem("")
        self.cb_modul.addItem("")
        self.cb_modul.setObjectName(u"cb_modul")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cb_modul.sizePolicy().hasHeightForWidth())
        self.cb_modul.setSizePolicy(sizePolicy)

        self.verticalLayout_3.addWidget(self.cb_modul)


        self.vl_modul.addWidget(self.gb_modul)


        self.horizontalLayout.addLayout(self.vl_modul)

        self.vl_versuchart = QVBoxLayout()
        self.vl_versuchart.setObjectName(u"vl_versuchart")
        self.gb_versuchart = QGroupBox(self.centralwidget)
        self.gb_versuchart.setObjectName(u"gb_versuchart")
        self.verticalLayout_14 = QVBoxLayout(self.gb_versuchart)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.cb_versuchart = QComboBox(self.gb_versuchart)
        self.cb_versuchart.addItem("")
        self.cb_versuchart.addItem("")
        self.cb_versuchart.setObjectName(u"cb_versuchart")
        sizePolicy.setHeightForWidth(self.cb_versuchart.sizePolicy().hasHeightForWidth())
        self.cb_versuchart.setSizePolicy(sizePolicy)

        self.verticalLayout_14.addWidget(self.cb_versuchart)


        self.vl_versuchart.addWidget(self.gb_versuchart)


        self.horizontalLayout.addLayout(self.vl_versuchart)

        self.vl_ablesungart = QVBoxLayout()
        self.vl_ablesungart.setObjectName(u"vl_ablesungart")
        self.bg_ablesungart = QGroupBox(self.centralwidget)
        self.bg_ablesungart.setObjectName(u"bg_ablesungart")
        self.verticalLayout_9 = QVBoxLayout(self.bg_ablesungart)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.cb_ablesungart = QComboBox(self.bg_ablesungart)
        self.cb_ablesungart.addItem("")
        self.cb_ablesungart.addItem("")
        self.cb_ablesungart.addItem("")
        self.cb_ablesungart.setObjectName(u"cb_ablesungart")
        sizePolicy.setHeightForWidth(self.cb_ablesungart.sizePolicy().hasHeightForWidth())
        self.cb_ablesungart.setSizePolicy(sizePolicy)

        self.verticalLayout_9.addWidget(self.cb_ablesungart)


        self.vl_ablesungart.addWidget(self.bg_ablesungart)


        self.horizontalLayout.addLayout(self.vl_ablesungart)

        self.vl_asci_lesen = QVBoxLayout()
        self.vl_asci_lesen.setObjectName(u"vl_asci_lesen")
        self.gb_asci_lesen = QGroupBox(self.centralwidget)
        self.gb_asci_lesen.setObjectName(u"gb_asci_lesen")
        self.verticalLayout_11 = QVBoxLayout(self.gb_asci_lesen)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.btn_asc_lesen = QPushButton(self.gb_asci_lesen)
        self.btn_asc_lesen.setObjectName(u"btn_asc_lesen")

        self.verticalLayout_11.addWidget(self.btn_asc_lesen)


        self.vl_asci_lesen.addWidget(self.gb_asci_lesen)


        self.horizontalLayout.addLayout(self.vl_asci_lesen)

        self.vl_Ablesevorgang = QVBoxLayout()
        self.vl_Ablesevorgang.setObjectName(u"vl_Ablesevorgang")
        self.gb_Ablesevorgang = QGroupBox(self.centralwidget)
        self.gb_Ablesevorgang.setObjectName(u"gb_Ablesevorgang")
        self.verticalLayout_13 = QVBoxLayout(self.gb_Ablesevorgang)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.label = QLabel(self.gb_Ablesevorgang)
        self.label.setObjectName(u"label")

        self.verticalLayout_13.addWidget(self.label)

        self.label_2 = QLabel(self.gb_Ablesevorgang)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout_13.addWidget(self.label_2)


        self.vl_Ablesevorgang.addWidget(self.gb_Ablesevorgang)


        self.horizontalLayout.addLayout(self.vl_Ablesevorgang)


        self.verticalLayout_5.addLayout(self.horizontalLayout)

        self.verticalSpacer = QSpacerItem(20, 50, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_5.addItem(self.verticalSpacer)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(-1, -1, 0, 0)
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(21, -1, 44, -1)
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")

        self.verticalLayout.addWidget(self.label_4)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(-1, -1, -1, 0)
        self.lineEdit_3 = QLineEdit(self.centralwidget)
        self.lineEdit_3.setObjectName(u"lineEdit_3")

        self.horizontalLayout_6.addWidget(self.lineEdit_3)

        self.label_10 = QLabel(self.centralwidget)
        self.label_10.setObjectName(u"label_10")

        self.horizontalLayout_6.addWidget(self.label_10)


        self.verticalLayout.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(-1, -1, -1, 0)
        self.lineEdit_2 = QLineEdit(self.centralwidget)
        self.lineEdit_2.setObjectName(u"lineEdit_2")

        self.horizontalLayout_5.addWidget(self.lineEdit_2)

        self.label_9 = QLabel(self.centralwidget)
        self.label_9.setObjectName(u"label_9")

        self.horizontalLayout_5.addWidget(self.label_9)


        self.verticalLayout.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(-1, -1, -1, 0)
        self.lineEdit = QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName(u"lineEdit")

        self.horizontalLayout_2.addWidget(self.lineEdit)

        self.label_20 = QLabel(self.centralwidget)
        self.label_20.setObjectName(u"label_20")
        font = QFont()
        font.setUnderline(False)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.label_20.setFont(font)
        self.label_20.setScaledContents(False)
        self.label_20.setAlignment(Qt.AlignCenter)
        self.label_20.setWordWrap(False)
        self.label_20.setMargin(0)
        self.label_20.setIndent(-4)

        self.horizontalLayout_2.addWidget(self.label_20)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.lineEdit_9 = QLineEdit(self.centralwidget)
        self.lineEdit_9.setObjectName(u"lineEdit_9")

        self.verticalLayout.addWidget(self.lineEdit_9)

        self.lineEdit_8 = QLineEdit(self.centralwidget)
        self.lineEdit_8.setObjectName(u"lineEdit_8")

        self.verticalLayout.addWidget(self.lineEdit_8)

        self.lineEdit_7 = QLineEdit(self.centralwidget)
        self.lineEdit_7.setObjectName(u"lineEdit_7")

        self.verticalLayout.addWidget(self.lineEdit_7)

        self.lineEdit_6 = QLineEdit(self.centralwidget)
        self.lineEdit_6.setObjectName(u"lineEdit_6")

        self.verticalLayout.addWidget(self.lineEdit_6)

        self.lineEdit_5 = QLineEdit(self.centralwidget)
        self.lineEdit_5.setObjectName(u"lineEdit_5")

        self.verticalLayout.addWidget(self.lineEdit_5)

        self.gb_modul_2 = QGroupBox(self.centralwidget)
        self.gb_modul_2.setObjectName(u"gb_modul_2")
        self.verticalLayout_7 = QVBoxLayout(self.gb_modul_2)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.cb_modul_2 = QComboBox(self.gb_modul_2)
        self.cb_modul_2.addItem("")
        self.cb_modul_2.addItem("")
        self.cb_modul_2.addItem("")
        self.cb_modul_2.addItem("")
        self.cb_modul_2.setObjectName(u"cb_modul_2")
        sizePolicy.setHeightForWidth(self.cb_modul_2.sizePolicy().hasHeightForWidth())
        self.cb_modul_2.setSizePolicy(sizePolicy)

        self.verticalLayout_7.addWidget(self.cb_modul_2)


        self.verticalLayout.addWidget(self.gb_modul_2)

        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")

        self.verticalLayout.addWidget(self.pushButton)


        self.horizontalLayout_3.addLayout(self.verticalLayout)

        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(21, -1, 44, -1)
        self.label_18 = QLabel(self.centralwidget)
        self.label_18.setObjectName(u"label_18")

        self.verticalLayout_8.addWidget(self.label_18)

        self.horizontalLayout_17 = QHBoxLayout()
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.horizontalLayout_17.setContentsMargins(-1, -1, -1, 0)
        self.lineEdit_34 = QLineEdit(self.centralwidget)
        self.lineEdit_34.setObjectName(u"lineEdit_34")

        self.horizontalLayout_17.addWidget(self.lineEdit_34)

        self.label_19 = QLabel(self.centralwidget)
        self.label_19.setObjectName(u"label_19")

        self.horizontalLayout_17.addWidget(self.label_19)


        self.verticalLayout_8.addLayout(self.horizontalLayout_17)

        self.horizontalLayout_18 = QHBoxLayout()
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.horizontalLayout_18.setContentsMargins(-1, -1, -1, 0)
        self.lineEdit_35 = QLineEdit(self.centralwidget)
        self.lineEdit_35.setObjectName(u"lineEdit_35")

        self.horizontalLayout_18.addWidget(self.lineEdit_35)

        self.label_23 = QLabel(self.centralwidget)
        self.label_23.setObjectName(u"label_23")

        self.horizontalLayout_18.addWidget(self.label_23)


        self.verticalLayout_8.addLayout(self.horizontalLayout_18)

        self.horizontalLayout_19 = QHBoxLayout()
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.horizontalLayout_19.setContentsMargins(-1, -1, -1, 0)
        self.lineEdit_36 = QLineEdit(self.centralwidget)
        self.lineEdit_36.setObjectName(u"lineEdit_36")

        self.horizontalLayout_19.addWidget(self.lineEdit_36)

        self.label_24 = QLabel(self.centralwidget)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setFont(font)
        self.label_24.setScaledContents(False)
        self.label_24.setAlignment(Qt.AlignCenter)
        self.label_24.setWordWrap(False)
        self.label_24.setMargin(0)
        self.label_24.setIndent(-4)

        self.horizontalLayout_19.addWidget(self.label_24)


        self.verticalLayout_8.addLayout(self.horizontalLayout_19)

        self.lineEdit_37 = QLineEdit(self.centralwidget)
        self.lineEdit_37.setObjectName(u"lineEdit_37")

        self.verticalLayout_8.addWidget(self.lineEdit_37)

        self.lineEdit_38 = QLineEdit(self.centralwidget)
        self.lineEdit_38.setObjectName(u"lineEdit_38")

        self.verticalLayout_8.addWidget(self.lineEdit_38)

        self.lineEdit_39 = QLineEdit(self.centralwidget)
        self.lineEdit_39.setObjectName(u"lineEdit_39")

        self.verticalLayout_8.addWidget(self.lineEdit_39)

        self.lineEdit_40 = QLineEdit(self.centralwidget)
        self.lineEdit_40.setObjectName(u"lineEdit_40")

        self.verticalLayout_8.addWidget(self.lineEdit_40)

        self.lineEdit_41 = QLineEdit(self.centralwidget)
        self.lineEdit_41.setObjectName(u"lineEdit_41")

        self.verticalLayout_8.addWidget(self.lineEdit_41)

        self.gb_modul_3 = QGroupBox(self.centralwidget)
        self.gb_modul_3.setObjectName(u"gb_modul_3")
        self.verticalLayout_10 = QVBoxLayout(self.gb_modul_3)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.cb_modul_3 = QComboBox(self.gb_modul_3)
        self.cb_modul_3.addItem("")
        self.cb_modul_3.addItem("")
        self.cb_modul_3.addItem("")
        self.cb_modul_3.addItem("")
        self.cb_modul_3.setObjectName(u"cb_modul_3")
        sizePolicy.setHeightForWidth(self.cb_modul_3.sizePolicy().hasHeightForWidth())
        self.cb_modul_3.setSizePolicy(sizePolicy)

        self.verticalLayout_10.addWidget(self.cb_modul_3)


        self.verticalLayout_8.addWidget(self.gb_modul_3)

        self.pushButton_2 = QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.verticalLayout_8.addWidget(self.pushButton_2)


        self.horizontalLayout_3.addLayout(self.verticalLayout_8)

        self.verticalLayout_22 = QVBoxLayout()
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.verticalLayout_22.setContentsMargins(21, -1, 44, -1)
        self.label_41 = QLabel(self.centralwidget)
        self.label_41.setObjectName(u"label_41")

        self.verticalLayout_22.addWidget(self.label_41)

        self.horizontalLayout_34 = QHBoxLayout()
        self.horizontalLayout_34.setObjectName(u"horizontalLayout_34")
        self.horizontalLayout_34.setContentsMargins(-1, -1, -1, 0)
        self.lineEdit_74 = QLineEdit(self.centralwidget)
        self.lineEdit_74.setObjectName(u"lineEdit_74")

        self.horizontalLayout_34.addWidget(self.lineEdit_74)

        self.label_42 = QLabel(self.centralwidget)
        self.label_42.setObjectName(u"label_42")

        self.horizontalLayout_34.addWidget(self.label_42)


        self.verticalLayout_22.addLayout(self.horizontalLayout_34)

        self.horizontalLayout_35 = QHBoxLayout()
        self.horizontalLayout_35.setObjectName(u"horizontalLayout_35")
        self.horizontalLayout_35.setContentsMargins(-1, -1, -1, 0)
        self.lineEdit_75 = QLineEdit(self.centralwidget)
        self.lineEdit_75.setObjectName(u"lineEdit_75")

        self.horizontalLayout_35.addWidget(self.lineEdit_75)

        self.label_43 = QLabel(self.centralwidget)
        self.label_43.setObjectName(u"label_43")

        self.horizontalLayout_35.addWidget(self.label_43)


        self.verticalLayout_22.addLayout(self.horizontalLayout_35)

        self.horizontalLayout_36 = QHBoxLayout()
        self.horizontalLayout_36.setObjectName(u"horizontalLayout_36")
        self.horizontalLayout_36.setContentsMargins(-1, -1, -1, 0)
        self.lineEdit_76 = QLineEdit(self.centralwidget)
        self.lineEdit_76.setObjectName(u"lineEdit_76")

        self.horizontalLayout_36.addWidget(self.lineEdit_76)

        self.label_44 = QLabel(self.centralwidget)
        self.label_44.setObjectName(u"label_44")
        self.label_44.setFont(font)
        self.label_44.setScaledContents(False)
        self.label_44.setAlignment(Qt.AlignCenter)
        self.label_44.setWordWrap(False)
        self.label_44.setMargin(0)
        self.label_44.setIndent(-4)

        self.horizontalLayout_36.addWidget(self.label_44)


        self.verticalLayout_22.addLayout(self.horizontalLayout_36)

        self.lineEdit_77 = QLineEdit(self.centralwidget)
        self.lineEdit_77.setObjectName(u"lineEdit_77")

        self.verticalLayout_22.addWidget(self.lineEdit_77)

        self.lineEdit_78 = QLineEdit(self.centralwidget)
        self.lineEdit_78.setObjectName(u"lineEdit_78")

        self.verticalLayout_22.addWidget(self.lineEdit_78)

        self.lineEdit_79 = QLineEdit(self.centralwidget)
        self.lineEdit_79.setObjectName(u"lineEdit_79")

        self.verticalLayout_22.addWidget(self.lineEdit_79)

        self.lineEdit_80 = QLineEdit(self.centralwidget)
        self.lineEdit_80.setObjectName(u"lineEdit_80")

        self.verticalLayout_22.addWidget(self.lineEdit_80)

        self.lineEdit_81 = QLineEdit(self.centralwidget)
        self.lineEdit_81.setObjectName(u"lineEdit_81")

        self.verticalLayout_22.addWidget(self.lineEdit_81)

        self.gb_modul_8 = QGroupBox(self.centralwidget)
        self.gb_modul_8.setObjectName(u"gb_modul_8")
        self.verticalLayout_23 = QVBoxLayout(self.gb_modul_8)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.cb_modul_8 = QComboBox(self.gb_modul_8)
        self.cb_modul_8.addItem("")
        self.cb_modul_8.addItem("")
        self.cb_modul_8.addItem("")
        self.cb_modul_8.addItem("")
        self.cb_modul_8.setObjectName(u"cb_modul_8")
        sizePolicy.setHeightForWidth(self.cb_modul_8.sizePolicy().hasHeightForWidth())
        self.cb_modul_8.setSizePolicy(sizePolicy)

        self.verticalLayout_23.addWidget(self.cb_modul_8)


        self.verticalLayout_22.addWidget(self.gb_modul_8)

        self.pushButton_7 = QPushButton(self.centralwidget)
        self.pushButton_7.setObjectName(u"pushButton_7")

        self.verticalLayout_22.addWidget(self.pushButton_7)


        self.horizontalLayout_3.addLayout(self.verticalLayout_22)


        self.verticalLayout_5.addLayout(self.horizontalLayout_3)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.cb_modul.setCurrentIndex(-1)
        self.cb_versuchart.setCurrentIndex(-1)
        self.cb_ablesungart.setCurrentIndex(-1)
        self.cb_modul_2.setCurrentIndex(-1)
        self.cb_modul_3.setCurrentIndex(-1)
        self.cb_modul_8.setCurrentIndex(-1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionOpen.setText(QCoreApplication.translate("MainWindow", u"Open...", None))
        self.actionCopy.setText(QCoreApplication.translate("MainWindow", u"Copy", None))
        self.actionSave.setText(QCoreApplication.translate("MainWindow", u"Save", None))
        self.actionSave_as.setText(QCoreApplication.translate("MainWindow", u"Save as...", None))
        self.actionPaste.setText(QCoreApplication.translate("MainWindow", u"Paste", None))
        self.actionCut.setText(QCoreApplication.translate("MainWindow", u"Cut", None))
        self.gb_modul.setTitle(QCoreApplication.translate("MainWindow", u"Modul", None))
        self.cb_modul.setItemText(0, QCoreApplication.translate("MainWindow", u"Modul 1", None))
        self.cb_modul.setItemText(1, QCoreApplication.translate("MainWindow", u"Modul 2", None))
        self.cb_modul.setItemText(2, QCoreApplication.translate("MainWindow", u"Modul 3", None))
        self.cb_modul.setItemText(3, QCoreApplication.translate("MainWindow", u"Modul 4", None))

        self.cb_modul.setCurrentText(QCoreApplication.translate("MainWindow", u"W\u00e4hle", None))
        self.cb_modul.setPlaceholderText(QCoreApplication.translate("MainWindow", u"W\u00e4hle", None))
        self.gb_versuchart.setTitle(QCoreApplication.translate("MainWindow", u"Versuchsart", None))
        self.cb_versuchart.setItemText(0, QCoreApplication.translate("MainWindow", u"CU 17", None))
        self.cb_versuchart.setItemText(1, QCoreApplication.translate("MainWindow", u"UU 19", None))

        self.cb_versuchart.setCurrentText(QCoreApplication.translate("MainWindow", u"W\u00e4hle", None))
        self.cb_versuchart.setPlaceholderText(QCoreApplication.translate("MainWindow", u"W\u00e4hle", None))
        self.bg_ablesungart.setTitle(QCoreApplication.translate("MainWindow", u"Ablesungsart", None))
        self.cb_ablesungart.setItemText(0, QCoreApplication.translate("MainWindow", u"Manuelle Auswahl von Datenspalten", None))
        self.cb_ablesungart.setItemText(1, QCoreApplication.translate("MainWindow", u"Spaltennummern", None))
        self.cb_ablesungart.setItemText(2, QCoreApplication.translate("MainWindow", u"Namenerkennung", None))

        self.cb_ablesungart.setCurrentText(QCoreApplication.translate("MainWindow", u"W\u00e4hle", None))
        self.cb_ablesungart.setPlaceholderText(QCoreApplication.translate("MainWindow", u"W\u00e4hle", None))
        self.gb_asci_lesen.setTitle(QCoreApplication.translate("MainWindow", u"ASCI Datei", None))
        self.btn_asc_lesen.setText(QCoreApplication.translate("MainWindow", u"Lesen", None))
        self.gb_Ablesevorgang.setTitle(QCoreApplication.translate("MainWindow", u"Infos zum Ablesevorgang", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Datenspalten ausgelesen: X", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Datenzeilen ausgelesen: Y", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Angaben zum Versuch #1", None))
        self.lineEdit_3.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Probenh\u00f6he", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"mm", None))
        self.lineEdit_2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Probendurchmesser", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"mm", None))
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Dichte", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>\n"
"<span style=\" vertical-align:normal;\">kg/m</span>\n"
"<span style=\" vertical-align:super;\">3</span>\n"
"</p>\n"
"</body></html>", None))
        self.lineEdit_9.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Material", None))
        self.lineEdit_8.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Probenbezeichnung", None))
        self.lineEdit_7.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Testnummer", None))
        self.lineEdit_6.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Projectnummer", None))
        self.lineEdit_5.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Pr\u00fcfdatum", None))
        self.gb_modul_2.setTitle(QCoreApplication.translate("MainWindow", u"Vorlage aufrufen", None))
        self.cb_modul_2.setItemText(0, QCoreApplication.translate("MainWindow", u"Modul 1", None))
        self.cb_modul_2.setItemText(1, QCoreApplication.translate("MainWindow", u"Modul 2", None))
        self.cb_modul_2.setItemText(2, QCoreApplication.translate("MainWindow", u"Modul 3", None))
        self.cb_modul_2.setItemText(3, QCoreApplication.translate("MainWindow", u"Modul 4", None))

        self.cb_modul_2.setCurrentText(QCoreApplication.translate("MainWindow", u"W\u00e4hle", None))
        self.cb_modul_2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"W\u00e4hle", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Als Vorlage speichern", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"Angaben zum Versuch #1", None))
        self.lineEdit_34.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Probenh\u00f6he", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"mm", None))
        self.lineEdit_35.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Probendurchmesser", None))
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"mm", None))
        self.lineEdit_36.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Dichte", None))
        self.label_24.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>\n"
"<span style=\" vertical-align:normal;\">kg/m</span>\n"
"<span style=\" vertical-align:super;\">3</span>\n"
"</p>\n"
"</body></html>", None))
        self.lineEdit_37.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Material", None))
        self.lineEdit_38.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Probenbezeichnung", None))
        self.lineEdit_39.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Testnummer", None))
        self.lineEdit_40.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Projectnummer", None))
        self.lineEdit_41.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Pr\u00fcfdatum", None))
        self.gb_modul_3.setTitle(QCoreApplication.translate("MainWindow", u"Vorlage aufrufen", None))
        self.cb_modul_3.setItemText(0, QCoreApplication.translate("MainWindow", u"Modul 1", None))
        self.cb_modul_3.setItemText(1, QCoreApplication.translate("MainWindow", u"Modul 2", None))
        self.cb_modul_3.setItemText(2, QCoreApplication.translate("MainWindow", u"Modul 3", None))
        self.cb_modul_3.setItemText(3, QCoreApplication.translate("MainWindow", u"Modul 4", None))

        self.cb_modul_3.setCurrentText(QCoreApplication.translate("MainWindow", u"W\u00e4hle", None))
        self.cb_modul_3.setPlaceholderText(QCoreApplication.translate("MainWindow", u"W\u00e4hle", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Als Vorlage speichern", None))
        self.label_41.setText(QCoreApplication.translate("MainWindow", u"Angaben zum Versuch #1", None))
        self.lineEdit_74.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Probenh\u00f6he", None))
        self.label_42.setText(QCoreApplication.translate("MainWindow", u"mm", None))
        self.lineEdit_75.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Probendurchmesser", None))
        self.label_43.setText(QCoreApplication.translate("MainWindow", u"mm", None))
        self.lineEdit_76.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Dichte", None))
        self.label_44.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>\n"
"<span style=\" vertical-align:normal;\">kg/m</span>\n"
"<span style=\" vertical-align:super;\">3</span>\n"
"</p>\n"
"</body></html>", None))
        self.lineEdit_77.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Material", None))
        self.lineEdit_78.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Probenbezeichnung", None))
        self.lineEdit_79.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Testnummer", None))
        self.lineEdit_80.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Projectnummer", None))
        self.lineEdit_81.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Pr\u00fcfdatum", None))
        self.gb_modul_8.setTitle(QCoreApplication.translate("MainWindow", u"Vorlage aufrufen", None))
        self.cb_modul_8.setItemText(0, QCoreApplication.translate("MainWindow", u"Modul 1", None))
        self.cb_modul_8.setItemText(1, QCoreApplication.translate("MainWindow", u"Modul 2", None))
        self.cb_modul_8.setItemText(2, QCoreApplication.translate("MainWindow", u"Modul 3", None))
        self.cb_modul_8.setItemText(3, QCoreApplication.translate("MainWindow", u"Modul 4", None))

        self.cb_modul_8.setCurrentText(QCoreApplication.translate("MainWindow", u"W\u00e4hle", None))
        self.cb_modul_8.setPlaceholderText(QCoreApplication.translate("MainWindow", u"W\u00e4hle", None))
        self.pushButton_7.setText(QCoreApplication.translate("MainWindow", u"Als Vorlage speichern", None))
    # retranslateUi

