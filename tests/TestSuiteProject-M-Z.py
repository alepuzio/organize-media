import unittest 
from OriginalFile import TestOriginalFile
from YearMonth import TestYearMonth
from Media import TestMedia
from Month import TestMonth

class ConfigTestCase(unittest.TestCase):


    def setUp(self):
        print ('/**************setup****************/')

    def runTest(self):
        print ('>runtest')

def suite():
    """
    Gather all the tests from this module in a test suite.
    """
    test_suite = unittest.TestSuite()
    test_suite.addTest(unittest.makeSuite(ConfigTestCase))
    return test_suite

mySuit = suite()

runner = unittest.TextTestRunner(verbosity=3)
runner.run(mySuit)
