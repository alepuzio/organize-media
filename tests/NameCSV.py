from PersonalLogging import PersonalLogging
import unittest
import os



class NameCSV:
    '''@overview: class about the name of the initial csv file of the files'''
    
    def __init__(self, new_directory):
        self.directory = new_directory
        self.logging = PersonalLogging("NameCSV")

    def name(self):
        '''@return complete path of the file ini'''    
        res = self.directory + os.sep + "images.csv"
        return res

class TestNameCSV(unittest.TestCase):

    def test_name(self):
        var = NameCSV("C:\\fake\\path")
        res = var.name()
        expected = "C:\\fake\\path\\images.csv"
        self.assertEqual(res, expected)
