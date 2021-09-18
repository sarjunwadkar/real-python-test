import os 
import sys 
print("hello world ", file=sys.stderr)
basedir = os.path.abspath(os.path.dirname(__file__))

DATABASE = 'flasktaskr.db'
USERNAME = 'admin'
PASSWORD = 'admin'
WTF_CSRF_ENABLED = True 
SECRET_KEY = ')g%\xea\x88*\x8b\xf8\x8e@(O5\x05g_\xe558\xa64\xf0\x83('

DATABASE_PATH = os.path.join(basedir, DATABASE)

#database uri 
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + DATABASE_PATH
