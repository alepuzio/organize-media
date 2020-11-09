import unittest
from daymonthyearr import DayMonthYear 
from DayMonthYear import Space
#from DayMonthYear import Slash

from PersonalLogging import PersonalLogging
from QuotationMark import QuotationMark


class Name:
    '''@overview: name fo the CSV final to upload'''
    
    def __init__(self, new_ini, new_manual, new_created):
        self.city = new_ini.city()
        self.country = new_ini.country()
        self.created = new_created
        self.description = new_manual.description()

    def string(self):
        '''@return the name as concatenation of elementary data'''
        return "{0}, {1} - {2}: {3}".format(self.city, self.country, Space(self.created).mmddyyyy(), self.description )

class FailFirst:
    '''@overview: control about the name of files in the CSV final to upload'''
    
    def __init__(self, new_origin):
        self.origin = new_origin

    def string(self):
        '''@return the name but it raises exception if the name is longer than 80 characters'''
        result = self.origin.string() 
        num_chars = len (result)
        if ( 79 < num_chars ):#TODO follow the standard way about constants
            raise Exception ("The name {0} has {1} chars, too much: please write another name".format( result, num_chars ) ) 
        else:
            return QuotationMark (result).string()


class TestName(unittest.TestCase):

    def test_string(self):
       pass 

