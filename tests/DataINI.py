from FileToWrite import FileToWrite
from PersonalLogging import PersonalLogging
from SafeFile import SafeFile

class DataINI:
    '''@class for the initial ini file of properties'''
    
    def __init__(self, new_safe_file):
        self.safefile = new_safe_file
        self.logging = PersonalLogging("DataINI")

    def data(self, list_rows):
        '''@return list of the field'''
        list_rows.append("Copyright=\n")
        list_rows.append("City=\n")#TODO in function of the topic
        list_rows.append("Price=\n")
        list_rows.append("SpecifySource=\n")
        list_rows.append("Region=\n")
        list_rows.append("Country=\n")
        return self.safefile.safe(list_rows)
        

class Image:
    def __init__(self, new_data_ini):
        self.data_ini = new_data_ini
        self.loggging = PersonalLogging("Image")

    def data(self):
        list_rows = []
        list_rows.append("[Image]\n")
        list_rows.append("ImageType=photo\n")#TODO in function of extension/media, it 's "photo" or "video"
        return self.data_ini.data(list_rows)
