import unittest
from PersonalLogging import PersonalLogging
from OriginalFile import OriginalFile
from SingleFinalData import SingleFinalData

from functools import reduce
class ImageJPG:
    '''@overview: class to select the JPG image'''

    def __init__(self, new_list_singledata_or_final_files):
        self.data =  new_list_singledata_or_final_files
        self.logging = PersonalLogging ("ImageJPG", False)

    def destination_single_data(self):
        '''@return the absolute paht of the copied files'''
        typemedia = ["jpg", "JPG"]
        self.logging.print("destination_single_data():" + str( self.data))
        filter_extension = list ( filter ( lambda x: x.tupla()[6].show() in typemedia, self.data))
        self.logging.print("filter_extension:" + str(filter_extension))
        directory =  reduce ( lambda x : x.tupla()[5].show(), filter_extension)
        self.logging.print("result:" + str( directory ))
        result = directory.physicalPath()
        return result

    def list_filename(self):
        '''@return the list of the copied filenames'''
        typemedia = ["jpg", "JPG"]
        filter_extension = list ( filter ( lambda x: x.tupla()[6].show() in typemedia, self.data))
        self.logging.print("filter_extension:" + str(filter_extension))
        result = []
        for tmp in  filter_extension:
            result.append(tmp.tupla()[5].show() +"." + tmp.tupla()[6].show() )
        return result

class TestImageJPG(unittest.TestCase):


    def test_destinazione_singledata(self):
        pathtmp = ".\\resources\\lugano"
        filetmp = "vecchia.jpg"
        originalFile = OriginalFile(pathtmp, filetmp)
        singledata = SingleFinalData(".\\newoutpiut", originalFile.tupla())
        list_final_data = []
        list_final_data.append(singledata)
        var = ImageJPG(list_final_data)
        result = var.destination_single_data()
        expected = ".\\newoutpiut\\2020\\202007\\lugano\\JPG"
        self.assertEqual(result ,expected)


    def test_list_filename(self):
        pathtmp = ".\\resources\\lugano"
        filetmp1 = "vecchia.jpg"
        filetmp2 = "_MG_3901.JPG"
        originalFile1 = OriginalFile(pathtmp, filetmp1)
        originalFile2 = OriginalFile(pathtmp, filetmp2)
        singledata1 = SingleFinalData(".\\newoutpiut", originalFile1.tupla())
        singledata2 = SingleFinalData(".\\newoutpiut", originalFile2.tupla())
        list_final_data = []
        list_final_data.append(singledata1)
        list_final_data.append(singledata2)
        var = ImageJPG(list_final_data)
        result = var.list_filename()
        expected = ["vecchia.JPG",  "_MG_3901.JPG"]
        self.assertEqual(result ,expected)



