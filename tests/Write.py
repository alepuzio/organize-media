import os
import sys
import unittest
from PersonalLogging import PersonalLogging

from Filesystem import FileSystem
from PersonalLogging import PersonalLogging
from GroupOriginalFiles import GroupOriginalFiles
from GroupReadFiles import GroupReadFiles
from GroupFiles import GroupFiles
from GroupDirectory import GroupDirectory
from DataINI import DataINI
from SafeFile import SafeFile
from FileToWrite import FileToWrite
from NameINI import NameINI


from NameCSV import NameCSV
from DataCSV import DataCSV

class Write:
    '''@overview: class to create CSV and INI file'''
    def __init__(self, new_directory):
        print("SWrite( " + str(new_directory))
        self.directory = new_directory[0]

    def __repr__(self):
        return 'Write(%s)' % (self.directory)

    def __str__(self):
        return "Write(%s)" % (self.directory)

    def __eq__(self, other):
        return self.directory == other.directory

    def original(self):
        return self.originalDirectory;


    def run(self):
        dest = NameINI ( self.directory )
        fileini = DataINI ( SafeFile ( FileToWrite (  dest.name() ) ) )
        fileini.data()
        filecsv = DataCSV ( SafeFile ( FileToWrite ( NameCSV(self.directory). name() ) ) ) 
        map_original_files  = GroupReadFiles ( FileSystem (self.directory).walk()   ).map()          
        filecsv.data ( map_original_files )
