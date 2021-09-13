import sqlite3

with sqlite3.connect("blog.db") as conn:
  cursor = conn.cursor()

  cursor.execute("""CREATE TABLE posts (title TEXT, post TEXT) """)

  cursor.execute('insert into posts values("Good", "I m good")')
  cursor.execute('insert into posts values("Well", "I m well")')
  cursor.execute('insert into posts values("Excellent", "I m excellent")')
  cursor.execute('insert into posts values("Okay", "I am okay")')
  

