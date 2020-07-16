from PersonalLogging import PersonalLogging
import os
import platform


        
class FileToWrite:
    '''@overview: class or file to be written'''

    def __init__(self, new_path):
        self.path = new_path
        self.logging = PersonalLogging ("FileToWrite", True)

    def hard_disk(self, list_rows):
        '''crete the physicalfile'''
        with open(self.path, "w") as fileini:
            for tmp in list_rows:
                fileini.write(tmp)
                self.logging.print(tmp)


    def __repr__(self):
        return "FiletoWrite[%s]" %self.path 
