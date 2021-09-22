import os 
import unittest 
import sys 

from views import app, db 
from _config import basedir 
from models import User, Task 

TEST_DB = 'test.db'

class AllTests(unittest.TestCase):
  
  def setUp(self):
    app.config['TESTING'] = True 
    app.config['WTF_CSRF_ENABLED'] = False 
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, TEST_DB)
    self.app = app.test_client()
    db.create_all()

  def tearDown(self):
    db.session.remove()
    db.drop_all()
    
  # def test_user_setup(self):
  #   new_user = User('michael', 'michael@gmail.com', 'michaelpwd')
  #   db.session.add(new_user)
  #   db.session.commit()
  #   result = db.session.query(User).all()
  #   for r in result:
  #     r.name 
  #   assert r.name == "michael"   

  # def test_form_is_present(self):
  #   response = self.app.get('/')
  #   self.assertEqual(response.status_code, 200)
  #   print("resp data {}".format(response.data, file=sys.stderr))
  #   self.assertIn(b'Please login to access your task list.', response.data)


  def login(self, name, password):
    return self.app.post('/', data=dict(name=name,password=password), follow_redirects=True)
  
  # def test_users_cannot_login_unless_registered(self):
  #   response = self.login('foo', 'bar')
  #   self.assertIn(b'Invalid username or password', response.data)


  # # test register user 
  # def register(self, name, email, password, confirm):
  #   return self.app.post('register/',
  #       data=dict(name=name, email=email, password=password, confirm=confirm),
  #       follow_redirects=True
  #     )

  # def test_users_can_login(self):
  #   self.register('Michael', 'michael@realpython.com', 'pythonpwd', 'pythonpwd')
  #   response = self.login('Michael', 'pythonpwd')
  #   self.assertIn(b'Welcome!', response.data)

  # def test_invalid_form_data(self):
  #   self.register('swanand', 'swanand@gmail.com', 'swapwd', 'swapwd')
  #   response = self.login('wronguser', 'foopwd')
  #   self.assertIn(b'Invalid username or password.', response.data)


  # def test_form_is_present_on_register_page(self):
  #   response = self.app.get('register/')
  #   self.assertEqual(response.status_code, 200)
  #   self.assertIn(b'Please register to access the task list.', response.data)

  # def test_user_registration(self):
  #   #self.app.get('register/', follow_redirects=True)
  #   resp = self.register('Michael', 'michael@realpython.com', 'python', 'python')
  #   self.assertIn(b'Thanks for registering. Please login.', resp.data)

  # # users can log out 
  # def logout(self):
  #   return self.app.get('logout/', follow_redirects=True)


  # def test_logged_in_users_can_logout(self):
  #   self.register('Fletcher', 'fletcher@realpython.com', 'python101', 'python101')
  #   self.login('Fletcher', 'python101')
  #   resp = self.logout()
  #   self.assertIn(b'Goodbye', resp.data)

  # def test_not_logged_in_users_cannot_logout(self):
  #   resp = self.logout()
  #   self.assertNotIn(b'Goodbye', resp.data)

  # def test_logged_in_users_can_access_tasks_page(self):
  #   self.register('Fletcher', 'fletcher@realypython.com', 'python101', 'python101')
  #   self.login('Fletcher', 'python101')
  #   resp = self.app.get('tasks/')
  #   self.assertEqual(resp.status_code, 200)
  #   self.assertIn(b'Add a new task:', resp.data)


  # # tasks 

  def create_user(self, name, email, password):
    new_user = User(name=name, email=email, password=password)
    db.session.add(new_user)
    db.session.commit()

  def create_task(self):
    return self.app.post('add/', data=dict(
      name='Go to the bank',
      due_date = '10/08/2019',
      priority = '1',
      posted_date = '10/08/2016',
      status='1'
      ),
      follow_redirects=True)

  # # user can add tasks 

  def test_users_can_add_tasks(self):
    self.create_user('Michael', 'michael@realpython.com', 'python')
    self.login('Michael', 'python')
    self.app.get('tasks/', follow_redirects=True)
    resp = self.create_task()
    self.assertIn(b'new entry was succesfully posted. Thanks', resp.data)


  def test_users_cannon_add_tasks_when_error(self):
    self.create_user('Michael', 'michael@realpython.com', 'python')
    self.login('Michael', 'python')
    self.app.get('tasks/', follow_redirects=True)
    resp = self.app.post('add/', data=dict(name='Go to the bank',
      due_date='',
      priority='1',
      posted_date='19/05/2016',
      status='1'), follow_redirects=True)

    self.assertIn(b'All fields are required.', resp.data)

  # user can complete tasks 
  def test_users_can_complete_tasks(self):
    self.create_user('Michael', 'michael@realpython.com', 'python')
    self.login('Michael', 'python')
    self.app.get('tasks/', follow_redirects=True)
    self.create_task()
    

    resp = self.app.get('complete/1/', follow_redirects=True)
    self.assertIn(b'The task is complete. Nice.', resp.data) 

  # # user can delete tasks 
  

  def test_user_can_delete_tasks(self):
    self.create_user('Michael', 'michael@realpython.com', 'python')
    self.login('Michael', 'python')
    self.app.get('tasks/', follow_redirects=True)
    result = self.create_task()
    
    resp = self.app.get('delete/1', follow_redirects=True)
    self.assertIn(b'The task was deleted', resp.data)

if __name__ == "__main__":
  unittest.main()
