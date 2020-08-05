import unittest

from PersonalLogging import PersonalLogging
from SafeFile import SafeFile
from FileToWrite import FileToWrite
#from DayMonthYear import DayMonthYear

#from Year import Year
from Month import Month
#from Day import Day
#from Topic import Topic
#from Filename import Filename
from Extension import Extension

class DataCSV:
    '''@overview: class for the partial csv fil'''
    
    def __init__(self, new_safe_file):
        self.safefile = new_safe_file
        self.logging = PersonalLogging("DataCSV")

    def data(self, map_file_single_data):
        '''@return list of data file'''
        list_rows = []
        list_rows.append("Created,FileName,Description,Keywords\n")
        
        self.logging.print("data():" + str(map_file_single_data))
        for tmp_file in map_file_single_data.keys():
            tmp_value = map_file_single_data[tmp_file]
            self.logging.print("tmp_file:" + str(tmp_file))
            self.logging.print("tmp_value:" + str(tmp_value))
            self.logging.print("tupla:" + str(tmp_value.tupla()))
            filename = self.filename(tmp_value.tupla())
            self.logging.print("filename:" + filename)
            #time = self.time(tmp_value)
            #list_rows.append( "%s,%s,%s,%s\n" % ( self.time( tmp_value ).show(), self.filename( tmp_value ), "  ", "  "))
            self.logging.print( "tmp: %s" % str(list_rows) )
        return self.safefile.safe(list_rows)
        
    
    def time(self, tmp_value):
        '''@return the day mm year of the file'''
        self.logging.print("TmpValue: " + str(tmp_value))
        year = tmp_value[0]
        month = tmp_value[1]
        day = tmp_value[6]
        self.logging.print("spezzati:" + str(day) + str(month) + str(year))
        time = None#DayMonthYear(day, month, year)
        self.logging.print( "unito:"+ time.show() )
        return time


    def filename(self, tmp_value):
        self.logging.print(">filename: " + str(tmp_value))
        '''@return thefilename and extensione of the file'''
        filename = "%s.%s"  % (tmp_value.position.name(), tmp_value.position.extension().name() )
        self.logging.print("<filename: " + filename)
        return filename


class TestDataCSV(unittest.TestCase):

    def test_filename(self):
        var = DataCSV(None)
        tmp_value = ( "2020", Month("03"), "30", "topic", "filename", Extension("jpg") )
        result = var.filename(tmp_value)
        expected = "filename.jpg"
        self.assertEqual ( result, expected )


