import unittest

from PersonalLogging import PersonalLogging
from SafeFile import SafeFile
from FileToWrite import FileToWrite
from LabelImage import LabelImage
from CSVImage import CSVImage

class FinalDataCSV:
    '''@overview: class for the partial csv fil'''
    
    def __init__(self, new_safe_file, new_list_manual_csv, new_properties_ini):
        self.safefile = new_safe_file
        self.list_data = new_list_manual_csv
        self.properties_ini = new_properties_ini
        self.logging = PersonalLogging("FinalDataCSV")

    def data(self):
        '''@return list of data file'''
        list_rows = []
        list_rows.append( "{0}\n".format ( LabelImage().csv() ) ) 
        self.logging.print("data():" + str ( self.list_data ) )
        for tmp_file in self.list_data:
            tmp_value = CSVImage(self.properties_ini, tmp_file)
            list_rows.append( "{0}\n".format ( tmp_value.data()))
            self.logging.print( "tmp: %s" % str(list_rows) )
        return self.safefile.safe(list_rows)
        
    


class TestFinalDataCSV(unittest.TestCase):

    def st_data(self):
        '''TODO heavy to prepare the input data'''
        pass
