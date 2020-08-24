import unittest
import os
from PersonalLogging import PersonalLogging
import csv
import re

class ReadFileCSV:
    '''@overview: it contains the properties in file INI'''

    def __init__(self, new_dir):
        self.dir = new_dir
        self.log = PersonalLogging("ReadCSV")

    def read(self):
        '''@return the object with the properties'''
        path =  self.dir + os.sep + "images.csv" #TODO concatenation of string to improve
        result = []
        with open(path, newline = '') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                result.append ( ReadCSV(row) )
        return result 

class ReadCSV:
    '''@overview: this class contains the single row of manual CSV'''

    def __init__(self, newrow):
        self.row = newrow

    def created(self):
        return self.row['Created'].strip()
    
    def fileName(self):
        return self.row['OriginalFilename'].strip()
    
    def description(self):
        return self.row['Description'].strip()
    
    def keywords(self):
        '''@return list of tags as one string
        the initial internal separator has to be ';'
        and become ','
        '''
        list_tags = re.sub(";",", " , self.row['Keywords'].strip())
        
        return "\"" + list_tags + "\""
   
    def __str__(self):
        return "ReadCSV:{0}".format(self.row)
    
    def __repr__(self):
       return "ReadCSV[{0}][{1}][{2}][{3}]".format(self.created(), self.fileName(), self.description(), self.keywords())
