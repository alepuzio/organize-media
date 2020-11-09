import csv
import os
import re
import unittest

from Extension import Extension
from NameFile import Manual
from PersonalLogging import PersonalLogging

from QuotationMark  import QuotationMark  
class Image:
    '''@overview: it contains the properties in file CSV manual about images'''

    def __init__(self, new_read_file_csv):
        self.read_file_csv = new_read_file_csv
        self.log = PersonalLogging("Image")

    def read(self):
        '''@return the object with the properties'''
        if self.valid():
            name =  Manual().name()            #'manual-data.csv'
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
            name = Manual().name() #'manual-data.csv'
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
        self.log = PersonalLogging("ReadFileCSV", False)

    def read(self,name):
        path =  "{0}{1}{2}".format(self.dir, os.sep , name)
        result = []
        exists = os.path.exists(path)
        if exists :
            with open(path, newline = '') as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    result.append ( ReadCSV(row) )
        else:
            raise Exception ("The file [{0}] is not present, I stop the elaboration ".format (path) )
        
        self.log.print("Elaborated file: {0}".format( len(result) ) )
        return result 
    

class ReadCSV:
    '''@overview: this class contains the single row of manual CSV'''

    def __init__(self, newrow):
        self.row = newrow
        
    def year(self):
        return self.row['Year'].strip() #TODO another class TimeCreated
   
    def day(self):
        return self.row['Day'].strip() #TODO another class TimeCreated

    def month(self):
        return self.row['Month'].strip() #TODO another class TimeCreated

    def fileName(self):
        return self.row['OriginalFilename'].strip()
    
    def description(self):
        return self.row['Description'].strip() #TODO create decorator
    
    def keywords(self):
        return Keyword(self.row['Keywords'].strip()).keyword()
   
    def __str__(self):
        return "ReadCSV:{0}".format(self.row)
    
    def __repr__(self):
        return "ReadCSV[{0}]/[{1}]/[{2}]:[{3}]-[{4}]-[{5}]".format(self.day(), self.month(), self.year(), self.fileName(), self.description(), self.keywords())


class Keyword:
    '''@overview: this class contains the list of keywords of the manual CSV'''

    def __init__(self, new_row):
        self.manual_tag = new_row
        self.log = PersonalLogging("Keyword")

    def keyword(self):
        '''@return list of tags as one string
        the initial internal separator has to be ';'
        and become ','
        '''
        list_tags = None #TODO put control if manual_tags is empty
        #TODO code defensive decorator
        self.log.print("manual_tags: {0}".format ( self.manual_tag ) )
        if ";" not in self.manual_tag:
            list_tags = ', THE TAG SEPARATOR HAS TO BE  ";"  IN {0}, CSV NOT UPLOABLE '.format (self.manual_tag) 
            raise Exception (list_tags)
        elif "\"" in self.manual_tag:
            list_tags = ', THE CHAR \" HAS NOT TO BE PRESENT IN {0}, CSV NOT UPLOABLE,'.format(self.manual_tag)
            raise Exception (list_tags)
        else: 
            list_tags = re.sub(";",", " , self.manual_tag)
        
        '''
        Being a csv rw, it's impossible that I can receive a CSV fielad with 1 comma between the 0 and len(field)
        I'm writing this comment for the future
        elif "," in self.manual_tag:
            list_tags = ', THE CHAR \" , \" HAS NOT TO BE PRESENT IN {0}, CSV NOT UPLOABLE,'.format(self.manual_tag)
            raise Exception (list_tags)
        '''
        return QuotationMark( list_tags  ).string()

'''TODO draft of the defensive decorator
class KeywordInvalidQuotationMark:
    @overview: controle the absence of comma in the input tag
        
    def __init__(self, new_origin):
        self.origin = new_origin

    def data(self):
        if "\"" in self.origin.manual_tag:
            list_tags = ', THE CHAR \" HAS NOT TO BE PRESENT IN {0}, CSV NOT UPLOABLE,'.format(self.origin.manual_tag)
            raise Exception (list_tags)
        else:
            return self.origin.data()

'''




class TestKeyword(unittest.TestCase):

    def test_standard_keyword(self):
        var = "tag1;tag2;tag3"
        result =  Keyword(var).keyword()
        expected = "\"tag1, tag2, tag3\""
        self.assertEqual(result, expected)

    def test_problem_losing_words(self):
        var = "entrance;facade,tree;blue;building;historical;landmark;museum;old;outdoor;palace;sky;square;state;symbol;view;army;historic"
        result =  Keyword(var).keyword()
        expected = "\"entrance, facade\""
        self.assertEqual(result, expected)


    def test_wrong_separator(self):
        pass

    def test_wrong_quotation_mark(self):
        pass