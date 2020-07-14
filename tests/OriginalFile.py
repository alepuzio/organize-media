from PersonalLogging import PersonalLogging
from AsString import AsString
import os
from Extension import Extension
from Year import Year
from Topic import Topic
import unittest
from Month import Month
#from Name import Name
from Root import Root
from Filename import Filename
from TimeFile import TimeFile

class OriginalFile:
    '''@overview this class represent the logical representation of a file to copy'''
    def __init__(self, newabsolutepath, newfilename):
       self.log = PersonalLogging("OriginalFile", False)
       self.absolutepath = newabsolutepath
       self.filename = newfilename


    def tupla(self):
        '''@return the elementary data of the original file in tupla'''
        self.log.print(">OriginalFIle.tupla(" + self.physicalFileAsString() + ")")
        completeDateTime = TimeFile(self.physicalFileAsString()).complete()
        year = Year(completeDateTime)
        month = Month(completeDateTime)
        topic = Topic(self.absolutepath)
        filename = Filename(self.filename)
        extension = Extension(self.filename)
        root = Root(self.absolutepath )
        res = (year, month, topic, filename, extension, root)
        self.log.print("<" + str(res))
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
            year = Year(time)
            month = Month(time)
            topic = Topic (pathtmp)
            filename = Filename(filetmp)
            extension = Extension(filetmp)
            root = Root (pathtmp)
            expected = (year, month, topic, filename, extension, root)
            self.assertEqual(result, expected)
        
        def test_physicalFile(self):
            filename = OriginalFile(".\\resources\\lugano", "vecchia.jpg")
            result = filename.physicalFile()
            self.assertEqual(result, ".\\resources\\lugano\\vecchia.jpg")

