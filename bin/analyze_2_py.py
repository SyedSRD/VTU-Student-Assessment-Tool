# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'analyze_2.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1342, 756)
        Form.setStyleSheet(".QWidget{  \n"
"     background-image:url(\'lb.jpg\');\n"
"     \n"
"     background-position:center;\n"
"     background-fill:yes;\n"
"     background-color: rgb(36, 36, 36);\n"
"     border-style: inset;\n"
"     border-width: 1px;\n"
"     border-radius: 5px;\n"
"     border-color: yellow;\n"
"     font: bold 14px;\n"
"     color:yellow;\n"
"     min-width: 1em;\n"
"    \n"
"}")
        self.gridLayout_5 = QtWidgets.QGridLayout(Form)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.frame = QtWidgets.QFrame(Form)
        self.frame.setStyleSheet(".QFrame{  \n"
"     background-image:url(\'lb.jpg\');\n"
"     \n"
"     background-position:center;\n"
"     background-fill:yes;\n"
"     background-color: rgb(36, 36, 36);\n"
"     border-style: inset;\n"
"     border-width: 1px;\n"
"     border-radius: 5px;\n"
"     border-color: yellow;\n"
"     font: bold 14px;\n"
"     color:yellow;\n"
"     min-width: 1em;\n"
"    \n"
"}")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout = QtWidgets.QGridLayout(self.frame)
        self.gridLayout.setObjectName("gridLayout")
        self.cbSubA = QtWidgets.QComboBox(self.frame)
        self.cbSubA.setStyleSheet("background-color: rgb(36,36,36);\n"
"color:rgb(255,255,255);\n"
"    border-style: inset;\n"
"    border-width: 1px;\n"
"    border-radius: 5px;\n"
"    border-color: yellow;\n"
"    font: 14px;\n"
"    min-width: 5em;\n"
"    padding: 4px;\n"
"\n"
"")
        self.cbSubA.setObjectName("cbSubA")
        self.gridLayout.addWidget(self.cbSubA, 3, 5, 1, 1)
        self.label_sub = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_sub.setFont(font)
        self.label_sub.setAlignment(QtCore.Qt.AlignCenter)
        self.label_sub.setObjectName("label_sub")
        self.gridLayout.addWidget(self.label_sub, 3, 4, 1, 1)
        self.spSemA = QtWidgets.QSpinBox(self.frame)
        self.spSemA.setStyleSheet("background-color: rgb(36,36,36);\n"
"color:rgb(255,255,255);\n"
"    border-style: inset;\n"
"    border-width: 1px;\n"
"    border-radius: 5px;\n"
"    border-color: yellow;\n"
"    font: 14px;\n"
"    min-width: 5em;\n"
"    padding: 4px;\n"
"\n"
"")
        self.spSemA.setMinimum(1)
        self.spSemA.setMaximum(8)
        self.spSemA.setObjectName("spSemA")
        self.gridLayout.addWidget(self.spSemA, 2, 3, 2, 1)
        self.rbCRA = QtWidgets.QRadioButton(self.frame)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.rbCRA.setFont(font)
        self.rbCRA.setObjectName("rbCRA")
        self.gridLayout.addWidget(self.rbCRA, 0, 3, 1, 1)
        self.line = QtWidgets.QFrame(self.frame)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout.addWidget(self.line, 1, 0, 1, 6)
        self.rbSubA = QtWidgets.QRadioButton(self.frame)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.rbSubA.setFont(font)
        self.rbSubA.setChecked(True)
        self.rbSubA.setObjectName("rbSubA")
        self.gridLayout.addWidget(self.rbSubA, 0, 1, 1, 1)
        self.label_sem = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_sem.setFont(font)
        self.label_sem.setAlignment(QtCore.Qt.AlignCenter)
        self.label_sem.setObjectName("label_sem")
        self.gridLayout.addWidget(self.label_sem, 2, 2, 2, 1)
        self.label_year = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_year.setFont(font)
        self.label_year.setAlignment(QtCore.Qt.AlignCenter)
        self.label_year.setObjectName("label_year")
        self.gridLayout.addWidget(self.label_year, 2, 0, 2, 1)
        self.spYrA = QtWidgets.QSpinBox(self.frame)
        self.spYrA.setStyleSheet("background-color: rgb(36,36,36);\n"
"color:rgb(255,255,255);\n"
"    border-style: inset;\n"
"    border-width: 1px;\n"
"    border-radius: 5px;\n"
"    border-color: yellow;\n"
"    font: 14px;\n"
"    min-width: 5em;\n"
"    padding: 4px;\n"
"\n"
"")
        self.spYrA.setMinimum(2017)
        self.spYrA.setMaximum(2050)
        self.spYrA.setObjectName("spYrA")
        self.gridLayout.addWidget(self.spYrA, 2, 1, 2, 1)
        self.tabAnalyz = QtWidgets.QTabWidget(self.frame)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.tabAnalyz.setFont(font)
        self.tabAnalyz.setStyleSheet("QTabWidget::pane { /* The tab widget frame */\n"
"    border-top: 2px solid #C2C7CB;\n"
"    position: absolute;\n"
"    top: -0.5em;\n"
"}\n"
"\n"
"QTabWidget::tab-bar {\n"
"    alignment: center;\n"
"}\n"
"\n"
"/* Style the tab using the tab sub-control. Note that\n"
"    it reads QTabBar _not_ QTabWidget */\n"
"QTabBar::tab {\n"
"    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                stop: 0 #E1E1E1, stop: 0.4 #DDDDDD,\n"
"                                stop: 0.5 #D8D8D8, stop: 1.0 #D3D3D3);\n"
"    border: 2px solid #C4C4C3;\n"
"    border-bottom-color: #C2C7CB; /* same as the pane color */\n"
"    border-top-left-radius: 8px;\n"
"    border-top-right-radius: 8px;\n"
"    min-width: 20ex;\n"
"    padding: 2px;\n"
"}\n"
"\n"
"QTabBar::tab:selected, QTabBar::tab:hover {\n"
"    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                stop: 0 #fafafa, stop: 0.4 #f4f4f4,\n"
"                                stop: 0.5 #e7e7e7, stop: 1.0 #fafafa);\n"
"}\n"
"\n"
"QTabBar::tab:selected {\n"
"    border-color: #9B9B9B;\n"
"    border-bottom-color: #C2C7CB; /* same as pane color */\n"
"}")
        self.tabAnalyz.setObjectName("tabAnalyz")
        self.tab3Desc = QtWidgets.QWidget()
        self.tab3Desc.setObjectName("tab3Desc")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.tab3Desc)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        spacerItem = QtWidgets.QSpacerItem(15, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem, 2, 0, 1, 1)
        self.lbTlStuCnt = QtWidgets.QLabel(self.tab3Desc)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.lbTlStuCnt.setFont(font)
        self.lbTlStuCnt.setObjectName("lbTlStuCnt")
        self.gridLayout_2.addWidget(self.lbTlStuCnt, 0, 4, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.tab3Desc)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.gridLayout_2.addWidget(self.label_8, 2, 1, 1, 2)
        self.label_6 = QtWidgets.QLabel(self.tab3Desc)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.gridLayout_2.addWidget(self.label_6, 1, 1, 1, 2)
        self.label_5 = QtWidgets.QLabel(self.tab3Desc)
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.gridLayout_2.addWidget(self.label_5, 1, 3, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.tab3Desc)
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 0, 3, 1, 1)
        self.lbTlPass = QtWidgets.QLabel(self.tab3Desc)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.lbTlPass.setFont(font)
        self.lbTlPass.setObjectName("lbTlPass")
        self.gridLayout_2.addWidget(self.lbTlPass, 1, 4, 1, 1)
        self.label = QtWidgets.QLabel(self.tab3Desc)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 0, 1, 1, 2)
        self.label_11 = QtWidgets.QLabel(self.tab3Desc)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.gridLayout_2.addWidget(self.label_11, 3, 1, 1, 2)
        self.label_17 = QtWidgets.QLabel(self.tab3Desc)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_17.setFont(font)
        self.label_17.setObjectName("label_17")
        self.gridLayout_2.addWidget(self.label_17, 4, 1, 1, 2)
        self.label_20 = QtWidgets.QLabel(self.tab3Desc)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_20.setFont(font)
        self.label_20.setObjectName("label_20")
        self.gridLayout_2.addWidget(self.label_20, 5, 1, 1, 2)
        self.label_10 = QtWidgets.QLabel(self.tab3Desc)
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.gridLayout_2.addWidget(self.label_10, 3, 3, 1, 1)
        self.lbTlAbsent = QtWidgets.QLabel(self.tab3Desc)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.lbTlAbsent.setFont(font)
        self.lbTlAbsent.setObjectName("lbTlAbsent")
        self.gridLayout_2.addWidget(self.lbTlAbsent, 3, 4, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.tab3Desc)
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.gridLayout_2.addWidget(self.label_7, 2, 3, 1, 1)
        self.label_16 = QtWidgets.QLabel(self.tab3Desc)
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_16.setFont(font)
        self.label_16.setObjectName("label_16")
        self.gridLayout_2.addWidget(self.label_16, 4, 3, 1, 1)
        self.lbHScore = QtWidgets.QLabel(self.tab3Desc)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.lbHScore.setFont(font)
        self.lbHScore.setObjectName("lbHScore")
        self.gridLayout_2.addWidget(self.lbHScore, 4, 4, 1, 1)
        self.label_21 = QtWidgets.QLabel(self.tab3Desc)
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_21.setFont(font)
        self.label_21.setObjectName("label_21")
        self.gridLayout_2.addWidget(self.label_21, 5, 3, 1, 1)
        self.label_22 = QtWidgets.QLabel(self.tab3Desc)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_22.setFont(font)
        self.label_22.setObjectName("label_22")
        self.gridLayout_2.addWidget(self.label_22, 6, 1, 1, 2)
        self.lbTlFail = QtWidgets.QLabel(self.tab3Desc)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.lbTlFail.setFont(font)
        self.lbTlFail.setObjectName("lbTlFail")
        self.gridLayout_2.addWidget(self.lbTlFail, 2, 4, 1, 1)
        self.label_23 = QtWidgets.QLabel(self.tab3Desc)
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_23.setFont(font)
        self.label_23.setObjectName("label_23")
        self.gridLayout_2.addWidget(self.label_23, 6, 3, 1, 1)
        self.lbLScore = QtWidgets.QLabel(self.tab3Desc)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.lbLScore.setFont(font)
        self.lbLScore.setObjectName("lbLScore")
        self.gridLayout_2.addWidget(self.lbLScore, 5, 4, 1, 1)
        self.label_14 = QtWidgets.QLabel(self.tab3Desc)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_14.setFont(font)
        self.label_14.setObjectName("label_14")
        self.gridLayout_2.addWidget(self.label_14, 7, 1, 1, 2)
        self.label_13 = QtWidgets.QLabel(self.tab3Desc)
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        self.gridLayout_2.addWidget(self.label_13, 7, 3, 1, 1)
        self.lbTlAverage = QtWidgets.QLabel(self.tab3Desc)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.lbTlAverage.setFont(font)
        self.lbTlAverage.setObjectName("lbTlAverage")
        self.gridLayout_2.addWidget(self.lbTlAverage, 7, 4, 1, 1)
        self.lbTlPassPer = QtWidgets.QLabel(self.tab3Desc)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.lbTlPassPer.setFont(font)
        self.lbTlPassPer.setObjectName("lbTlPassPer")
        self.gridLayout_2.addWidget(self.lbTlPassPer, 6, 4, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 200, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        self.gridLayout_2.addItem(spacerItem1, 8, 3, 1, 1)
        self.tabAnalyz.addTab(self.tab3Desc, "")
        self.tb1Tbl = QtWidgets.QWidget()
        self.tb1Tbl.setObjectName("tb1Tbl")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.tb1Tbl)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.tblAna = QtWidgets.QTableWidget(self.tb1Tbl)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tblAna.sizePolicy().hasHeightForWidth())
        self.tblAna.setSizePolicy(sizePolicy)
        self.tblAna.setStyleSheet(" QTableWidget {border-style: outset;\n"
"    border-width: 1px;\n"
"    border-radius: 10px;\n"
"    border-color: black;\n"
"    font: 14px;\n"
"    color:white;\n"
"gridline-color: #fffff8;\n"
"\n"
"}\n"
"QHeaderView::section {\n"
"    background-color: rgb(36,36,36);\n"
"    padding: 5px;\n"
"    font-size: 11pt;\n"
"    color:white;\n"
"    border-style: none;\n"
"    border-bottom: 1px solid #fffff8;\n"
"    border-right: 1px solid #fffff8;\n"
"    border-radius: 5px; \n"
"}\n"
"\n"
"QHeaderView::section:horizontal\n"
"{\n"
"    border-top: 1px solid #fffff8;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QHeaderView::section:vertical\n"
"{\n"
"    border-left: 1px solid #fffff8;\n"
"    border-radius: 5px;\n"
"}\n"
"QTableWidget QTableCornerButton::section {\n"
"    background-color: #333333;\n"
"    border: 1px solid #333333;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QWidget {\n"
"    background-color: #333333;\n"
"    color: #fffff8;\n"
"    font-size: 10pt;\n"
"\n"
"}")
        self.tblAna.setRowCount(1)
        self.tblAna.setObjectName("tblAna")
        self.tblAna.setColumnCount(6)
        item = QtWidgets.QTableWidgetItem()
        self.tblAna.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblAna.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblAna.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblAna.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblAna.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblAna.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblAna.setHorizontalHeaderItem(5, item)
        self.gridLayout_3.addWidget(self.tblAna, 0, 0, 1, 5)
        spacerItem2 = QtWidgets.QSpacerItem(20, 5, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_3.addItem(spacerItem2, 3, 4, 1, 1)
        self.leUSNA = QtWidgets.QLineEdit(self.tb1Tbl)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.leUSNA.sizePolicy().hasHeightForWidth())
        self.leUSNA.setSizePolicy(sizePolicy)
        self.leUSNA.setMinimumSize(QtCore.QSize(40, 0))
        self.leUSNA.setStyleSheet(".QLineEdit{ background-color: qlineargradient(spread:pad, x1:1, y1:0.551, x2:1, y2:0, stop:0 rgba(255, 255,255, 255), stop:1 rgba(255,255 , 255, 255));\n"
"    border-style: inset;\n"
"    border-width: 1px;\n"
"    border-radius: 10px;\n"
"    border-color: black;\n"
"    font: bold 14px;\n"
"    min-width: 2em;\n"
"    padding: 2px;}\n"
"")
        self.leUSNA.setObjectName("leUSNA")
        self.gridLayout_3.addWidget(self.leUSNA, 1, 2, 1, 1)
        self.cbSelTA = QtWidgets.QComboBox(self.tb1Tbl)
        self.cbSelTA.setMinimumSize(QtCore.QSize(80, 0))
        self.cbSelTA.setStyleSheet("background-color: rgb(36,36,36);\n"
"color:rgb(255,255,255);\n"
"    border-style: inset;\n"
"    border-width: 1px;\n"
"    border-radius: 5px;\n"
"    border-color: yellow;\n"
"    font: 12px;\n"
"    min-width: 5em;\n"
"    padding: 4px;\n"
"\n"
"")
        self.cbSelTA.setObjectName("cbSelTA")
        self.gridLayout_3.addWidget(self.cbSelTA, 2, 2, 1, 1)
        self.lbAnaUSN = QtWidgets.QLabel(self.tb1Tbl)
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.lbAnaUSN.setFont(font)
        self.lbAnaUSN.setAlignment(QtCore.Qt.AlignCenter)
        self.lbAnaUSN.setObjectName("lbAnaUSN")
        self.gridLayout_3.addWidget(self.lbAnaUSN, 1, 1, 1, 1)
        self.lbAnaSelect = QtWidgets.QLabel(self.tb1Tbl)
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.lbAnaSelect.setFont(font)
        self.lbAnaSelect.setAlignment(QtCore.Qt.AlignCenter)
        self.lbAnaSelect.setObjectName("lbAnaSelect")
        self.gridLayout_3.addWidget(self.lbAnaSelect, 2, 1, 1, 1)
        self.tabAnalyz.addTab(self.tb1Tbl, "")
        self.tb2Grp = QtWidgets.QWidget()
        self.tb2Grp.setObjectName("tb2Grp")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.tb2Grp)
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_4.setObjectName("gridLayout_4")
        spacerItem3 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem3, 2, 0, 1, 1)
        self.tableWidget_2 = QtWidgets.QTableWidget(self.tb2Grp)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableWidget_2.sizePolicy().hasHeightForWidth())
        self.tableWidget_2.setSizePolicy(sizePolicy)
        self.tableWidget_2.setObjectName("tableWidget_2")
        self.tableWidget_2.setColumnCount(0)
        self.tableWidget_2.setRowCount(0)
        self.gridLayout_4.addWidget(self.tableWidget_2, 0, 4, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_4.addItem(spacerItem4, 3, 2, 1, 1)
        self.tableWidget = QtWidgets.QTableWidget(self.tb2Grp)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableWidget.sizePolicy().hasHeightForWidth())
        self.tableWidget.setSizePolicy(sizePolicy)
        self.tableWidget.setMinimumSize(QtCore.QSize(750, 0))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.gridLayout_4.addWidget(self.tableWidget, 0, 0, 1, 4)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem5, 2, 4, 1, 1)
        self.cbSelGA = QtWidgets.QComboBox(self.tb2Grp)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cbSelGA.sizePolicy().hasHeightForWidth())
        self.cbSelGA.setSizePolicy(sizePolicy)
        self.cbSelGA.setMinimumSize(QtCore.QSize(100, 0))
        self.cbSelGA.setStyleSheet("background-color: rgb(36,36,36);\n"
"color:rgb(255,255,255);\n"
"    border-style: inset;\n"
"    border-width: 1px;\n"
"    border-radius: 5px;\n"
"    border-color: yellow;\n"
"    font: 12px;\n"
"   \n"
"    padding: 4px;\n"
"\n"
"")
        self.cbSelGA.setObjectName("cbSelGA")
        self.gridLayout_4.addWidget(self.cbSelGA, 2, 3, 1, 1)
        self.lbAnaSelect_2 = QtWidgets.QLabel(self.tb2Grp)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbAnaSelect_2.sizePolicy().hasHeightForWidth())
        self.lbAnaSelect_2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.lbAnaSelect_2.setFont(font)
        self.lbAnaSelect_2.setObjectName("lbAnaSelect_2")
        self.gridLayout_4.addWidget(self.lbAnaSelect_2, 2, 2, 1, 1)
        self.tabAnalyz.addTab(self.tb2Grp, "")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.tab)
        self.gridLayout_6.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.label_18 = QtWidgets.QLabel(self.tab)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_18.setFont(font)
        self.label_18.setObjectName("label_18")
        self.gridLayout_6.addWidget(self.label_18, 3, 1, 1, 1)
        self.crl_2 = QtWidgets.QLabel(self.tab)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.crl_2.setFont(font)
        self.crl_2.setObjectName("crl_2")
        self.gridLayout_6.addWidget(self.crl_2, 3, 5, 1, 1)
        self.label_26 = QtWidgets.QLabel(self.tab)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_26.setFont(font)
        self.label_26.setObjectName("label_26")
        self.gridLayout_6.addWidget(self.label_26, 4, 1, 1, 1)
        self.crl_1 = QtWidgets.QLabel(self.tab)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.crl_1.setFont(font)
        self.crl_1.setObjectName("crl_1")
        self.gridLayout_6.addWidget(self.crl_1, 2, 5, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.tab)
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.gridLayout_6.addWidget(self.label_9, 4, 3, 1, 1)
        self.label_12 = QtWidgets.QLabel(self.tab)
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.gridLayout_6.addWidget(self.label_12, 5, 3, 1, 1)
        self.label_28 = QtWidgets.QLabel(self.tab)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_28.setFont(font)
        self.label_28.setObjectName("label_28")
        self.gridLayout_6.addWidget(self.label_28, 5, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.tab)
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.gridLayout_6.addWidget(self.label_4, 2, 3, 1, 1)
        spacerItem6 = QtWidgets.QSpacerItem(15, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_6.addItem(spacerItem6, 4, 0, 1, 1)
        self.crl_3 = QtWidgets.QLabel(self.tab)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.crl_3.setFont(font)
        self.crl_3.setObjectName("crl_3")
        self.gridLayout_6.addWidget(self.crl_3, 4, 5, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.tab)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.gridLayout_6.addWidget(self.label_3, 2, 1, 1, 1)
        self.crl_4 = QtWidgets.QLabel(self.tab)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.crl_4.setFont(font)
        self.crl_4.setObjectName("crl_4")
        self.gridLayout_6.addWidget(self.crl_4, 5, 5, 1, 1)
        self.label_29 = QtWidgets.QLabel(self.tab)
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_29.setFont(font)
        self.label_29.setObjectName("label_29")
        self.gridLayout_6.addWidget(self.label_29, 3, 3, 1, 1)
        self.label_15 = QtWidgets.QLabel(self.tab)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_15.setFont(font)
        self.label_15.setObjectName("label_15")
        self.gridLayout_6.addWidget(self.label_15, 8, 1, 1, 1)
        self.label_24 = QtWidgets.QLabel(self.tab)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_24.setFont(font)
        self.label_24.setObjectName("label_24")
        self.gridLayout_6.addWidget(self.label_24, 6, 1, 1, 1)
        spacerItem7 = QtWidgets.QSpacerItem(20, 180, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        self.gridLayout_6.addItem(spacerItem7, 9, 3, 1, 1)
        self.label_31 = QtWidgets.QLabel(self.tab)
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_31.setFont(font)
        self.label_31.setObjectName("label_31")
        self.gridLayout_6.addWidget(self.label_31, 7, 3, 1, 1)
        self.crl_6 = QtWidgets.QLabel(self.tab)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.crl_6.setFont(font)
        self.crl_6.setObjectName("crl_6")
        self.gridLayout_6.addWidget(self.crl_6, 7, 5, 1, 1)
        self.label_32 = QtWidgets.QLabel(self.tab)
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_32.setFont(font)
        self.label_32.setObjectName("label_32")
        self.gridLayout_6.addWidget(self.label_32, 6, 3, 1, 1)
        self.crl_7 = QtWidgets.QLabel(self.tab)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.crl_7.setFont(font)
        self.crl_7.setObjectName("crl_7")
        self.gridLayout_6.addWidget(self.crl_7, 8, 5, 1, 1)
        self.crl_5 = QtWidgets.QLabel(self.tab)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.crl_5.setFont(font)
        self.crl_5.setObjectName("crl_5")
        self.gridLayout_6.addWidget(self.crl_5, 6, 5, 1, 1)
        self.label_27 = QtWidgets.QLabel(self.tab)
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_27.setFont(font)
        self.label_27.setObjectName("label_27")
        self.gridLayout_6.addWidget(self.label_27, 8, 3, 1, 1)
        self.label_25 = QtWidgets.QLabel(self.tab)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_25.setFont(font)
        self.label_25.setObjectName("label_25")
        self.gridLayout_6.addWidget(self.label_25, 7, 1, 1, 1)
        self.label_19 = QtWidgets.QLabel(self.tab)
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_19.setFont(font)
        self.label_19.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_19.setObjectName("label_19")
        self.gridLayout_6.addWidget(self.label_19, 1, 3, 1, 1)
        self.crl = QtWidgets.QLabel(self.tab)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.crl.setFont(font)
        self.crl.setObjectName("crl")
        self.gridLayout_6.addWidget(self.crl, 1, 5, 1, 1)
        self.label_30 = QtWidgets.QLabel(self.tab)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_30.setFont(font)
        self.label_30.setObjectName("label_30")
        self.gridLayout_6.addWidget(self.label_30, 1, 1, 1, 2)
        self.tabAnalyz.addTab(self.tab, "")
        self.gridLayout.addWidget(self.tabAnalyz, 4, 0, 1, 6)
        self.gridLayout_5.addWidget(self.frame, 0, 0, 2, 2)
        spacerItem8 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_5.addItem(spacerItem8, 1, 1, 1, 1)

        self.retranslateUi(Form)
        self.tabAnalyz.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_sub.setText(_translate("Form", "subject"))
        self.rbCRA.setText(_translate("Form", "Class Ranking"))
        self.rbSubA.setText(_translate("Form", "Subject Wise"))
        self.label_sem.setText(_translate("Form", "sem"))
        self.label_year.setText(_translate("Form", "Year"))
        self.lbTlStuCnt.setText(_translate("Form", "0"))
        self.label_8.setText(_translate("Form", "Fail"))
        self.label_6.setText(_translate("Form", "Pass"))
        self.label_5.setText(_translate("Form", ":"))
        self.label_2.setText(_translate("Form", ":"))
        self.lbTlPass.setText(_translate("Form", "0"))
        self.label.setText(_translate("Form", "Total Students"))
        self.label_11.setText(_translate("Form", "Absent"))
        self.label_17.setText(_translate("Form", "Highest Scored"))
        self.label_20.setText(_translate("Form", "Lowest Scored"))
        self.label_10.setText(_translate("Form", ":"))
        self.lbTlAbsent.setText(_translate("Form", "0"))
        self.label_7.setText(_translate("Form", ":"))
        self.label_16.setText(_translate("Form", ":"))
        self.lbHScore.setText(_translate("Form", "0"))
        self.label_21.setText(_translate("Form", ":"))
        self.label_22.setText(_translate("Form", "Pass Percentage"))
        self.lbTlFail.setText(_translate("Form", "0"))
        self.label_23.setText(_translate("Form", ":"))
        self.lbLScore.setText(_translate("Form", "0"))
        self.label_14.setText(_translate("Form", "Subject Average"))
        self.label_13.setText(_translate("Form", ":"))
        self.lbTlAverage.setText(_translate("Form", "0"))
        self.lbTlPassPer.setText(_translate("Form", "0"))
        self.tabAnalyz.setTabText(self.tabAnalyz.indexOf(self.tab3Desc), _translate("Form", "Description"))
        item = self.tblAna.verticalHeaderItem(0)
        item.setText(_translate("Form", "1"))
        item = self.tblAna.horizontalHeaderItem(0)
        item.setText(_translate("Form", "USN"))
        item = self.tblAna.horizontalHeaderItem(1)
        item.setText(_translate("Form", "Subcode"))
        item = self.tblAna.horizontalHeaderItem(2)
        item.setText(_translate("Form", "Internal"))
        item = self.tblAna.horizontalHeaderItem(3)
        item.setText(_translate("Form", "External"))
        item = self.tblAna.horizontalHeaderItem(4)
        item.setText(_translate("Form", "Total"))
        item = self.tblAna.horizontalHeaderItem(5)
        item.setText(_translate("Form", "Result"))
        self.lbAnaUSN.setText(_translate("Form", "By USN:"))
        self.lbAnaSelect.setText(_translate("Form", "Select : "))
        self.tabAnalyz.setTabText(self.tabAnalyz.indexOf(self.tb1Tbl), _translate("Form", "Table"))
        self.lbAnaSelect_2.setText(_translate("Form", "Select : "))
        self.tabAnalyz.setTabText(self.tabAnalyz.indexOf(self.tb2Grp), _translate("Form", "Graph"))
        self.label_18.setText(_translate("Form", "First Class with Distinction"))
        self.crl_2.setText(_translate("Form", "0"))
        self.label_26.setText(_translate("Form", "First Class"))
        self.crl_1.setText(_translate("Form", "0"))
        self.label_9.setText(_translate("Form", ":"))
        self.label_12.setText(_translate("Form", ":"))
        self.label_28.setText(_translate("Form", "Second Class"))
        self.label_4.setText(_translate("Form", ":"))
        self.crl_3.setText(_translate("Form", "0"))
        self.label_3.setText(_translate("Form", "Topper"))
        self.crl_4.setText(_translate("Form", "0"))
        self.label_29.setText(_translate("Form", ":"))
        self.label_15.setText(_translate("Form", "Pass Percent"))
        self.label_24.setText(_translate("Form", "NO. of Students  Failed"))
        self.label_31.setText(_translate("Form", ":"))
        self.crl_6.setText(_translate("Form", "0"))
        self.label_32.setText(_translate("Form", ":"))
        self.crl_7.setText(_translate("Form", "0"))
        self.crl_5.setText(_translate("Form", "0"))
        self.label_27.setText(_translate("Form", ":"))
        self.label_25.setText(_translate("Form", "NO. of Students  Passed"))
        self.label_19.setText(_translate("Form", ":"))
        self.crl.setText(_translate("Form", "0"))
        self.label_30.setText(_translate("Form", "Total Students"))
        self.tabAnalyz.setTabText(self.tabAnalyz.indexOf(self.tab), _translate("Form", "Descriptions"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

