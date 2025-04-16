import sqlite3

def create(dbname):
    

    conn = sqlite3.connect(dbname)
    c = conn.cursor()
    
    # Create table
    c.execute('''CREATE TABLE IF NOT EXISTS student(
                                       USN text PRIMARY KEY,
                                       name text NOT NULL,
                                       scheme int NOT NULL,
                                       email text,
                                       phno integer);
                                       ''')
    c.execute('''CREATE TABLE IF NOT EXISTS department(
                                       depnumber text PRIMARY KEY,
                                       depname text,
                                       depofficeno int);
                                       ''')
    c.execute('''CREATE TABLE IF NOT EXISTS subject (
                                        subcode text PRIMARY KEY,
                                        subtitle text NOT NULL,
                                        sem integer NOT NULL,
                                        depnumber text);
                                       ''')
    c.execute(''' CREATE TABLE IF NOT EXISTS internal(
                                        USN text PRIMARY KEY,
                                        first int,
                                        second int,
                                        third int,
                                        interavg int NOT NULL,
                                        scored int NOT NULL,
                                        FOREIGN KEY (USN) REFERENCES student (USN));
                                        ''')
    c.execute(''' CREATE TABLE IF NOT EXISTS result(
                                            USN text PRIMARY KEY,
                                            depname text,
                                            subcode text NOT NULL UNIQUE,
                                            internal integer NOT NULL,
                                            external text,
                                            total text,
                                            result text,
                                            FOREIGN KEY (depname) REFERENCES department (depnumber)
                                            FOREIGN KEY (subcode) REFERENCES subject (subcode)
                                            FOREIGN KEY (USN) REFERENCES student (USN))
                                            ;''')
                                          
    # Save (commit) the changes
    conn.commit()
    c.close()
    conn.close()
    
if __name__ == "__main__":
    create('E:ubdt.db')
