from views import db 
from models import Task
from datetime import date 

db.create_all()

db.session.add(Task("Finish this tutorial", date(2019,9,21),10, 1))
db.session.add(Task("Finish Real Python", date(2020,8,8), 10, 1))

db.session.commit()