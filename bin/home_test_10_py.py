# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'home_test_11.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
# from PyQt5 import QtWebKitWidgets
from PyQt5.QtWebEngineWidgets import QWebEngineView

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1350, 810)
        MainWindow.setLayoutDirection(QtCore.Qt.LeftToRight)
        MainWindow.setStyleSheet(" .QFrame { background-color: qlineargradient(spread:pad, x1:0.432034, y1:0.75, x2:0.292, y2:0, stop:0.0847458 rgba(61, 61, 61, 228), stop:1 rgba(254, 254, 254, 255)) }\n"
"\n"
"\n"
"")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setMinimumSize(QtCore.QSize(1350, 700))
        self.centralwidget.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.centralwidget.setStyleSheet(".QWidget{background-color:qlineargradient(spread:pad, x1:0.53, y1:0.454409, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));\n"
"background-image:url(\'login.jpg\')}\n"
"")
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame2 = QtWidgets.QFrame(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame2.sizePolicy().hasHeightForWidth())
        self.frame2.setSizePolicy(sizePolicy)
        self.frame2.setMinimumSize(QtCore.QSize(0, 30))
        self.frame2.setStyleSheet(" .QFrame { background-color :qlineargradient(spread:pad, x1:1, y1:0.551, x2:1, y2:0, stop:0 rgba(0, 3,5, 255), stop:1 rgba(30,130 , 240, 255)) }")
        self.frame2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.frame2.setLineWidth(5)
        self.frame2.setMidLineWidth(0)
        self.frame2.setObjectName("frame2")
        self.verticalLayout.addWidget(self.frame2)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.horizontalLayout_2.setSpacing(9)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setMinimumSize(QtCore.QSize(90, 0))
        self.frame.setMaximumSize(QtCore.QSize(90, 16777215))
        self.frame.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.frame.setStyleSheet(".QFrame{\n"
"background-image: url(\'login1.jpg\');\n"
"}")
        self.frame.setFrameShape(QtWidgets.QFrame.Panel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame.setObjectName("frame")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.btn_home = QtWidgets.QToolButton(self.frame)
        self.btn_home.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.btn_home.setAutoFillBackground(False)
        self.btn_home.setInputMethodHints(QtCore.Qt.ImhNone)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("F:/Rsync/Syed/project files/VTUBroadSpec/bin/icon/home.duckduckgo.com.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_home.setIcon(icon)
        self.btn_home.setIconSize(QtCore.QSize(72, 72))
        self.btn_home.setCheckable(True)
        self.btn_home.setChecked(True)
        self.btn_home.setPopupMode(QtWidgets.QToolButton.DelayedPopup)
        self.btn_home.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        self.btn_home.setAutoRaise(True)
        self.btn_home.setArrowType(QtCore.Qt.NoArrow)
        self.btn_home.setObjectName("btn_home")
        self.verticalLayout_5.addWidget(self.btn_home)
        self.btn_new = QtWidgets.QToolButton(self.frame)
        self.btn_new.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.btn_new.setAutoFillBackground(False)
        self.btn_new.setStyleSheet(".QToolButton{background-image:url(\"C:/Users/SYED/Desktop/icon.ico\")}")
        self.btn_new.setInputMethodHints(QtCore.Qt.ImhNone)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("F:/Rsync/Syed/project files/VTUBroadSpec/bin/icon/new.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_new.setIcon(icon1)
        self.btn_new.setIconSize(QtCore.QSize(72, 72))
        self.btn_new.setCheckable(True)
        self.btn_new.setChecked(False)
        self.btn_new.setPopupMode(QtWidgets.QToolButton.DelayedPopup)
        self.btn_new.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        self.btn_new.setAutoRaise(True)
        self.btn_new.setArrowType(QtCore.Qt.NoArrow)
        self.btn_new.setObjectName("btn_new")
        self.verticalLayout_5.addWidget(self.btn_new)
        self.btn_analyse = QtWidgets.QToolButton(self.frame)
        self.btn_analyse.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.btn_analyse.setAutoFillBackground(False)
        self.btn_analyse.setInputMethodHints(QtCore.Qt.ImhNone)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("F:/Rsync/Syed/project files/VTUBroadSpec/bin/icon/bw-analysis.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_analyse.setIcon(icon2)
        self.btn_analyse.setIconSize(QtCore.QSize(72, 72))
        self.btn_analyse.setCheckable(False)
        self.btn_analyse.setChecked(False)
        self.btn_analyse.setPopupMode(QtWidgets.QToolButton.DelayedPopup)
        self.btn_analyse.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        self.btn_analyse.setAutoRaise(True)
        self.btn_analyse.setArrowType(QtCore.Qt.NoArrow)
        self.btn_analyse.setObjectName("btn_analyse")
        self.verticalLayout_5.addWidget(self.btn_analyse)
        self.btn_setting = QtWidgets.QToolButton(self.frame)
        self.btn_setting.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.btn_setting.setAutoFillBackground(False)
        self.btn_setting.setInputMethodHints(QtCore.Qt.ImhNone)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("F:/Rsync/Syed/project files/VTUBroadSpec/bin/icon/Settings.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_setting.setIcon(icon3)
        self.btn_setting.setIconSize(QtCore.QSize(72, 72))
        self.btn_setting.setCheckable(False)
        self.btn_setting.setChecked(False)
        self.btn_setting.setPopupMode(QtWidgets.QToolButton.DelayedPopup)
        self.btn_setting.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        self.btn_setting.setAutoRaise(True)
        self.btn_setting.setArrowType(QtCore.Qt.NoArrow)
        self.btn_setting.setObjectName("btn_setting")
        self.verticalLayout_5.addWidget(self.btn_setting)
        spacerItem = QtWidgets.QSpacerItem(20, 200, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        self.verticalLayout_5.addItem(spacerItem)
        self.horizontalLayout_2.addWidget(self.frame)
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setAutoFillBackground(False)
        self.stackedWidget.setStyleSheet(".QStackedWidget{margin:0px;}\n"
".QWidget{\n"
"                \n"
"                background-color:rgb(235, 235, 235)}")
        self.stackedWidget.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.stackedWidget.setObjectName("stackedWidget")
        self.stk_home = QtWidgets.QWidget()
        self.stk_home.setToolTip("")
        self.stk_home.setToolTipDuration(1000)
        self.stk_home.setStyleSheet(".QWidget{  \n"
"     border-style:inset;\n"
"      background-image:url(\'euro.jpg\');\n"
"     \n"
"     background-position:left;\n"
"     background-fill:yes;\n"
"}")
        self.stk_home.setObjectName("stk_home")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.stk_home)
        self.gridLayout_3.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.hmLE = QtWidgets.QLineEdit(self.stk_home)
        self.hmLE.setStyleSheet(".QLineEdit{ background-color: qlineargradient(spread:pad, x1:1, y1:0.551, x2:1, y2:0, stop:0 rgba(255, 255,255, 255), stop:1 rgba(20,80 , 180, 255));\n"
"    border-style: inset;\n"
"    border-width: 1px;\n"
"    border-radius: 10px;\n"
"    border-color: black;\n"
"    font: bold 14px;\n"
"    min-width: 6em;\n"
"    padding: 6px;}\n"
"")
        self.hmLE.setObjectName("hmLE")
        self.gridLayout_3.addWidget(self.hmLE, 1, 1, 1, 1)
        # self.hmWeb = QtWebKitWidgets.QWebView(self.stk_home)
        self.hmWeb = QWebEngineView(self.stk_home);
        self.hmWeb.setEnabled(True)
        self.hmWeb.setUrl(QtCore.QUrl("about:blank"))
        self.hmWeb.setObjectName("hmWeb")
        self.gridLayout_3.addWidget(self.hmWeb, 2, 0, 1, 3)
        self.hmLbl = QtWidgets.QLabel(self.stk_home)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.hmLbl.setFont(font)
        self.hmLbl.setStyleSheet("color:rgb(230,250,250)")
        self.hmLbl.setObjectName("hmLbl")
        self.gridLayout_3.addWidget(self.hmLbl, 1, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 5, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_3.addItem(spacerItem1, 0, 1, 1, 1)
        self.hmbtn = QtWidgets.QPushButton(self.stk_home)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.hmbtn.sizePolicy().hasHeightForWidth())
        self.hmbtn.setSizePolicy(sizePolicy)
        self.hmbtn.setMinimumSize(QtCore.QSize(116, 0))
        self.hmbtn.setStyleSheet(".QPushButton:pressed {background-color: qlineargradient(spread:pad, x1:1, y1:0.551, x2:1, y2:0, stop:0 rgba(70, 73,75, 240), stop:1 rgba(50,180 , 255, 255));\n"
"    border-style: outset;\n"
"    border-width: 1px;\n"
"    border-radius: 10px;\n"
"    border-color: grey;\n"
"    font: bold 14px;\n"
"    color:yellow;\n"
"    min-width: 7em;\n"
"    padding: 6px;}\n"
".QPushButton { background-color: qlineargradient(spread:pad, x1:1, y1:0.551, x2:1, y2:0, stop:0 rgba(10, 13,15, 255), stop:1 rgba(20,80 , 180, 255));\n"
"    border-style: inset;\n"
"    border-width: 1px;\n"
"    border-radius: 10px;\n"
"    border-color: black;\n"
"    font: bold 14px;\n"
"    color:rgb(220,250,250);\n"
"    min-width: 6em;\n"
"    padding: 6px;}\n"
"")
        self.hmbtn.setDefault(False)
        self.hmbtn.setFlat(False)
        self.hmbtn.setObjectName("hmbtn")
        self.gridLayout_3.addWidget(self.hmbtn, 1, 2, 1, 1)
        self.stackedWidget.addWidget(self.stk_home)
        self.stk_new = QtWidgets.QWidget()
        self.stk_new.setStyleSheet(".QWidget{  \n"
"    \n"
"    \n"
"      background-image:url(\'lb.jpg\');\n"
"     background-repeat:no repeat;\n"
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
        self.stk_new.setObjectName("stk_new")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.stk_new)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(15)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.tabWidget = QtWidgets.QTabWidget(self.stk_new)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.tabWidget.setFont(font)
        self.tabWidget.setStyleSheet("QTabWidget::pane { /* The tab widget frame */\n"
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
        self.tabWidget.setTabPosition(QtWidgets.QTabWidget.North)
        self.tabWidget.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.tabWidget.setElideMode(QtCore.Qt.ElideNone)
        self.tabWidget.setDocumentMode(False)
        self.tabWidget.setTabsClosable(False)
        self.tabWidget.setMovable(False)
        self.tabWidget.setTabBarAutoHide(True)
        self.tabWidget.setObjectName("tabWidget")
        self.tb_root = QtWidgets.QWidget()
        self.tb_root.setAutoFillBackground(True)
        self.tb_root.setObjectName("tb_root")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.tb_root)
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_5.setObjectName("gridLayout_5")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_5.addItem(spacerItem2, 3, 0, 1, 2)
        self.pbtnRrm = QtWidgets.QPushButton(self.tb_root)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pbtnRrm.sizePolicy().hasHeightForWidth())
        self.pbtnRrm.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pbtnRrm.setFont(font)
        self.pbtnRrm.setStyleSheet(".QPushButton:pressed {  \n"
"    background-color: Transparent;\n"
"    border:none;\n"
"    font: bold 10;\n"
"    color:blue;\n"
"    }\n"
".QPushButton:hover {  \n"
"   color:blue;\n"
"    }\n"
".QPushButton:pressed {\n"
"color:yellow;\n"
"font:  bold 15;\n"
"\n"
"}\n"
"")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("F:/down/gtk-remove.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pbtnRrm.setIcon(icon4)
        self.pbtnRrm.setFlat(True)
        self.pbtnRrm.setObjectName("pbtnRrm")
        self.gridLayout_5.addWidget(self.pbtnRrm, 3, 4, 1, 1)
        self.tblWR = QtWidgets.QTableWidget(self.tb_root)
        self.tblWR.setAutoFillBackground(True)
        self.tblWR.setStyleSheet(" QTableWidget {border-style: outset;\n"
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
        self.tblWR.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.tblWR.setRowCount(1)
        self.tblWR.setColumnCount(1)
        self.tblWR.setObjectName("tblWR")
        item = QtWidgets.QTableWidgetItem()
        self.tblWR.setVerticalHeaderItem(0, item)
        self.gridLayout_5.addWidget(self.tblWR, 2, 0, 1, 8)
        self.lbRtable = QtWidgets.QLabel(self.tb_root)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lbRtable.setFont(font)
        self.lbRtable.setAlignment(QtCore.Qt.AlignCenter)
        self.lbRtable.setObjectName("lbRtable")
        self.gridLayout_5.addWidget(self.lbRtable, 1, 0, 1, 1)
        self.cbRtable = QtWidgets.QComboBox(self.tb_root)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cbRtable.sizePolicy().hasHeightForWidth())
        self.cbRtable.setSizePolicy(sizePolicy)
        self.cbRtable.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.cbRtable.setToolTip("")
        self.cbRtable.setStyleSheet("background-color: rgb(36,36,36);\n"
"color:rgb(255,255,255);\n"
"    border-style: inset;\n"
"    border-width: 1px;\n"
"    border-radius: 5px;\n"
"    border-color: yellow;\n"
"    font: 14px;\n"
"    min-width: 8em;\n"
"    padding: 2px;\n"
"\n"
"")
        self.cbRtable.setFrame(False)
        self.cbRtable.setObjectName("cbRtable")
        self.gridLayout_5.addWidget(self.cbRtable, 1, 4, 1, 1)
        self.pbtnRset = QtWidgets.QPushButton(self.tb_root)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pbtnRset.sizePolicy().hasHeightForWidth())
        self.pbtnRset.setSizePolicy(sizePolicy)
        self.pbtnRset.setMinimumSize(QtCore.QSize(116, 0))
        self.pbtnRset.setStyleSheet(".QPushButton {background-color: rgb(36,36,36);\n"
"color:rgb(255,255,255);\n"
"    border-style: inset;\n"
"    border-width: 1px;\n"
"    border-radius: 10px;\n"
"    border-color: yellow;\n"
"    font: 14px;\n"
"    min-width: 6em;\n"
"    padding: 6px;\n"
"}\n"
".QPushButton:pressed {background-color: rgb(66,66,66);\n"
"color:yellow;\n"
"font: 16px;\n"
" border-style: outset;\n"
"border-width: 1.5px;\n"
"}")
        self.pbtnRset.setObjectName("pbtnRset")
        self.gridLayout_5.addWidget(self.pbtnRset, 3, 6, 1, 1)
        self.pbtnRsv = QtWidgets.QPushButton(self.tb_root)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pbtnRsv.sizePolicy().hasHeightForWidth())
        self.pbtnRsv.setSizePolicy(sizePolicy)
        self.pbtnRsv.setMinimumSize(QtCore.QSize(116, 0))
        self.pbtnRsv.setStyleSheet(".QPushButton {background-color: rgb(36,36,36);\n"
"color:rgb(255,255,255);\n"
"    border-style: inset;\n"
"    border-width: 1px;\n"
"    border-radius: 10px;\n"
"    border-color: yellow;\n"
"    font: 14px;\n"
"    min-width: 6em;\n"
"    padding: 6px;\n"
"}\n"
".QPushButton:pressed {background-color: rgb(66,66,66);\n"
"color:yellow;\n"
"font: 16px;\n"
" border-style: outset;\n"
"border-width: 1.5px;\n"
"}")
        self.pbtnRsv.setObjectName("pbtnRsv")
        self.gridLayout_5.addWidget(self.pbtnRsv, 3, 7, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_5.addItem(spacerItem3, 3, 5, 1, 1)
        self.pbtnRadd = QtWidgets.QPushButton(self.tb_root)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pbtnRadd.sizePolicy().hasHeightForWidth())
        self.pbtnRadd.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pbtnRadd.setFont(font)
        self.pbtnRadd.setStyleSheet(".QPushButton:pressed {  \n"
"    background-color: Transparent;\n"
"    border:none;\n"
"    font: bold 10;\n"
"    color:blue;\n"
"    }\n"
".QPushButton:hover {  \n"
"   color:blue;\n"
"    }\n"
".QPushButton:pressed {\n"
"color:yellow;\n"
"font:  bold 15;\n"
"\n"
"}\n"
"")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("F:/down/gtk-add.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pbtnRadd.setIcon(icon5)
        self.pbtnRadd.setFlat(True)
        self.pbtnRadd.setObjectName("pbtnRadd")
        self.gridLayout_5.addWidget(self.pbtnRadd, 3, 2, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(10, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_5.addItem(spacerItem4, 0, 4, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_5.addItem(spacerItem5, 4, 2, 1, 1)
        self.tabWidget.addTab(self.tb_root, "")
        self.tb_Internal = QtWidgets.QWidget()
        self.tb_Internal.setObjectName("tb_Internal")
        self.gridLayout = QtWidgets.QGridLayout(self.tb_Internal)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.InChSave = QtWidgets.QCheckBox(self.tb_Internal)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.InChSave.sizePolicy().hasHeightForWidth())
        self.InChSave.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.InChSave.setFont(font)
        self.InChSave.setObjectName("InChSave")
        self.gridLayout.addWidget(self.InChSave, 6, 9, 1, 1)
        self.InLbYear = QtWidgets.QLabel(self.tb_Internal)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.InLbYear.sizePolicy().hasHeightForWidth())
        self.InLbYear.setSizePolicy(sizePolicy)
        self.InLbYear.setMinimumSize(QtCore.QSize(50, 0))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.InLbYear.setFont(font)
        self.InLbYear.setStatusTip("")
        self.InLbYear.setAlignment(QtCore.Qt.AlignCenter)
        self.InLbYear.setObjectName("InLbYear")
        self.gridLayout.addWidget(self.InLbYear, 1, 1, 1, 1)
        self.InLbSU = QtWidgets.QLabel(self.tb_Internal)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.InLbSU.setFont(font)
        self.InLbSU.setAlignment(QtCore.Qt.AlignCenter)
        self.InLbSU.setObjectName("InLbSU")
        self.gridLayout.addWidget(self.InLbSU, 4, 3, 1, 1)
        self.InCbSub = QtWidgets.QComboBox(self.tb_Internal)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.InCbSub.sizePolicy().hasHeightForWidth())
        self.InCbSub.setSizePolicy(sizePolicy)
        self.InCbSub.setToolTip("")
        self.InCbSub.setStyleSheet("background-color: rgb(36,36,36);\n"
"color:rgb(255,255,255);\n"
"    border-style: inset;\n"
"    border-width: 1px;\n"
"    border-radius: 5px;\n"
"    border-color: yellow;\n"
"    font: 14px;\n"
"    min-width: 8em;\n"
"    padding: 2px;\n"
"\n"
"")
        self.InCbSub.setMaxVisibleItems(5)
        self.InCbSub.setObjectName("InCbSub")
        self.gridLayout.addWidget(self.InCbSub, 1, 5, 1, 2)
        self.InbtnRst = QtWidgets.QPushButton(self.tb_Internal)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.InbtnRst.sizePolicy().hasHeightForWidth())
        self.InbtnRst.setSizePolicy(sizePolicy)
        self.InbtnRst.setMinimumSize(QtCore.QSize(116, 0))
        self.InbtnRst.setStyleSheet(".QPushButton {background-color: rgb(36,36,36);\n"
"color:rgb(255,255,255);\n"
"    border-style: inset;\n"
"    border-width: 1px;\n"
"    border-radius: 10px;\n"
"    border-color: yellow;\n"
"    font: 14px;\n"
"    min-width: 6em;\n"
"    padding: 6px;\n"
"}\n"
".QPushButton:pressed {background-color: rgb(66,66,66);\n"
"color:yellow;\n"
"font: 16px;\n"
" border-style: outset;\n"
"border-width: 1.5px;\n"
"}")
        self.InbtnRst.setObjectName("InbtnRst")
        self.gridLayout.addWidget(self.InbtnRst, 7, 8, 1, 1)
        self.InbtnAdd = QtWidgets.QPushButton(self.tb_Internal)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.InbtnAdd.sizePolicy().hasHeightForWidth())
        self.InbtnAdd.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.InbtnAdd.setFont(font)
        self.InbtnAdd.setStyleSheet(".QPushButton:pressed {  \n"
"    background-color: Transparent;\n"
"    border:none;\n"
"    font: bold 10;\n"
"    color:blue;\n"
"    }\n"
".QPushButton:hover {  \n"
"   color:blue;\n"
"    }\n"
".QPushButton:pressed {\n"
"color:yellow;\n"
"font:  bold 15;\n"
"\n"
"}\n"
"")
        self.InbtnAdd.setIcon(icon5)
        self.InbtnAdd.setFlat(True)
        self.InbtnAdd.setObjectName("InbtnAdd")
        self.gridLayout.addWidget(self.InbtnAdd, 4, 1, 1, 1)
        self.IntblW = QtWidgets.QTableWidget(self.tb_Internal)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.IntblW.sizePolicy().hasHeightForWidth())
        self.IntblW.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.IntblW.setFont(font)
        self.IntblW.setStyleSheet(" QTableWidget {border-style: outset;\n"
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
        self.IntblW.setRowCount(1)
        self.IntblW.setObjectName("IntblW")
        self.IntblW.setColumnCount(6)
        item = QtWidgets.QTableWidgetItem()
        self.IntblW.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.IntblW.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.IntblW.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.IntblW.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.IntblW.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.IntblW.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.IntblW.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.IntblW.setItem(0, 0, item)
        self.gridLayout.addWidget(self.IntblW, 3, 1, 1, 9)
        self.InLeSU = QtWidgets.QLineEdit(self.tb_Internal)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.InLeSU.sizePolicy().hasHeightForWidth())
        self.InLeSU.setSizePolicy(sizePolicy)
        self.InLeSU.setMinimumSize(QtCore.QSize(0, 0))
        self.InLeSU.setStyleSheet(".QLineEdit{ background-color: qlineargradient(spread:pad, x1:1, y1:0.551, x2:1, y2:0, stop:0 rgba(255, 255,255, 255), stop:1 rgba(255,255 , 255, 255));\n"
"    border-style: inset;\n"
"    border-width: 1px;\n"
"    border-radius: 10px;\n"
"    border-color: black;\n"
"    font: 14px;\n"
"    \n"
"    padding: 5px;}\n"
"")
        self.InLeSU.setObjectName("InLeSU")
        self.gridLayout.addWidget(self.InLeSU, 4, 4, 1, 2)
        self.InbtnRm = QtWidgets.QPushButton(self.tb_Internal)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.InbtnRm.sizePolicy().hasHeightForWidth())
        self.InbtnRm.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.InbtnRm.setFont(font)
        self.InbtnRm.setStyleSheet(".QPushButton:pressed {  \n"
"    background-color: Transparent;\n"
"    border:none;\n"
"    font: bold 10;\n"
"    color:blue;\n"
"    }\n"
".QPushButton:hover {  \n"
"   color:blue;\n"
"    }\n"
".QPushButton:pressed {\n"
"color:yellow;\n"
"font:  bold 15;\n"
"\n"
"}\n"
"")
        self.InbtnRm.setIcon(icon4)
        self.InbtnRm.setFlat(True)
        self.InbtnRm.setObjectName("InbtnRm")
        self.gridLayout.addWidget(self.InbtnRm, 4, 2, 1, 1)
        spacerItem6 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        self.gridLayout.addItem(spacerItem6, 2, 3, 1, 1)
        self.InbtnSave = QtWidgets.QPushButton(self.tb_Internal)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.InbtnSave.sizePolicy().hasHeightForWidth())
        self.InbtnSave.setSizePolicy(sizePolicy)
        self.InbtnSave.setMinimumSize(QtCore.QSize(116, 0))
        self.InbtnSave.setStyleSheet(".QPushButton {background-color: rgb(36,36,36);\n"
"color:rgb(255,255,255);\n"
"    border-style: inset;\n"
"    border-width: 1px;\n"
"    border-radius: 10px;\n"
"    border-color: yellow;\n"
"    font: 14px;\n"
"    min-width: 6em;\n"
"    padding: 6px;\n"
"}\n"
".QPushButton:pressed {background-color: rgb(66,66,66);\n"
"color:yellow;\n"
"font: 16px;\n"
" border-style: outset;\n"
"border-width: 1.5px;\n"
"}")
        self.InbtnSave.setObjectName("InbtnSave")
        self.gridLayout.addWidget(self.InbtnSave, 7, 9, 1, 1)
        self.line_5 = QtWidgets.QFrame(self.tb_Internal)
        self.line_5.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.gridLayout.addWidget(self.line_5, 5, 1, 1, 9)
        self.InLbSub = QtWidgets.QLabel(self.tb_Internal)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.InLbSub.setFont(font)
        self.InLbSub.setAlignment(QtCore.Qt.AlignCenter)
        self.InLbSub.setObjectName("InLbSub")
        self.gridLayout.addWidget(self.InLbSub, 1, 4, 1, 1)
        self.InSbYear = QtWidgets.QSpinBox(self.tb_Internal)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.InSbYear.sizePolicy().hasHeightForWidth())
        self.InSbYear.setSizePolicy(sizePolicy)
        self.InSbYear.setMinimumSize(QtCore.QSize(142, 0))
        self.InSbYear.setStyleSheet("background-color: rgb(36,36,36);\n"
"color:rgb(255,255,255);\n"
"    border-style: inset;\n"
"    border-width: 1px;\n"
"    border-radius: 5px;\n"
"    border-color: yellow;\n"
"    font: 14px;\n"
"    min-width: 8em;\n"
"    padding: 2px;\n"
"\n"
"")
        self.InSbYear.setMinimum(2018)
        self.InSbYear.setMaximum(3000)
        self.InSbYear.setSingleStep(1)
        self.InSbYear.setDisplayIntegerBase(10)
        self.InSbYear.setObjectName("InSbYear")
        self.gridLayout.addWidget(self.InSbYear, 1, 2, 1, 1)
        spacerItem7 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout.addItem(spacerItem7, 0, 4, 1, 1)
        spacerItem8 = QtWidgets.QSpacerItem(20, 5, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout.addItem(spacerItem8, 8, 9, 1, 1)
        spacerItem9 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem9, 7, 10, 1, 1)
        self.tabWidget.addTab(self.tb_Internal, "")
        self.tb_edit = QtWidgets.QWidget()
        self.tb_edit.setObjectName("tb_edit")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.tb_edit)
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_4.setHorizontalSpacing(9)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.EdbtnSave = QtWidgets.QPushButton(self.tb_edit)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.EdbtnSave.sizePolicy().hasHeightForWidth())
        self.EdbtnSave.setSizePolicy(sizePolicy)
        self.EdbtnSave.setMinimumSize(QtCore.QSize(116, 0))
        self.EdbtnSave.setStyleSheet(".QPushButton {background-color: rgb(36,36,36);\n"
"color:rgb(255,255,255);\n"
"    border-style: inset;\n"
"    border-width: 1px;\n"
"    border-radius: 10px;\n"
"    border-color: yellow;\n"
"    font: 14px;\n"
"    min-width: 6em;\n"
"    padding: 6px;\n"
"}\n"
".QPushButton:pressed {background-color: rgb(66,66,66);\n"
"color:yellow;\n"
"font: 16px;\n"
" border-style: outset;\n"
"border-width: 1.5px;\n"
"}")
        self.EdbtnSave.setObjectName("EdbtnSave")
        self.gridLayout_4.addWidget(self.EdbtnSave, 5, 7, 1, 1)
        self.line_4 = QtWidgets.QFrame(self.tb_edit)
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.gridLayout_4.addWidget(self.line_4, 4, 1, 1, 7)
        self.EdLeSN = QtWidgets.QLineEdit(self.tb_edit)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.EdLeSN.sizePolicy().hasHeightForWidth())
        self.EdLeSN.setSizePolicy(sizePolicy)
        self.EdLeSN.setMinimumSize(QtCore.QSize(400, 0))
        self.EdLeSN.setStyleSheet(".QLineEdit{ background-color: qlineargradient(spread:pad, x1:1, y1:0.551, x2:1, y2:0, stop:0 rgba(255, 255,255, 255), stop:1 rgba(255,255 , 255, 255));\n"
"    border-style: inset;\n"
"    border-width: 1px;\n"
"    border-radius: 10px;\n"
"    border-color: black;\n"
"    font: 14px;\n"
"    \n"
"    padding: 5px;}\n"
"")
        self.EdLeSN.setObjectName("EdLeSN")
        self.gridLayout_4.addWidget(self.EdLeSN, 3, 2, 1, 1)
        self.EdLeSU = QtWidgets.QLineEdit(self.tb_edit)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.EdLeSU.sizePolicy().hasHeightForWidth())
        self.EdLeSU.setSizePolicy(sizePolicy)
        self.EdLeSU.setMinimumSize(QtCore.QSize(400, 0))
        self.EdLeSU.setStyleSheet(".QLineEdit{ background-color: qlineargradient(spread:pad, x1:1, y1:0.551, x2:1, y2:0, stop:0 rgba(255, 255,255, 255), stop:1 rgba(255,255 , 255, 255));\n"
"    border-style: inset;\n"
"    border-width: 1px;\n"
"    border-radius: 10px;\n"
"    border-color: black;\n"
"    font: 14px;\n"
"    \n"
"    padding: 5px;}\n"
"")
        self.EdLeSU.setObjectName("EdLeSU")
        self.gridLayout_4.addWidget(self.EdLeSU, 3, 4, 1, 4)
        self.EdbtnRst = QtWidgets.QPushButton(self.tb_edit)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.EdbtnRst.sizePolicy().hasHeightForWidth())
        self.EdbtnRst.setSizePolicy(sizePolicy)
        self.EdbtnRst.setMinimumSize(QtCore.QSize(116, 0))
        self.EdbtnRst.setStyleSheet(".QPushButton {background-color: rgb(36,36,36);\n"
"color:rgb(255,255,255);\n"
"    border-style: inset;\n"
"    border-width: 1px;\n"
"    border-radius: 10px;\n"
"    border-color: yellow;\n"
"    font: 14px;\n"
"    min-width: 6em;\n"
"    padding: 6px;\n"
"}\n"
".QPushButton:pressed {background-color: rgb(66,66,66);\n"
"color:yellow;\n"
"font: 16px;\n"
" border-style: outset;\n"
"border-width: 1.5px;\n"
"}")
        self.EdbtnRst.setObjectName("EdbtnRst")
        self.gridLayout_4.addWidget(self.EdbtnRst, 5, 6, 1, 1)
        self.EdLbSN = QtWidgets.QLabel(self.tb_edit)
        self.EdLbSN.setMinimumSize(QtCore.QSize(200, 0))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.EdLbSN.setFont(font)
        self.EdLbSN.setAlignment(QtCore.Qt.AlignCenter)
        self.EdLbSN.setObjectName("EdLbSN")
        self.gridLayout_4.addWidget(self.EdLbSN, 3, 1, 1, 1)
        self.EdbtnLd = QtWidgets.QPushButton(self.tb_edit)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.EdbtnLd.sizePolicy().hasHeightForWidth())
        self.EdbtnLd.setSizePolicy(sizePolicy)
        self.EdbtnLd.setMinimumSize(QtCore.QSize(150, 0))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.EdbtnLd.setFont(font)
        self.EdbtnLd.setStyleSheet(".QPushButton {background-color: rgb(36,36,36);\n"
"color:rgb(255,255,255);\n"
"    border-style: inset;\n"
"    border-width: 1px;\n"
"    border-radius: 10px;\n"
"    border-color: yellow;\n"
"    font:bold 16px;\n"
"    min-width: 6em;\n"
"    padding: 6px;\n"
"}\n"
".QPushButton:pressed {background-color: rgb(66,66,66);\n"
"color:yellow;\n"
"font: bold 18px;\n"
" border-style: outset;\n"
"border-width: 1.5px;\n"
"}")
        self.EdbtnLd.setAutoDefault(False)
        self.EdbtnLd.setFlat(False)
        self.EdbtnLd.setObjectName("EdbtnLd")
        self.gridLayout_4.addWidget(self.EdbtnLd, 5, 1, 1, 1)
        spacerItem10 = QtWidgets.QSpacerItem(5, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem10, 1, 0, 1, 1)
        self.EdLbSU = QtWidgets.QLabel(self.tb_edit)
        self.EdLbSU.setMinimumSize(QtCore.QSize(150, 0))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.EdLbSU.setFont(font)
        self.EdLbSU.setAlignment(QtCore.Qt.AlignCenter)
        self.EdLbSU.setObjectName("EdLbSU")
        self.gridLayout_4.addWidget(self.EdLbSU, 3, 3, 1, 1)
        self.EdtblW = QtWidgets.QTableWidget(self.tb_edit)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.EdtblW.setFont(font)
        self.EdtblW.setStyleSheet(" QTableWidget {border-style: outset;\n"
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
        self.EdtblW.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.EdtblW.setFrameShadow(QtWidgets.QFrame.Raised)
        self.EdtblW.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectItems)
        self.EdtblW.setRowCount(1)
        self.EdtblW.setObjectName("EdtblW")
        self.EdtblW.setColumnCount(7)
        item = QtWidgets.QTableWidgetItem()
        self.EdtblW.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.EdtblW.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.EdtblW.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        font.setStrikeOut(False)
        item.setFont(font)
        self.EdtblW.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.EdtblW.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.EdtblW.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.EdtblW.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.EdtblW.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        item.setFlags(QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled)
        self.EdtblW.setItem(0, 2, item)
        self.gridLayout_4.addWidget(self.EdtblW, 1, 1, 1, 7)
        spacerItem11 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_4.addItem(spacerItem11, 0, 1, 1, 1)
        spacerItem12 = QtWidgets.QSpacerItem(20, 5, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_4.addItem(spacerItem12, 6, 1, 1, 1)
        spacerItem13 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem13, 5, 8, 1, 1)
        self.tabWidget.addTab(self.tb_edit, "")
        self.tb_scrap = QtWidgets.QWidget()
        self.tb_scrap.setObjectName("tb_scrap")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.tb_scrap)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setHorizontalSpacing(20)
        self.gridLayout_2.setVerticalSpacing(50)
        self.gridLayout_2.setObjectName("gridLayout_2")
        spacerItem14 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem14, 0, 0, 2, 1)
        self.ScpLeRV = QtWidgets.QLineEdit(self.tb_scrap)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ScpLeRV.sizePolicy().hasHeightForWidth())
        self.ScpLeRV.setSizePolicy(sizePolicy)
        self.ScpLeRV.setMinimumSize(QtCore.QSize(116, 25))
        self.ScpLeRV.setStyleSheet(".QLineEdit{ background-color: qlineargradient(spread:pad, x1:1, y1:0.551, x2:1, y2:0, stop:0 rgba(255, 255,255, 255), stop:1 rgba(255,255 , 255, 255));\n"
"    border-style: inset;\n"
"    border-width: 1px;\n"
"    border-radius: 10px;\n"
"    border-color: black;\n"
"    font: bold 14px;\n"
"    min-width: 6em;\n"
"    padding: 6px;}\n"
"")
        self.ScpLeRV.setObjectName("ScpLeRV")
        self.gridLayout_2.addWidget(self.ScpLeRV, 4, 1, 1, 3)
        self.ScpLeAr = QtWidgets.QLineEdit(self.tb_scrap)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ScpLeAr.sizePolicy().hasHeightForWidth())
        self.ScpLeAr.setSizePolicy(sizePolicy)
        self.ScpLeAr.setMinimumSize(QtCore.QSize(116, 25))
        self.ScpLeAr.setStyleSheet(".QLineEdit{ background-color: qlineargradient(spread:pad, x1:1, y1:0.551, x2:1, y2:0, stop:0 rgba(255, 255,255, 255), stop:1 rgba(255,255 , 255, 255));\n"
"    border-style: inset;\n"
"    border-width: 1px;\n"
"    border-radius: 10px;\n"
"    border-color: black;\n"
"    font: bold 14px;\n"
"    min-width: 6em;\n"
"    padding: 6px;}\n"
"")
        self.ScpLeAr.setObjectName("ScpLeAr")
        self.gridLayout_2.addWidget(self.ScpLeAr, 5, 1, 1, 3)
        self.ScpbtnRV = QtWidgets.QPushButton(self.tb_scrap)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ScpbtnRV.sizePolicy().hasHeightForWidth())
        self.ScpbtnRV.setSizePolicy(sizePolicy)
        self.ScpbtnRV.setMinimumSize(QtCore.QSize(116, 34))
        self.ScpbtnRV.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.ScpbtnRV.setStyleSheet(".QPushButton:pressed {background-color: qlineargradient(spread:pad, x1:1, y1:0.551, x2:1, y2:0, stop:0 rgba(70, 73,75, 240), stop:1 rgba(50,180 , 255, 255));\n"
"    border-style: outset;\n"
"    border-width: 1px;\n"
"    border-radius: 10px;\n"
"    border-color: grey;\n"
"    font: bold 14px;\n"
"    color:yellow;\n"
"    min-width: 7em;\n"
"    padding: 6px;}\n"
".QPushButton { background-color: qlineargradient(spread:pad, x1:1, y1:0.551, x2:1, y2:0, stop:0 rgba(10, 13,15, 255), stop:1 rgba(20,80 , 180, 255));\n"
"    border-style: inset;\n"
"    border-width: 1px;\n"
"    border-radius: 10px;\n"
"    border-color: black;\n"
"    font: bold 14px;\n"
"    color:rgb(220,250,250);\n"
"    min-width: 6em;\n"
"    padding: 6px;}\n"
"")
        self.ScpbtnRV.setAutoDefault(True)
        self.ScpbtnRV.setDefault(False)
        self.ScpbtnRV.setFlat(False)
        self.ScpbtnRV.setObjectName("ScpbtnRV")
        self.gridLayout_2.addWidget(self.ScpbtnRV, 4, 4, 1, 1)
        self.ScpLeRg = QtWidgets.QLineEdit(self.tb_scrap)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ScpLeRg.sizePolicy().hasHeightForWidth())
        self.ScpLeRg.setSizePolicy(sizePolicy)
        self.ScpLeRg.setMinimumSize(QtCore.QSize(116, 25))
        self.ScpLeRg.setStyleSheet(".QLineEdit{ background-color: qlineargradient(spread:pad, x1:1, y1:0.551, x2:1, y2:0, stop:0 rgba(255, 255,255, 255), stop:1 rgba(255,255 , 255, 255));\n"
"    border-style: inset;\n"
"    border-width: 1px;\n"
"    border-radius: 10px;\n"
"    border-color: black;\n"
"    font: bold 14px;\n"
"    min-width: 6em;\n"
"    padding: 6px;}\n"
"")
        self.ScpLeRg.setObjectName("ScpLeRg")
        self.gridLayout_2.addWidget(self.ScpLeRg, 3, 1, 1, 3)
        self.ScpbtnRg = QtWidgets.QPushButton(self.tb_scrap)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ScpbtnRg.sizePolicy().hasHeightForWidth())
        self.ScpbtnRg.setSizePolicy(sizePolicy)
        self.ScpbtnRg.setMinimumSize(QtCore.QSize(116, 34))
        self.ScpbtnRg.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.ScpbtnRg.setStyleSheet(".QPushButton:pressed {background-color: qlineargradient(spread:pad, x1:1, y1:0.551, x2:1, y2:0, stop:0 rgba(70, 73,75, 240), stop:1 rgba(50,180 , 255, 255));\n"
"    border-style: outset;\n"
"    border-width: 1px;\n"
"    border-radius: 10px;\n"
"    border-color: grey;\n"
"    font: bold 14px;\n"
"    color:yellow;\n"
"    min-width: 7em;\n"
"    padding: 6px;}\n"
".QPushButton { background-color: qlineargradient(spread:pad, x1:1, y1:0.551, x2:1, y2:0, stop:0 rgba(10, 13,15, 255), stop:1 rgba(20,80 , 180, 255));\n"
"    border-style: inset;\n"
"    border-width: 1px;\n"
"    border-radius: 10px;\n"
"    border-color: black;\n"
"    font: bold 14px;\n"
"    color:rgb(220,250,250);\n"
"    min-width: 6em;\n"
"    padding: 6px;}\n"
"")
        self.ScpbtnRg.setAutoDefault(True)
        self.ScpbtnRg.setDefault(False)
        self.ScpbtnRg.setFlat(False)
        self.ScpbtnRg.setObjectName("ScpbtnRg")
        self.gridLayout_2.addWidget(self.ScpbtnRg, 3, 4, 1, 1)
        self.ScpbtnAr = QtWidgets.QPushButton(self.tb_scrap)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ScpbtnAr.sizePolicy().hasHeightForWidth())
        self.ScpbtnAr.setSizePolicy(sizePolicy)
        self.ScpbtnAr.setMinimumSize(QtCore.QSize(116, 34))
        self.ScpbtnAr.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.ScpbtnAr.setStyleSheet(".QPushButton:pressed {background-color: qlineargradient(spread:pad, x1:1, y1:0.551, x2:1, y2:0, stop:0 rgba(70, 73,75, 240), stop:1 rgba(50,180 , 255, 255));\n"
"    border-style: outset;\n"
"    border-width: 1px;\n"
"    border-radius: 10px;\n"
"    border-color: grey;\n"
"    font: bold 14px;\n"
"    color:yellow;\n"
"    min-width: 7em;\n"
"    padding: 6px;}\n"
".QPushButton { background-color: qlineargradient(spread:pad, x1:1, y1:0.551, x2:1, y2:0, stop:0 rgba(10, 13,15, 255), stop:1 rgba(20,80 , 180, 255));\n"
"    border-style: inset;\n"
"    border-width: 1px;\n"
"    border-radius: 10px;\n"
"    border-color: black;\n"
"    font: bold 14px;\n"
"    color:rgb(220,250,250);\n"
"    min-width: 6em;\n"
"    padding: 6px;}\n"
"")
        self.ScpbtnAr.setAutoDefault(True)
        self.ScpbtnAr.setDefault(False)
        self.ScpbtnAr.setFlat(False)
        self.ScpbtnAr.setObjectName("ScpbtnAr")
        self.gridLayout_2.addWidget(self.ScpbtnAr, 5, 4, 1, 1)
        self.ScpLbDL = QtWidgets.QLabel(self.tb_scrap)
        self.ScpLbDL.setEnabled(True)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.ScpLbDL.setFont(font)
        self.ScpLbDL.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.ScpLbDL.setAlignment(QtCore.Qt.AlignCenter)
        self.ScpLbDL.setObjectName("ScpLbDL")
        self.gridLayout_2.addWidget(self.ScpLbDL, 2, 4, 1, 1)
        self.ScpLbURL = QtWidgets.QLabel(self.tb_scrap)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ScpLbURL.sizePolicy().hasHeightForWidth())
        self.ScpLbURL.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.ScpLbURL.setFont(font)
        self.ScpLbURL.setAlignment(QtCore.Qt.AlignCenter)
        self.ScpLbURL.setObjectName("ScpLbURL")
        self.gridLayout_2.addWidget(self.ScpLbURL, 2, 2, 1, 1)
        spacerItem15 = QtWidgets.QSpacerItem(17, 198, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem15, 7, 3, 1, 1)
        self.line_2 = QtWidgets.QFrame(self.tb_scrap)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.gridLayout_2.addWidget(self.line_2, 6, 1, 1, 4)
        spacerItem16 = QtWidgets.QSpacerItem(20, 5, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_2.addItem(spacerItem16, 0, 2, 1, 1)
        spacerItem17 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem17, 3, 5, 1, 1)
        self.tabWidget.addTab(self.tb_scrap, "")
        self.verticalLayout_2.addWidget(self.tabWidget)
        self.stackedWidget.addWidget(self.stk_new)
        self.horizontalLayout_2.addWidget(self.stackedWidget)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1350, 31))
        self.menubar.setStyleSheet(".QMenuBar{\n"
" border-style: none;\n"
"border-radius: 2px;\n"
" border-width: 1px;\n"
"\n"
"background-color: rgb(36, 36, 36);\n"
"border-color: yellow;\n"
"font: bold 18px;\n"
"color:rgb(255,255,255);\n"
"\n"
"\n"
"}\n"
"\n"
".QMenuBar:pressed{\n"
"background-color: rgb(36, 36, 36);\n"
"border-color: grey;\n"
"font: bold 14px;\n"
"color:rgb(0,0,0);\n"
"\n"
"}\n"
"\n"
" \n"
"   \n"
"    \n"
"   \n"
"    ")
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setStyleSheet(".QMenu{background-color: rgb(36, 36,36);\n"
"border-color: yellow;\n"
"color:rgb(240,240,240);\n"
"border-style: outset;\n"
"border-width: 1px;\n"
"border-radius: 10px;\n"
"    \n"
"font: bold 16px;\n"
"    \n"
"min-width: 7em;\n"
"padding: 2px;\n"
"}\n"
".QMenu:pressed{\n"
"background-color: rgb(36, 36,136);\n"
"\n"
"}")
        self.menuFile.setObjectName("menuFile")
        self.menuEdit = QtWidgets.QMenu(self.menubar)
        self.menuEdit.setStyleSheet(".QMenu{background-color: rgb(36, 36,36);\n"
"border-color: yellow;\n"
"color:rgb(240,240,240);\n"
"border-style: outset;\n"
"border-width: 1px;\n"
"border-radius: 10px;\n"
"    \n"
"font: bold 16px;\n"
"    \n"
"min-width: 7em;\n"
"padding: 2px;\n"
"}\n"
".QMenu:pressed{\n"
"background-color: rgb(36, 36,136);\n"
"\n"
"}")
        self.menuEdit.setObjectName("menuEdit")
        MainWindow.setMenuBar(self.menubar)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)
        self.toolBar = QtWidgets.QToolBar(MainWindow)
        self.toolBar.setAutoFillBackground(False)
        self.toolBar.setStyleSheet(".QToolBar{background-color: rgb(36, 36, 36);\n"
                                   "font: bold 18px;\n"
                                   "color:rgb(255,255,255);\n"
                                   "}")
        self.toolBar.setFloatable(True)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.actionScrap = QtWidgets.QAction(MainWindow)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("F:/VTUBroadSpec/bin/icon/Internet.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionScrap.setIcon(icon6)
        self.actionScrap.setObjectName("actionScrap")
        self.actionD_Settings = QtWidgets.QAction(MainWindow)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap("F:/VTUBroadSpec/bin/icon/Settings.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionD_Settings.setIcon(icon7)
        self.actionD_Settings.setObjectName("actionD_Settings")
        self.actionAbout = QtWidgets.QAction(MainWindow)
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap("F:/VTUBroadSpec/bin/icon/Help and support.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionAbout.setIcon(icon8)
        self.actionAbout.setObjectName("actionAbout")
        self.actionDocs = QtWidgets.QAction(MainWindow)
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap("F:/VTUBroadSpec/bin/icon/doc file.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionDocs.setIcon(icon9)
        self.actionDocs.setObjectName("actionDocs")
        self.actionAnalyse = QtWidgets.QAction(MainWindow)
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap("F:/VTUBroadSpec/bin/icon/bw-analysis.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionAnalyse.setIcon(icon10)
        self.actionAnalyse.setObjectName("actionAnalyse")
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.actionPref = QtWidgets.QAction(MainWindow)
        self.actionPref.setObjectName("actionPref")
        self.actionNew = QtWidgets.QAction(MainWindow)
        self.actionNew.setEnabled(True)
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap("F:/VTUBroadSpec/bin/icon/FolderGrey.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionNew.setIcon(icon11)
        self.actionNew.setVisible(True)
        self.actionNew.setIconVisibleInMenu(True)
        self.actionNew.setPriority(QtWidgets.QAction.NormalPriority)
        self.actionNew.setObjectName("actionNew")
        self.menuFile.addAction(self.actionNew)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionAnalyse)
        self.menuFile.addAction(self.actionScrap)
        self.menuFile.addSeparator()
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionExit)
        self.menuEdit.addAction(self.actionD_Settings)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.toolBar.addAction(self.actionNew)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionScrap)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionD_Settings)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(0)
        self.tabWidget.setCurrentIndex(3)
        self.EdbtnRst.clicked.connect(self.EdtblW.reset)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Student Result Report Generation"))
        self.btn_home.setToolTip(_translate("MainWindow", "Home"))
        self.btn_home.setStatusTip(_translate("MainWindow", "Home page of the application"))
        self.btn_home.setText(_translate("MainWindow", "Home"))
        self.btn_new.setToolTip(_translate("MainWindow", "New "))
        self.btn_new.setStatusTip(_translate("MainWindow", "create,edit,scrap the marks"))
        self.btn_new.setText(_translate("MainWindow", "New"))
        self.btn_analyse.setToolTip(_translate("MainWindow", "Analyse"))
        self.btn_analyse.setStatusTip(_translate("MainWindow", "analyse the data/marks"))
        self.btn_analyse.setText(_translate("MainWindow", "Analyse"))
        self.btn_setting.setToolTip(_translate("MainWindow", "Settings"))
        self.btn_setting.setStatusTip(_translate("MainWindow", "set the costume settings to default"))
        self.btn_setting.setText(_translate("MainWindow", "Settings"))
        self.stk_home.setStatusTip(_translate("MainWindow", "Home Page"))
        self.hmLbl.setText(_translate("MainWindow", "  Current link :"))
        self.hmbtn.setText(_translate("MainWindow", "Go!"))
        self.tabWidget.setStatusTip(_translate("MainWindow", "Cancels the current download"))
        self.pbtnRrm.setStatusTip(_translate("MainWindow", "Save the content to selected file ."))
        self.pbtnRrm.setText(_translate("MainWindow", "Remove Row"))
        self.lbRtable.setText(_translate("MainWindow", "Table:"))
        self.cbRtable.setStatusTip(_translate("MainWindow", "select subjects"))
        self.pbtnRset.setStatusTip(_translate("MainWindow", "Reset to orignal contents"))
        self.pbtnRset.setText(_translate("MainWindow", "Reset"))
        self.pbtnRsv.setStatusTip(_translate("MainWindow", "Save the content to selected file ."))
        self.pbtnRsv.setText(_translate("MainWindow", "Save"))
        self.pbtnRadd.setStatusTip(_translate("MainWindow", "Reset to orignal contents"))
        self.pbtnRadd.setText(_translate("MainWindow", "Add Row"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tb_root), _translate("MainWindow", "Root"))
        self.tb_Internal.setStatusTip(_translate("MainWindow", "Internal"))
        self.InChSave.setText(_translate("MainWindow", "Save as CSV"))
        self.InLbYear.setText(_translate("MainWindow", "  Year :"))
        self.InLbSU.setText(_translate("MainWindow", "Search by USN:"))
        self.InCbSub.setStatusTip(_translate("MainWindow", "select subjects"))
        self.InbtnRst.setStatusTip(_translate("MainWindow", "Reset to orignal contents"))
        self.InbtnRst.setText(_translate("MainWindow", "Reset"))
        self.InbtnAdd.setText(_translate("MainWindow", "Add"))
        item = self.IntblW.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "1"))
        item = self.IntblW.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "USN"))
        item = self.IntblW.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "First Test"))
        item = self.IntblW.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Second Test"))
        item = self.IntblW.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Third Test"))
        item = self.IntblW.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "min Average"))
        item = self.IntblW.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Scored"))
        __sortingEnabled = self.IntblW.isSortingEnabled()
        self.IntblW.setSortingEnabled(False)
        item = self.IntblW.item(0, 0)
        item.setText(_translate("MainWindow", "n"))
        self.IntblW.setSortingEnabled(__sortingEnabled)
        self.InbtnRm.setText(_translate("MainWindow", "Remove"))
        self.InbtnSave.setStatusTip(_translate("MainWindow", "Save the content to selected file ."))
        self.InbtnSave.setText(_translate("MainWindow", "Save"))
        self.InLbSub.setText(_translate("MainWindow", "Subject :"))
        self.InSbYear.setStatusTip(_translate("MainWindow", "select year"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tb_Internal), _translate("MainWindow", "Internal"))
        self.tb_edit.setStatusTip(_translate("MainWindow", "edit database file"))
        self.EdbtnSave.setStatusTip(_translate("MainWindow", "Save the content to selected file ."))
        self.EdbtnSave.setText(_translate("MainWindow", "Save"))
        self.EdbtnRst.setStatusTip(_translate("MainWindow", "Reset to orignal contents"))
        self.EdbtnRst.setText(_translate("MainWindow", "Reset"))
        self.EdLbSN.setText(_translate("MainWindow", "Search by Name:"))
        self.EdbtnLd.setToolTip(_translate("MainWindow", "load table"))
        self.EdbtnLd.setStatusTip(_translate("MainWindow", "load student table"))
        self.EdbtnLd.setText(_translate("MainWindow", "LOAD"))
        self.EdbtnLd.setShortcut(_translate("MainWindow", "Ctrl+L"))
        self.EdLbSU.setText(_translate("MainWindow", "By USN:"))
        item = self.EdtblW.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "USN"))
        item = self.EdtblW.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Name"))
        item = self.EdtblW.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Scheme"))
        item = self.EdtblW.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Department"))
        item = self.EdtblW.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Gender"))
        item = self.EdtblW.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "E-Mail"))
        item = self.EdtblW.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "Phone Number"))
        __sortingEnabled = self.EdtblW.isSortingEnabled()
        self.EdtblW.setSortingEnabled(False)
        item = self.EdtblW.item(0, 2)
        item.setText(_translate("MainWindow", "hh"))
        self.EdtblW.setSortingEnabled(__sortingEnabled)
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tb_edit), _translate("MainWindow", "Edit"))
        self.tb_scrap.setStatusTip(_translate("MainWindow", "get data from server"))
        self.ScpLeRV.setStatusTip(_translate("MainWindow", "Plz specify the current url for results"))
        self.ScpLeRV.setPlaceholderText(_translate("MainWindow", "http://results.vtu.ac.in/results17/result_page.php?usn="))
        self.ScpLeAr.setStatusTip(_translate("MainWindow", "Plz specify the current url for results"))
        self.ScpLeAr.setPlaceholderText(_translate("MainWindow", "http://results.vtu.ac.in/results17/result_page.php?usn="))
        self.ScpbtnRV.setStatusTip(_translate("MainWindow", "Starts Scraping"))
        self.ScpbtnRV.setText(_translate("MainWindow", "RV"))
        self.ScpLeRg.setStatusTip(_translate("MainWindow", "Plz specify the current url for results"))
        self.ScpLeRg.setPlaceholderText(_translate("MainWindow", "http://results.vtu.ac.in/results17/result_page.php?usn="))
        self.ScpbtnRg.setStatusTip(_translate("MainWindow", "Starts Scraping"))
        self.ScpbtnRg.setText(_translate("MainWindow", "Regular"))
        self.ScpbtnAr.setStatusTip(_translate("MainWindow", "Starts Scraping"))
        self.ScpbtnAr.setText(_translate("MainWindow", "Arrear"))
        self.ScpLbDL.setText(_translate("MainWindow", "Download"))
        self.ScpLbURL.setText(_translate("MainWindow", "Results URL"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tb_scrap), _translate("MainWindow", "Scrap"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuEdit.setTitle(_translate("MainWindow", "Edit"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))
        self.actionScrap.setText(_translate("MainWindow", "Scrap"))
        self.actionScrap.setStatusTip(_translate("MainWindow", "collect data from web / from vtu website"))
        self.actionScrap.setShortcut(_translate("MainWindow", "Ctrl+R"))
        self.actionD_Settings.setText(_translate("MainWindow", "Default Settings"))
        self.actionD_Settings.setStatusTip(_translate("MainWindow", "set the costume settings to default"))
        self.actionAbout.setText(_translate("MainWindow", "About"))
        self.actionAbout.setStatusTip(_translate("MainWindow", "about the developers"))
        self.actionAbout.setShortcut(_translate("MainWindow", "F2"))
        self.actionDocs.setText(_translate("MainWindow", "Docs"))
        self.actionDocs.setToolTip(_translate("MainWindow", "Documentation"))
        self.actionDocs.setStatusTip(_translate("MainWindow", "documentation for the application"))
        self.actionDocs.setShortcut(_translate("MainWindow", "F3"))
        self.actionAnalyse.setText(_translate("MainWindow", "Analyse"))
        self.actionAnalyse.setStatusTip(_translate("MainWindow", "analyse the data/marks"))
        self.actionAnalyse.setShortcut(_translate("MainWindow", "F5"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.actionExit.setStatusTip(_translate("MainWindow", "closes the appliction"))
        self.actionExit.setShortcut(_translate("MainWindow", "Ctrl+Q"))
        self.actionPref.setText(_translate("MainWindow", "Preferenceses"))
        self.actionPref.setStatusTip(_translate("MainWindow", "change the prefrencess"))
        self.actionNew.setText(_translate("MainWindow", "New"))
        self.actionNew.setToolTip(_translate("MainWindow", "for new database"))
        self.actionNew.setStatusTip(_translate("MainWindow", "create,edit,scrap the marks"))
        self.actionNew.setShortcut(_translate("MainWindow", "Ctrl+N"))

# from PyQt5 import QtWebKitWidgets

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

