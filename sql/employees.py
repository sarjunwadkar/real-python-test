import csv
import sqlite3

# with sqlite3.connect("new.db") as conn :
#   cursor = conn.cursor()

#   employees = csv.reader(open("employees.csv", "r"))

#   cursor.execute("create table employees(firstname TEXT, lastname TEXT)")

#   cursor.executemany("insert into employees(firstname, lastname) values(?,?)", employees)

#############################################

# conn = sqlite3.connect("new.db")
# cursor = conn.cursor()

# try:
#   cursor.execute("INSERT INTO population2 values('kolhapur','IN',567463)")
#   cursor.execute("INSERT INTO population2 values('Mumbai','IN',1727463)")

# except sqlite3.OperationalError:
#   print("Oops something went wrong. try again...")

# conn.close()

##############################################

# import sqlite3

# with sqlite3.connect("new.db") as conn :
#   c = conn.cursor()

#   for row in c.execute("SELECT firstname, lastname from employees"):
#       print(row)

###############################################

import sqlite3 

with sqlite3.connect("new.db") as conn :
  cursor = conn.cursor()

  cursor.execute("SELECT firstname, lastname from employees")

  rows = cursor.fetchall()

  for r in rows:
    print(r[0],r[1])
    

