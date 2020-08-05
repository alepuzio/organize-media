import sys
import unittest
import os
import unittest

from Filesystem import FileSystem
from PersonalLogging import PersonalLogging
from GroupOriginalFiles import GroupOriginalFiles
from GroupReadFiles import GroupReadFiles
from GroupFiles import GroupFiles
from GroupDirectory import GroupDirectory
from SafeFile import SafeFile
from FileToWrite import FileToWrite


class Copy:
    '''@overview: class to copy file'''
    def __init__(self, args):
        self.source = args[0]
        self.dest = args[1]

    def __repr__(self):
        return 'Copy(source = %s, dest = %s )' % (self.source, self.dest)

    def __str__(self):
        return "Copy(%s,%s)" % (self.source, self.dest)

    def __eq__(self, other):
        return self.source == other.source and self.dest == other.dest

    def run(self):
        '''the copy of the files '''
        begin = FileSystem(self.source).walk()
        map_original_files = GroupReadFiles(begin).map()
        group_original_files = GroupOriginalFiles(map_original_files)
        group_final_files = group_original_files.map( self.dest )
        dir_to_create = GroupDirectory(group_final_files.values())
        list_dir = dir_to_create.write()
        group_files = GroupFiles(group_final_files)
#        group_files.copy()

