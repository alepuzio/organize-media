import sys
import os
import unittest

from Filesystem import FileSystem
from PersonalLogging import PersonalLogging
from GroupOriginalFiles import GroupOriginalFiles
from Control import  Control
from GroupReadFiles import GroupReadFiles
from GroupFiles import GroupFiles
from GroupDirectory import GroupDirectory
from DataINI import DataINI
from SafeFile import SafeFile
from FileToWrite import FileToWrite
from SafeCSV import SafeCSV


class Main:
    '''@overview entry point of the application'''

    def __init__(self, newRoot):
        self.originalDirectory = newRoot [ 1 ]
        self.log = PersonalLogging ( "Main", True )
        self.finalDirectory = newRoot [ 2 ]

    def original(self):
        return self.originalDirectory;

    def final(self):
        return self.finalDirectory;


if __name__ == '__main__':
    # TODO controls length of param
    # use args module
    controls = Control(sys.argv)
    if  controls.act():
        m = Main(sys.argv)
        begin = FileSystem( m.original()) # m.final() )
        listfiles = begin.walk()
        groupReadFiles = GroupReadFiles(listfiles)
        map_original_files = groupReadFiles.map()
        group_original_files = GroupOriginalFiles(map_original_files)
        group_final_files = group_original_files.map(m.final() )
        dir_to_create = GroupDirectory(group_final_files.values())
        list_dir = dir_to_create.write()
        group_files = GroupFiles(group_final_files)
        group_files.copy()

        ##TODO levare sotto altr parametro
        print("Main:" + str(list_dir)) 
        dest = NameINI(tmp)
        fileini = DataINI ( SafeFile ( FileToWrite (  NameINI(tmp) ) ) )
        fileini.data()

        m = Main(sys.argv)
        dest = NameCSV(tmp)
        filecsv = DataCSV ( SafeFile ( FileToWrite ( dest ) ) )
        begin = FileSystem( m.original()))
        listfiles = begin.walk()
        map_original_files = groupReadFiles.map()
        filecsv.data( map_original_files )
