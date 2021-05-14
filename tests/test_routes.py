import os
import unittest

from app import app

class TestRoutes(unittest.TestCase):
  def setUp(self):
    self.client = app.test_client()

  def test_index_page(self):
    res = self.client.get('/')
    self.assertEqual(res.status_code, 200)
    self.assertIn(b'Welcome back, Emil', res.data)

if __name__ == '__main__':
    unittest.main()