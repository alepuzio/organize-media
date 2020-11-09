import os
import sys
import unittest


from .data_ini import DataINI
from .data_ini import Image
from .data_ini import Video
from .data_ini import DataDraft

from tests.extension import Extension

from .group_directory import GroupDirectory
from .group_files import GroupFiles
from .group_original_files import GroupOriginalFiles
from .group_read_files import GroupReadFiles

from .filesystem import FileSystem
from .file_to_write import FileToWrite

from .manual_data_CSV import ManualDataCSV

from NameFile import Manual
from NameFile import NameCSV
from NameFile import NameINI
from NameFile import NameDraft
from NameFile import NameSelected

from PersonalLogging import PersonalLogging

from SafeFile import SafeFile
from UnsafeFile import UnsafeFile



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
            raise Exception ("Unkown type of file: {0} on [{1}]".format( extension, path[0] ) )
 
        fileini.data()# TODO put exception o r message if there's any image of video
        filecsv = ManualDataCSV ( SafeFile ( FileToWrite ( NameCSV(self.directory, Manual() ). name() ) ) ) 
        map_original_files = GroupReadFiles ( FileSystem ( self.directory ).walk()   ).map()          
        filecsv.data ( map_original_files )
        DataDraft ( UnsafeFile ( FileToWrite ( NameDraft ( self.directory ).name() ) ) ) .data()
    
        DataDraft ( UnsafeFile ( FileToWrite ( NameSelected ( self.directory ).name() ) ) ) .data()

