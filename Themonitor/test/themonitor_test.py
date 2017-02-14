import unittest
import os
import sys

# Add source home into python path and import themonitor.py
mypath = os.path.abspath('..')
sys.path.insert(0,mypath)
import themonitor

class ThemonitorTestCase(unittest.TestCase):
    def setUp(self):
        self.app = themonitor.app.test_client()
        pass

    def tearDown(self):
        pass

    def test_site(self):
        rv = self.app.get('/')
        assert "The Monitor" in rv.data

if __name__ == '__main__':
    unittest.main()
