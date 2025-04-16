import sqlite3,time,sys
import hashlib


def login():
    m=hashlib.md5()
    
    while True:# for i in range(3):
        username = input("please enter your username: ")
        password = input("please enter your password: ")
        
        m.update(password.encode('utf-8'))
        hash1=m.hexdigest()
        del m
        
        with sqlite3.connect("logindata.db") as db:
            cursor = db.cursor()
        try:
            
            find_user =("SELECT * FROM user WHERE username = ? AND password = ?")
            cursor.execute(find_user,[(username),(hash1)])
            results = cursor.fetchall()

            if results:
                for i in results:
                    print("welcome "+i[2])
                    #return("exit")
                break
            
            else:
                print("Username amd password invalid")
                again =input("Do you want to try again?(y/n):")
                if again.lower() =="n":
                    print("Goodbye")
                    time.sleep(1)
                    #return("exit")
                    break
        except sqlite3.OperationalError as e:
            cursor.execute(" CREATE TABLE user(username text PRIMARY KEY,firstname text,surname text,password text);")
            db.commit()
    cursor.close()
    db.close()
    
def newUser():
    m=hashlib.md5()
    found = 0
    while found == 0:
        username = input("please enter a username: ")
        with sqlite3.connect("logindata.db") as db:
            cursor = db.cursor()
        try:
            findUser = ("SELECT * FROM user WHERE username = ?")
            cursor.execute(findUser,[(username)])

            if cursor.fetchall():
                print("Username is taken, please try again")
            else:
                found = 1;
                
        except sqlite3.OperationalError as e:
            cursor.execute(" CREATE TABLE user(username text PRIMARY KEY,firstname text,surname text,password text);")
            db.commit()
            
    firstname = input("Enter your first name: ")
    surname = input("Enter your surname: ")
    password = input("please enter your password: ")
    password1 = input("please enter your same password: ")
    while password != password1:
        print("Your password didn't match, please try again")
        password = input("please enter your password: ")
        password1 = input("please enter your same password: ")
    m.update(password.encode('utf-8'))
    hash2=m.hexdigest()
    insertdata = '''INSERT INTO user(username,firstname,surname,password)
    VALUES(?,?,?,?)'''
    cursor.execute(insertdata,[(username),(firstname),(surname),(hash2)])
    db.commit()
    cursor.close()
    db.close()
    del m

def menu():
    while True:
        print("Welcome to ....... ")
        menu =('''
        1 - Create New User
        2 - Login
        3 - Exit\n''')
        
        userchoice = input(menu)


        if userchoice == "1":
           newUser()

           
        elif userchoice == "2":
            login()
            
        elif userchoice == "3":
             print("Goodbye")
             sys.exit()
             
        else:            
           print("Command not in given choice ")

menu()
     
