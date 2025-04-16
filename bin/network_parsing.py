# -*- coding: utf-8 -*-
"""
Created on Fri Jan 26 21:58:55 2018

@author: SYED
"""


import sqlite3
import urllib
from bs4 import BeautifulSoup
import pandas as pd
import dbCreat
import numpy as np
#parsing for  subject names

    
def parseSub(dbname,usn,url1 = 'http://results.vtu.ac.in/vitaviresultcbcs/resultpage.php' ,cSem=1):
    

    #usnF="E:\\VTUBroadSpec\\bin\\"+usn+".html"
    try:
        
        payload = {'lns':usn} #PARAMETER  FOR POST REQUEST
        print(usn,url1 )
        
        data = urllib.parse.urlencode(payload)
        print(data )
        data = data.encode('ascii')
        print(data )
        r = urllib.request.urlopen(url1, data).read()  #READING THE RESULT PAGE
        
        bs=BeautifulSoup(r,'html.parser')
#        print(bs,"\n\n7777777\n")
        print("*****\n\n\n\n\n\n\nSubject parse*****\n\n\\\\\n\n\n")
    except Exception as e:
        print("*****Network Broken*****",e)
        pass
    try:
        
        #print(bs,"\n\n")
        yt=[]
        yk=[]
        bc=bs.findAll('div')
        
        print(bc)
        bc=str(bc).split('Semester')[1].split('</b>')[0].replace(' ','').replace(':','')
        print(bc,"\n\n7777777\n\n\n\n\n\n\n\n\n")
        #if(bc==str(cSem)):
            
        tag=bs.find('div',{'class':"divTableBody"}).findAll('div',{'class',"divTableRow"}) #parse to get td
       #print(tag,"\n\n7777777\n")
        for t in tag:
            print (t,'\ntt\n')
            
            s=str(t).split('<div class="divTableCell"')#[1].split('</div>')[0]
            sk=s[1].split('</div>')[0].split('>')[1]
            
            #print (s,sk,'\nmkkmm\n')
            st=s[2].split('>')[1].split('</div')[0]
            #print (st,'\nmmm\n')
            st=st.replace(' &amp; ',' and ')
            print (st,'\n')
            yk.append(sk)
            yt.append(st)
    
       # print (y,'\n')
       # print (len(y),'\n\n\n\n\n')
    
        #redundent
    #    for x in range(0,len(yt),2):
    #        if x>1:
    #            subjects.insert(x-1,yt[x]+' : '+yt[x+1])
    #        else:
    #            subjects.insert(x,yt[x]+' : '+yt[x+1])
        del yk[0]
        del yt[0]
        print(yk,yt,type(bc))
        insertSub(dbname,yk,yt,int(bc),usn)
    except Exception as e:
        print("***kkkkkkk**Network Broken**kkkkkkkkkkk***",e)
        
    return bc
    
def insertSub(dbname,sc,st,ssem,usn):
    try:
        dbn='file:'+dbname+'?mode=rw'
        print(dbn)
        con=sqlite3.connect(dbn,uri=True) 
         
    except Exception as e:                           #to make sure db file exists
        print("file doesnt exist creating new database file")
        dbCreat.creat(dbname)
    c=con.cursor()#connect to db
    dpn=usn[5:7]
    c.execute("SELECT dno FROM department WHERE dname='"+dpn+"';")
    dn=c.fetchall()
    dn=int((dn[0])[0])
    print(dn)
    
    qry1="INSERT OR REPLACE INTO subject VALUES(?,?,?,?);"  
    print(qry1)
    
    for i in range(len(sc)) :
        print(type(sc[i]),type(st[i]),type(ssem),type(dn))
        c.execute(qry1,[(sc[i]),(st[i]),(ssem),(dn)])
    
    con.commit()
    c.close()
    con.close()
    print("5587")
    
#function for aquiring marks  

def parseVal(nusn,url1="http://results.vtu.ac.in/vitaviresultnoncbcs/resultpage.php",usn1='4ub14cs001',k=False,d='4',cSem=1,f=1):
        mrks=[]
       
        
#    for n in range(1,nusn+1):
#        y=[]
#        if n <10:
#            if k is True:
#                usn=usn1+d+'0'+str(n)
#            else:
#                usn=usn1+'00'+str(n)
#        else:
#            if k is True:
#                usn=usn1+d+str(n)
#            else:
#                usn=usn1+'0'+str(n)
                
#        Ul=str(url)+usn
#        print(Ul)


        
        try:
            payload = {'lns':usn1}
            #print(usn1,url1 )
            
            data = urllib.parse.urlencode(payload)
            print(data )
            data = data.encode('ascii')
            print(data )
            r = urllib.request.urlopen(url1, data).read() 
        
            bs=BeautifulSoup(r,'html.parser')
            print('\n\n\n\n\n555\n\n\n')
        except Exception as e:
            print("*****Network Broken*****\n Cant get the values")
            return e

        try:
            bc=bs.findAll('div')
            sm=bs.findAll('div',{'style':"text-align:center;padding:5px;"})
#            print(bc,"\n\n7777777\n")
            bc=str(bc).split('Semester')[1].split('</b>')[0].replace(' ','').replace(':','')
#            print(bc)
            if(bc==str(cSem) or f==0):
                
                name=bs.find('td',{'style':"padding-left:15px"}).text
                
                name=str(name).split(': ')[1]
                print(name)
                print('\n\n\n\n\n\n ',name,'\n\n\n\n\n')
                
                
                
                tag=bs.find('div',{'class':"divTableBody"}).findAll('div',{'class',"divTableRow"}) #parse to get td
#                print(tag)
                k=[]
                for t in tag[1:]:
                    
#                    print(t)
                    for s in t.findAll('div',{'class':"divTableCell"}):
                        #s=t.findAll('div',{'class':"divTableCell"})
#                        print(s)
                        k.append(s.text)
                
                mrks=k
#                mrks.append(y)
#                usn5.append(usn)

            else:
                
                sm=str(sm[1]).split('Semester')[1].split('</b>')[0].replace(' ','').replace(':','')        
#                print(sm)
                
                if sm==str(cSem):
                    name=bs.find('td',{'style':"padding-left:15px"}).text
                
                    name=str(name).split(': ')[1]
                    print(name)
                    #print('\n\n\n\n\n\n ',name,'\n\n\n\n\n')
                    
                    
                    
                    tag=bs.findAll('div',{'class':"divTableBody"})[1].findAll('div',{'class',"divTableRow"}) #parse to get td
#                    print(tag)
                    k=[]
                    for t in tag[1:]:
#                        print(t)
                        for s in t.findAll('div',{'class':"divTableCell"}):
                            #s=t.findAll('div',{'class':"divTableCell"})
                            k.append(s.text)
                            
#                    print(k)
                    mrks=k
    #                mrks.append(y)
    #                usn5.append(usn)
                    
        except Exception as e:
            print(e)
        print (mrks,name,'\n\n\n')        
        return mrks,name
        
#def sepVal(sub,usn,d1,d2,mrks,sb=0):
#    
#    internal=[];external=[];total=[];result=[]
#    #print('\n\n\n',sub[sb])
#    for y in range(len(usn)):
#        
#        internal.append(mrks[y][sb][0])
#        external.append(mrks[y][sb][1])
#        total.append(mrks[y][sb][2])
#        result.append(mrks[y][sb][3])
#    #print('\n\n\n\n',internal,external,total,result,'\n\n\n\n')
#    dt1={'Internal':internal};dt2={'External':external};dt3={'Total':total};dt4={'Result':result}
#    d1.update(d2),d1.update(dt1);d1.update(dt2);d1.update(dt3);d1.update(dt4)
#    
#    #print(d1)
#    df=pd.DataFrame(d1)
#    df.set_index('USN',inplace=True)
#    print(df)
#    return df
    
                                          
#main cluase
def insertV(dbname,usnk,name,mrks):
    try:
        dbn='file:'+dbname+'?mode=rw'
        print(dbn)
        con=sqlite3.connect(dbn,uri=True) 
         
    except Exception as e:                           #to make sure db file exists
        print("file doesnt exist creating new database file")
        dbCreat.creat(dbname)
    c=con.cursor()#connect to db
    
    year=int(usnk[3:5])
    d=int(usnk[7])
    print(year,d,type(year) ,"\n\n\n\n")
    if year==14:
        if d==0:
            shm=2010
    elif year==15 or year==16 :
        if year==15 and d==4:
            shm=2010
        else:
            shm=2015
    elif year>=17:
        if year==17 and d==4:
            shm=2015
        else:
            shm=2017
    dpn=usnk[5:7]
    c.execute("SELECT dno FROM department WHERE dname='"+dpn+"';")
    dn=c.fetchall()
    dn=int((dn[0])[0])
    print(dn)
    
    #print(dpn,type(dpn) ,"\n\n\n\n")
    
    
    qry1="INSERT OR REPLACE INTO student VALUES(?,?,?,?,NULL,NULL,NULL);"  
    print(qry1)
    c.execute(qry1,[(usnk),(name),(shm),(dn)])
    
    
    qry1="INSERT OR REPLACE INTO marks VALUES(?,?,?,?,?,?);"  
    print(qry1)
    for i in range(0,len(mrks),6):
        print(mrks[i+1],usnk)
        c.execute(qry1,[(usnk),(mrks[i]),(mrks[i+2]),(mrks[i+3]),(mrks[i+4]),(mrks[i+5])])
        con.commit()
    
    
    c.execute("SELECT * FROM student;")
    print(c.fetchall())
    c.close()
    con.close()
    
    
    
    
def webScraping(dbname,urlnc='http://results.vtu.ac.in/vitaviresultnoncbcs/resultpage.php',urlc='http://results.vtu.ac.in/vitaviresultcbcs/resultpage.php',ulst=None,usn11="4ub14cs001",curSem=1,noStu=1):
    try:
        #print(usn11)
        URLnonCBCS=urlnc
        URLCBCS=urlc
        
        if ulst and type(ulst[1]) == type(1):
            print(ulst)
            for i in range(0,len(ulst),2):
                try:
                    print("list\n\n",ulst[i],ulst[i+1])
                    try:
                        mrks,name=parseVal(noStu,url1=URLCBCS,usn1=ulst[i],cSem=ulst[i+1])
                    
                    except Exception as e:
                        mrks,name=parseVal(noStu,url1=URLnonCBCS,usn1=ulst[i],cSem=ulst[i+1])
                    
                    if name :   
                        insertV(dbname,ulst[i],name,mrks)
                    
                    
                
                except Exception as e:
                    print(e)
                    continue
        elif ulst :
            print(ulst)
            for usnt in ulst:
                try:
                    print("list\n\n",usnt)
                    try:
                        mrks,name=parseVal(noStu,url1=URLCBCS,usn1=usnt,f=0)
                    
                    except Exception as e:
                        mrks,name=parseVal(noStu,url1=URLnonCBCS,usn1=usnt,f=0)
                    
                    if name :   
                        insertV(dbname,usnt,name,mrks)
                    
                    
                
                except Exception as e:
                    print(e)
                    continue
        
        else:
            USNList=[] #to fetch the usn from usnlist.txt
            
            with open("usnlist.txt",'r') as f:
                for lines in f.readlines():
                        USNList.append(lines.replace("\n",""))
            #print(USNList)
            
            for usn111 in USNList:
                
                    try:
                        #fetch the required info from first usn
                        
                        sem=0
                        print(usn111,"heyyyyyyyyyy",type(usn111))
                        if usn111=='4ub14cs001':
                            sem=parseSub(dbname,usn=usn111,url1=URLnonCBCS,cSem=curSem)
                        else:
                            
                            try:
                                
                                sem=parseSub(dbname,usn=usn111,url1=URLCBCS,cSem=curSem)
                                    #if sem is not 0:
                                        
                            except Exception as e:
                                for i in range(2,10): 
                                    try:
                                        usn2=usn111.split(usn111[-3])[0]+'00'+str(i)
                                        #print(usn2,"\n555555\n\n\n")
                                        sem=parseSub(dbname,usn=usn2,url1=URLCBCS,cSem=curSem)
                                        break;
                                    except Exception as e:
                                        print(e)
                                        continue
                            #print(subCode,subTitle,sem)
                        
                        
                        
                        k=int(usn111[3:5])+1
                        usnD=usn111[:3]+str(k)+usn111[5:7]
                        usnN=usn111[:7]+'0'
                        print(k,usnD,noStu,type(noStu))
                        noStu=int(noStu)
                        m1=[usnN + '0' + str(x) for x in range(1,10)]
                        m=[usnN + str(x) for x in range(10,noStu+1)]
                        
                        if noStu>30:
                            noStu=30
                        ds=[usnD + '40' + str(x) for x in range(1,10)]
                        ds1=[usnD + '4' + str(x) for x in range(10,noStu+1)]
                        print(k,usnD,usnN,noStu)
                        usnlist=m1+m+ds+ds1
                        
                        
                        
                        print("syed\n",usnlist)
                        
                        for usnt in usnlist:
                            try:
                                try:
                                    mrks,name=parseVal(noStu,url1=URLCBCS,usn1=usnt,cSem=sem)
                                #mrks1,usn71,name2=parseVal(noStu,url1=URLCBCS,usn1=usnD,k=True,cSem=sem)
                                #parseVal(noStu,url1=URLnonCBCS,usn1='4ub14cs',k=False,d='4',cSem=1)
                                   # name="akhil"
                                    #print(mrks,name)
                                    #remove after completion
                                except Exception as e:
                                    mrks,name=parseVal(noStu,url1=URLnonCBCS,usn1=usnt,cSem=sem)
                                #mrks1,usn71,name2=parseVal(noStu,url1=URLnonCBCS,usn1=usnD,k=True,cSem=sem)      
                                    #print(mrks,name)
                                    #remove after completion
                                if name :   
                                    insertV(dbname,usnt,name,mrks)
                                
                                
                            
                            except Exception as e:
                                print(e)
                                continue
                    
                    except Exception as e:
                        print(e)
                        continue
    
        
        
    except Exception as e:
        return e
   
if __name__ == "__main__":
#    k=['4ub15cs427', '4ub15cs428', '4ub15cs429']
    webScraping('studb7.db',curSem=1,noStu=1)





