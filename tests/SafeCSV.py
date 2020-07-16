from PersonalLogging import PersonalLogging
from SafeFile import SafeFile
from FileToWrite import FileToWrite
from DayMonthYear import DayMonthYear

class SafeCSV:
    '''@class for the initial ini file of properties'''
    
    def __init__(self, new_safe_file):
        self.safefile = new_safe_file
        self.logging = PersonalLogging("SafeCSV")

    def data(self, list_single_data):
        '''@return list of the field'''
        list_rows = []
        list_rows.append("Created,FileName,Description,Keywords\n")
        
        self.logging.print("data():" + str(list_single_data))
        for tmp in list_single_data:
            element = tmp.tupla()
            filename = "%s.%s"  % (element[5].show(), element[6].show() )
            year = element[1]
            month = element[2]
            day = element[7]

            self.logging.print(str(day) + str(month) + str(year))
            time = DayMonthYear(day, month, year)
            list_rows.append( "%s,%s,%s,%s\n" % ( time.show(), filename, "  ", "  "))
            self.logging.print( "tmp: %s" % str(list_rows) )
        return self.safefile.safe(list_rows)
        

