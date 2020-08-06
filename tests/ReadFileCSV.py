import unittest
import os
from PersonalLogging import PersonalLogging
import csv



class ReadFileCSV:
    '''@overview: it contains the properties in file INI'''

    def __init__(self, new_dir):
        self.dir = new_dir
        self.log = PersonalLogging("ReadCSV")

    def read(self):
        '''@return the object with the properties'''

        path =  self.dir + os.sep+ "images.csv" #TODO concatenation of string to improve
        result = []
        with open(path, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                result.append ( ReadCSV(row) )
        return result 



class ReadCSV:
    '''overview: this class contains the single row of manual CSV'''

    def __init__(self, newrow):
        self.row = newrow

    def created(self):
        return self.row['Created']
    
    def fileName(self):
        return self.row['FileName'].strip()
    
    def description(self):
        return self.row['Description']
    
    def keywords(self):
        return self.row['Keywords'].strip()
   
    def __str__(self):
       return "ReadCSV[0][1][2][3]".format(self.created(), self.fileName(), self.description(), self.keywords())
    
    def __repr__(self):
       return "ReadCSV[{0}][{1}][{2}][{3}]".format(self.created(), self.fileName(), self.description(), self.keywords())
