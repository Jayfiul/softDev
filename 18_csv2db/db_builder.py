#The Bottlers (Jeff Chen, Yusha Aziz, Fang Chen)
#SoftDev  
#K18 :: SQLITE3 BASICS
#25 Oct 2022
#Time spent: 1.0 hrs

import sqlite3   #enable control of an sqlite database
import csv       #facilitate CSV I/O


DB_FILE="discobandit.db"

db = sqlite3.connect(DB_FILE) #open if file exists, otherwise create
c = db.cursor()               #facilitate db ops -- you will use cursor to trigger db events

#==========================================================

# if c.execute("select name from sqlite_schema where type = 'table'").fetchall() == []:

# CREATING COURSES
tbleName = "courses"
parameters = "code TEXT, mark INT, id INT"

command = (f"create table if not exists {tbleName} ({parameters})")
c.execute(command)

with open("./courses.csv") as file:
	reader = csv.DictReader(file)
	for row in reader:
		code = row['code']
		mark = row['mark']
		id = row['id']
		command = (f"insert into {tbleName} values(\"{code}\", {mark}, {id})")
		c.execute(command)

# CREATING STUDENTS
tbleName = "students"
parameters = "name TEXT, age INT, id INT"

command = (f"create table if not exists {tbleName} ({parameters})")
c.execute(command)

with open("./students.csv") as file:
	reader = csv.DictReader(file)
	for row in reader:
		name = row['name']
		age = row['age']
		id = row['id']
		command = (f"insert into {tbleName} values(\"{name}\", {age}, {id})")
		c.execute(command)

print(c.execute('select * from courses').fetchall())
print(c.execute('select * from students').fetchall())

#==========================================================

db.commit() #save changes
db.close()  #close database