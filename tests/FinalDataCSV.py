import unittest

from CSVImage import CSVImage
from CSVVideo import CSVVideo

from FileToWrite import FileToWrite
from Label import LabelImage
from Label import LabelVideo
from PersonalLogging import PersonalLogging
from SafeFile import SafeFile



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
        if self.image():#TODO creare decorator
            self.logging.print("label image")
            list_rows.append( "{0}\n".format ( LabelImage().csv() ) ) 
        else:
            self.logging.print("label video")
            list_rows.append( "{0}\n".format ( LabelVideo().csv() ) ) 
        for tmp_file in self.list_data:
            if self.image():
                tmp_value = CSVImage(self.properties_ini, tmp_file)
            else:
                tmp_value = CSVVideo(self.properties_ini, tmp_file)
        list_rows.append( "{0}\n".format ( tmp_value.data()))
        self.logging.print( "tmp: %s" % str(list_rows) )
        return self.safefile.safe(list_rows)
        
    def image(self):
        '''@return True if the row is about an image, False if it's abouta a video
        '''
        return self.properties_ini.imagetype() == "photo" #TODO create decorator


class TestFinalDataCSV(unittest.TestCase):

    def st_data(self):
        '''TODO heavy to prepare the input data'''
        pass
