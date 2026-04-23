import unittest
from app import app

class BasicTests(unittest.TestCase):
    def test_home(self):
        tester = app.test_client(self)
        response = tester.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'GitHub Actions is working!', response.data)

if __name__ == '__main__':
    unittest.main()