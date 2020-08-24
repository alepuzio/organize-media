import csv
import os
import re
import unittest

from Extension import Extension

from PersonalLogging import PersonalLogging


class Image:
    '''@overview: it contains the properties in file CSV manual about images'''

    def __init__(self, new_read_file_csv):
        self.read_file_csv = new_read_file_csv
        self.log = PersonalLogging("Image")

    def read(self):
        '''@return the object with the properties'''
        if self.valid():
            name = 'manual-data.csv'
            res = self.read_file_csv.read(name)
        else:
            res = Video ( self.read_file_csv ).read()
        return res
    
    def valid(self):
        #TODO centralize in an object
        path = self.read_file_csv.dir.split ( os.sep )
        path.reverse()
        extension = Extension ( path[0] )
        return extension.image()

class Video:
    '''@overview: it contains the properties in file CSV manual about videos'''

    def __init__(self, new_read_file_csv):
        self.read_file_csv = new_read_file_csv
        self.log = PersonalLogging("Video")

    def read(self):
        '''@return the object with the properties'''
        if self.valid():
            name = 'manual-data.csv'
            res = self.read_file_csv.read(name)
        else:
            res = Video ( self.read_file_csv ).read()
        return res
 
    def valid(self):
        #TODO centralize in an object
        path = self.read_file_csv.dir.split ( os.sep )
        path.reverse()
        extension = Extension ( path[0] )
        return extension.video()

class ReadFileCSV:
    '''@overview: it contains the properties in file INI'''

    def __init__(self, new_dir):
        self.dir = new_dir
        self.log = PersonalLogging("ReadFileCSV")

    def read(self,name):
        path =  self.dir + os.sep + name #TODO concatenation of string to improve
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
