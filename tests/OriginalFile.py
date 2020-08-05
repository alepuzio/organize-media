from PersonalLogging import PersonalLogging
from AsString import AsString
import os
from Extension import Extension
import unittest
from Month import Month
from TimeFile import TimeFile
from Time import Time
from Position import Position
from InitialData import InitialData

class OriginalFile:
    '''@overview this class represent the logical representation of a file to copy'''
    def __init__(self, newabsolutepath, newfilename):
       self.log = PersonalLogging("OriginalFile", False)
       self.absolutepath = newabsolutepath
       self.filename = newfilename

    def tupla(self):
        '''@return the elementary data of the original file in tupla'''
        self.log.print(">OriginalFIle.tupla(" + self.physicalFileAsString() + ")")
        completeDateTime = Time(TimeFile(self.physicalFileAsString()).complete())
        position = Position(self.absolutepath, self.filename)        
        res = InitialData(position, completeDateTime)
        self.log.print("<" + str(res.tupla()))
        return res
    
    def physicalFile(self):
        '''@return the complete path '''
        return self.absolutepath + os.sep + self.filename

    def physicalFileAsString(self):
        '''@return the complete path as String'''
        return AsString(self.physicalFile()).show()

    def __str__(self):
        return self.physicalFileAsString()
    
    def __repr__(self):
       return "OriginalFile(" +str(self.absolutepath) + "," + str(self.filename) + ")"
    
    def __eq__(self, other):
        return self.physicalFile() == self.physicalFile()




class TestOriginalFile(unittest.TestCase):
        
        def test_tupla(self):
            pathtmp = ".\\resources\\lugano"
            filetmp =  "vecchia.jpg"
            filename = OriginalFile( pathtmp, filetmp)
            result = filename.tupla() 
            time = "Wed Jun 10 17:04:28 2020"
            expected = ("2020", "06", "lugano", "vecchia", Extension("JPG"), ".\\resources")
            self.assertEqual(result, expected)
        
        def test_physicalFile(self):
            filename = OriginalFile(".\\resources\\lugano", "vecchia.jpg")
            result = filename.physicalFile()
            self.assertEqual(result, ".\\resources\\lugano\\vecchia.jpg")

