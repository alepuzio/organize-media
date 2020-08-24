from PersonalLogging import PersonalLogging
import unittest
import os



class NameINI:
    '''@overview: class about the name of the initial ini file of properties'''
    
    def __init__(self, new_directory):
        self.directory = new_directory
        self.logging = PersonalLogging("NameINI")

    def name(self):
        '''@return complete path of the file ini'''    
        self.logging.print("name1:" + str ( self.directory ) )
        self.logging.print("name2:" + str ( self.directory + os.sep ) )

        res = self.directory + os.sep + "common.ini"
        return res

class TestNameINI(unittest.TestCase):

    def test_name(self):
        var = NameINI("C:\\fake\\path")
        res = var.name()
        expected = "C:\\fake\\path\\common.ini"
        self.assertEqual(res, expected)
