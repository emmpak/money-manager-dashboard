import os
import unittest

from app import app, db
from app.models import User, Transfer

class TestRoutes(unittest.TestCase):
  def setUp(self):
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite://'
    db.create_all()

    self.client = app.test_client()

    u = User(username="username", email="username@mail.com")
    db.session.add(u)
    for _ in range(20):
      t = Transfer(currency="USD", amount=100, originator=u)
      db.session.add(t)
    db.session.commit()

  def tearDown(self):
    db.session.remove()
    db.drop_all()

  def test_index_page(self):
    res = self.client.get('/')
    self.assertEqual(res.status_code, 200)
    self.assertIn(b'Welcome back, Emil', res.data)
    self.assertIn(b'Transfer', res.data)

if __name__ == '__main__':
    unittest.main()