import unittest 

#from AbsolutePath import TestAbsolutePath
from AsString import TestAsString
from Control import TestControl
from Extension import TestExtension
from Filename import TestFilename
from GroupDirectory import TestGroupDirectory
#from GroupOriginalFiles import TestGroupOriginalFiles
from GroupReadFiles import TestGroupReadFiles
from ImageJPG import TestImageJPG
from Field import TestField






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
