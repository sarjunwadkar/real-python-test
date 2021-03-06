from flask import Flask , render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_pyfile('_config.py')
db = SQLAlchemy(app)

from project.users.views import users_blueprint 
from project.tasks.views import tasks_blueprint

app.register_blueprint(users_blueprint)
app.register_blueprint(tasks_blueprint)

@app.errorhandler(404)
def not_found_error(error):
  return render_template('404.html'), 404


@app.errorhandler(500)
def internal_error(error):
  return render_template('500.html'), 500 
  