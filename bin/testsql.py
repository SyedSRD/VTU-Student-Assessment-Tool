# -*- coding: utf-8 -*-
"""
Created on Wed May  9 08:44:31 2018

@author: SYED
"""
#import csv
#lt=[]
#with open('USN_RV.csv', 'r') as f:
#  reader = csv.reader(f,delimiter=',')
#  lt = list(reader)
#print((lt[0:-1])[0])

#import urllib
#import urllib3
#from bs4 import BeautifulSoup
#url = 'http://results.vtu.ac.in/vitaviresultcbcs/resultpage.php'
#payload = {'lns':"4ub15cs001"}
#
###
##http = urllib3.PoolManager()
##
##r = http.request('POST', 'http://results.vtu.ac.in/vitaviresultnoncbcs/resultpage.php',
##                 body=payload)
##print(r.read())
##
##print(usn,url )
#data = urllib.parse.urlencode(payload)
#print(data)
#data = data.encode('ascii')
#print(data)
#r= urllib.request.urlopen(url, data).read() 
#
#bs=BeautifulSoup(r,'html.parser')
#try:
#        
#        #print(bs,"\n\n")
#        yt=[]
#        yk=[]
#        bc=bs.findAll('div')
#        #print(bc,"\n\n7777777\n")
#        
#        bc=str(bc).split('Semester')[1].split('</b>')[0].replace(' ','').replace(':','')
#        print(bc,"\n\n7777777\n\n\n\n\n\n\n\n\n")
#        #if(bc==str(cSem)):
#            
#        tag=bs.find('div',{'class':"divTableBody"}).findAll('div',{'class',"divTableRow"}) #parse to get td
#       #print(tag,"\n\n7777777\n")
#        for t in tag:
##            print (t,'\ntt\n')
#            
#            s=str(t).split('<div class="divTableCell"')#[1].split('</div>')[0]
#            sk=s[1].split('</div>')[0].split('>')[1]
#            
#            #print (s,sk,'\nmkkmm\n')
#            st=s[2].split('>')[1].split('</div')[0]
#            #print (st,'\nmmm\n')
#            st=st.replace(' &amp; ',' and ')
##            print (st,'\n')
#            yk.append(sk)
#            yt.append(st)
    
       # print (y,'\n')
       # print (len(y),'\n\n\n\n\n')
    
        #redundent
    #    for x in range(0,len(yt),2):
    #        if x>1:
    #            subjects.insert(x-1,yt[x]+' : '+yt[x+1])
    #        else:
    #            subjects.insert(x,yt[x]+' : '+yt[x+1])
#        del yk[0]
#        del yt[0]
##        print(yk,yt,type(bc))
#except Exception as e:
#        print("*****Network Broken**kkkkkkkkkkk***",e)
#        pass
##import requests
import sqlite3
#try:
#    s=[]
#    con= sqlite3.connect("studb7.db")
#    c=con.cursor()
#    qry="SELECT musn,sem FROM marks as m,subject as s WHERE m.msubcode=s.subcode AND m.result='F';"
#    c.execute(qry)
#    sem=c.fetchall()
#    for x in sem:
##        s.append((x[0],x[1]))
#        s=s+list(x)
#    print(s,type(s[1]))
#    if type(s[1])== type(1):
#        print("yes")
#    c.close()
#    con.close()
#except Exception as e:
#    print(e)                       
#
#

#
#payload = {'usn':"4ub14cs057"}
#r=requests.post("http://results.vtu.ac.in/vitaviresultnoncbcs/resultpage.php", data=payload)
#with open("4ub15cs0057.html","w") as f:
#    f.write(r.content)

##php=open(usnF,'rb').read().decode()
#print(r.encoding,r.text)
#bs=BeautifulSoup(r.text,'html.parser')
#bc=bs.findAll('div')
##print(bs)
#bc=str(bc).split('Semester')[1].split('</b>')[0].replace(' ','').replace(':','')
#tag=bs.find('div',{'class':"divTableBody"}).findAll('div',{'class',"divTableRow"}) #parse to get td
##print(bc,tag)
#k=[]
#y=[]
#for t in tag[1:]:
#                    
#    print(t)
#    for s in t.findAll('div',{'class':"divTableCell"}):
#        #s=t.findAll('div',{'class':"divTableCell"})
#        print(s)
#        k.append(s.text)
#
#mrks=k
#print(mrks)
#for i in range(0,len(mrks),6):
#    print(mrks[i],mrks[i+2],mrks[i+3],mrks[i+4],mrks[i+5])
#sm=bs.findAll('div',{'style':"text-align:center;padding:5px;"})
#tag=bs.findAll('div',{'class':"divTableBody"})[1].findAll('div',{'class',"divTableRow"}) #parse to get td
#print(tag)
#k=[]
#for t in tag[1:]:
#    print(t)
#    for s in t.findAll('div',{'class':"divTableCell"}):
#        #s=t.findAll('div',{'class':"divTableCell"})
#        k.append(s.text)
#        
#print(k)
#for i in range(0,10,2):
#    print(i)
#n=15
#if n>30:
#    n=30
#print( n)
#
#try:
#    
#    
#     payload = {'lsn':"4ub14cs058"}
#     r=requests.post("http://results.vtu.ac.in/vitaviresultnoncbcs/resultpage.php", data=payload)
#     print(r)
#     bs=BeautifulSoup(r.content,'html.parser')
#     bc=bs.findAll('div')
#     print(bc)
##
##
#         
##                conn= sqlite3.connect("studb7.db")
##                c=conn.cursor()
##                uname="syed"
##                _defaultHmPgURL=c.execute("SELECT value FROM setting WHERE name='homeurl';").fetchone()
##            
###                c.execute(qry)
###                r=c.fetchall()
###                r=int((r[0])[0])
##                print(_defaultHmPgURL)
##                c.close()
##                conn.close()  
#except Exception as e:
#    print("155\t",e)




#usnk='4ub16cs401'
#year=int(usnk[3:5])
#d=int(usnk[7])
#print(year,d,type(year) ,"\n\n\n\n")
#if year==14:
#    if d==0:
#        shm=2010
#elif year==15 or year==16 :
#    if year==15 and d==4:
#        shm=2010
#    else:
#        shm=2015
#elif year>=17:
#    if year==17 and d==4:
#        shm=2015
#    else:
#        shm=2017
#dpn=usnk[5:7]
#print(shm)



con= sqlite3.connect("studb7.db")
c=con.cursor()
#qry="SELECT name,max(mks) FROM (SELECT name,sum(m.total)as mks FROM student s,marks m ,subject ss WHERE USN=mUSN AND msubcode=subcode AND ss.sem=7 GROUP BY mUSN )"
#qry="SELECT count(mks) FROM (SELECT sum(m.total)as mks FROM student s,marks m ,subject ss WHERE USN=mUSN AND msubcode=subcode AND ss.sem=7 GROUP BY mUSN ) WHERE mks>552"
qry="SELECT count(*) FROM marks m ,subject ss WHERE msubcode=subcode AND ss.sem=5 GROUP BY subcode"
c.execute(qry)
name=c.fetchone()
print(name[0])



