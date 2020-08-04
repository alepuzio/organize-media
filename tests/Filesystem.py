import os
from PersonalLogging import PersonalLogging
from OriginalFile import OriginalFile

import unittest

class FileSystem:
    '''@overview: this class reads the files inside a directory'''

    def __init__(self, newInputDir):
        '''It read a directory and the subdirectory
        inputDIr: complete path of the root directory'''
        self.inputDir = newInputDir;
        self.log = PersonalLogging("FileSystem", False)

    def walk(self):
        '''@return the list of the read file
        It traverses root directory, and list directories as dirs and files as files
        in recursive way'''
        #TODO concatenation of string
        self.log.print("Directory.walk("+str(self.inputDir)+")");
        readfiles = [];
        return self.walksubdir(self.inputDir, readfiles);
       
    def walksubdir(self, partialRoot, readfiles):
        '''@return the partial list of the files'''
        for root, dirs, files in os.walk(partialRoot):
            for filetmp in files:
                readfiles.append (str(root) + os.sep + str(filetmp) ) ;
                self.log.print("Directory.walksubdir.filetmp(" + str(filetmp) + ")");
            for directory in dirs:
                self.walksubdir(directory, readfiles)
        self.log.print("Directory.walksubdir(" + str( readfiles ) + "): li trasformo in OriginalFile in una funzione a parte");
        return readfiles;

         

class TestFileSystem(unittest.TestCase):
    def test_walk_1_file_no_subdirecotry(self):
        listfiles = FileSystem(".\\resources\\lugano\\", "\\resources\\output\\").walk()
        numberelement = len(listfiles)
        self.assertEqual(numberelement, 6)
    
    def test_walk_1_file_1_subdirecotry(self):
        listfiles = FileSystem(".\\resources\\lugano\\jpg\\", "\\resources\\output\\jpg").walk()
        numberelement = len(listfiles)
        self.assertEqual(numberelement, 3)
    
    def test_walk_0_file_1_subdirecotry(self):
        listfiles = FileSystem(".\\resources\\lugano\\not-file\\", "\\resources\\output\\").walk()
        numberelement = len(listfiles)
        self.assertEqual(numberelement, 0)
    
    def test_walk_0_file_0_subdirecotry(self):
        listfiles = FileSystem(".\\resources\\lugano\\notexisting", "\\resources\\output\\").walk()
        numberelement = len(listfiles)
        self.assertEqual(numberelement, 0)
