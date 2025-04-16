# -*- coding: utf-8 -*-
"""
Created on Mon Feb 19 16:10:52 2018

@author: SYED
"""
import sqlite3

def create(dbname):
    

    conn = sqlite3.connect(dbname)
    c = conn.cursor()
    
    # Create table
    c.execute('''CREATE TABLE IF NOT EXISTS student(
                                       USN text PRIMARY KEY,
                                       name text,
                                       scheme int,
                                       email text,
                                       phno integer)
                                       ''')
    
    
    
    c.execute('''CREATE TABLE IF NOT EXISTS csesub (
                                        subcode text PRIMARY KEY,
                                        subtitle text NOT NULL,
                                        sem integer NOT NULL)
                                       ''')
    
    
    c.execute(''' CREATE TABLE IF NOT EXISTS cseresult(
                                            USN text PRIMARY KEY,
                                            subcode text NOT NULL UNIQUE,
                                            internal integer NOT NULL,
                                            external text,
                                            total text,
                                            result text,
                                            FOREIGN KEY (subcode) REFERENCES csesub (subcode)
                                            FOREIGN KEY (USN) REFERENCES student (USN)
                                        )''')
    # Save (commit) the changes
    conn.commit()
    c.close()
    conn.close()
    
if __name__ == "__main__":
    create('E:\\VTUBroadSpec\\bin\\ubdt.db')