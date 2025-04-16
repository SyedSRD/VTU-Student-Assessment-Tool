# -*- coding: utf-8 -*-
"""
Created on Sun Apr  8 09:27:08 2018

@author: SYED
"""

import home_test_10_py
import Login_1_py


from PyQt5 import QtCore, QtWidgets
#import MWindowF

import validators # for url vALIDATING
import network_parsing,dbCreat,Setting_tab1_py,analyze_2_py
import threading
import sys,csv,os
import sqlite3 #DATABASE
#import pandas as pd 
import matplotlib # GRAPH
import matplotlib.style as stl 
import matplotlib.pyplot as plt

matplotlib.use("Qt5Agg")
from PyQt5.QtWidgets import QSizePolicy
import numpy as np
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

s=os.getcwd()

#matplotlib.style.use('default')
stl.use('bmh')
#print(stl.available)

class Log(QtWidgets.QWidget,Login_1_py.Ui_Form):
    
    def __init__(self,parent=None):
        super(Log,self).__init__(parent)
        self.setWindowModality(QtCore.Qt.ApplicationModal)
        self.setupUi(self)
        
        self.dbname="studb7.db"    
        
        self.LgbtnLog.clicked.connect(self.logUser)
        self.LgbtnCreat.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(1))
        self.LgbtnCreatC.clicked.connect(self.creatUser)
        self.LgbtnBack.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(0))
        
        
    def creatUser(self):
        try:
            
            self.fname=self.LgLeFName.text()
            self.lname=self.LgLeLName.text() 
            self.uname=self.LgLeUNameC.text()
            self.upass=self.LgLePassC.text()
            self.urpass=self.LgLeRPass.text()
            self.phnum=self.LgLeEmail.text()
            if self.uname=='' or self.fname=='' or self.lname=='':
                self.LgLbCon.setStyleSheet("QLabel { color :red;font: bold 20px; }")
                self.LgLbCon.setText("Invalid Name")
            elif self.phnum=='':
                self.LgLbCon.setStyleSheet("QLabel { color :red;font: bold 20px; }")
                self.LgLbCon.setText("Invalid Number")
                
            elif self.upass=="" or self.upass!=self.urpass :
                self.LgLbCon.setStyleSheet("QLabel { color :red;font: bold 20px; }")
                self.LgLbCon.setText("Password doesn't match")
                
            else:
                k=dbCreat.newUser(self.dbname,self.uname,self.upass,self.fname,self.lname,self.phnum)
                if k:
                    self.LgLbCon.setStyleSheet("QLabel { color :red;font: bold 20px; }")
                    self.LgLbCon.setText("Name taken")
                else:   
                    self.LgLbCon.setStyleSheet("QLabel { color :green;font: italic 25px; }")
                    
                    QtCore.QTimer.singleShot(5000,1,lambda : self.stackedWidget.setCurrentIndex(0) )
                    self.LgLbCon.setText("User created")
                    
                    
                    
        except Exception as e:
            print(e)
    def logUser(self):
        try:
            self.uname=self.LgLeUName.text()
            self.upass=self.LgLePass.text()
            print(self.uname,self.upass)
            res=dbCreat.login(self.dbname,self.uname,self.upass)
            if res:
                
                self.form1=mainD6(self.uname)
                self.form1.show()
                
                self.close()
                
            else:
                self.LgLbLog.setStyleSheet("QLabel { color :red;font: bold 18px; }")
                self.LgLbLog.setText("Username and Password is invalid")
        except Exception as e:
            print(e)
        #
    
    def closeEvent(self,event):
        if self.closeFlag1==False or self.closeFlag2==False:
            quit_msg = "Are you sure you want to exit the Setting Window"
            reply = QtWidgets.QMessageBox.question(self, 'Message', 
                             quit_msg, QtWidgets.QMessageBox.Yes, QtWidgets.QMessageBox.No)
        
            if reply == QtWidgets.QMessageBox.Yes:
                event.accept()
            else:
                event.ignore()
        else:
            self.close()

def slp():
    for i in range(10000000):
        i=i+i*i
    print(i)   
    
    
    
#####################################################################################
#####################################################################################
#####################################################################################
#####################################################################################



class Set(QtWidgets.QWidget,Setting_tab1_py.Ui_Form):
    def __init__(self,parent=None):
        super(Set,self).__init__(parent)
        s=os.getcwd()
        self.closeFlag1=False
        self.dbn=os.path.join(s,'studb7.db')
        con=sqlite3.connect(self.dbn)
        c=con.cursor()
        self.setWindowModality(QtCore.Qt.ApplicationModal)
        self.setupUi(self)
        
        self.bbxM.button(QtWidgets.QDialogButtonBox.Cancel).setText("Close")
        try:
            
            
            self._curBranch=''.join(c.execute("SELECT value FROM setting WHERE name='branch';").fetchone())
#            self._curScheme=''.join(c.execute("SELECT value FROM setting WHERE name='scheme';").fetchone())
#            self._DBSavePath=''.join(c.execute("SELECT value FROM setting WHERE name='dbsavepath';").fetchone())
            self._defaultHmPgURL=''.join(c.execute("SELECT value FROM setting WHERE name='homeurl';").fetchone())
            self._csvPath=''.join(c.execute("SELECT value FROM setting WHERE name='csvpath';").fetchone())
#            self._searchPath=''.join(c.execute("SELECT value FROM setting WHERE name='searchpath';").fetchone())
            self._saveMsgCrt=''.join(c.execute("SELECT value FROM setting WHERE name='savemsgcrt';").fetchone())
#            self._saveMsgEdt=''.join(c.execute("SELECT value FROM setting WHERE name='savemsgedt';").fetchone())
            self._defaultScrpURL=''.join(c.execute("SELECT value FROM setting WHERE name='scrapurl';").fetchone())
            self._stuCnt=''.join(c.execute("SELECT value FROM setting WHERE name='studentcount';").fetchone())
            
            #print(self._DBSavePath)
            
        except Exception as e:
            print (e)
            pass
        
#################################################################################
        # Main Setting tab Signals
        self.pbtnM.clicked.connect(self.fnBrw)
#        schm=['2010','2014','2015','2016','2017']
#        self.cbScmSetM.addItems(schm)
        b=[]
        brn=[]
        b=c.execute("SELECT dtitle FROM department;").fetchall()

        for x in b:
            brn.append(x[0])
        print(brn)

        self.cbBrSetM.addItems(brn)
        self.bbxM.accepted.connect(self.saveMainSet)
        self.bbxM.rejected.connect(self.close)
        self._curBranchText=self.cbBrSetM.itemText(int(self._curBranch))

#################################################################################
        self.cbBrSetM.setCurrentIndex(int(self._curBranch))
        
        
        self.leUrlM.setText(self._defaultHmPgURL)
        self.chbM.setChecked(bool(int(self._saveMsgCrt)))
        
        self.leCsvM.setText(self._csvPath)
        
        self.leSrpM.setText(self._defaultScrpURL)
        self.spSrpM.setValue(int(self._stuCnt))
        
        c.close()
        con.close()
        
#################################################################################
#################################################################################
    
            
    def closeEvent(self,event):
        if self.closeFlag1==False:
            quit_msg = "Are you sure you want to exit the Setting Window"
            reply = QtWidgets.QMessageBox.question(self, 'Message', 
                             quit_msg, QtWidgets.QMessageBox.Yes, QtWidgets.QMessageBox.No)
        
            if reply == QtWidgets.QMessageBox.Yes:
                event.accept()
            else:
                event.ignore()
        else:
            self.close()
        self.closeFlag1=False
         
        
        
    def saveMainSet(self):
        try:
            self.closeFlag1=True
            self._defaultHmPgURL=self.leUrlM.text()
            self._curBranch=str(self.cbBrSetM.currentIndex())
#            self._curScheme=str(self.cbScmSetM.currentIndex())
#            self._DBSavePath=self.leDPSetM.text()
            self._curBranchText=self.cbBrSetM.currentText()
            self._csvPath=self.leCsvM.text()
            #self._searchPath=self.leEdtSN.text()
            self._defaultScrpURL=self.leSrpM.text()
              
            self._stuCnt=self.spSrpM.text()
            
            if self.chbM.checkState()== QtCore.Qt.Checked:
                self._saveMsgCrt='1'
            else:
                self._saveMsgCrt='0'
                
            con=sqlite3.connect(self.dbn)
            c=con.cursor()
            qry1="UPDATE setting SET value="+self._curBranch+" WHERE name='branch' ;"
#            qry2="UPDATE setting SET value="+self._curScheme+" WHERE name='scheme' ;"
#            qry3="UPDATE setting SET value='"+self._DBSavePath+"' WHERE name='dbsavepath' ;"
            qry2="UPDATE setting SET value='"+self._defaultHmPgURL+"' WHERE name='homeurl' ;"
            qry3="UPDATE setting SET value='"+self._csvPath+"' WHERE name='csvpath' ;"
#            qry2="UPDATE setting SET value='"+self._searchPath+"' WHERE name='searchpath' ;"
            qry4="UPDATE setting SET value="+self._saveMsgCrt+" WHERE name='savemsgcrt' ;"
#            qry4="UPDATE setting SET value="+self._saveMsgEdt+" WHERE name='savemsgedt' ;"
            qry5="UPDATE setting SET value='"+self._defaultScrpURL+"' WHERE name='scrapurl' ;"
            qry6="UPDATE setting SET value="+self._stuCnt+" WHERE name='studentcount' ;"
            
            c.execute(qry1)
            c.execute(qry2)
            c.execute(qry3)
            c.execute(qry4)
            c.execute(qry5)
            c.execute(qry6)
            
            
            con.commit()
            c.close()
            con.close()
        except Exception as e:
            print (e)
            
        
        QtWidgets.QMessageBox.about(self, "DONE", "The settings are saved")
        
        
        
    def fnBrw(self):
        savePath = str(QtWidgets.QFileDialog.getExistingDirectory(self,"save Path"))
        self.leCsvM.setText(savePath)
    
    
        
        
#####################################################################################
#####################################################################################
#####################################################################################
#####################################################################################



class mainD6(QtWidgets.QMainWindow,home_test_10_py.Ui_MainWindow):
    def __init__(self,uname,parent=None):
        try:
            super(mainD6,self).__init__(parent)
            self.setupUi(self)
            self.setAttribute(QtCore.Qt.WA_DeleteOnClose)
            
            self.form3=Set()
            self.form4=Analyze()
            
            
            self.__fname='studb7.db'
            self.__uname=uname
            conn= sqlite3.connect(self.__fname)
            c=conn.cursor()
            try:
                
                
                
                qry="SELECT priv FROM user WHERE username='"+self.__uname+"';"
                c.execute(qry)
                r=c.fetchall()
                r=int((r[0])[0])
                print(r)
                  
            except Exception as e:
                 print("155\t",e)
            if r==2:
                self.tb_edit.deleteLater()
                self.tb_root.deleteLater()
                self.tb_scrap.deleteLater()
                self.btn_setting.setDisabled(True)
            if r==1:
                self.tb_root.deleteLater()
                
                     # signal for toolbuttons 
            self.btn_home.clicked.connect(self.fnbtnHome)
            
            self.btn_new.clicked.connect(lambda :self.fnbtnNew(0))
            self.btn_setting.clicked.connect(self.fnSettingWindow)
            self.btn_analyse.clicked.connect(self.fnAnalyzeWindow)
            
            #signal for menuitems
            self.actionNew.triggered.connect(self.fnbtnNew)
            self.actionScrap.triggered.connect(lambda: self.fnbtnNew(1))
            
            self.actionExit.triggered.connect(self.close)
            self.actionD_Settings.triggered.connect(self.fnSettingWindow)
            self.actionAnalyse.triggered.connect(self.fnAnalyzeWindow)
            #signal from home 
            self.hmLE.setPlaceholderText(self.form3._defaultHmPgURL)
            
            self.hmWeb.load(QtCore.QUrl(self.form3._defaultHmPgURL)) 
            self.hmWeb.show()
            
            
            self.hmbtn.clicked.connect(self.webPageLoad)
            self.hmWeb.urlChanged.connect(self.webPagedr)
            
            
            #signal from Internal tab 
            
            self.InbtnAdd.setShortcut("Ctrl+1")
            self.InbtnAdd.setToolTip("Add..Ctrl+1")
            self.InbtnAdd.clicked.connect(self.fnInAdd)
            self.InbtnRm.setShortcut("Ctrl+2")
            self.InbtnRm.setToolTip("Remove..Ctrl+2")
            self.InbtnRm.clicked.connect(self.fnInRm)
            
            
            self.InbtnRst.setShortcut("Ctrl+1")
            self.InbtnRst.setToolTip("Reset..Ctrl+r")
            self.InbtnRst.clicked.connect(self.fnLoadSub)
            
            self.InbtnSave.setShortcut("Ctrl+s")
            self.InbtnSave.setToolTip("Save..Ctrl+s")
            self.InbtnSave.clicked.connect(self.fnInSave)
            
            a=[]
            subn=[]
            a=c.execute("SELECT subtitle FROM subject;").fetchall()
    
            for x in a:
                subn.append(x[0])
            print(subn)
            
            self.InCbSub.setMaxVisibleItems(7)
            self.InCbSub.addItems(subn)
            self.InLeSU.textChanged.connect(self.fnInLoadby)
            self.InCbSub.currentIndexChanged.connect(self.fnLoadSub)
            c.close()
            conn.close()


            #signal from edit tab 
            
           
            self.EdbtnSave.setShortcut("Ctrl+s")
            self.EdbtnSave.setToolTip("Save..Ctrl+s")
            self.EdbtnSave.clicked.connect(self.fnSave)

            self.EdbtnRst.clicked.connect(self.fnLoadSt)
            self.EdbtnLd.clicked.connect(self.fnLoadSt)
            self.EdLeSN.textChanged.connect(lambda :self.fnLoadby(0))
            self.EdLeSU.textChanged.connect(lambda :self.fnLoadby(1))
            
            
            #signal from Scrap tab
            
            
            self.ScpbtnRg.clicked.connect(self.fnDownloadRg)
            self.ScpbtnRV.clicked.connect(self.fnDownloadRV)
            self.ScpbtnAr.clicked.connect(self.fnDownloadAr)
            
            self.ScpLeRg.setText(self.form3._defaultScrpURL)
            self.ScpLeRV.setText(self.form3._defaultScrpURL)
            self.ScpLeAr.setText(self.form3._defaultScrpURL)
#            
#            Signals for root
            
            try:
                conn= sqlite3.connect(self.__fname)
                c=conn.cursor()
                y=c.execute("SELECT name FROM sqlite_master WHERE type='table';").fetchall()
                subNames=[]
                for x in y:
                    subNames=subNames+list(x)
                print(subNames)
                
                self.cbRtable.addItems(subNames)
                self.cbRtable.currentIndexChanged.connect(self.fnLoadTbl)
                c.close()
                conn.close()
            except Exception as e:
                 print(e)
            self.pbtnRadd.setShortcut("Ctrl+1")
            self.pbtnRadd.setToolTip("Add..Ctrl+1")
            self.pbtnRadd.clicked.connect(self.fnRAdd)
            self.pbtnRrm.setShortcut("Ctrl+2")
            self.pbtnRrm.setToolTip("Remove..Ctrl+2")
            self.pbtnRrm.clicked.connect(self.fnRRm)
            
            self.pbtnRsv.setShortcut("Ctrl+s")
            self.pbtnRsv.setToolTip("Save..Ctrl+s")
            self.pbtnRsv.clicked.connect(self.fnRSave)

            self.pbtnRset.clicked.connect(self.fnLoadTbl)

            
        except Exception as e:
            print (e)
            
        
#################################################################################
#################################################################################


    
        # slots for toolbtn and menu items
    def fnbtnHome(self):
        print("hiii")
        self.btn_home.setChecked(True)
        self.stackedWidget.setCurrentIndex(0)
        self.btn_new.setChecked(False)
        
    def fnbtnNew(self,a=0):
        self.btn_new.setChecked(True)
        self.stackedWidget.setCurrentIndex(1)
        self.tabWidget.setCurrentIndex(1)
        self.btn_home.setChecked(False)
        self.InSbYear.setFocus()
        if a==1:
            self.tabWidget.setCurrentIndex(3)
            self.ScpLeRg.setFocus()
            
    def fnbtnConv(self):
        self.btn_home.setChecked(False)
        self.stackedWidget.setCurrentIndex(2)
        self.btn_new.setChecked(False)
    def fnSettingWindow(self):
        try:
            self.form3.show()
        except Exception as e:
            print (e)
        
    
    def fnAnalyzeWindow(self):
        try:
            self.form4.show()
        except Exception as e:
            print (e)
        
         
        
    def closeEvent(self,event):

        quit_msg = "Are you sure you want to exit the program?"
        reply = QtWidgets.QMessageBox.question(self, 'Message', 
                         quit_msg, QtWidgets.QMessageBox.Yes, QtWidgets.QMessageBox.No)
    
        if reply == QtWidgets.QMessageBox.Yes:
            event.accept()
            
        else:
            event.ignore()
        
#################################################################################
    # slots for home

    def webPageLoad(self):
        url =self.hmLE.text()
        if url:
            self.hmWeb.load(QtCore.QUrl(url))
            self.hmWeb.show()
            
        else:
            QtWidgets.QMessageBox.about(self, "ERROR", "The link field is empty plz specify a valid url")
            
    def webPagedr(self):
        url1=self.hmWeb.url()
        self.hmLE.setText(url1.toString())
        
#################################################################################
#################################################################################


#   slot for root
    def fnRAdd(self):
        rowPosition = self.tblWR.rowCount()
        
        self.tblWR.insertRow(rowPosition)
    def fnRRm(self):
        selected = self.tblWR.currentRow()
        
        self.tblWR.removeRow(selected)
        
        
    def fnLoadTbl(self):
        
        
        try:
            conn= sqlite3.connect(self.__fname)
            c=conn.cursor()
            tbl=self.cbRtable.currentText()
            qry="SELECT * FROM '"+tbl+"';"
            result=c.execute(qry)
            self.loadDataR(result)
            
            c.close()
            conn.close()
            
        except Exception as e:
            print(e)
        
    def loadDataR(self,result):
        try:
            col=[0]
            self.tblWR.setRowCount(0)
            self.tblWR.setColumnCount(1)
            
            for row_number,row_data in enumerate(result):
#                print(row_number)
                
                self.tblWR.insertRow(row_number)
                for col_num,data in enumerate(row_data):
                    item=QtWidgets.QTableWidgetItem(str(data))
                    print(col_num,col,"\n")
                    if col_num not in col:
                        col.append(col_num)
                        self.tblWR.insertColumn(col_num)
                    self.tblWR.setItem(row_number,col_num,item)
             
                    
        except Exception as e:
            print(e)
    
    def fnRSave(self):  
        
        save_msg = "Are you sure you want to save the data?"
        reply = QtWidgets.QMessageBox.question(self, 'Message', 
                         save_msg, QtWidgets.QMessageBox.Yes, QtWidgets.QMessageBox.No)
    
        if  reply == QtWidgets.QMessageBox.Yes:
            
            
            tbl=self.cbRtable.currentText()
            print(tbl)

            
            row_count = self.tblWR.rowCount()
            col_count = self.tblWR.columnCount()
            
         
            conn= sqlite3.connect(self.__fname)
            c=conn.cursor()
          
                
            try:
                
                rd=[]
                for row in range(row_count):
                    rowdata= self.collectDatafmTable(row,self.tblWR)
                    print(rowdata)
                    
                    rd.append(tuple(rowdata))
                rd=tuple(rd,)
                print(rd)
                
                s=col_count*",?"
                print(s)
                dl="DELETE FROM '"+tbl+"';"
                c.execute(dl)
                inq="INSERT OR REPLACE INTO '"+tbl+"' VALUES("+s[1:]+");"
                
                c.executemany(inq, rd)
                conn.commit()
                c.close()
                conn.close()
                
            except Exception as e:
                print(e)
                
#################################################################################
#   Slot fo internal
        
    def fnInAdd(self):
        rowPosition = self.IntblW.rowCount()
        
        self.IntblW.insertRow(rowPosition)
    def fnInRm(self):
        selected = self.IntblW.currentRow()
        
        self.IntblW.removeRow(selected)
        
    def fnLoadSub(self):
        try:
            
            conn= sqlite3.connect(self.__fname)
            c=conn.cursor()
            sub=self.InCbSub.currentText()
            c.execute("SELECT subcode FROM subject where subtitle='"+sub+"';")
            scode=c.fetchone()
            
            qry="SELECT * FROM internal WHERE subcode='"+scode[0]+"' ;"
            print(qry)
            result=c.execute(qry)
            self.loadDataIn(result)
            
            
            c.close()
            conn.close()
            
        except Exception as e:
            print(e)
    def fnInLoadby(self):
        try:
            conn= sqlite3.connect(self.__fname)
            c=conn.cursor()
            sub=self.InCbSub.currentText()
            c.execute("SELECT subcode FROM subject where subtitle='"+sub+"';")
            scode=c.fetchone()
            
            strnm=self.InLeSU.text()
            strnm="'%"+strnm+"%'"
            qry="SELECT * FROM internal WHERE iUSN like "+strnm+" AND subcode='"+scode[0]+"';"
            print(qry)
            result=c.execute(qry)
            self.loadDataIn(result)
        except Exception as e:
            print(e)
        c.close()
        conn.close()
        
    def loadDataIn(self,result):
        self.IntblW.setRowCount(0)
        for row_number,row_data in enumerate(result):
            self.IntblW.insertRow(row_number)
            for col_num,data in enumerate(row_data):
                item=QtWidgets.QTableWidgetItem(str(data))
                if col_num!=6:
                    self.IntblW.setItem(row_number,col_num,item)
                
    def fnInSave(self):  
        
        save_msg = "Are you sure you want to save the data?"
        reply = QtWidgets.QMessageBox.question(self, 'Message', 
                         save_msg, QtWidgets.QMessageBox.Yes, QtWidgets.QMessageBox.No)
    
        if  reply == QtWidgets.QMessageBox.Yes:
            
            year=self.InSbYear.value()
            
            sub=self.InCbSub.currentText()
            print(sub)

            
            row_count = self.IntblW.rowCount()
            col_count = self.IntblW.columnCount()
            
         
            conn= sqlite3.connect(self.__fname)
            c=conn.cursor()
          
                
            try:
                c.execute("SELECT subcode FROM subject where subtitle='"+sub+"';")
                scode=c.fetchone()
                rd=[]
                for row in range(row_count):
                    rowdata= self.collectDatafmTable(row,self.IntblW)
                    print(rowdata)

                    rd.append(tuple(rowdata)+scode)
                rd=tuple(rd,)
                print(rd)
                inq="INSERT OR REPLACE INTO internal VALUES(?, ?, ?, ?, ?, ?, ?)"
                
                c.executemany(inq, rd)
                conn.commit()
                c.close()
                conn.close()
                
            except Exception as e:
                print(e)
        
            try:  
                if self.InChSave.isChecked() is True:
    #                self.form1._DBSavePath="E:\\VTUBroadSpec\\bin"
    #                self.form1._curBranchText.split(",")[0]
                    dbs=os.path.join("E:\\VTUBroadSpec\\bin","Internal")
                    os.makedirs(dbs, exist_ok=True)
                    os.chdir(dbs)
                    ys=os.path.join(dbs,str(year))
                    os.makedirs(ys,exist_ok=True)
                    os.chdir(ys)
    #                ss=os.path.join(ys,str(sem))
    #                os.makedirs(ss,exist_ok=True)
    #                os.chdir(ss)
                    
                    
                    path = QtWidgets.QFileDialog.getSaveFileName(self, 'Save File',self.form3._csvPath, 'CSV(*.csv)')
                    #print(type(path[0]),path)
                    
                    if path[0] != '':
                            
                            with open(path[0],'w') as stream:
                                
                                writer = csv.writer(stream,quoting=csv.QUOTE_MINIMAL)
                                
                                # write headers
                                csv_row = []
                                for col in range(col_count):
                                    csv_row.append(self.IntblW.horizontalHeaderItem(col).text())
                     
                                writer.writerow(csv_row)
                                print('yeah header')
                                
                                #write data
                                
                                for row in range(row_count):
                                    rowdata= self.collectDatafmTable(row,self.IntblW)
                                    
                                    writer.writerow(rowdata)
                                    
                                
            except Exception as e:
                    print(e)
#################################################################################
#################################################################################

    
    #Slot for Edit tab 
    
    def fnLoadby(self,a):
        try:
            conn= sqlite3.connect(self.__fname)
            c=conn.cursor()
            
            if a== 0:
                strnm=self.EdLeSN.text()
                strnm="'%"+strnm+"%'"
                qry="SELECT * FROM student WHERE name like "+strnm+";"
            else:
                strnm=self.EdLeSU.text()
                strnm="'%"+strnm+"%'"
                qry="SELECT * FROM student WHERE USN like "+strnm+";"
            print(qry)
            result=c.execute(qry)
            self.loadData(result)
        except Exception as e:
            print(e)
        c.close()
        conn.close()
    
    def fnLoadSt(self):
        
        
        qry="SELECT * FROM student;"
        
        try:
            conn= sqlite3.connect(self.__fname)
            c=conn.cursor()
            result=c.execute(qry)
            self.loadData(result)
            
            c.close()
            conn.close()
            
        except Exception as e:
            print(e)
        
    def loadData(self,result):
        self.EdtblW.setRowCount(0)
        for row_number,row_data in enumerate(result):
            self.EdtblW.insertRow(row_number)
            for col_num,data in enumerate(row_data):
                item=QtWidgets.QTableWidgetItem(str(data))
                if col_num==3:
                    item.setFlags(QtCore.Qt.ItemIsEnabled)
                self.EdtblW.setItem(row_number,col_num,item)
    
        
        
    def fnSave(self):
        
        save_msg = "Are you sure you want to save the data?"
        reply = QtWidgets.QMessageBox.question(self, 'Message', 
                         save_msg, QtWidgets.QMessageBox.Yes, QtWidgets.QMessageBox.No)
        
        if reply == QtWidgets.QMessageBox.Yes:
        
                try:
                    
                    con= sqlite3.connect(self.__fname)
                        
                    c=con.cursor()
                    rd=[]
                    for row in range(self.EdtblW.rowCount()):
                         rowdata= self.collectDatafmTable(row,self.EdtblW)
                         rd.append(tuple(rowdata))
                    rd=tuple(rd)
                    inq="INSERT OR REPLACE INTO student VALUES(?, ?, ?, ?, ?, ? ,?)"
                    c.executemany(inq, rd)
                    con.commit()
                    c.close()
                    con.close()
                        
                       
                except Exception as e:
                    print(e)
        else:
                QtWidgets.QMessageBox.about(self, "ERROR", "No file/database is chosen")
#################################################################################

    def collectDatafmTable(self,row,tw):
        
        rowdata = []
        for column in range(tw.columnCount()):
            item = tw.item(row, column)
            
            if item is not None:
                rowdata.append(str(item.text()))
            else:
                rowdata.append('')
        
        return rowdata   
        
#################################################################################
#################################################################################


#            slot for scrap

    def fnDownloadRg(self):
#        url=self.ScpLeRg.text()
        #k=re.match('^[1-4]\w{2}\d{2}\w{2,3}\d{2}$',usn)
        try:
            url1=self.ScpLeRg.text()
            if url1 is '' or not validators.url(url1):
                QtWidgets.QMessageBox.about(self, "ERROR", "please insert a valid URL")
                
            else:
                
                try:
                    self.ScpLeRg.setDisabled(True)
                    self.ScpLeAr.setDisabled(True)
                    self.ScpLeRV.setDisabled(True)
                    self.ScpbtnRg.setDisabled(True)
                    self.ScpbtnAr.setDisabled(True)
                    self.ScpbtnRV.setDisabled(True)
                    t=threading.Thread(target=self.thread1,args=(self.__fname,url1))
                   
                    t.start()
                    
                    
                except Exception as e:
                    print(e)
                    
                    pass
        
                        
        except Exception as e:
                print(e)
                
                
    def fnDownloadRV(self):
        try:
            url1=self.ScpLeRV.text()
            if url1 is '' or not validators.url(url1):
                QtWidgets.QMessageBox.about(self, "ERROR", "please insert a valid URL")
                
            else:
                
                try:
                    k=[]
                    con= sqlite3.connect(self.__fname)
                    c=con.cursor()
                    qry="SELECT mUSN FROM marks WHERE result='F';"
                    c.execute(qry)
                    res=c.fetchall()
                    for i in res:
                        k.append(i[0])
                    print("syed",k)
#                    with open("USN_RV.txt",'w')as f:
#                        f.write(str(k))
#                        f.close()
                    if k:
                        spamWriter = csv.writer(open('USN_RV.csv', 'w'), delimiter=',',quotechar='|', quoting=csv.QUOTE_MINIMAL)    
                        spamWriter.writerow(k)
                        
                        
    #                    with open('USN_RV.csv', 'r') as f:
    #                      reader = csv.reader(f,delimiter=',')
    #                      lt = list(reader)
    #                    print((lt[0:-1]))
                        
                        
                        self.ScpLeRg.setDisabled(True)
                        self.ScpLeAr.setDisabled(True)
                        self.ScpLeRV.setDisabled(True)
                        self.ScpbtnRg.setDisabled(True)
                        self.ScpbtnAr.setDisabled(True)
                        self.ScpbtnRV.setDisabled(True)
                        
                        
                        t=threading.Thread(target=self.thread1,args=(self.__fname,url1,k))
                       
                        t.start()
                    c.close()
                    con.close()
                    
                except Exception as e:
                    print(e)
                    
                    pass
        
        except Exception as e:
                print(e)
                
    def fnDownloadAr(self):
#        url=self.ScpLeRg.text()
        #k=re.match('^[1-4]\w{2}\d{2}\w{2,3}\d{2}$',usn)
        try:
            url1=self.ScpLeAr.text()
            if url1 is '' or not validators.url(url1):
                QtWidgets.QMessageBox.about(self, "ERROR", "please insert a valid URL")
                
            else:
                
                try:
                    s=[]
                    con= sqlite3.connect(self.__fname)
                    c=con.cursor()
                    qry="SELECT musn,sem FROM marks as m,subject as s WHERE m.msubcode=s.subcode AND m.result='F';"
                    c.execute(qry)
                    res=c.fetchall()
                    for x in res:
                        s=s+list(x)
                    print(s)
                    if s:
                        spamWriter = csv.writer(open('USN_Ar.csv', 'w'), delimiter=',',quotechar='|', quoting=csv.QUOTE_MINIMAL)    
                        spamWriter.writerow(s)
                    
                
                    
                    
                    
                        self.ScpLeRg.setDisabled(True)
                        self.ScpLeAr.setDisabled(True)
                        self.ScpLeRV.setDisabled(True)
                        self.ScpbtnRg.setDisabled(True)
                        self.ScpbtnAr.setDisabled(True)
                        self.ScpbtnRV.setDisabled(True)
                        
                        
                        t=threading.Thread(target=self.thread1,args=(self.__fname,url1,s))
                       
                        t.start()
                    
                    
                    c.close()
                    con.close()
                except Exception as e:
                    print(e)
                    
                    pass
        
                        
        except Exception as e:
                print(e)
                
    
    def thread1(self,fname,url1,ulst=None):
            
        
        #ct=int(self.form1._stuCnt)
        try:
            network_parsing.webScraping(self.__fname,urlc=url1,ulst=ulst,noStu=str(self.form3._stuCnt))
            
            
        except Exception as e:
            
            QtWidgets.QMessageBox.about(self, "ERROR", "\n  please contact Syed")        
        
        self.ScpLeRg.setEnabled(True)
        self.ScpLeAr.setEnabled(True)
        self.ScpLeRV.setEnabled(True)
        self.ScpbtnRg.setEnabled(True)
        self.ScpbtnAr.setEnabled(True)
        self.ScpbtnRV.setEnabled(True)
        
        
        
#################################################################################
#################################################################################
#################################################################################
#################################################################################

class MyMplCanvas(FigureCanvas):
    """Ultimately, this is a QWidget (as well as a FigureCanvasAgg, etc.)."""
    def __init__(self, parent=None, width=5, height=3, dpi=100):
        self.fig = Figure(figsize=(width, height), dpi=dpi)
        
        self.axes = self.fig.add_subplot(111)
        # We want the axes cleared every time plot() is called
        

        FigureCanvas.__init__(self, self.fig)
        self.setParent(parent)

        FigureCanvas.setSizePolicy(self,
                QSizePolicy.Expanding,
                QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)

#################################################################################
#################################################################################
class Analyze(QtWidgets.QWidget,analyze_2_py.Ui_Form):
    def __init__(self,parent=None):
        super(Analyze,self).__init__(parent)
        self.setWindowModality(QtCore.Qt.ApplicationModal)
        self.setupUi(self)
        
        
        self.__fname=os.path.join(s,'studb7.db')
#        self.leAnaName.textChanged.connect(lambda :self.fnLoadby(0))
        
        listm=['All','Total above 100','Total 100 to 70','Total 70 to 50','Total below 50','External below 35','internal below 15','Fail']
        self.cbSelTA.addItems(listm)
        self.cbSelTA.currentIndexChanged.connect(self.fnLoadSelect)
        
        self.sc = MyMplCanvas(self.tb2Grp, width=5, height=4, dpi=100)
        self.gridLayout_4.addWidget(self.sc,0, 0, 1,6)
        
        self.sc2 = MyMplCanvas(self.tb2Grp, width=5, height=4, dpi=100)
        self.gridLayout_4.addWidget(self.sc2,0, 6, 1,1)
        
        listmp=['Total','External','Internal']
        self.cbSelGA.addItems(listmp)
        self.cbSelGA.currentIndexChanged.connect(self.fnLoadSelect2)
        
        if self.rbSubA.isChecked() is True:
            self.tabAnalyz.removeTab(3)
            self.fnChangeSub()
            self.fnPopupBaseAna()
            self.leUSNA.textChanged.connect(lambda :self.fnLoadby(1,0))
        self.leUSNA.textChanged.connect(lambda :self.fnLoadby(1,1))
            
        self.rbCRA.toggled.connect(self.fndisableWid)
        self.rbSubA.toggled.connect(self.fndisableWid)
        
        self.spSemA.valueChanged.connect(self.fnChangeSub)
        self.spSemA.valueChanged.connect(self.fnChangeClass)
        self.cbSubA.currentIndexChanged.connect(self.fnPopupBaseAna)
        
    def fndisableWid(self):
                
        if self.rbCRA.isChecked() is True:
            self.cbSubA.setDisabled(True)
            self.cbSelTA.setDisabled(True)
            self.spYrA.setDisabled(False)
            self.spSemA.setDisabled(False)
            self.tabAnalyz.removeTab(0)
            self.tabAnalyz.removeTab(1)
            self.tabAnalyz.removeTab(2)
            self.tabAnalyz.addTab(self.tab,'Descriptions')
            self.tabAnalyz.addTab(self.tb1Tbl,'Table')
            self.fnChangeClass()
            self.fnPopupBaseAna1()

        else:
            self.spYrA.setDisabled(False)
            self.spSemA.setDisabled(False)
            self.cbSubA.setDisabled(False)
            self.tb1Tbl.setDisabled(False)
            self.tabAnalyz.removeTab(0)
            
            self.tabAnalyz.addTab(self.tb1Tbl,'Table')
            self.tabAnalyz.addTab(self.tb2Grp,'Graph')
            self.tabAnalyz.addTab(self.tab3Desc,'Description')

            
            self.fnChangeSub()
            
    def fnChangeClass(self):
        
        
        
        con=sqlite3.connect(self.__fname)
        c=con.cursor()
        x=self.spSemA.value()
        y=self.spYrA.value()
        
        self.replaceContentClass(c,x)
        
        c.close()
        con.close()
         
        
    def replaceContentClass(self,c,x):
        try:
            
            x=str(x)
            
            qry2="SELECT count(*) FROM marks m ,subject ss WHERE msubcode=subcode AND ss.sem=5 GROUP BY subcode"
            res=c.execute(qry2).fetchone()[0]
            k=res
            self.crl.setText(str(k))
            
            qry2="SELECT name,max(mks) FROM (SELECT name,sum(m.total)as mks FROM student s,marks m ,subject ss WHERE USN=mUSN AND msubcode=subcode AND ss.sem="+x+" GROUP BY mUSN )"
            res=c.execute(qry2).fetchone()[0]
            self.crl_1.setText(str(res))
            
            
            qry2="SELECT count(mks) FROM (SELECT sum(m.total)as mks FROM student s,marks m ,subject ss WHERE USN=mUSN AND msubcode=subcode AND ss.sem="+x+" GROUP BY mUSN ) WHERE mks>630"
            res=c.execute(qry2).fetchone()[0]
            self.crl_2.setText(str(res))
            
            
            qry2="SELECT count(mks) FROM (SELECT sum(m.total)as mks FROM student s,marks m ,subject ss WHERE USN=mUSN AND msubcode=subcode AND ss.sem="+x+" GROUP BY mUSN ) WHERE mks>540"
            res=c.execute(qry2).fetchone()[0]
            self.crl_3.setText(str(res))
            
            
            qry2="SELECT count(mks) FROM (SELECT sum(m.total)as mks FROM student s,marks m ,subject ss WHERE USN=mUSN AND msubcode=subcode AND ss.sem="+x+" GROUP BY mUSN ) WHERE mks>315"
            res=c.execute(qry2).fetchone()[0]
            self.crl_4.setText(str(res))
            
            qry2="SELECT count(mUSN) FROM marks m ,subject ss WHERE msubcode=subcode AND ss.sem="+x+" AND m.result= 'F' GROUP BY subcode"
            res=c.execute(qry2).fetchone()[0]
            s=res
            self.crl_5.setText(str(s))
            
            
            self.crl_6.setText(str(k-s))
            
            
            self.totalStu=int(self.crl.text())
            pasStu=int(self.crl_6.text())
            self.percent=(pasStu/self.totalStu)*100
            
            self.crl_7.setText(str(self.percent)+"%")
            
        except Exception as e:
            print(e)
            
    def fnChangeSub(self):
        
        skk=[]
        
        con=sqlite3.connect(self.__fname)
        c=con.cursor()
        x=self.spSemA.value()
        y=self.spYrA.value()
        
        
        print(x,type(x),y)
        c.execute("SELECT subtitle FROM subject WHERE sem="+str(x)+";")
        res=c.fetchall()
        print(res)
        
        for x in res:
           skk.append(x[0])
        print(skk)
        self.cbSubA.clear()
        self.cbSubA.addItems(skk)
        c.close()
        con.close()
        
        
        
        
    def fnLoadSelect(self):
        conn= sqlite3.connect(self.__fname)
        c=conn.cursor()
        k=self.cbSelTA.currentIndex()
        strt=self.cbSubA.currentText()
        strt="'"+strt+"'"
        try:
            if k==1:
                qry1="SELECT * FROM marks m , subject s WHERE s.subtitle="+str(strt)+" AND s.subcode=m.msubcode AND m.total >= 100 ;"
                
            elif k==2:
                qry1="SELECT * FROM marks m , subject s WHERE s.subtitle="+str(strt)+" AND s.subcode=m.msubcode AND m.total <= 100 AND m.total>=70 ;"
            elif k==3:
                qry1="SELECT * FROM marks m , subject s WHERE s.subtitle="+str(strt)+" AND s.subcode=m.msubcode AND m.total <= 70 AND m.total>=50 ;"
            elif k==4:
                qry1="SELECT * FROM marks m , subject s WHERE s.subtitle="+str(strt)+" AND s.subcode=m.msubcode AND m.total <= 50 ;"
            elif k==5:
                qry1="SELECT * FROM marks m , subject s WHERE s.subtitle="+str(strt)+" AND s.subcode=m.msubcode AND m.external <= 35 ;"
            elif k==6:
                qry1="SELECT * FROM marks m , subject s WHERE s.subtitle="+str(strt)+" AND s.subcode=m.msubcode AND m.internal <= 15 ;"
            elif k==7:
                qry1="SELECT * FROM marks m , subject s WHERE s.subtitle="+str(strt)+" AND s.subcode=m.msubcode AND m.result = 'F' ;"
            else:
                qry1="SELECT * FROM marks m , subject s WHERE s.subtitle="+str(strt)+" AND s.subcode=m.msubcode ;"
                
                
            result=c.execute(qry1)
            
            self.loadDataAna(result)
            
        except Exception as e:
            print(e)
        c.close()
        conn.close()    
            
    def fnLoadby(self,a,b):
        try:
            conn= sqlite3.connect(self.__fname)
            c=conn.cursor()
            strt=self.cbSubA.currentText()
            strt="'"+strt+"'"
            
            strnm=self.leUSNA.text()
            strnm="'%"+strnm+"%'"
            if b==0:
                
                qry="SELECT * FROM marks m , subject s WHERE s.subtitle="+str(strt)+" AND s.subcode=m.msubcode AND mUSN like "+strnm+";"
            else:
                strt1=self.spSemA.value()
                strt1="'"+str(strt1)+"'"
                qry="SELECT * FROM marks m , subject s WHERE s.subcode=m.msubcode AND s.sem="+strt1+" AND mUSN like "+strnm+";"
            print(qry)
            result=c.execute(qry)
            self.loadDataAna(result)
        except Exception as e:
            print(e)
        c.close()
        conn.close()
        
    def fnPopupBaseAna1(self):
        
        strt=self.spSemA.value()
        strt="'"+str(strt)+"'"
        print(strt)
        
        qry="SELECT * FROM marks m,subject s WHERE s.subcode=m.msubcode AND s.sem="+strt+"; "
        print(qry)
        try:
            
            conn= sqlite3.connect(self.__fname)
            c=conn.cursor()
            result=c.execute(qry)
            self.loadDataAna(result)
            self.replaceContentClass(c,strt)
            c.close()
            conn.close()
            
        except Exception as e:
            print(e)
    def fnPopupBaseAna(self):
        
        strt=self.cbSubA.currentText()
        strt="'"+strt+"'"
        print(strt)
        qry="SELECT * FROM marks m , subject s WHERE s.subtitle="+str(strt)+" AND s.subcode=m.msubcode ;"
        print(qry)
        try:
            
            conn= sqlite3.connect(self.__fname)
            c=conn.cursor()
            result=c.execute(qry)
            self.loadDataAna(result)
            self.replaceContent(c,strt)
            c.close()
            conn.close()
            
        except Exception as e:
            print(e)
            
    def loadDataAna(self,result):
        self.tblAna.setRowCount(0)
        for row_number,row_data in enumerate(result):
            self.tblAna.insertRow(row_number)
            for col_num,data in enumerate(row_data):
                self.tblAna.setItem(row_number,col_num,QtWidgets.QTableWidgetItem(str(data))) 
           
                
    
            
    def replaceContent(self,c,strt):
        try:
            self.cbSelTA.setCurrentIndex(0)
            self.cbSelGA.setCurrentIndex(0)
            
            qry2="SELECT COUNT() FROM marks m , subject s WHERE s.subtitle="+str(strt)+" AND s.subcode=m.msubcode ;"
            res=c.execute(qry2).fetchone()[0]
            self.lbTlStuCnt.setText(str(res))
            
            
            qry2="SELECT COUNT() FROM marks m , subject s WHERE s.subtitle="+str(strt)+" AND s.subcode=m.msubcode AND m.result = 'P' ;"
            res=c.execute(qry2).fetchone()[0]
            self.lbTlPass.setText(str(res))
            
            
            qry2="SELECT COUNT() FROM marks m , subject s WHERE s.subtitle="+str(strt)+" AND s.subcode=m.msubcode AND result = 'F' ;"
            res=c.execute(qry2).fetchone()[0]
            self.lbTlFail.setText(str(res))
            
            
            qry2="SELECT COUNT() FROM marks m , subject s WHERE s.subtitle="+str(strt)+" AND s.subcode=m.msubcode AND result = 'A' ;"
            res=c.execute(qry2).fetchone()[0]
            self.lbTlAbsent.setText(str(res))
            
            qry2="SELECT MAX(total) FROM marks m , subject s WHERE s.subtitle="+str(strt)+" AND s.subcode=m.msubcode ;"
            res=c.execute(qry2).fetchone()[0]
            self.lbHScore.setText(str(res))
            
            qry2="SELECT MIN(total) FROM marks m , subject s WHERE s.subtitle="+str(strt)+" AND s.subcode=m.msubcode ;"
            res=c.execute(qry2).fetchone()[0]
            self.lbLScore.setText(str(res))
            
            qry2="SELECT AVG(total) FROM marks m , subject s WHERE s.subtitle="+str(strt)+" AND s.subcode=m.msubcode ;"
            res=c.execute(qry2).fetchone()[0]
            self.lbTlAverage.setText(str(res)+"%")
            
            self.totalStu=int(self.lbTlStuCnt.text())
            pasStu=int(self.lbTlPass.text())
            self.percent=(pasStu/self.totalStu)*100
            
            self.lbTlPassPer.setText(str(self.percent)+"%")
        
            qry2="SELECT st.name FROM student st,marks m, subject s WHERE s.subtitle="+str(strt)+" AND s.subcode=m.msubcode AND st.USN=m.mUSN ;"
            res=c.execute(qry2).fetchall()
            
            self.__x1=[x[0] for x in res]
            
            
            
            qry2="SELECT total FROM marks m , subject s WHERE s.subtitle="+str(strt)+" AND s.subcode=m.msubcode ;"
            res=c.execute(qry2).fetchall()
            
            self.__y1=[x[0] for x in res]
            
            qry2="SELECT external FROM marks m , subject s WHERE s.subtitle="+str(strt)+" AND s.subcode=m.msubcode ;"
            res=c.execute(qry2).fetchall()
            
            self.__y2=[x[0] for x in res]
            
            qry2="SELECT internal FROM marks m , subject s WHERE s.subtitle="+str(strt)+" AND s.subcode=m.msubcode ;"
            res=c.execute(qry2).fetchall()
            self.__y3=[x[0] for x in res]
            x1=np.arange(0,125,10)
            self.plotHist(x1,self.__y1,50,"Total")
            self.plotPie(self.__x1,self.__y1,50,"Total")
        except Exception as e:
            print(e)
            
            
    def fncls(self):
        plt.close()
    def fnLoadSelect2(self):
        k=self.cbSelGA.currentIndex()
        if k==1:
            x1=np.arange(0,100,10)
            self.plotHist(x1,self.__y2,35,"External")
            self.plotPie(self.__x1,self.__y2,35,"External")
        elif k==2:
            x1=np.arange(0,40,5)
            self.plotHist(x1,self.__y3,15,"Internal")
            self.plotPie(self.__x1,self.__y3,15,"Internal")
        else:
            x1=np.arange(0,125,10)
            self.plotHist(x1,self.__y1,50,"Total")
            self.plotPie(self.__x1,self.__y1,50,"Total")
        
         
    def plotHist(self,x,y,l,tl):
            
            try:
               
                self.gridLayout_4.removeWidget(self.sc)
                self.sc.deleteLater()
                del self.sc
                self.sc = MyMplCanvas(self.tb2Grp, width=5, height=4, dpi=80)
                self.gridLayout_4.addWidget(self.sc,0, 0, 1, 6)
            
#                x1=np.arange(0,125,10)
                self.sc.axes.set_xlabel('Marks',fontsize=20,color="red")
                self.sc.axes.set_ylabel('Frequency',fontsize=20,color="red")
                self.sc.axes.set_title(tl,fontsize=30,color="k")
                self.sc.axes.hist(y,x,histtype='bar',rwidth=0.8)
                y1=np.array(y)
                self.sc.axes.axvline(y1.mean(), color='k', linestyle='dashed', linewidth=1)
                
                pos=[0.05,0.12,0.9,0.82]
                self.sc.axes.set_position(pos, which='both')
               
                
            except Exception as e:
                print(e)
                
    def plotPie(self,x,y,l,tl):
        
            try:
                self.gridLayout_4.removeWidget(self.sc2)
                self.sc2.deleteLater()
                del self.sc2
                self.sc2 = MyMplCanvas(self.tb2Grp, width=5, height=4, dpi=100)
                self.gridLayout_4.addWidget(self.sc2,0, 6, 1, 1)
            
                k=sum(i>l for i in y )
                passPer=(k/self.totalStu)*100
                slices=[passPer,abs(passPer-100)]
                self.sc2.axes.pie(slices,labels=['Pass','Fail'],colors=['g','r'],startangle=90,shadow=True,autopct='%1.1f%%',explode=(0,0.1))
                self.sc2.axes.set_title(tl,fontsize=40,color="k")

                pos=[0.05,0.12,0.9,0.82]
                self.sc.axes.set_position(pos, which='both')
               
                
            except Exception as e:
                print(e)
                
    

#################################################################################
#################################################################################
#################################################################################
################################################################################
#################################################################################
################################################################################
def webengine_hack():
    from PyQt5 import QtWidgets
    app = QtWidgets.QApplication.instance()
    if app is not None:
        import sip
        app.quit()
    #     sip.delete(app)
    
    QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_ShareOpenGLContexts)
    app = QtWidgets.qApp = QtWidgets.QApplication(sys.argv)

    return app

try:
    # just for testing
    from PyQt5 import QtWidgets
    import MWindowF
    app = QtWidgets.QApplication([''])
    from PyQt5 import QtWebEngineWidgets
except ImportError as exception:
    print('\nRetrying webengine import...')
    app = webengine_hack()


app=QtCore.QCoreApplication.instance()
if app is None:
   app = QtWidgets.QApplication(sys.argv)
app.setStyle(QtWidgets.QStyleFactory.create('Fusion'))
form=Log()
#form=mainD6('s')

form.show()

app.exec_()      