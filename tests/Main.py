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
        # print("str gorup_original_files: " + str(group_original_files))
        group_final_files = group_original_files.map(m.final() )
        print(str(group_final_files))
        dir_to_create = GroupDirectory(group_final_files.values())
        dir_to_create.write()
        group_files = GroupFiles(group_final_files)
        group_files.copy()
        


