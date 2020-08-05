import unittest
from PersonalLogging import PersonalLogging
from AsString import AsString
import os
from Extension import Extension
from Month import Month
from TimeFile import TimeFile
from Time import Time
from Position import Position

class InitialData:
    '''@overview class about hthe data of the read files'''

    #TODO change form POJO to object, add some kind of logic
    def __init__(self, newposition , newtime):
        self.time = newtime
        self.position = newposition
        self.log = PersonalLogging("IntialData", False)

    def tupla(self):
        '''@return the elementary data of the original file in tupla'''
        self.log.print(">InitialData.tupla(" + str(self.position) + ")")
        day = self.time.day()
        year = self.time.year()
        month = self.time.month()
        topic = self.position.topic()
        name = self.position.name()
        extension = self.position.extension()#.name()
        root = self.position.root()
        res = (year, month, topic, name, extension, root, day)
        self.log.print( "<" + str(res ))
        return res


    def __str__(self):
        return self.position
    
    def __repr__(self):
       return "InitialData(" +str(self.time) + "," + str(self.position) + ")"
    
    def __eq__(self, other):
        return self.position == self.position




class TestInitialData(unittest.TestCase):
        
        def test_tupla(self):
            pathtmp = ".\\resources\\lugano"
            filetmp =  "vecchia.jpg"
            filename = InitialData ( Position( pathtmp, filetmp ), Time ( TimeFile (  pathtmp + os.sep + filetmp ).complete() ) )    
            result = filename.tupla() 
            time = "Wed Aug 3 17:04:28 2020"
            year = "2020"
            month = Month("Aug")
            topic = "lugano"
            filename = "vecchia"
            extension = Extension("jpg")
            root = ".\\resources"
            day = "3"
            expected = (year, month, topic, filename, extension, root, day)
            self.assertEqual(result, expected)
        

