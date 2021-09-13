from flask import Flask, render_template, request, session, flash, redirect, url_for , g
import sqlite3

DATABASE = 'blog.db'
USERNAME = 'admin'
PASSWORD = 'admin'
SECRET_key = '8\x07\xa5\x87wW%\xda\xf3 \xae}\x9c\xcf\xfdbF\x96\x1c\xb8p\xd0\xac\xb1'

app = Flask(__name__)

app.config.from_object(__name__)

def connect_db():
  return sqlite3.connect(app.config['DATABASE'])

@app.route('/')
def login():
  return render_template('login.html')

@app.route('/main')
def main():
  return render_template('main.html')

if __name__ == '__main__':
  app.run(debug=True)
