import unittest
import os
import sys
from coverage import coverage

# initialise coverage, this might need amending depending on your environment
cov = coverage(branch=True, omit=['flask/*', 'themonitor_test.py', '/Library/*', '/home/travis/virtualenv/*'])
cov.start()

# Add source home into python path and import themonitor.py
mypath = os.path.abspath('..')
sys.path.insert(0,mypath)
import themonitor
from Themonitor.themonitor import which_CCHost as Whost
from Themonitor.themonitor import nslookup as lookup

class ThemonitorTestCase(unittest.TestCase):
    def setUp(self):
        self.app = themonitor.app.test_client()
        pass

    def tearDown(self):
        pass

    def test_index(self):
        rv = self.app.get('/')
        assert "The Monitor" in rv.data

    def test_site(self):
        rv = self.app.get('/site')
        assert "stage.tools.bbc.co.uk" in rv.data

    def test_host(self):
        rv = self.app.get('/host')
        assert "mon" in rv.data

    def test_api_site(self):
        rv = self.app.get('/api/v1.0/site')
        assert "Active_site" in rv.data

    def test_api_whichCCHost(self):
        rv = self.app.get('/api/v1.0/host')
        assert "Active_CC_host" in rv.data

    def test_whichCCHost(self):
        rv = Whost()
        assert "mon"

    def test_whichSite(self):
        rv = lookup()
        assert "tools.bbc.co.uk"



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
