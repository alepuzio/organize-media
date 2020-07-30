from PersonalLogging import PersonalLogging
from SafeFile import SafeFile
from FileToWrite import FileToWrite
from DayMonthYear import DayMonthYear

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
            filename = "%s.%s"  % (tmp_value[5].show(), tmp_value[6].show() )
            year = tmp_value[1]
            month = tmp_value[2]
            day = tmp_value[7]

            self.logging.print(str(day) + str(month) + str(year))
            time = DayMonthYear(day, month, year)
            list_rows.append( "%s,%s,%s,%s\n" % ( time.show(), filename, "  ", "  "))
            self.logging.print( "tmp: %s" % str(list_rows) )
        return self.safefile.safe(list_rows)
        

