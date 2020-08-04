import unittest

from PersonalLogging import PersonalLogging
from SafeFile import SafeFile
from FileToWrite import FileToWrite
from DayMonthYear import DayMonthYear

from Year import Year
from Month import Month
from Day import Day
from Topic import Topic
from Filename import Filename
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
            tmp_value = map_file_single_data[tmp_file].tupla()
            filename = self.filename(tmp_value)
            time = self.time(tmp_value)
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
        time = DayMonthYear(day, month, year)
        self.logging.print( "unito:"+ time.show() )
        return time


    def filename(self, tmp_value):
        '''@return thefilename and extensione of the file'''
        filename = "%s.%s"  % (tmp_value[3].show(), tmp_value[4].show() )
        return filename


class TestDataCSV(unittest.TestCase):

    def test_time(self):
        var = DataCSV(None)
        tmp_value = ( Year("2020"), Month("03"), Day("30"), Topic("topic"), Filename("filename"), Extension("jpg") )
        result = var.filename(tmp_value)
        expected = "filename.jpg"
        self.assertEqual ( result, expected )


