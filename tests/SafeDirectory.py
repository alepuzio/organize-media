import os
import platform
from PersonalLogging import PersonalLogging
import errno


class SafeDirectory:
        '''this class creates the directory if it does'nt exists, otherwise it does'nt modify the directory'''    
        def __init__(self, newpath):
           self.path = newpath
           self.logging = PersonalLogging("CreateDirectorySafely")
           #self.mappa = newmappa
        
        def create(self):
            '''create the directoryy''' 
            exists = os.path.exists(self.path)
            if(exists):
                self.logging.print("Existing directory: %s" % self.path)
            else:
                try:
                    os.makedirs(self.path)
                    self.logging.print("Created directory: %s" % self.path)
                except OSError as e:
                    if e.errno != errno.EEXIST:
                       self.loggin.warn("Error in creating directory: %s" % self.path)
                       raise

        def __repr__ (self):
            return self.path

