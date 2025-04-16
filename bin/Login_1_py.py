# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Login_3.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(726, 500)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        Form.setMinimumSize(QtCore.QSize(700, 500))
        Form.setMaximumSize(QtCore.QSize(726, 500))
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.stackedWidget = QtWidgets.QStackedWidget(Form)
        self.stackedWidget.setStyleSheet("background-image: url(\'C:\\\\Users\\\\SYED\\\\Downloads\\\\Backup-of-DefaultDesktop-small.jpg\');\n"
"background-repeat: no-repeat; \n"
"background-position: center;\n"
"")
        self.stackedWidget.setObjectName("stackedWidget")
        self.page_5 = QtWidgets.QWidget()
        self.page_5.setStyleSheet(".QFrame{\n"
"background-image: url(\'login.jpg\');\n"
"background-repeat: no-repeat; \n"
"background-position: center;\n"
"}\n"
"")
        self.page_5.setObjectName("page_5")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.page_5)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.frame = QtWidgets.QFrame(self.page_5)
        self.frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame.setObjectName("frame")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.frame)
        self.gridLayout_3.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.gridLayout_3.setContentsMargins(-1, 5, -1, 5)
        self.gridLayout_3.setHorizontalSpacing(0)
        self.gridLayout_3.setVerticalSpacing(2)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.cbRemember = QtWidgets.QCheckBox(self.frame)
        font = QtGui.QFont()
        font.setPointSize(7)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(True)
        font.setWeight(50)
        self.cbRemember.setFont(font)
        self.cbRemember.setObjectName("cbRemember")
        self.gridLayout_3.addWidget(self.cbRemember, 3, 1, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 80, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_3.addItem(spacerItem, 0, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(170, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem1, 1, 0, 1, 1)
        self.LgLeUName = QtWidgets.QLineEdit(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.LgLeUName.sizePolicy().hasHeightForWidth())
        self.LgLeUName.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.LgLeUName.setFont(font)
        self.LgLeUName.setMouseTracking(True)
        self.LgLeUName.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.LgLeUName.setStyleSheet(".QLineEdit{ background-color: qlineargradient(spread:pad, x1:1, y1:0.551, x2:1, y2:0, stop:0 rgba(25, 25,25, 25), stop:1 rgba(25, 80 , 180, 255));\n"
"    border-style: inset;\n"
"    border-width: 1px;\n"
"    border-radius: 10px;\n"
"    border-color: black;\n"
"    font: bold 14px;\n"
"    color:WHITE;\n"
"    min-width: 6em;\n"
"    padding: 6px;}\n"
"\n"
"")
        self.LgLeUName.setAlignment(QtCore.Qt.AlignCenter)
        self.LgLeUName.setPlaceholderText("USERNAME")
        self.LgLeUName.setObjectName("LgLeUName")
        self.gridLayout_3.addWidget(self.LgLeUName, 1, 1, 1, 1)
        self.LgLePass = QtWidgets.QLineEdit(self.frame)
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.LgLePass.setFont(font)
        self.LgLePass.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.LgLePass.setStyleSheet(".QLineEdit{ background-color: qlineargradient(spread:pad, x1:1, y1:0.551, x2:1, y2:0, stop:0 rgba(25, 25,25, 25), stop:1 rgba(25, 80 , 180, 255));\n"
"    border-style: inset;\n"
"    border-width: 1px;\n"
"    border-radius: 10px;\n"
"    border-color: black;\n"
"    font: bold 14px;\n"
"    color:WHITE;\n"
"    min-width: 6em;\n"
"    padding: 6px;}\n"
"")
        self.LgLePass.setEchoMode(QtWidgets.QLineEdit.Password)
        self.LgLePass.setAlignment(QtCore.Qt.AlignCenter)
        self.LgLePass.setObjectName("LgLePass")
        self.gridLayout_3.addWidget(self.LgLePass, 2, 1, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(180, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem2, 1, 2, 1, 1)
        self.line = QtWidgets.QFrame(self.frame)
        self.line.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line.setLineWidth(1)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setObjectName("line")
        self.gridLayout_3.addWidget(self.line, 4, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color:rgb(14, 100, 250)")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout_3.addWidget(self.label_2, 0, 1, 1, 1)
        self.LgLbLog = QtWidgets.QLabel(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.LgLbLog.sizePolicy().hasHeightForWidth())
        self.LgLbLog.setSizePolicy(sizePolicy)
        self.LgLbLog.setMinimumSize(QtCore.QSize(300, 0))
        self.LgLbLog.setText("")
        self.LgLbLog.setAlignment(QtCore.Qt.AlignCenter)
        self.LgLbLog.setObjectName("LgLbLog")
        self.gridLayout_3.addWidget(self.LgLbLog, 7, 1, 1, 1)
        self.LgbtnLog = QtWidgets.QPushButton(self.frame)
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.LgbtnLog.setFont(font)
        self.LgbtnLog.setStyleSheet(".QPushButton { background-color: qlineargradient(spread:pad, x1:1, y1:0.551, x2:1, y2:0, stop:0 rgba(25, 25,25, 100), stop:1 rgba(25, 80 , 180, 255));\n"
"    \n"
"    border-style: outset;\n"
"    border-width: 1px;\n"
"    border-radius: 9px;\n"
"    border-color: black;\n"
"    font: bold 14px;\n"
"    min-width: 10em;\n"
"    padding: 6px;\n"
"    margin:4px\n"
"    \n"
"}\n"
".QPushButton:pressed {background-color: qlineargradient(spread:pad, x1:1, y1:0.551, x2:1, y2:0, stop:0 rgba(25, 25,125, 200), stop:1 rgba(25, 80 , 80, 155));\n"
"    border-style: inset;\n"
"    border-width: 1px;\n"
"    border-radius: 9px;\n"
"    border-color: black;\n"
"    font: bold 14px;\n"
"    \n"
"    color: rgb(255, 255, 255);\n"
"    min-width: 6em;\n"
"    padding: 6px;}\n"
"\n"
".QPushButton:hover {color: rgb(255, 255, 255);}\n"
"\n"
"")
        self.LgbtnLog.setObjectName("LgbtnLog")
        self.gridLayout_3.addWidget(self.LgbtnLog, 6, 1, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(20, 60, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_3.addItem(spacerItem3, 8, 1, 1, 1)
        self.LgbtnCreat = QtWidgets.QPushButton(self.frame)
        font = QtGui.QFont()
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(True)
        font.setWeight(50)
        self.LgbtnCreat.setFont(font)
        self.LgbtnCreat.setStyleSheet(".QPushButton:pressed {  \n"
"    background-color: Transparent;\n"
"    border:none;\n"
"    font: bold ;\n"
"    color:blue;\n"
"    }\n"
".QPushButton:hover {  \n"
"   color:blue;\n"
"    }\n"
"")
        self.LgbtnCreat.setAutoDefault(False)
        self.LgbtnCreat.setDefault(False)
        self.LgbtnCreat.setFlat(True)
        self.LgbtnCreat.setObjectName("LgbtnCreat")
        self.gridLayout_3.addWidget(self.LgbtnCreat, 8, 2, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_3.addItem(spacerItem4, 5, 1, 1, 1)
        self.gridLayout_2.addWidget(self.frame, 1, 0, 1, 1)
        self.stackedWidget.addWidget(self.page_5)
        self.page_6 = QtWidgets.QWidget()
        self.page_6.setStyleSheet(".QFrame{background-image: url(\'login.jpg\');\n"
"background-repeat: no-repeat; \n"
"background-position: center;}\n"
"")
        self.page_6.setObjectName("page_6")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.page_6)
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_4.setSpacing(0)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.frame_2 = QtWidgets.QFrame(self.page_6)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.frame_2)
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_5.setSpacing(0)
        self.gridLayout_5.setObjectName("gridLayout_5")
        spacerItem5 = QtWidgets.QSpacerItem(20, 80, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_5.addItem(spacerItem5, 0, 1, 1, 1)
        spacerItem6 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_5.addItem(spacerItem6, 10, 5, 1, 1)
        spacerItem7 = QtWidgets.QSpacerItem(60, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_5.addItem(spacerItem7, 1, 0, 1, 1)
        self.LgLbCon = QtWidgets.QLabel(self.frame_2)
        self.LgLbCon.setText("")
        self.LgLbCon.setAlignment(QtCore.Qt.AlignCenter)
        self.LgLbCon.setObjectName("LgLbCon")
        self.gridLayout_5.addWidget(self.LgLbCon, 10, 1, 1, 2)
        self.LgbtnBack = QtWidgets.QPushButton(self.frame_2)
        self.LgbtnBack.setMinimumSize(QtCore.QSize(192, 0))
        self.LgbtnBack.setStyleSheet(".QPushButton { background-color: qlineargradient(spread:pad, x1:1, y1:0.551, x2:1, y2:0, stop:0 rgba(25, 25,25, 100), stop:1 rgba(25, 80 , 180, 255));\n"
"    \n"
"    border-style: outset;\n"
"    border-width: 1px;\n"
"    border-radius: 9px;\n"
"    border-color: black;\n"
"    font: bold 14px;\n"
"    min-width: 10em;\n"
"    padding: 6px;\n"
"    margin:4px\n"
"    \n"
"}\n"
".QPushButton:pressed {background-color: qlineargradient(spread:pad, x1:1, y1:0.551, x2:1, y2:0, stop:0 rgba(25, 25,125, 200), stop:1 rgba(25, 80 , 80, 155));\n"
"    border-style: inset;\n"
"    border-width: 1px;\n"
"    border-radius: 9px;\n"
"    border-color: black;\n"
"    font: bold 14px;\n"
"    \n"
"    color: rgb(255, 255, 255);\n"
"    min-width: 6em;\n"
"    padding: 6px;}\n"
"\n"
".QPushButton:hover {color: rgb(255, 255, 255);}\n"
"\n"
"")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("F:/down/back_2-512.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.LgbtnBack.setIcon(icon)
        self.LgbtnBack.setIconSize(QtCore.QSize(24, 20))
        self.LgbtnBack.setObjectName("LgbtnBack")
        self.gridLayout_5.addWidget(self.LgbtnBack, 10, 3, 1, 1)
        self.LgLeRPass = QtWidgets.QLineEdit(self.frame_2)
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.LgLeRPass.setFont(font)
        self.LgLeRPass.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.LgLeRPass.setStyleSheet(".QLineEdit{ background-color: qlineargradient(spread:pad, x1:1, y1:0.551, x2:1, y2:0, stop:0 rgba(25, 25,25, 25), stop:1 rgba(25, 80 , 180, 255));\n"
"    border-style: inset;\n"
"    border-width: 1px;\n"
"    border-radius: 10px;\n"
"    border-color: black;\n"
"    font: bold 14px;\n"
"    color:WHITE;\n"
"    min-width: 6em;\n"
"    padding: 6px;}\n"
"\n"
"")
        self.LgLeRPass.setText("")
        self.LgLeRPass.setEchoMode(QtWidgets.QLineEdit.Password)
        self.LgLeRPass.setAlignment(QtCore.Qt.AlignCenter)
        self.LgLeRPass.setObjectName("LgLeRPass")
        self.gridLayout_5.addWidget(self.LgLeRPass, 5, 1, 1, 2)
        self.LgbtnCreatC = QtWidgets.QPushButton(self.frame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.LgbtnCreatC.sizePolicy().hasHeightForWidth())
        self.LgbtnCreatC.setSizePolicy(sizePolicy)
        self.LgbtnCreatC.setMinimumSize(QtCore.QSize(192, 0))
        self.LgbtnCreatC.setStyleSheet(".QPushButton { background-color: qlineargradient(spread:pad, x1:1, y1:0.551, x2:1, y2:0, stop:0 rgba(25, 25,25, 100), stop:1 rgba(25, 80 , 180, 255));\n"
"    \n"
"    border-style: outset;\n"
"    border-width: 1px;\n"
"    border-radius: 9px;\n"
"    border-color: black;\n"
"    font: bold 14px;\n"
"    min-width: 10em;\n"
"    padding: 6px;\n"
"    margin:4px\n"
"    \n"
"}\n"
".QPushButton:pressed {background-color: qlineargradient(spread:pad, x1:1, y1:0.551, x2:1, y2:0, stop:0 rgba(25, 25,125, 200), stop:1 rgba(25, 80 , 80, 155));\n"
"    border-style: inset;\n"
"    border-width: 1px;\n"
"    border-radius: 9px;\n"
"    border-color: black;\n"
"    font: bold 14px;\n"
"    \n"
"    color: rgb(255, 255, 255);\n"
"    min-width: 6em;\n"
"    padding: 6px;}\n"
"\n"
".QPushButton:hover {color: rgb(255, 255, 255);}\n"
"\n"
"")
        self.LgbtnCreatC.setObjectName("LgbtnCreatC")
        self.gridLayout_5.addWidget(self.LgbtnCreatC, 10, 4, 1, 1)
        self.LgLeFName = QtWidgets.QLineEdit(self.frame_2)
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.LgLeFName.setFont(font)
        self.LgLeFName.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.LgLeFName.setStyleSheet(".QLineEdit{ background-color: qlineargradient(spread:pad, x1:1, y1:0.551, x2:1, y2:0, stop:0 rgba(25, 25,25, 25), stop:1 rgba(25, 80 , 180, 255));\n"
"    border-style: inset;\n"
"    border-width: 1px;\n"
"    border-radius: 10px;\n"
"    border-color: black;\n"
"    font: bold 14px;\n"
"    color:WHITE;\n"
"    min-width: 6em;\n"
"    padding: 6px;}\n"
"\n"
"")
        self.LgLeFName.setText("")
        self.LgLeFName.setAlignment(QtCore.Qt.AlignCenter)
        self.LgLeFName.setObjectName("LgLeFName")
        self.gridLayout_5.addWidget(self.LgLeFName, 1, 1, 1, 3)
        self.LgLePassC = QtWidgets.QLineEdit(self.frame_2)
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.LgLePassC.setFont(font)
        self.LgLePassC.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.LgLePassC.setStyleSheet(".QLineEdit{ background-color: qlineargradient(spread:pad, x1:1, y1:0.551, x2:1, y2:0, stop:0 rgba(25, 25,25, 25), stop:1 rgba(25, 80 , 180, 255));\n"
"    border-style: inset;\n"
"    border-width: 1px;\n"
"    border-radius: 10px;\n"
"    border-color: black;\n"
"    font: bold 14px;\n"
"    color:WHITE;\n"
"    min-width: 6em;\n"
"    padding: 6px;}\n"
"\n"
"")
        self.LgLePassC.setText("")
        self.LgLePassC.setEchoMode(QtWidgets.QLineEdit.Password)
        self.LgLePassC.setAlignment(QtCore.Qt.AlignCenter)
        self.LgLePassC.setObjectName("LgLePassC")
        self.gridLayout_5.addWidget(self.LgLePassC, 4, 1, 1, 2)
        self.LgLeEmail = QtWidgets.QLineEdit(self.frame_2)
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.LgLeEmail.setFont(font)
        self.LgLeEmail.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.LgLeEmail.setStyleSheet(".QLineEdit{ background-color: qlineargradient(spread:pad, x1:1, y1:0.551, x2:1, y2:0, stop:0 rgba(25, 25,25, 25), stop:1 rgba(25, 80 , 180, 255));\n"
"    border-style: inset;\n"
"    border-width: 1px;\n"
"    border-radius: 10px;\n"
"    border-color: black;\n"
"    font: bold 14px;\n"
"    color:WHITE;\n"
"    min-width: 6em;\n"
"    padding: 6px;}\n"
"\n"
"")
        self.LgLeEmail.setText("")
        self.LgLeEmail.setAlignment(QtCore.Qt.AlignCenter)
        self.LgLeEmail.setObjectName("LgLeEmail")
        self.gridLayout_5.addWidget(self.LgLeEmail, 6, 1, 1, 3)
        self.LgLeLName = QtWidgets.QLineEdit(self.frame_2)
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.LgLeLName.setFont(font)
        self.LgLeLName.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.LgLeLName.setStyleSheet(".QLineEdit{ background-color: qlineargradient(spread:pad, x1:1, y1:0.551, x2:1, y2:0, stop:0 rgba(25, 25,25, 25), stop:1 rgba(25, 80 , 180, 255));\n"
"    border-style: inset;\n"
"    border-width: 1px;\n"
"    border-radius: 10px;\n"
"    border-color: black;\n"
"    font: bold 14px;\n"
"    color:WHITE;\n"
"    min-width: 6em;\n"
"    padding: 6px;}\n"
"\n"
"")
        self.LgLeLName.setText("")
        self.LgLeLName.setAlignment(QtCore.Qt.AlignCenter)
        self.LgLeLName.setObjectName("LgLeLName")
        self.gridLayout_5.addWidget(self.LgLeLName, 2, 1, 1, 3)
        self.LgLeUNameC = QtWidgets.QLineEdit(self.frame_2)
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.LgLeUNameC.setFont(font)
        self.LgLeUNameC.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.LgLeUNameC.setStyleSheet(".QLineEdit{ background-color: qlineargradient(spread:pad, x1:1, y1:0.551, x2:1, y2:0, stop:0 rgba(25, 25,25, 25), stop:1 rgba(25, 80 , 180, 255));\n"
"    border-style: inset;\n"
"    border-width: 1px;\n"
"    border-radius: 10px;\n"
"    border-color: black;\n"
"    font: bold 14px;\n"
"    color:WHITE;\n"
"    min-width: 6em;\n"
"    padding: 6px;}\n"
"\n"
"")
        self.LgLeUNameC.setText("")
        self.LgLeUNameC.setAlignment(QtCore.Qt.AlignCenter)
        self.LgLeUNameC.setObjectName("LgLeUNameC")
        self.gridLayout_5.addWidget(self.LgLeUNameC, 3, 1, 1, 2)
        spacerItem8 = QtWidgets.QSpacerItem(20, 50, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_5.addItem(spacerItem8, 9, 1, 1, 1)
        self.label = QtWidgets.QLabel(self.frame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMinimumSize(QtCore.QSize(0, 40))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setStyleSheet("color:rgb(14, 118, 250)")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout_5.addWidget(self.label, 0, 3, 1, 1)
        self.gridLayout_4.addWidget(self.frame_2, 0, 0, 1, 1)
        self.stackedWidget.addWidget(self.page_6)
        self.gridLayout.addWidget(self.stackedWidget, 0, 0, 1, 1)

        self.retranslateUi(Form)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Login"))
        self.cbRemember.setText(_translate("Form", "remember me"))
        self.LgLePass.setPlaceholderText(_translate("Form", "PASSWORD"))
        self.label_2.setText(_translate("Form", "Login User"))
        self.LgbtnLog.setText(_translate("Form", "LOGIN"))
        self.LgbtnCreat.setText(_translate("Form", "Create account"))
        self.LgbtnBack.setText(_translate("Form", "Back"))
        self.LgLeRPass.setPlaceholderText(_translate("Form", "RE ENTER PASSWORD"))
        self.LgbtnCreatC.setText(_translate("Form", "CREATE"))
        self.LgLeFName.setPlaceholderText(_translate("Form", "FIRSTNAME"))
        self.LgLePassC.setPlaceholderText(_translate("Form", "PASSWORD"))
        self.LgLeEmail.setPlaceholderText(_translate("Form", "EMAIL"))
        self.LgLeLName.setPlaceholderText(_translate("Form", "LASTNAME"))
        self.LgLeUNameC.setPlaceholderText(_translate("Form", "USERNAME"))
        self.label.setText(_translate("Form", "Create User"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

