# -*- coding: utf-8 -*-
"""
Created on Sun Nov  5 17:10:10 2017

@author: SYED
""" 

from PyQt5 import QtCore, QtWidgets

import validators
import network_parsing,SettingF,analyzeF
import threading
import sys,csv,os,re
import sqlite3

import matplotlib
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

class Set(QtWidgets.QWidget,SettingF.Ui_Form):
    def __init__(self,parent=None):
        super(Set,self).__init__(parent)
        
        self.closeFlag1=False
        self.closeFlag2=False
        self.setWindowModality(QtCore.Qt.ApplicationModal)
        self.setupUi(self)
        self.bbxSetM.button(QtWidgets.QDialogButtonBox.Cancel).setText("Close")
        self.bbxSetN.button(QtWidgets.QDialogButtonBox.Cancel).setText("Close")
        try:
            k=os.path.join(s,'crap\\Manifest.db')
            con=sqlite3.connect(k)
            c=con.cursor()
            
            self._curBranch=''.join(c.execute("SELECT value FROM setting WHERE name='branch';").fetchone())
            self._curScheme=''.join(c.execute("SELECT value FROM setting WHERE name='scheme';").fetchone())
            self._DBSavePath=''.join(c.execute("SELECT value FROM setting WHERE name='dbsavepath';").fetchone())
            self._defaultHmPgURL=''.join(c.execute("SELECT value FROM setting WHERE name='homeurl';").fetchone())
            self._csvPath=''.join(c.execute("SELECT value FROM setting WHERE name='csvpath';").fetchone())
            self._searchPath=''.join(c.execute("SELECT value FROM setting WHERE name='searchpath';").fetchone())
            self._saveMsgCrt=''.join(c.execute("SELECT value FROM setting WHERE name='savemsgcrt';").fetchone())
            self._saveMsgEdt=''.join(c.execute("SELECT value FROM setting WHERE name='savemsgedt';").fetchone())
            self._defaultScrpURL=''.join(c.execute("SELECT value FROM setting WHERE name='scrapurl';").fetchone())
            self._stuCnt=''.join(c.execute("SELECT value FROM setting WHERE name='studentcount';").fetchone())
            
            print(self._DBSavePath)
            c.close()
            con.close()
        except Exception as e:
            print (e)
            
            
        
#################################################################################
        # Main Setting tab Signals
        self.pbtnBrwSetM.clicked.connect(self.fnBrw)
        schm=['2010','2014','2015','2016','2017']
        self.cbScmSetM.addItems(schm)
        b=[]
        curFile=os.path.join(s,'crap\\BranchList.txt')
        with open(curFile,'r') as f:
                for lines in f.readlines():
                    b.append(lines.replace("\n",""))
        f.close()
        c=[i[4:-1] for i in b]
        self.cbBrSetM.addItems(c)
        self.bbxSetM.accepted.connect(self.saveMainSet)
        self.bbxSetM.rejected.connect(self.close)
        print(self._curBranch)
        self._curBranchText=self.cbBrSetM.itemText(int(self._curBranch))
#################################################################################
        #NEW Setting tab Signals
       
        self.pbtnCrtSN.clicked.connect(self.fnBrwCrtN)
        self.pbtnEdtSN.clicked.connect(self.fnBrwEdtN)

        self.bbxSetN.accepted.connect(self.saveNewSet)
        self.bbxSetN.rejected.connect(self.close)
        
#################################################################################
        self.cbBrSetM.setCurrentIndex(int(self._curBranch))
        self.cbScmSetM.setCurrentIndex(int(self._curScheme))
        self.leDPSetM.setText(self._DBSavePath)
        self.leUrlSetM.setText(self._defaultHmPgURL)
        self.chbCrtSN.setChecked(bool(int(self._saveMsgCrt)))
        self.chbEdtSN.setChecked(bool(int(self._saveMsgEdt)))
        self.leCrtSN.setText(self._csvPath)
        self.leEdtSN.setText(self._searchPath)
        self.leSrpSN.setText(self._defaultScrpURL)
        self.spSrpSN.setValue(int(self._stuCnt))
        
        
        
#################################################################################
#################################################################################
    
            
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
        self.closeFlag1=False
        self.closeFlag2=False  
        
        
    def saveMainSet(self):
        self.closeFlag1=True
        self._defaultHmPgURL=self.leUrlSetM.text()
        self._curBranch=str(self.cbBrSetM.currentIndex())
        self._curScheme=str(self.cbScmSetM.currentIndex())
        self._DBSavePath=self.leDPSetM.text()
        self._curBranchText=self.cbBrSetM.currentText()
        curFile=os.path.join(s,'Manifest.db')
        con=sqlite3.connect(curFile)
        c=con.cursor()
        qry1="UPDATE setting SET value="+self._curBranch+" WHERE name='branch' ;"
        qry2="UPDATE setting SET value="+self._curScheme+" WHERE name='scheme' ;"
        qry3="UPDATE setting SET value='"+self._DBSavePath+"' WHERE name='dbsavepath' ;"
        qry4="UPDATE setting SET value='"+self._defaultHmPgURL+"' WHERE name='homeurl' ;"
        try:
            c.execute(qry1)
            c.execute(qry2)
            c.execute(qry3)
            c.execute(qry4)
            
            con.commit()
            c.close()
            con.close()
        except Exception as e:
            print (e)
            
        
        QtWidgets.QMessageBox.about(self, "DONE", "The settings are saved")
        
        
        
    def fnBrw(self):
        savePath = str(QtWidgets.QFileDialog.getExistingDirectory(self,"save Path"))
        self.leDPSetM.setText(savePath)
    
    def fnBrwCrtN(self):
        savePath = str(QtWidgets.QFileDialog.getExistingDirectory(self,"save Path"))
        self.leCrtSN.setText(savePath)
        
        
    def fnBrwEdtN(self):
        savePath = str(QtWidgets.QFileDialog.getExistingDirectory(self,"save Path"))
        self.leEdtSN.setText(savePath)
        
    def saveNewSet(self):
        self.closeFlag2=True
        try:
            self._csvPath=self.leCrtSN.text()
            self._searchPath=self.leEdtSN.text()
            
            if self.chbCrtSN.checkState()== QtCore.Qt.Checked:
                self._saveMsgCrt='1'
            else:
                self._saveMsgCrt='0'
                
            if self.chbEdtSN.checkState()== QtCore.Qt.Checked:
                self._saveMsgEdt='1'
            else:
                self._saveMsgEdt='0'     
            
            self._defaultScrpURL=self.leSrpSN.text()
              
            self._stuCnt=self.spSrpSN.text()
                        
            
            curFile=os.path.join(s,'Manifest.db')
            con=sqlite3.connect(curFile)
            c=con.cursor()
            qry1="UPDATE setting SET value='"+self._csvPath+"' WHERE name='csvpath' ;"
            qry2="UPDATE setting SET value='"+self._searchPath+"' WHERE name='searchpath' ;"
            qry3="UPDATE setting SET value="+self._saveMsgCrt+" WHERE name='savemsgcrt' ;"
            qry4="UPDATE setting SET value="+self._saveMsgEdt+" WHERE name='savemsgedt' ;"
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
        
#################################################################################
#################################################################################          
#################################################################################
#################################################################################

import MWindowF 
class mainD5(QtWidgets.QMainWindow,MWindowF.Ui_MainWindow):
    def __init__(self,parent=None):
        super(mainD5,self).__init__(parent)
        self.setupUi(self)
        self.setAttribute(QtCore.Qt.WA_DeleteOnClose)
        self.form1=Set()
        self.form2=Analyze()
        self.lbScpStatus.setText("")
        self.__fname=''
        self.__sname=''
        

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
        self.hmLE.setPlaceholderText(self.form1._defaultHmPgURL)
        
        self.hmWeb.load(QtCore.QUrl(self.form1._defaultHmPgURL))     #"http://www.google.co.in"))
        self.hmWeb.show()
        
        
        self.hmbtn.clicked.connect(self.webPageLoad)
        self.hmWeb.urlChanged.connect(self.webPagedr)
        
        
        #signal from create tab 
        self.pbtnCrtAdd.setShortcut("Ctrl+1")
        self.pbtnCrtAdd.setToolTip("Add..Ctrl+1")
        self.pbtnCrtAdd.clicked.connect(self.fnpbtnAdd)
        self.pbtnCrtRm.setShortcut("Ctrl+2")
        self.pbtnCrtRm.setToolTip("Remove..Ctrl+2")
        self.pbtnCrtRm.clicked.connect(self.fnpbtnRm)
        
        self.pbtnCrtSave.setShortcut("Ctrl+s")
        self.pbtnCrtSave.setToolTip("Save..Ctrl+s")
        self.pbtnCrtSave.clicked.connect(self.fnpbtnSave)
        
        
        a=[]
        curFile=os.path.join(s,'scChemPhy.txt')
        with open(curFile,'r') as f:
                for lines in f.readlines():
                    a.append(lines.replace("\n",""))
        f.close()
        
        self.sbCrtSem.valueChanged.connect(self.fnSubValue) 
        self.cbCrtSub.addItems(a)
        
        
        #signal from edit tab 
        self.pbtnEdtAdd.setShortcut("Ctrl+1")
        self.pbtnEdtAdd.setToolTip("Add..Ctrl+1")
        self.pbtnEdtAdd.clicked.connect(self.fnAdd)
        self.pbtnEdtRm.setShortcut("Ctrl+2")
        self.pbtnEdtRm.setToolTip("Remove..Ctrl+2")
        self.pbtnEdtRm.clicked.connect(self.fnRm)
        
        self.pbtnEdtDel.clicked.connect(self.fnDrop)
        
        
        self.pbtnEdtSave.setShortcut("Ctrl+s")
        self.pbtnEdtSave.setToolTip("Save..Ctrl+s")
        self.pbtnEdtSave.clicked.connect(self.fnSave)
        
        self.pbtnEdtBrowse.clicked.connect(self.fnBrowse)
        self.cbEdtSN.activated.connect(self.fnPopupBase)
        self.pbtnEdtReset.clicked.connect(self.fnPopupBase)
        
        
        #signal from Scrap tab
        
        
        self.pbtnScpLoad.clicked.connect(self.fnDownload)
        
        self.leScpURL.setText(self.form1._defaultScrpURL)
        
#################################################################################
#################################################################################


    
        # slots for toolbtn and menu items
    def fnbtnHome(self):
        self.btn_home.setChecked(True)
        self.stackedWidget.setCurrentIndex(0)
        self.btn_new.setChecked(False)
    def fnbtnNew(self,a=0):
        self.btn_new.setChecked(True)
        self.stackedWidget.setCurrentIndex(1)
        self.tabWidget.setCurrentIndex(0)
        self.btn_home.setChecked(False)
        self.sbCrtYear.setFocus()
        if a==1:
            self.tabWidget.setCurrentIndex(2)
            self.spScpYear.setFocus()
    def fnbtnConv(self):
        self.btn_home.setChecked(False)
        self.stackedWidget.setCurrentIndex(2)
        self.btn_new.setChecked(False)
    def fnSettingWindow(self):
        try:
            self.form1.show()
        except Exception as e:
            print (e)
        
    
    def fnAnalyzeWindow(self):
        try:
            self.form2.show()
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
# slots for create tab 

    def collectDatafmTable(self,row,tw):
        
        rowdata = []
        for column in range(tw.columnCount()):
            item = tw.item(row, column)
            
            if item is not None:
                rowdata.append(str(item.text()))
            else:
                rowdata.append('')
        
        return rowdata
        
    

    # slots for create tab 
    
    def fnSubValue(self):
        b=[]
        self.cbCrtSub.clear()
        k=self.sbCrtSem.value()
        if k==1 or k==2:
            curFile=os.path.join(s,'scChemPhy.txt')
            with open(curFile,'r') as f:
                    for lines in f.readlines():
                        b.append(lines.replace("\n",""))
            f.close()
        else:
            stg=self.form1._curBranchText.split(",")[1]
            stg=stg[1:]+"Sub.txt"
            
            
            with open(stg,'r') as f:
                    for lines in f.readlines():
                        b.append(lines.replace("\n",""))
            f.close()
        
                
        self.cbCrtSub.addItems(b)
    
    
    def fnpbtnAdd(self):
        rowPosition = self.tableWidgetCrt.rowCount()
        
        self.tableWidgetCrt.insertRow(rowPosition)
    def fnpbtnRm(self):
        selected = self.tableWidgetCrt.currentRow()
        
        self.tableWidgetCrt.removeRow(selected)
        
        
    def fnpbtnSave(self):  
        if self.form1._saveMsgCrt == '1':
            save_msg = "Are you sure you want to save the data?"
            reply = QtWidgets.QMessageBox.question(self, 'Message', 
                             save_msg, QtWidgets.QMessageBox.Yes, QtWidgets.QMessageBox.No)
        
        if  self.form1._saveMsgCrt == '0' or reply == QtWidgets.QMessageBox.Yes:
            
            year=self.sbCrtYear.value()
            sem=self.sbCrtSem.value()
            sub=self.cbCrtSub.currentText()
            
            dbs=os.path.join(self.form1._DBSavePath,self.form1._curBranchText.split(",")[0])
            os.makedirs(dbs, exist_ok=True)
            os.chdir(dbs)
            ys=os.path.join(dbs,str(year))
            os.makedirs(ys,exist_ok=True)
            os.chdir(ys)
            ss=os.path.join(ys,str(sem))
            os.makedirs(ss,exist_ok=True)
            os.chdir(ss)
            
            
            
            row_count = self.tableWidgetCrt.rowCount()
            col_count = self.tableWidgetCrt.columnCount()
            
            
            if self.rbtnCrtNewdb.isChecked() is True:
                sub1=(sub,)
                
                
                conn= sqlite3.connect("Regular.db")
                c=conn.cursor()
                y=c.execute("SELECT name FROM sqlite_master WHERE type='table';").fetchall()
                
                
                if sub1 in list(y):
                    QtWidgets.QMessageBox.about(self, "ERROR", "Table already exists try edit tab")
                else:
                    ctn="CREATE TABLE '"+sub+"' (usn TEXT UNIQUE,name TEXT NOT NULL,internal INT ,external INT ,total INT ,result TEXT)"
                    
                    
                    
                    try:
                        
                        
                        rd=[]
                        for row in range(row_count):
                            rowdata= self.collectDatafmTable(row,self.tableWidgetCrt)
                            rd.append(tuple(rowdata))
                        rd=tuple(rd)
                        
                        inq="INSERT OR REPLACE INTO '"+sub+"' VALUES(?, ?, ?, ?, ?, ?)"
                        c.execute(ctn)
                        c.executemany(inq, rd)
                        conn.commit()
                        c.close()
                        conn.close()
                        
                    except Exception as e:
                        print(e)
            
                
            elif self.rbtnCrtCSV.isChecked() is True:
                
                path = QtWidgets.QFileDialog.getSaveFileName(self, 'Save File',self.form1._csvPath, 'CSV(*.csv)')
                #print(type(path[0]),path)
                try:
                    if path[0] != '':
                        
                        with open(path[0],'w') as stream:
                            
                            writer = csv.writer(stream,quoting=csv.QUOTE_MINIMAL)
                            
                            # write headers
                            csv_row = []
                            for col in range(col_count):
                                csv_row.append(self.tableWidgetCrt.horizontalHeaderItem(col).text())
                 
                            writer.writerow(csv_row)
                            print('yeah header')
                            
                            #write data
                            
                            for row in range(row_count):
                                rowdata= self.collectDatafmTable(row,self.tableWidgetCrt)
                                
                                writer.writerow(rowdata)
                                
                            
                except Exception as e:
                    print(e)
            
    
#################################################################################
    #slots for edit tab
    
    def fnBrowse(self):
        fname = QtWidgets.QFileDialog.getOpenFileName(self, 'Open File',self.form1._searchPath, 'DB(*.db)')
        self.__fname=fname[0]
        self.leEdtdbFile.setText(fname[0])
        self.cbEdtSN.clear()
        try:
            conn= sqlite3.connect(fname[0])
            c=conn.cursor()
            y=c.execute("SELECT name FROM sqlite_master WHERE type='table';").fetchall()
            subNames=[]
            for x in y:
                subNames=subNames+list(x)
            
            self.cbEdtSN.addItems(subNames)
            strt=self.cbEdtSN.currentText()
            strt="'"+strt+"'"
            qry="SELECT * FROM "+str(strt)
            result=c.execute(qry)
            self.loadData(result)
            
            c.close()
            conn.close()
            
            
        except Exception as e:
            print(e)
    
    def fnPopupBase(self):
        
        strt=self.cbEdtSN.currentText()
        strt="'"+strt+"'"
        
        qry="SELECT * FROM "+str(strt)
        
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
        self.tableWidgetEdt.setRowCount(0)
        for row_number,row_data in enumerate(result):
            self.tableWidgetEdt.insertRow(row_number)
            for col_num,data in enumerate(row_data):
                self.tableWidgetEdt.setItem(row_number,col_num,QtWidgets.QTableWidgetItem(str(data)))
    
    
    
    def fnAdd(self):
        rowPosition = self.tableWidgetEdt.rowCount()
        
        self.tableWidgetEdt.insertRow(rowPosition)
    def fnRm(self):
        selected = self.tableWidgetEdt.currentRow()
        
        self.tableWidgetEdt.removeRow(selected)

    def fnDrop(self):
        save_msg = "Are you sure you want to delete this table ?"
        reply = QtWidgets.QMessageBox.question(self, 'Message', 
                         save_msg, QtWidgets.QMessageBox.Yes, QtWidgets.QMessageBox.No)
        if reply == QtWidgets.QMessageBox.Yes:
            strt=self.cbEdtSN.currentText()
            strt="'"+strt+"'"
            try:
                conn= sqlite3.connect(self.__fname)
                c=conn.cursor()
                c.execute("DROP TABLE "+strt+" ;")
                
                
                self.cbEdtSN.clear()
                self.tableWidgetEdt.clearContents()
                y=c.execute("SELECT name FROM sqlite_master WHERE type='table';").fetchall()
                subNames=[]
                for x in y:
                    subNames=subNames+list(x)
                
                self.cbEdtSN.addItems(subNames)
                c.close()
                conn.close()
                QtWidgets.QMessageBox.about(self, "DONE", "The table is deleted")
            except Exception as e:
                print(e)
           
            
            
    def fnSave(self):
        if self.form1._saveMsgEdt == '1':
            save_msg = "Are you sure you want to save the data?"
            reply = QtWidgets.QMessageBox.question(self, 'Message', 
                             save_msg, QtWidgets.QMessageBox.Yes, QtWidgets.QMessageBox.No)
        
        if self.form1._saveMsgEdt == '0' or reply == QtWidgets.QMessageBox.Yes:
            
            
            self.__sname=self.cbEdtSN.currentText()
            if self.__sname:
                try:
                    if self.rbtnEdtCpy.isChecked() is True:
                        
                        fname='copy_'+self.__sname+'.db'
                        dn=os.path.dirname(self.__fname)
                        fname=os.path.join(dn,fname)
                        
                        con= sqlite3.connect(fname)
                        
                    else:
                        
                        con= sqlite3.connect(self.__fname)
                        
                    ctn="CREATE TABLE IF NOT EXISTS '"+self.__sname+"' (usn TEXT UNIQUE,name TEXT NOT NULL,internal INT ,external INT ,total INT ,result TEXT)"
                    try:
                        
                        c=con.cursor()
                        c.execute(ctn)
                        
                        rd=[]
                        
                        for row in range(self.tableWidgetEdt.rowCount()):
                            rowdata= self.collectDatafmTable(row,self.tableWidgetEdt)
                            rd.append(tuple(rowdata))
                        rd=tuple(rd)
                        
                        
                        inq="INSERT OR REPLACE INTO '"+self.__sname+"' VALUES(?, ?, ?, ?, ?, ?)"
                        c.executemany(inq, rd)
                        con.commit()
                        c.close()
                        con.close()
                        
                    except Exception as e:
                        print(e)
                
                        
                except Exception as e:
                    print(e)
            else:
                QtWidgets.QMessageBox.about(self, "ERROR", "No file/database is chosen")
#################################################################################

    def fnDownload(self):
        
        usn=self.leScpUSN.text()
        k=re.match('^[1-4]\w{2}\d{2}\w{2,3}\d{2}$',usn)
        try:
        
            if k: 
                    self.leScpUSN.setDisabled(True)
                    self.lbScpStatus.setText("")
                
                    url1=self.leScpURL.text()
                    if url1 == '' or not validators.url(url1):
                        QtWidgets.QMessageBox.about(self, "ERROR", "please insert a valid URL")
                        
                    else:
                        self.lbScpStatus.setStyleSheet("QLabel { color : blue; }");
                        self.lbScpStatus.setText("Connecting...")
                        
                        year=self.spScpYear.value()
                        self.spScpYear.setDisabled(True)
                        sem=self.spScpSem.value()
                        self.spScpSem.setDisabled(True)
                        try:
                            
                            
                            if self.rbtnScpReg.isChecked() is True:
                                fname='Regular.db'
                                
                            else:
                                
                                fname='RV.db'
                            self.rbtnScpReg.setDisabled(True)
                            self.rbtnScpRV.setDisabled(True)
                            self.leScpURL.setDisabled(True)
                            
                            
                            t=threading.Thread(target=self.thread1,args=(fname,year,sem,url1,usn))
                           
                            t.start()
                            self.lbScpStatus.setStyleSheet("QLabel { color : red,blue,green; }");
                            self.lbScpStatus.setText("Downloading...")
                            
                        except Exception as e:
                            print(e)
                            
                            pass
                
                        
            else:    
                QtWidgets.QMessageBox.about(self, "ERROR", "please insert a valid USN")
        except Exception as e:
                print(e)
    def thread1(self,fname,year,sem,url1,usn):
            
        dbs=os.path.join(self.form1._DBSavePath,self.form1._curBranchText.split(",")[0])
        os.makedirs(dbs, exist_ok=True)
        os.chdir(dbs)
        ys=os.path.join(dbs,str(year))
        os.makedirs(ys,exist_ok=True)
        os.chdir(ys)
        ss=os.path.join(ys,str(sem))
        os.makedirs(ss,exist_ok=True)
        os.chdir(ss)
        
        ct=int(self.form1._stuCnt)
        try:
            network_parsing.webScraping(fname,usn11=usn,url=url1,curSem=sem,noStu=ct)
            
            
        except Exception as e:
            
            QtWidgets.QMessageBox.about(self, "ERROR", "\n  please contact Syed")        
        os.chdir(s)
        
        self.lbScpStatus.setStyleSheet("QLabel { color : green; }");
        self.lbScpStatus.setText("DONE!")
        self.spScpYear.setEnabled(True)
        self.spScpSem.setEnabled(True)
        self.rbtnScpReg.setEnabled(True)
        self.rbtnScpRV.setEnabled(True)
        self.leScpURL.setEnabled(True)
        self.leScpUSN.setEnabled(True)
        
        
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
class Analyze(QtWidgets.QWidget,analyzeF.Ui_Form):
    def __init__(self,parent=None):
        super(Analyze,self).__init__(parent)
        self.setWindowModality(QtCore.Qt.ApplicationModal)
        self.setupUi(self)
        
        self.pbtnAnaBrowse.clicked.connect(self.fnBrowseAna)
        self.cbAnaSN.activated.connect(self.fnPopupBaseAna)
        self.leAnaName.textChanged.connect(lambda :self.fnLoadby(0))
        self.leAnaUSN.textChanged.connect(lambda :self.fnLoadby(1))
        listm=['All','Total above 100','Total 100 to 70','Total 70 to 50','Total below 50','External below 35','internal below 15','Fail']
        self.cbAnaSelect.addItems(listm)
        self.cbAnaSelect.currentIndexChanged.connect(self.fnLoadSelect)
        
        self.pbtnAnaHist.clicked.connect(self.fnLoadHist)
        self.pbtnAnaPie.clicked.connect(self.fnLoadPie)
        self.pbtnAnaClose.clicked.connect(self.fncls)
        
        self.sc = MyMplCanvas(self.tb2Grp, width=5, height=4, dpi=100)
        self.gridLayout_4.addWidget(self.sc,0, 0, 1,7)
        
        listmp=['Total','External','Internal']
        self.cbAnaSelect2.addItems(listmp)
        self.cbAnaSelect2.currentIndexChanged.connect(self.fnLoadSelect2)
        
    def fncls(self):
        plt.close()
    def fnLoadSelect2(self):
        k=self.cbAnaSelect2.currentIndex()
        if k==1:
            self.plotscatter(self.__x1,self.__y2,35,"External")
        elif k==2:
            self.plotscatter(self.__x1,self.__y3,15,"Internal")
        else:
            self.plotscatter(self.__x1,self.__y1,50,"Total")
        
        
        
        
    def fnLoadSelect(self):
        conn= sqlite3.connect(self.__fname)
        c=conn.cursor()
        k=self.cbAnaSelect.currentIndex()
        strt=self.cbAnaSN.currentText()
        strt="'"+strt+"'"
        try:
            if k==1:
                qry1="SELECT * FROM "+strt+" WHERE total >= 100 ;"
                
            elif k==2:
                qry1="SELECT * FROM "+strt+" WHERE total <= 100 AND total>=70 ;"
            elif k==3:
                qry1="SELECT * FROM "+strt+" WHERE total <= 70 AND total>=50 ;"
            elif k==4:
                qry1="SELECT * FROM "+strt+" WHERE total <= 50 ;"
            elif k==5:
                qry1="SELECT * FROM "+strt+" WHERE external <= 35 ;"
            elif k==6:
                qry1="SELECT * FROM "+strt+" WHERE internal <= 15 ;"
            elif k==7:
                qry1="SELECT * FROM "+strt+" WHERE result = 'F' ;"
            else:
                qry1="SELECT * FROM "+strt+";"
                
                
            result=c.execute(qry1)
            
            self.loadDataAna(result)
            
        except Exception as e:
            print(e)
        c.close()
        conn.close()    
            
    def fnLoadby(self,a):
        try:
            conn= sqlite3.connect(self.__fname)
            c=conn.cursor()
            strt=self.cbAnaSN.currentText()
            
            strt="'"+strt+"'"
            
            if a== 0:
                strnm=self.leAnaName.text()
                strnm="'%"+strnm+"%'"
                qry="SELECT * FROM "+strt+" WHERE name like "+strnm+";"
            else:
                strnm=self.leAnaUSN.text()
                strnm="'%"+strnm+"%'"
                qry="SELECT * FROM "+strt+" WHERE USN like "+strnm+";"
            print(qry)
            result=c.execute(qry)
            self.loadDataAna(result)
        except Exception as e:
            print(e)
        c.close()
        conn.close()
        
    def fnPopupBaseAna(self):
        
        strt=self.cbAnaSN.currentText()
        strt="'"+strt+"'"
        print(strt)
        qry="SELECT * FROM "+str(strt)
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
           
                
    def fnBrowseAna(self):
        fname = QtWidgets.QFileDialog.getOpenFileName(self, 'Open File',os.getcwd(), 'DB(*.db)')
        self.__fname=fname[0]
        self.leAnadbFile.setText(fname[0])
        self.cbAnaSN.clear()
        try:
            conn= sqlite3.connect(fname[0])
            c=conn.cursor()
            y=c.execute("SELECT name FROM sqlite_master WHERE type='table';").fetchall()
            subNames=[]
            for x in y:
                subNames=subNames+list(x)
            print(subNames)
            self.cbAnaSN.addItems(subNames)
            strt=self.cbAnaSN.currentText()
            strt="'"+strt+"'"
            qry="SELECT * FROM "+str(strt)
            result=c.execute(qry)
            self.loadDataAna(result)
            
            self.replaceContent(c,strt)
           
            c.close()
            conn.close()
           
        except Exception as e:
            print(e)
            
            
    def replaceContent(self,c,strt):
        try:
            self.cbAnaSelect.setCurrentIndex(0)
            self.cbAnaSelect2.setCurrentIndex(0)
            
            qry2="SELECT COUNT() FROM "+strt+";"
            res=c.execute(qry2).fetchone()[0]
            self.lbTlStuCnt.setText(str(res))
            
            
            qry2="SELECT COUNT() FROM "+strt+"WHERE result = 'P' ;"
            res=c.execute(qry2).fetchone()[0]
            self.lbTlPass.setText(str(res))
            
            
            qry2="SELECT COUNT() FROM "+strt+"WHERE result = 'F' ;"
            res=c.execute(qry2).fetchone()[0]
            self.lbTlFail.setText(str(res))
            
            
            qry2="SELECT COUNT() FROM "+strt+"WHERE result = 'A' ;"
            res=c.execute(qry2).fetchone()[0]
            self.lbTlAbsent.setText(str(res))
            
            qry2="SELECT MAX(total) FROM "+strt+";"
            res=c.execute(qry2).fetchone()[0]
            self.lbHScore.setText(str(res))
            
            qry2="SELECT MIN(total) FROM "+strt+";"
            res=c.execute(qry2).fetchone()[0]
            self.lbLScore.setText(str(res))
            
            qry2="SELECT AVG(total) FROM "+strt+";"
            res=c.execute(qry2).fetchone()[0]
            self.lbTlAverage.setText(str(res)+"%")
            
            self.totalStu=int(self.lbTlStuCnt.text())
            pasStu=int(self.lbTlPass.text())
            self.percent=(pasStu/self.totalStu)*100
            
            self.lbTlPassPer.setText(str(self.percent)+"%")
        
            qry2="SELECT name FROM "+strt+";"
            res=c.execute(qry2).fetchall()
            
            self.__x1=[x[0] for x in res]
            
            
            
            qry2="SELECT total FROM "+strt+";"
            res=c.execute(qry2).fetchall()
            
            self.__y1=[x[0] for x in res]
            
            qry2="SELECT external FROM "+strt+";"
            res=c.execute(qry2).fetchall()
            
            self.__y2=[x[0] for x in res]
            
            qry2="SELECT internal FROM "+strt+";"
            res=c.execute(qry2).fetchall()
            self.__y3=[x[0] for x in res]
            self.plotscatter(self.__x1,self.__y1,50,"Total")
            
        except Exception as e:
            print(e)
    def plotscatter(self,x,y,l,tl):
        
            try:
                self.gridLayout_4.removeWidget(self.sc)
                self.sc.deleteLater()
                del self.sc
                self.sc = MyMplCanvas(self.tb2Grp, width=5, height=4, dpi=80)
                self.gridLayout_4.addWidget(self.sc,0, 0, 1, 7)
            
                x1=np.arange(1,len(x)+1)
                self.sc.axes.set_xlabel('Names',fontsize=20,color="red")
                self.sc.axes.set_ylabel('Marks',fontsize=20,color="red")
                self.sc.axes.set_title(tl,fontsize=30,color="k")
                self.sc.axes.scatter(x1,y,label="score",s=100,marker="*",color="c")
                
                self.sc.axes.axhline(l,color='k',linewidth=2)
                self.sc.axes.set_xticks(x1)
                self.sc.axes.set_xticklabels(x, rotation=40, fontsize=10)
                self.sc.axes.legend()
                pos=[0.05,0.12,0.9,0.82]
                self.sc.axes.set_position(pos, which='both')
               
                
            except Exception as e:
                print(e)
    def fnLoadHist(self):
        
        
        txt=self.leAnadbFile.text()
        if txt == "" or not os.path.exists(txt):
            QtWidgets.QMessageBox.about(self,"Error","Please select the valid File")
        else:    
            try:
                plt.ion()
                plt.show(block=False)
                plt.cla()
                y=np.arange(0,125,10)
                cb=self.cbAnaSelect2.currentIndex()
                if cb==1:
                    y=np.arange(0,100,10)
                    plt.hist(self.__y2,y,histtype='bar',rwidth=0.8)
                    plt.title("External")
                elif cb==2:
                    y=np.arange(0,25)
                    plt.hist(self.__y3,y,histtype='bar',rwidth=0.8)
                    plt.title("Internal")
                else :
                    plt.hist(self.__y1,y,histtype='bar',rwidth=0.8)
                    plt.title("Total")
                    
                    
                plt.xlabel('X')
                plt.ylabel('Number of Students')
                
            
                plt.draw()
                plt.pause(0.001)
                input("Press [enter] to continue.")
                
            except Exception as e:
                print(e)
                
                
    def fnLoadPie(self):
        
        
        txt=self.leAnadbFile.text()
        if txt == "" or not os.path.exists(txt):
            QtWidgets.QMessageBox.about(self,"Error","Please select the valid File")
        else:    
            try:
                plt.ion()
                plt.show(block=False)
                plt.cla()
                
                cb=self.cbAnaSelect2.currentIndex()
                if cb==1:
                    k=sum(i>50 for i in self.__y2 )
                    passPer=(k/self.totalStu)*100
                    slices=[passPer,abs(passPer-100)]
                    plt.pie(slices,labels=['Pass','Fail'],colors=['r','g'],startangle=90,shadow=True,autopct='%1.1f%%',explode=(0,0.1))
                    plt.title("External")  
                elif cb==2:
                    k=sum(i>15 for i in self.__y3 )
                    passPer=(k/self.totalStu)*100
                    slices=[passPer,abs(passPer-100)]
                    plt.pie(slices,labels=['Pass','Fail'],colors=['r','g'],startangle=90,shadow=True,autopct='%1.1f%%',explode=(0,0.1))
                    plt.title("Internal")
                else :
                    t=self.percent-100
                    slices=[self.percent,abs(t)]
                    plt.pie(slices,labels=['Pass','Fail'],colors=['r','g'],startangle=90,shadow=True,autopct='%1.1f%%',explode=(0,0.1))
                    plt.title("Total")
                    
                  
                plt.draw()
                plt.pause(0.001)
                input("Press [enter] to continue.")
                
            except Exception as e:
                print(e)


#################################################################################
#################################################################################
# def webengine_hack():
#     from PyQt5 import QtWidgets
#     app = QtWidgets.QApplication.instance()
#     if app is not None:
#         import sip
#         app.quit()
#     #     sip.delete(app)
    
#     QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_ShareOpenGLContexts)
#     app = QtWidgets.qApp = QtWidgets.QApplication(sys.argv)

#     return app

# try:
#     # just for testing
#     from PyQt5 import QtWidgets
#     import MWindowF
#     app = QtWidgets.QApplication([''])
#     from PyQt5 import QtWebEngineWidgets
# except ImportError as exception:
#     print('\nRetrying webengine import...')
#     app = webengine_hack()
#     # from PyQt5 import QtWebEngineWidgets
    
app=QtCore.QCoreApplication.instance()
if app is None:
   app = QtWidgets.QApplication(sys.argv)
    
app.setStyle(QtWidgets.QStyleFactory.create('Fusion'))
form=mainD5()

form.show()

app.exec_()