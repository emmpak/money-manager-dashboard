import os
import unittest

from config import basedir
from app import app, db
from app.models import User

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

