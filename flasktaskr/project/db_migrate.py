from views import db 
from _config import DATABASE_PATH

import sqlite3 
from datetime import datetime 

with sqlite3.connect(DATABASE_PATH) as conn :

  cursor = conn.cursor()
  cursor.execute("ALTER TABLE tasks RENAME to old_tasks")

  db.create_all()

  cursor.execute("SELECT name, due_date, priority, status from old_tasks order by task_id asc")

  data = [
    (row[0], row[1], row[2], row[3], datetime.now(),1) for row in cursor.fetchall()
  ]

  cursor.executemany("""insert into tasks(name,due_date, priority,status, posted_date, user_id) VALUES(?,?,?,?,?,?)""", data)

  db.session.commit()
