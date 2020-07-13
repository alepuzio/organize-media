import os
import platform
import time

from datetime import datetime


class PrepareFile:
    '''this class open and close the file'''

    def __init__(self, newfile):
        self.file = newfile;

    def analize(self):
        '''return the LogicalFile of the current phisical file'''
        fileToAnalize  = open(self.file, "r");
        path  =  os.path.abspath ( self.file);
        statinfo =  self.stat();
        logicalFile = DefensiveLogicalFile(LogicalFile(fileToAnalize, path, statinfo) ) ;
        fileToAnalize.close();
        return logicalFile;

    def size(self):
        ''' size of the file in byte''' 
        fileToAnalize  = open(self.file, "r");
        statinfo = self.stat();
        fileToAnalize.close();
        return statinfo.st_size;

    def stat(self):
       statinfo = os.stat(self.file);
       return statinfo;


class ExtractDataFromFile:
    '''@overview: this class extract the data of the read file'''
    
    def __init__(self, new_data):
        self.data = new_data
        self.log = MioLogging("ExtractDataFromFile")
        
    def __repr__ (self):
         return "ExtractDataFromFile"
    
    def extractExtension(self):
        pieces = self.data.split(".")
        pieces.reverse();
        file_extension = pieces[0]
        return file_extension



