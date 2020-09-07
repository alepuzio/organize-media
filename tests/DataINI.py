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
    '''@overview: label about the image INI file'''
    def __init__(self, new_data_ini):
        self.data_ini = new_data_ini
        self.loggging = PersonalLogging("Image")

    def data(self):
        list_rows = []
        list_rows.append("[Image]\n")
        list_rows.append("ImageType=photo\n")
        return self.data_ini.data(list_rows)

class Video:
    '''@overview: labels about the video INI file'''

    def __init__(self, new_data_ini):
        self.data_ini = new_data_ini
        self.loggging = PersonalLogging("Video")

    def data(self):
        list_rows = []
        list_rows.append("[Video]\n")
        list_rows.append("ImageType=video\n")
        return self.data_ini.data(list_rows)

class DataDraft:
    '''@class for the initial draft file about the tags'''
    
    def __init__(self, new_safe_file):
        self.safefile = new_safe_file
        self.logging = PersonalLogging("DataDraft", True)

    def data(self, list_rows):
        '''@return list of the field'''
        self.logging.print("data")
        list_rows.append("empty file, only temporary data\n")
        return self.safefile.safe(list_rows)
