import unittest
import os
from PersonalLogging import PersonalLogging
from OriginalFile import OriginalFile
from SingleFinalData import SingleFinalData
from SafeDirectory import SafeDirectory

class GroupDirectory:
    '''@overivew: this class create the new directory  fro mthe final data tupla'''

    def __init__(self, new_list_finaltupla):
        self.list_final_tupla = new_list_finaltupla
        self.logging = PersonalLogging("GroupDirectory", False)

    def various_directory(self):
        '''@return  the list of the new directory with complete path'''
        result = []
        for filetmp in self.list_final_tupla:
            self.logging.print("filetmp:" + str(filetmp))
            data_tmp = filetmp.tupla()
            self.logging.print("filetmp[0]:" + str(filetmp.tupla()[0]))
            data = ( data_tmp[0], data_tmp[1].show(), data_tmp[2].show(), data_tmp[3].show(), data_tmp[4], data_tmp[5].show() )
            limit = len(data)
            for place in range(1, limit ):
                result.append(os.sep.join(data[0:place]))
                self.logging.print(str(place) + ">" + str(result) )
            self.logging.print("filetmp:" + str(result ))
        return result

    def unique(self, listtmp):
        '''@return the list with 1 occurrence for every element'''
        result = set()
        listtmp.sort()
        for tmp in listtmp:
            result.add(tmp)
        return result

    def createDirectories(self, list_dir):
        '''crete all not existing directory'''
        for element in list_dir:
            possible_dir = SafeDirectory(element)
            possible_dir.create()
        self.logging.print("The directories are created on filesystem")


    def write(self):
        '''create the directory and doesn't modifiy the existing'''
        list_dir = self.various_directory()
        to_write = self.unique(list_dir)
        self.createDirectories(to_write)
        return to_write

class TestGroupDirectory(unittest.TestCase):

    def test_various_directory(self):
        pathtmp = ".\\resources\\lugano"
        filetmp = "vecchia.jpg"
        originalFile = OriginalFile(pathtmp, filetmp)
        filename = SingleFinalData(".\\newoutput", originalFile.tupla())
        list_singlefinaldata = []
        list_singlefinaldata.append(filename)

        result = GroupDirectory(list_singlefinaldata).various_directory()
        expected = []
        expected.append(".\\newoutput")
        expected.append(".\\newoutput\\2020")
        expected.append(".\\newoutput\\2020\\202007")
        expected.append(".\\newoutput\\2020\\202007\\lugano")
        expected.append(".\\newoutput\\2020\\202007\\lugano\\JPG")
        for place in range(0, len(result)):
            print(str(place) + ">" + str(result[place]) )
            
        self.assertEqual(result[0], expected[0])
        self.assertEqual(result[1], expected[1])
        self.assertEqual(result[2], expected[2])
        self.assertEqual(result[3], expected[3]) 
        self.assertEqual(result[4], expected[4])
        

