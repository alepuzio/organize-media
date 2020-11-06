import unittest

from CSVImage import CSVImage
from CSVVideo import CSVVideo

from FileToWrite import FileToWrite
from test_label import LabelImage
from test_label import LabelVideo
from PersonalLogging import PersonalLogging
from SafeFile import SafeFile



class FinalDataTag:
    '''@overview: class for the good tags'''
    
    def __init__(self, new_safe_file, new_list_tag):
        self.safefile = new_safe_file
        self.list_data = new_list_tag
        self.logging = PersonalLogging("FinalDataTag", False )

    def data(self):
        '''@return list of data file'''
        list_rows = []
        for tmp_value in self.list_data:
                list_rows.append ( "{0};".format ( tmp_value ) ) 
        self.logging.print ( "tmp: %s" % str ( list_rows ) )
        list_rows.sort()
        return self.safefile.safe ( list_rows )
        


class TestFinalDataTag(unittest.TestCase):

    def st_data(self):
        '''TODO heavy to prepare the input data'''
        pass
