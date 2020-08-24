from PersonalLogging import PersonalLogging
import unittest
import os



class NameCSV:
    '''@overview: class about the name of the initial csv file of the files'''
    
    def __init__(self, new_directory, new_name_csv):
        self.logging = PersonalLogging("NameCSV")
        self.directory = new_directory
        self.namecsv = new_name_csv 

    def name(self):
        '''@return complete path of the file ini'''    
        res = self.directory + os.sep + self.namecsv.name()
        return res

class Manual:
    '''@overview: class with the data about the CSV to write manually'''
    def __init__(self):
        self.filename = "manual-data.csv"
    
    def name(self):
        return self.filename


class Final:
    '''@overview: class with the data about the CSV to write automatically'''
    def __init__(self):
        self.filename = "final-data-to-upload.csv"
    
    def name(self):
        return str(self.filename)


class TestNameCSV(unittest.TestCase):

    def test_name_manual(self):
        var = NameCSV("C:\\fake\\path", Manual()) 
        res = var.name()
        expected = "C:\\fake\\path\\manual-data.csv"
        self.assertEqual(res, expected)
    
    def test_name_final(self):
        var = NameCSV("C:\\fake\\path", Final()) 
        res = var.name()
        expected = "C:\\fake\\path\\final-data-to-upload.csv"
        self.assertEqual(res, expected)
