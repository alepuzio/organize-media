from PersonalLogging import PersonalLogging
import os
import platform


        
class FileToWrite:
    '''@overview: class or file to be written'''

    def __init__(self, new_path):
        self.path = new_path
        self.logging = PersonalLogging ("FileToWrite", False)

    def hard_disk(self, list_rows):
        '''crete the physicalfile'''
        self.logging.print("<head_disk:" + str(list_rows))
        with open(self.path, "w") as fileini:
            for tmp in list_rows:
                self.logging.print(tmp)
                fileini.write(tmp)


    def __repr__(self):
        return "FiletoWrite[%s]" %self.path 
