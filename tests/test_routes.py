import unittest
import os
import sys

topdir = os.path.join(os.path.dirname(__file__), "..")
sys.path.append(topdir)

from app import app

class TestRoutes(unittest.TestCase):
  def setUp(self):
    self.client = app.test_client()

  def test_index_page(self):
    res = self.client.get('/')
    self.assertEqual(res.status_code, 200)

if __name__ == '__main__':
    unittest.main()