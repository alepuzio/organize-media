import unittest

from PersonalLogging import PersonalLogging
from SafeFile import SafeFile
from FileToWrite import FileToWrite
from DayMonthYear import DayMonthYear

from Month import Month
from Extension import Extension

class ManualDataCSV:
    '''@overview: class for the partial csv fil'''
    
    def __init__(self, new_safe_file):
        self.safefile = new_safe_file
        self.logging = PersonalLogging("ManualDataCSV")

    def data(self, map_file_single_data):
        '''@return list of data file'''
        list_rows = []
        list_rows.append("Created,OriginalFilename,Description,Keywords")
        
        self.logging.print("data():" + str(map_file_single_data))
        for tmp_file in map_file_single_data.keys():
            tmp_value = map_file_single_data[tmp_file]
            list_rows.append( "%s\t,%s\t,%s\t,%s\n" % ( self.time( tmp_value.tupla() ).show(), self.filename( tmp_value.tupla() ), "  ", "  "))
            self.logging.print( "tmp: %s" % str(list_rows) )
        return self.safefile.safe(list_rows)
        
    
    def time(self, tmp_value):
        '''@return the day mm year of the file'''
        year = tmp_value.time.year()
        month = tmp_value.time.month().single_number()
        day = tmp_value.time.day()
        time = DayMonthYear(day, month, year)
        return time


    def filename(self, tmp_value):
        '''@return thefilename and extensione of the file'''
        filename = "%s.%s"  % (tmp_value.position.name(), tmp_value.position.extension().name() )
        return filename


class TestManualDataCSV(unittest.TestCase):

    def st_filename(self):
        '''TODO rifare'''
        var = ManualDataCSV(None)
        tmp_value = ( "2020", Month("Jun"), "30", "topic", "filename", Extension("jpg") )
        result = var.filename(tmp_value)
        expected = "filename.jpg"
        self.assertEqual ( result, expected )


    def st_time(self):
        '''TODO rifare'''
        var = ManualDataCSV(None)
        tmp_value = ( "2020", Month("Jun"), "30", "topic", "filename", Extension("jpg") )
        result = var.time(tmp_value)
        expected = "30/03/2020"
        self.assertEqual ( result, expected )
