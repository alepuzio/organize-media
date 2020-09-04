import os
import platform
from PersonalLogging import PersonalLogging
import errno
from FileToWrite import FileToWrite
 

class UnsafeFile:
    '''@overview: this class creates the file if it does'nt exists, otherwise it modifies the file''' 

    def __init__(self, new_file_to_write):
        self.file_to_write = new_file_to_write
        self.logging = PersonalLogging("UnsafeFile")

    def safe(self, list_rows):
        '''@return create the file '''
        try:
            self.file_to_write.hard_disk(list_rows)
            self.logging.print("Created file: %s" % self.file_to_write)
        except OSError as e:
            if e.errno != errno.EEXIST:
                self.logging.warn("Error in creating file: %s" % self.file_to_write)
                raise

    def __repr__ (self):
        return self.file_to_write

