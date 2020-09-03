import os
import sys
import unittest

from Copy import Copy

from FileToWrite import FileToWrite
from FinalDataCSV import FinalDataCSV
from NameCSV import Final
from NameCSV import NameCSV

from PersonalLogging import PersonalLogging

from ReadFileTag import ReadFileTag

from SafeFile import SafeFile
from Write import Write


    #TODO mettere controllo che il path passato deve avere il sepratore os.sep corretto
    # altrimenti ci saranno problemi con i file


class ListTag:
    '''@overview: class to list the tags in one row'''
    def __init__(self, new_args ):
        self.directory = new_args[0]

    def __repr__(self):
        return 'ListTag(%s)' % (self.directory)

    def __str__(self):
        return "ListTag(%s)" % (self.directory)

    def __eq__(self, other):
        return self.directory == other.directory
    
    def run(self):
        '''run the list 
        - reading the file draft
        - building TagList
        - print the tags in a row
        '''
        print("run")
        ReadFileTag(self.directory).read()

