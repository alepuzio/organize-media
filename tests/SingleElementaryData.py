from PersonalLogging import PersonalLogging
#from Name import Name
from AsString import AsString
import os
import unittest
from Month import Month
from Media import Media

class SingleElementaryData:
    '''@overwview this class represent the elementary data necessaryt ot run the copy of the original file'''
    def __init__(self, newroot, neworiginalFile):
       self.log = PersonalLogging("SingleFinalData", False)
       self.root = newroot
       self.originaltupla = neworiginaltupla


    def tupla(self):
        '''trasform data of the original file in tupla'''
        self.log.print("tupla iniziale:\n" + AsString(self.originaltupla).show())
        #        self.log.print("tupla iniziale:-" + self.originaltupla + "-")
        # originaltupla (year, month, topic, filename, extension, root)
        year = self.originaltupla[0]
        self.log.print("year:" + year)
        month = self.originaltupla[1]
        self.log.print("month:" + month) 
        finalmonth =  Month(month).number()
        yearmonth = AsString(year + finalmonth).show()
        topic = self.originaltupla[2] 
        filename = self.originaltupla[3]
        extension = self.originaltupla[4]
        root = self.root
        media = Media(self.originaltupla[4]).directory()
        return (root, year, yearmonth, topic, media, filename, extension)

    def physicalFile(self):
        '''return the complete path as String'''
        data = self.tupla()
        path  = os.sep.join(data[0:6])
        return AsString(path + "." + data[6] ).show()
    #TODO sistemare il __repr__() e __str__()

class TestSingleFinalData(unittest.TestCase):
        
        def test_tupla_yearmonth(self):
            element = ("2020", "Jun", "lugano", "noemfile", "jpg", ".\\resources")
            filename = SingleFinalData(".\\nuova", element)
            result = filename.tupla()
            self.assertEqual(result[2], "202006")

        def test_tupla_name(self): 
            element = ("2020", "Jun", "lugano", "noemfile", "jpg", ".\\resources")
            filename =  SingleFinalData(".\\", element)
            result = filename.tupla()
            self.assertEqual(result[5], "noemfile")

        def test_tupla_year(self):
            element = ("2020", "Jun", "lugano", "noemfile", "jpg", ".\\resources")
            filename =  SingleFinalData(".\\", element)
            result = filename.tupla()
            self.assertEqual(result[1], "2020")

        def test_tupla_topic(self):
            element = ("2020", "Jun", "lugano", "noemfile", "jpg", ".\\resources")
            filename = SingleFinalData(".\\", element)
            result = filename.tupla()
            self.assertEqual(result[3], "lugano")
        
        def test_tupla_extension(self):
            element = ("2020", "Jun", "lugano", "noemfile", "jpg", ".\\resources")
            filename = SingleFinalData(".\\", element)
            result = filename.tupla()
            self.assertEqual(result[6], "jpg")
            
        def test_tupla_year(self):
            element = ("2020", "Jun", "lugano", "noemfile", "jpg", ".\\resources")
            filename = SingleFinalData(".\\", element)
            result = filename.tupla()
            self.assertEqual(result[1], "2020")

        def test_tupla_directory_from_extension(self):
            element = ("2020", "Jun", "lugano", "noemfile", "jpg", ".\\resources")
            filename =  SingleFinalData(".\\", element)
            result = filename.tupla()
            self.assertEqual(result[4], "JPG")
        
        def test_tupla_physicalFile(self):
            element = ("2020", "Jun", "lugano", "noemfile", "jpg", ".\\resources")
            filename =  SingleFinalData(".\\output", element)
            result = filename.physicalFile()
            self.assertEqual(result, ".\\output\\2020\\202006\\lugano\\JPG\\noemfile.jpg")


