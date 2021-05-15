import os
import unittest
from flask import session

from app import app, db
from app.models import User, Transfer

class TestRoutes(unittest.TestCase):
  def setUp(self):
    app.config['TESTING'] = True
    app.config['WTF_CSRF_ENABLED'] = False
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite://'
    db.create_all()

    self.client = app.test_client()

    u = User(username="user", email="username@mail.com")
    u.set_password("test")
    db.session.add(u)
    for _ in range(20):
      t = Transfer(currency="USD", amount=100, originator=u)
      db.session.add(t)
    db.session.commit()

  def tearDown(self):
    db.session.remove()
    db.drop_all()

  def test_index_page(self):
    res = self.login()
    self.assertEqual(res.status_code, 200)
    self.assertIn(b'Welcome back, user', res.data)
    self.assertIn(b'Transfer', res.data)

  def test_index_page_anonymous(self):
    res = self.client.get('/')
    self.assertEqual(res.status_code, 302)

  def test_index_page_redirect(self):
    res = self.client.get('/', follow_redirects=True)
    self.assertEqual(res.status_code, 200)
    self.assertIn(b'Log In', res.data)

  def test_login_paget(self):
      res = self.client.get('/login')
      self.assertEqual(res.status_code, 200)
      self.assertIn(b'Log In', res.data)

  def test_log_out_page(self):
    self.login()
    res = self.logout()
    self.assertEquals(res.status_code, 200)
    self.assertIn(b'Log In', res.data)

  def login(self):
    return self.client.post('/login', data={'username': 'user', 'password': 'test'}, follow_redirects=True)

  def logout(self):
    return self.client.get('/logout', follow_redirects=True)

if __name__ == '__main__':
    unittest.main()