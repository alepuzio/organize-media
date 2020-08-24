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
        manual_tags = self.row['Keywords'].strip()
        list_tags = None
        if ";" not in manual_tags:
            '''error, it must be more than 1 tag with sep ;
            '''
            list_tags = ',,,,,,ERROR IN SEPARATOR TAGS IN MANUAL CSV,, THE TAG SEPARATOR HAS TO BE  ";" , CSV NOT UPLOABLE,,'
        elif "\"" in manual_tags:
            '''error, the char "\"" has not to be present
            '''
            list_tags = ',,,,,,ERROR IN LISTING TAG IN MANUAL CSV,,: \" HAS NOT TO BE PRESENT,, CSV NOT UPLOABLE,'
        else: 
            list_tags = re.sub(";",", " , manual_tags)
        return "\"" + list_tags + "\""
   
    def __str__(self):
        return "ReadCSV:{0}".format(self.row)
    
    def __repr__(self):
       return "ReadCSV[{0}][{1}][{2}][{3}]".format(self.created(), self.fileName(), self.description(), self.keywords())
