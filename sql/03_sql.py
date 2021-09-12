import sqlite3

with sqlite3.connect("new.db") as conn :
  cursor = conn.cursor()

  cities = [
  ('Boston', 'MA',343431), 
  ('Chicago', 'IL', 352522),
  ('Houston', 'TX', 23453),
  ('Phoneix', 'AZ', 344553)
  ]

  cursor.executemany("INSERT INTO population values(?,?,?)", cities)
