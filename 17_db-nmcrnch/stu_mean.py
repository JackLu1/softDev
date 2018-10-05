#Team Pepe2.0 -- Jack Lu, Bill Ni
#SoftDev1 pd8
#K16 - No Trouble
#2018-10-04

import sqlite3   #enable control of an sqlite database
import csv       #facilitates CSV I/O

# table = courses
# code, mark, id

# table = students
# name, age, id

db = sqlite3.connect('dbase.db') #open db of students
c = db.cursor()               #facilitate db ops

command = "SELECT name, students.id, mark FROM students, courses WHERE students.id = courses.id"
grades = c.execute(command)
for i in grades:
    print(i)

#grades = {}
#foo = c.execute("SELECT mark FROM courses WHERE id=1")
#for i in foo:
#    print(type(i))
#    print(i)

db.commit() #save changes
db.close()  #close database

