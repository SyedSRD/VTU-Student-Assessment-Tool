# -*- coding: utf-8 -*-
"""
Created on Tue Feb 20 16:40:41 2018

@author: surajnraikar
"""

import sqlite3
conn = sqlite3.connect('surajpro.db')
c = conn.cursor()

# Create table
c.execute('''CREATE TABLE student(
                                   USN text PRIMARY KEY,
                                   NAME text,
                                   SEM integer,
                                   SCHEME text,
                                   EMAIL_ID text,
                                   MOB_NO integer)
                                   ''')



c.execute('''CREATE TABLE CseSub (
                                    SUBCODE PRIMARY KEY,
                                    NAME text NOT NULL,
                                    SUBTITLE text NOT NULL,
                                    SEM integer NOT NULL)
                                   ''')


c.execute(''' CREATE TABLE CseResult(
                                        USN text PRIMARY KEY,
                                        INTERNAL integer NOT NULL,
                                      EXTERNAL integer text,
                                       TOTAL text,
                                       RESULT text,
                                       SUBCODE integer,
                                        FOREIGN KEY (USN) REFERENCES student (USN)
                                    )''')
# Save (commit) the changes
conn.commit()

conn.close()