from datetime import date 

from project import db 
from project.models import Task, User 

db.create_all()

db.session.add(User("admin", "admin@gmail.com", "admin", "admin"))


db.session.add(Task("Finish this tutorial", date(2019,9,21),10, date(2019,8,21),1,1))
db.session.add(Task("Finish Real Python", date(2020,8,8),5, date(2020,7,8), 10, 1))

db.session.commit()