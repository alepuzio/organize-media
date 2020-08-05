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


