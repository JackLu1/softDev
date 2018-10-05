#Team Pepe2.0 -- Jack Lu, Bill Ni
#SoftDev1 pd8
#K16 - No Trouble
#2018-10-04

import sqlite3   #enable control of an sqlite database
import csv       #facilitates CSV I/O


# --------------------------------- DB of courses -------------------------------------

DB_FILE="dbase.db"

db = sqlite3.connect(DB_FILE) #open if file exists, otherwise create
c = db.cursor()               #facilitate db ops

c.execute("CREATE TABLE courses(code TEXT, mark INTEGER, id INTEGER )")

with open("courses.csv") as csvfile:
    read = csv.DictReader(csvfile)
    for row in read:
        c.execute("INSERT INTO courses VALUES(\'{}\', {}, {})".format( row['code'], row['mark'], row['id'] ))

db.commit() #save changes
db.close()  #close database

# --------------------------------- DB of peeps -------------------------------------

dbase = sqlite3.connect('dbase.db')
cur = dbase.cursor()

cur.execute("CREATE TABLE students(name TEXT, age INTEGER, id INTEGER)")

with open("peeps.csv") as csvfile:
    read = csv.DictReader(csvfile)
    for row in read:
        cur.execute("INSERT INTO students VALUES(\'{}\', {}, {})".format( row['name'], row['age'], row['id'] ))

dbase.commit() #save changes
dbase.close()  #close database
