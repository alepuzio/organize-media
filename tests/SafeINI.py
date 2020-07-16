from PersonalLogging import PersonalLogging
from SafeFile import SafeFile
from FileToWrite import FileToWrite

class SafeINI:
    '''@class for the initial ini file of properties'''
    
    def __init__(self, new_safe_file):
        self.safefile = new_safe_file
        self.logging = PersonalLogging("SafeINI")

    def data(self):
        '''@return list of the field'''
        list_rows = []
        list_rows.append("Copyright=\n")
        list_rows.append("City=\n")
        list_rows.append("Price=\n")
        list_rows.append("SpecifySource=\n")
        list_rows.append("Region=\n")
        list_rows.append("ImageType=\n")
        list_rows.append("Country=\n")
        return self.safefile.safe(list_rows)
        

