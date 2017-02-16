import unittest
import os
import sys
from coverage import coverage

# initialise coverage, this might need amending depending on your environment
cov = coverage(branch=True, omit=['flask/*', 'themonitor_test.py', '/Library/*'])
cov.start()

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

    def test_index(self):
        rv = self.app.get('/')
        assert "The Monitor" in rv.data

    def test_lookup(self):
        rv = self.app.get('/lookup')
        assert "stage.tools.bbc.co.uk" in rv.data

    def test_api_site(self):
        rv = self.app.get('/api/v1.0/site')
        assert "Active_site" in rv.data


if __name__ == '__main__':
    try:
        unittest.main()
    except:
        pass
    cov.stop()
    cov.save()
    print("\n\nCoverage Report:\n")
    cov.report()
    basedir = os.path.join(os.path.dirname(__file__), 'Themonitor')
    print("HTML version: " + os.path.join(basedir, "tmp/coverage/index.html"))
    cov.html_report(directory='tmp/coverage')
    #cov.erase()