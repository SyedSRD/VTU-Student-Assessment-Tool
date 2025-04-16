# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Setting_tab1.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(850, 500)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        Form.setMinimumSize(QtCore.QSize(850, 500))
        Form.setMaximumSize(QtCore.QSize(850, 500))
        Form.setStyleSheet(".QWidget{  \n"
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
        self.horizontalLayout = QtWidgets.QHBoxLayout(Form)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.tbSet = QtWidgets.QTabWidget(Form)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.tbSet.setFont(font)
        self.tbSet.setStyleSheet("QTabWidget::pane { /* The tab widget frame */\n"
"    border-top: 1px solid rgb(36,36,36);\n"
"}\n"
"\n"
"QTabWidget::tab-bar {\n"
"    left: 1px; /* move to the right by 5px */\n"
"}\n"
"\n"
"/* Style the tab using the tab sub-control. Note that\n"
"    it reads QTabBar _not_ QTabWidget */\n"
"QTabBar::tab {\n"
"     background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                stop: 0 #fafafa, stop: 0.4 #f4f4f4,\n"
"                                stop: 0.5 #e7e7e7, stop: 1.0 #fafafa);\n"
"    border: 2px solid #C4C4C3;\n"
"    border-bottom-color: #C2C7CB; /* same as the pane color */\n"
"    border-top-left-radius: 8px;\n"
"    border-top-right-radius: 8px;\n"
"    min-width: 20ex;\n"
"    padding: 2px;\n"
"}\n"
"")
        self.tbSet.setObjectName("tbSet")
        self.tab_New = QtWidgets.QWidget()
        self.tab_New.setStyleSheet("")
        self.tab_New.setObjectName("tab_New")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.tab_New)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        spacerItem = QtWidgets.QSpacerItem(20, 5, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_2.addItem(spacerItem, 6, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.tab_New)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 0, 1, 1, 1)
        self.gbCrt = QtWidgets.QGroupBox(self.tab_New)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.gbCrt.setFont(font)
        self.gbCrt.setObjectName("gbCrt")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.gbCrt)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.pbtnM = QtWidgets.QPushButton(self.gbCrt)
        self.pbtnM.setStyleSheet(".QPushButton {background-color: rgb(36,36,36);\n"
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
        self.pbtnM.setObjectName("pbtnM")
        self.gridLayout_3.addWidget(self.pbtnM, 0, 3, 1, 1)
        self.lbCSV = QtWidgets.QLabel(self.gbCrt)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.lbCSV.setFont(font)
        self.lbCSV.setObjectName("lbCSV")
        self.gridLayout_3.addWidget(self.lbCSV, 0, 0, 1, 1)
        self.leCsvM = QtWidgets.QLineEdit(self.gbCrt)
        self.leCsvM.setStyleSheet(".QLineEdit{ background-color: qlineargradient(spread:pad, x1:1, y1:0.551, x2:1, y2:0, stop:0 rgba(255, 255,255, 255), stop:1 rgba(255,255 , 255, 255));\n"
"    border-style: inset;\n"
"    border-width: 1px;\n"
"    border-radius: 10px;\n"
"    border-color: black;\n"
"    font: bold 14px;\n"
"    min-width: 2em;\n"
"    padding: 2px;}\n"
"")
        self.leCsvM.setObjectName("leCsvM")
        self.gridLayout_3.addWidget(self.leCsvM, 0, 2, 1, 1)
        self.chbM = QtWidgets.QCheckBox(self.gbCrt)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.chbM.setFont(font)
        self.chbM.setObjectName("chbM")
        self.gridLayout_3.addWidget(self.chbM, 4, 0, 1, 3)
        self.cbBrSetM = QtWidgets.QComboBox(self.gbCrt)
        self.cbBrSetM.setStyleSheet("background-color: rgb(36,36,36);\n"
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
        self.cbBrSetM.setObjectName("cbBrSetM")
        self.gridLayout_3.addWidget(self.cbBrSetM, 1, 2, 1, 1)
        self.label = QtWidgets.QLabel(self.gbCrt)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout_3.addWidget(self.label, 1, 0, 1, 1)
        self.gridLayout_2.addWidget(self.gbCrt, 2, 1, 1, 4)
        self.bbxM = QtWidgets.QDialogButtonBox(self.tab_New)
        self.bbxM.setStyleSheet(".QPushButton {background-color: rgb(36,36,36);\n"
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
        self.bbxM.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.bbxM.setObjectName("bbxM")
        self.gridLayout_2.addWidget(self.bbxM, 5, 2, 1, 1)
        self.gbSrp = QtWidgets.QGroupBox(self.tab_New)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.gbSrp.setFont(font)
        self.gbSrp.setObjectName("gbSrp")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.gbSrp)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.lburlSrpSN = QtWidgets.QLabel(self.gbSrp)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setKerning(True)
        self.lburlSrpSN.setFont(font)
        self.lburlSrpSN.setObjectName("lburlSrpSN")
        self.gridLayout_5.addWidget(self.lburlSrpSN, 0, 0, 1, 1)
        self.leSrpM = QtWidgets.QLineEdit(self.gbSrp)
        self.leSrpM.setStyleSheet(".QLineEdit{ background-color: qlineargradient(spread:pad, x1:1, y1:0.551, x2:1, y2:0, stop:0 rgba(255, 255,255, 255), stop:1 rgba(255,255 , 255, 255));\n"
"    border-style: inset;\n"
"    border-width: 1px;\n"
"    border-radius: 10px;\n"
"    border-color: black;\n"
"    font: bold 14px;\n"
"    min-width: 2em;\n"
"    padding: 2px;}\n"
"")
        self.leSrpM.setText("")
        self.leSrpM.setObjectName("leSrpM")
        self.gridLayout_5.addWidget(self.leSrpM, 0, 1, 1, 2)
        self.lbNSrpSN = QtWidgets.QLabel(self.gbSrp)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.lbNSrpSN.setFont(font)
        self.lbNSrpSN.setObjectName("lbNSrpSN")
        self.gridLayout_5.addWidget(self.lbNSrpSN, 1, 0, 1, 1)
        self.spSrpM = QtWidgets.QSpinBox(self.gbSrp)
        self.spSrpM.setStyleSheet("background-color: rgb(36,36,36);\n"
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
        self.spSrpM.setObjectName("spSrpM")
        self.gridLayout_5.addWidget(self.spSrpM, 1, 1, 1, 1)
        self.gridLayout_2.addWidget(self.gbSrp, 4, 1, 1, 4)
        self.leUrlM = QtWidgets.QLineEdit(self.tab_New)
        self.leUrlM.setStyleSheet(".QLineEdit{ background-color: qlineargradient(spread:pad, x1:1, y1:0.551, x2:1, y2:0, stop:0 rgba(255, 255,255, 255), stop:1 rgba(255,255 , 255, 255));\n"
"    border-style: inset;\n"
"    border-width: 1px;\n"
"    border-radius: 10px;\n"
"    border-color: black;\n"
"    font: bold 14px;\n"
"    min-width: 2em;\n"
"    padding: 2px;}\n"
"")
        self.leUrlM.setObjectName("leUrlM")
        self.gridLayout_2.addWidget(self.leUrlM, 0, 2, 1, 3)
        self.tbSet.addTab(self.tab_New, "")
        self.horizontalLayout.addWidget(self.tbSet)

        self.retranslateUi(Form)
        self.tbSet.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Setting"))
        self.label_2.setText(_translate("Form", "Home default URL:"))
        self.gbCrt.setTitle(_translate("Form", "Internal"))
        self.pbtnM.setText(_translate("Form", "Browes"))
        self.lbCSV.setText(_translate("Form", "CSV save path :"))
        self.chbM.setText(_translate("Form", "Allow save message display"))
        self.label.setText(_translate("Form", "Branch :"))
        self.gbSrp.setTitle(_translate("Form", "Scrap"))
        self.lburlSrpSN.setText(_translate("Form", "Default URL:"))
        self.lbNSrpSN.setText(_translate("Form", "Number of Students:"))
        self.tbSet.setTabText(self.tbSet.indexOf(self.tab_New), _translate("Form", "Main"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

