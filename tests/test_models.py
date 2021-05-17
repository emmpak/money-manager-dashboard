import os
import unittest

from config import basedir
from app import app, db
from app.models import User, Transfer

TEST_DB = 'test.db'

class TestModels(unittest.TestCase):
  def setUp(self):
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, TEST_DB)
    self.client = app.test_client()
    db.create_all()

  def tearDown(self):
    db.session.remove()
    db.drop_all()

  def test_user_creation(self):
    u = User(username="user", email="user@example.com")
    db.session.add(u)
    db.session.commit()
    users = User.query.all()
    self.assertEqual(len(users), 1)
  
  def test_password(self):
    u = User(username="user", email="user@example.com")
    p = "test"
    u.set_password(p)
    self.assertTrue(u.check_password(p))
    self.assertFalse(u.check_password('t'))

  def test_transfer_creation(self):
    u = User(username="user", email="user@example.com")
    db.session.add(u)
    db.session.commit()
    t = Transfer(currency="GBP", amount=100, originator=u)
    transfers = Transfer.query.all()
    self.assertEqual(len(transfers), 1)
