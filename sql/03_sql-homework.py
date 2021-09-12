import sqlite3

conn = sqlite3.connect("cars.db")

# cursor = conn.cursor()

# rows = [
# ('Ford','Fiesta', 2345),
# ('Ford','Figo',3434),
# ('Ford', 'endevour',1234),
# ('Honda','Amaze',4556),
# ('Honda', 'city',8976)
# ]

# cursor.executemany("insert into inventory values(?,?,?)", rows)

# conn.commit()
# cursor.close()


#################################

# cursor = conn.cursor()
# cursor.execute("update inventory set Quantity = 2353 where make ='Ford' and model= 'Figo' ")
# conn.commit()
# cursor.close()


#################################

# cursor = conn.cursor()
# cursor.execute("select make,model, quantity from inventory where make ='Ford'")

# rows =  cursor.fetchall()

# for x in rows:
#   print(x)
#   

####################################

import sqlite3

with sqlite3.connect("new.db") as conn:
  cursor = conn.cursor()

  cursor.execute("CREATE TABLE regions ('city' TEXT, 'region' TEXT)")

  cities = [
  ('New York City', 'Northeast'),
  ('San Francisco', 'West'),
  ('Chicago', 'Midwest'),
  ('Houston', 'South'),
  ('Phoenix', 'West'),
  ('Boston', 'Northeast'),
  ('Los Angeles', 'West'),
  ('Houston', 'South'),
  ('Philadelphia', 'Northeast'),
  ('San Antonio', 'South'),
  ('San Diego', 'West'),
  ('Dallas', 'South'),
  ('San Jose', 'West'),
  ('Jacksonville', 'South'),
  ('Indianapolis', 'Midwest'),
  ('Austin', 'South'),
  ('Detroit', 'Midwest')
  ]

  cursor.executemany("INSERT INTO regions values(?, ?)", cities)

  cursor.execute("SELECT * FROM regions ORDER BY region ASC")

  rows = cursor.fetchall()

  for r in rows:
    print(r[0],r[1])
    