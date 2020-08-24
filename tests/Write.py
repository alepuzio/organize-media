import os
import sys
import unittest


from DataINI import DataINI
from DataINI import Image

from GroupDirectory import GroupDirectory
from GroupFiles import GroupFiles
from GroupOriginalFiles import GroupOriginalFiles
from GroupReadFiles import GroupReadFiles

from Filesystem import FileSystem
from FileToWrite import FileToWrite
from ManualDataCSV import ManualDataCSV
from NameCSV import Manual
from NameCSV import NameCSV
from NameINI import NameINI

from PersonalLogging import PersonalLogging
from SafeFile import SafeFile




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
        fileini = Image ( DataINI ( SafeFile ( FileToWrite ( NameINI ( self.directory ).name() ) ) ) ) 
        fileini.data()# TODO put exception o r message if there's any image of video
        filecsv = ManualDataCSV ( SafeFile ( FileToWrite ( NameCSV(self.directory, Manual() ). name() ) ) ) 
        map_original_files  = GroupReadFiles ( FileSystem (self.directory).walk()   ).map()          
        filecsv.data ( map_original_files )
