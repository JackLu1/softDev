#Team Tall_PPL: Jack Lu, Thomas Zhao
#SoftDev1 pd8
#K17 -- Average
#2018-10-05

import sqlite3   #enable control of an sqlite database

db = sqlite3.connect('dbase.db') #old db with info to use
c = db.cursor()

idandnames = {} #dict for id and names --> {id1: name1, id2: name2 ...}

def extractData():
    command0 = '''SELECT students.id, name, code, mark FROM students, courses 
    WHERE students.id = courses.id''' #only if a student is matched with a record in a course
    grades = c.execute(command0)
    return grades #returns data structure with each student's record in a course

def useData(data):
    idandgrades = {} #dict for id and grades --> {id1: [grade0, grade1], id2: [grade0, grade1, grade2] ...}

    for entry in data:

        #print '\n' + 'entry: ' + str(entry) + '\n'
        
        if entry[0] in idandgrades: #if id is already a key in the dict
            gradeList = idandgrades[entry[0]]
            gradeList.append(entry[3])
            idandgrades[entry[0]] = gradeList #appends the grade to the list
            
        else: #if id is NOT a key in the dict
            idandgrades[entry[0]] = [entry[3]] #creates key, value pair with list of that grade as the value
            idandnames[entry[0]] = [entry[1]] #adds key, value pair with name as value
        #print(idandgrades)
        #print(idandnames)
    #print idandgrades
    return idandgrades

def calcAverage(data): #adds up grades in list for each student and divides by len(listOfGrades)
    for entry in data:
        average = 0
        for grade in data[entry]:
            average = average + grade
        average = average / len(data[entry])
        data[entry] = average #reassigns value to be average

    #print data

    for i in idandnames: #displays requested info in terminal
        print 'NAME: ' + str(idandnames[i][0]) + ', ID: ' + str(i) + ', AVERAGE: ' + str(data[i])
    
    return data

def addData(tableData):
    make_avg_table = "CREATE TABLE peeps_avg (id INTEGER PRIMARY KEY, average INTEGER)"
    c.execute(make_avg_table)
    for i in tableData:
        cmd = 'INSERT INTO peeps_avg VALUES(?,?)'
        c.execute(cmd, (i, tableData[i]))

def addCourse(code, mark, id_num):
    cmd = 'INSERT INTO courses VALUES(?, ?, ?)'
    params = (code, mark, id_num)
    c.execute(cmd, params)

def main():
    grades = extractData()
    inputtedGrades = useData(grades)
    dataForTable = calcAverage(inputtedGrades)
    addData(dataForTable)
    addCourse('english', 55, 1)
    
#main()
addCourse('calc', 55, 1)

db.commit() #save changes
db.close()  #close database

