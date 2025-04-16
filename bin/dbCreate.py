# -*- coding: utf-8 -*-
"""
Created on Fri Mar  2 22:31:34 2018

@author:BHARAT PRATAP S S ,SURAJ N RAIKAR AND SYED SULTAN S Q H H A 
"""


import sqlite3,time,sys
import hashlib
def create(dbname):
    
    with sqlite3.connect(dbname) as db:
        cursor = db.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS student(
                                           USN text PRIMARY KEY,
                                           name text NOT NULL,
                                           scheme int ,
                                           stdno text,
                                           email text,
                                           phno integer,
                                           
                                           FOREIGN KEY (scheme) REFERENCES maximum (scheme),
                                           FOREIGN KEY (stdno) REFERENCES department (dno));
                                           ''')
        
        cursor.execute('''CREATE TABLE IF NOT EXISTS department(
                                           dno  text PRIMARY KEY,
                                           dname   text,
                                           dtitle text,
                                           dofficeno int);
                                           ''')
        
        cursor.execute('''CREATE TABLE IF NOT EXISTS subject (
                                            subcode  text PRIMARY KEY,
                                            subtitle  text NOT NULL,
                                            sem integer NOT NULL,
                                            sjdno int,
                                            FOREIGN KEY (sjdno) REFERENCES department (dno));
                                           ''')
    
        cursor.execute('''CREATE TABLE IF NOT EXISTS maximum (
                                            scheme  text PRIMARY KEY,
                                            internal  text NOT NULL,
                                            external integer NOT NULL,
                                            mini project int,
                                            project int );
                                            ''')
    
        cursor.execute('''CREATE TABLE IF NOT EXISTS internal(
                                            iUSN  text PRIMARY KEY,
                                            first int,
                                            second int,
                                            third int,
                                            interavg int NOT NULL,
                                            scored int NOT NULL,
                                            subcode  text,
                                            FOREIGN KEY (iUSN) REFERENCES student (USN),
                                            FOREIGN KEY (subcode) REFERENCES subject (subcode));
                                            ''')
        
        cursor.execute('''CREATE TABLE IF NOT EXISTS marks(
                                                mUSN text PRIMARY KEY,
                                                internal integer NOT NULL,
                                                external text,
                                                total text,
                                                result char(1),
                                                FOREIGN KEY (mUSN) REFERENCES student (USN));
                                                ''')
        cursor.execute('''CREATE TABLE IF NOT EXISTS user(
                                                id INTEGER PRIMARY KEY AUTOINCREMENT,
                                                username  text UNIQUE,
                                                firstname  text NOT NULL,
                                                surname text NOT NULL,
                                                email text NOT NULL,
                                                priv int NOT NULL,
                                                password  text NOT NULL);
                                                ''')
        
        cursor.execute('''CREATE TABLE IF NOT EXISTS login_session(
                                                id INTEGER PRIMARY KEY,
                                                date DATE,
                                                start_time TIME,
                                                end_time TIME,
                                                FOREIGN KEY (id) REFERENCES user (id));
                                                ''')
                                                     
        
        
        db.commit()
        cursor.execute("SELECT * FROM user")
        print(cursor.fetchall())
        cursor.close()
        
    
    
    
 
def login(dbname):
    
    
    while True:# for i in range(3):
        username = input("please enter your username: ")
        password = input("please enter your password: ")
        with sqlite3.connect(dbname) as db:
            cursor = db.cursor()
                
        
            
        m=hashlib.md5()
        m.update(password.encode('utf-8'))
        hash0=m.hexdigest()
        m.update(hash0.encode('utf-8'))
        hash1=m.hexdigest()
        
        del m
        try:
            
            find_user =("SELECT * FROM user WHERE username = ? AND password = ? ;")
            cursor.execute(find_user,[(username),(hash1)])
            results = cursor.fetchall()

            if results:
                for i in results:
                    print("welcome user "+i[2])
                    #return("exit")
                break
            
            else:
                print("Username and password invalid")
                again =input("Do you want to try again?(y/n):")
                if again.lower() =="n":
                    print("see you later")
                    time.sleep(1)
                    #return("exit")
                    break
    
        except sqlite3.OperationalError as e:
            create(dbname)
        except Exception as e:
            print(e)
    cursor.close()
    db.close()
    
    
    
def newUser(dbname):
    m=hashlib.md5()
    found = 0
    while found == 0:
        username = input("please enter a username: ")
        with sqlite3.connect(dbname) as db:
                cursor = db.cursor()
        
        try:
            findUser = ("SELECT * FROM user WHERE username = ?")
            cursor.execute(findUser,[(username)])

            if cursor.fetchall():
                print("Username is taken, please try again")
            else:
                found = 1;
        
        except sqlite3.OperationalError as e:
            create(dbname)
        except Exception as e:
            print(e)
    firstname = input("Enter your first name: ")
    surname = input("Enter your lastname: ")
    password = input("please enter your password: ")
    password1 = input("please enter your password again: ")
    while password != password1:
        print("Your password didn't match, please try again!!!!!!")
        password = input("please enter your password: ")
        password1 = input("please enter your password again: ")
        
    m.update(password.encode('utf-8'))
    hash2=m.hexdigest()
    m.update(hash2.encode('utf-8'))
    hash3=m.hexdigest()
    
    insertdata = '''INSERT INTO user(username,firstname,surname,priv,password)
    VALUES(?,?,?,?,?)'''
    cursor.execute(insertdata,[(username),(firstname),(surname),(2),(hash3)])
    db.commit()
    cursor.close()
    db.close()
    del m

def setPriv(p,dbname):
    
    with sqlite3.connect(dbname) as db:
                c = db.cursor()
    c.execute("SELECT * FROM user;") 
    print(c.fetchall())          
    uid=input("Enter user id:\t")
    username=input("Enter username:\t")
    qry1="UPDATE user SET priv=? WHERE id=? AND username=? ;"
    c.execute(qry1,[(p),(uid),(username)])
    db.commit()
    c.close()
    db.close()
    
def menu(dbname):
    while True:
        print("Welcome to database ....... ")
        menu =('''
   1 - Create New User login
   2 - Login
   3 - set Privillage
   4 - Exit\n''')
        
        userchoice = input(menu)


        if userchoice == "1":
           newUser(dbname)

           
        elif userchoice == "2":
            login(dbname)
            
        elif userchoice == "3":
            p=input("Enter privilage (1/2):\t")
            #print(type(int(p)))
            if p == "1" or p == "2":
                setPriv(p,dbname)
            else:
                print("Privilage mismatch try again ")
        elif userchoice == "4":
             print("see you later")
             sys.exit()
             
        else:            
           print("Command not in given choice ")

if __name__ == "__main__":
    menu("studb2.db")
     
