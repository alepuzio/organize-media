from PersonalLogging import PersonalLogging
#from Name import Name
from AsString import AsString
import os
import unittest
from Month import Month
from Media import Media
from YearMonth import YearMonth
from OriginalFile import OriginalFile

class SingleFinalData:
    '''@ovewview this class represent the final data necessaryt ot run the copy of the original file'''

    def __init__(self, newroot, neworiginaltupla):
       self.log = PersonalLogging("SingleFinalData", False)
       self.root = newroot
       self.originaltupla = neworiginaltupla


    def tupla(self):
        '''trasform data of the original file in tupla'''
        self.log.print("tupla iniziale:\n" + AsString(self.originaltupla).show())
        #        self.log.print("tupla iniziale:-" + self.originaltupla + "-")
        # originaltupla (year, month, topic, filename, extension, root)
        year = self.originaltupla[0]
        self.log.print("year:" + year.show())
        month = self.originaltupla[1]
        self.log.print("month:" + month.show()) 
        yearmonth = YearMonth(year, month)
        topic = self.originaltupla[2] 
        filename = self.originaltupla[3]
        extension = self.originaltupla[4]
        root = self.root
        media = Media(self.originaltupla[4]).directory()
        return (root, year, yearmonth, topic, media, filename, extension)

    def physicalFile(self):
        '''return the complete path as String'''
        data = self.tupla()
        listdata = [data[0], data[1].show(), data[2].show(), data[3].show(), data[4], data[5].show()]
        path = os.sep.join(listdata[0:6])
        return AsString(path + "." + data[6].show() ).show()
        
    def __repr__(self):
        return "SingleFinalData[" + self.physicalFile() + "]\n>>>" + str(self.tupla())

    def __eq__(self, other):
        return self.physicalFile() == other.physicalFile()

class TestSingleFinalData(unittest.TestCase):
        
        def test_tupla_yearmonth(self):
            pathtmp = ".\\resources\\lugano"
            filetmp = "vecchia.jpg"
            originalFile = OriginalFile(pathtmp, filetmp)
            filename = SingleFinalData(".\\newoutput", originalFile.tupla())
            result = filename.tupla()
            self.assertEqual(result[2].show(), "202006")

        def test_tupla_name(self): 
            pathtmp = ".\\resources\\lugano"
            filetmp = "vecchia.jpg"
            originalFile = OriginalFile(pathtmp, filetmp)
            filename = SingleFinalData(".\\newoutput", originalFile.tupla())
            result = filename.tupla()
            self.assertEqual(result[5].show(), "vecchia")

        def test_tupla_year(self):
            pathtmp = ".\\resources\\lugano"
            filetmp = "vecchia.jpg"
            originalFile = OriginalFile(pathtmp, filetmp)
            filename = SingleFinalData(".\\newoutput", originalFile.tupla())
            result = filename.tupla()
            self.assertEqual(result[1].show(), "2020")

        def test_tupla_topic(self):
            pathtmp = ".\\resources\\lugano"
            filetmp = "vecchia.jpg"
            originalFile = OriginalFile(pathtmp, filetmp)
            filename = SingleFinalData(".\\newoutput", originalFile.tupla())
            result = filename.tupla()
            self.assertEqual(result[3].show(), "lugano")
        
        def test_tupla_extension(self):
            pathtmp = ".\\resources\\lugano"
            filetmp = "vecchia.jpg"
            originalFile = OriginalFile(pathtmp, filetmp)
            filename = SingleFinalData(".\\newoutput", originalFile.tupla())
            result = filename.tupla()
            self.assertEqual(result[6].show(), "jpg")
            
        def test_tupla_year(self):
            pathtmp = ".\\resources\\lugano"
            filetmp = "vecchia.jpg"
            originalFile = OriginalFile(pathtmp, filetmp)
            filename = SingleFinalData(".\\newoutput", originalFile.tupla())
            result = filename.tupla()
            self.assertEqual(result[1].show(), "2020")

        def test_tupla_directory_from_extension(self):
            pathtmp = ".\\resources\\lugano"
            filetmp = "vecchia.jpg"
            originalFile = OriginalFile(pathtmp, filetmp)
            filename = SingleFinalData(".\\newoutput", originalFile.tupla())
            result = filename.tupla()
            self.assertEqual(result[4], "JPG")
        
        def test_tupla_physicalFile(self):
            pathtmp = "D:\\workspacePython\\organize-set-microstock\\tests\\resources\\lugano"
            filetmp = "vecchia.jpg"
            originalFile = OriginalFile(pathtmp, filetmp)
            filename = SingleFinalData("C:\\users\\microstock\\newoutput", originalFile.tupla())
            result = filename.physicalFile()
            self.assertEqual(result, "C:\\users\\microstock\\newoutput\\2020\\202006\\lugano\\JPG\\vecchia.jpg")


