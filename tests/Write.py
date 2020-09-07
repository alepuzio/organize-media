import os
import sys
import unittest


from DataINI import DataINI
from DataINI import Image
from DataINI import Video
from DataINI import DataDraft

from Extension import Extension

from GroupDirectory import GroupDirectory
from GroupFiles import GroupFiles
from GroupOriginalFiles import GroupOriginalFiles
from GroupReadFiles import GroupReadFiles

from Filesystem import FileSystem
from FileToWrite import FileToWrite

from ManualDataCSV import ManualDataCSV

from NameFile import Manual
from NameFile import NameCSV
from NameFile import NameINI
from NameFile import NameDraft

from PersonalLogging import PersonalLogging
from SafeFile import SafeFile




class Write:
    '''@overview: class to create CSV and INI file'''
    def __init__(self, new_directory):
        self.directory = new_directory[0]

    def __repr__(self):
        return 'Write(%s)' % (self.directory)

    def __str__(self):
        return "Write(%s)" % (self.directory)

    def __eq__(self, other):
        return self.directory == other.directory

    def original(self):
        return self.originalDirectory

    def run(self):
        data_ini = DataINI ( SafeFile ( FileToWrite ( NameINI ( self.directory ).name() ) ) ) 
        
        #TODO centralize in an object
        path = self.directory.split ( os.sep )
        path.reverse()
        extension = Extension ( path[0] )

        if extension.image():
            fileini = Image ( data_ini ) 
        elif extension.video():
            fileini = Video ( data_ini )
        else:
            raise Error ("Unkown type of file: {0}".format( extension ) )
        
        fileini.data()# TODO put exception o r message if there's any image of video
        filecsv = ManualDataCSV ( SafeFile ( FileToWrite ( NameCSV(self.directory, Manual() ). name() ) ) ) 
        map_original_files = GroupReadFiles ( FileSystem ( self.directory ).walk()   ).map()          
        filecsv.data ( map_original_files )

        DataDraft ( SafeFile ( FileToWrite ( NameDraft ( self.directory ).name() ) ) ) .data

