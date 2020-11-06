import unittest
import re

class DayMonthYear:
    '''@overview: this class incapsulate the data about the year'''

    def __init__(self, newday, newmonth , newyear ):
        self.year = newyear
        self.month = newmonth
        self.day = newday

    def show(self, separator):
        '''@return creation year as 'ddseparatormmseparatoryyyy'
           @param separator = string
        '''
        return separator.join ( [self.day, self.month , self.year] )

    def __repr__(self):
        return "DayMonthYear[" + self.day +"][" + self.month +  "][" + self.year + "]"

    def inverse(self, separator):
        '''@return time as 'yyyyseparatormmseparatordd  '
           @param separator = string
        '''
        return separator.join ( [self.year, self.month , self.day] )
    
    def mmddyyyy(self, separator):
        '''@return mmddyyyy
           @param separator = string
        '''
        return separator.join ( [self.month , self.day, self.year] )

class Slash:
    '''@overview: decorator with slash'''
    def __init__(self, newdaymonthyear):
        self.daymonthyear = newdaymonthyear
        self.sep = "/"

    def show(self):
        return self.daymonthyear.show(self.sep)

    def inverse(self):
        return self.daymonthyear.inverse(self.sep)

class Space:
    '''@overview: decorator with one space'''
    def __init__(self, newdaymonthyear):
        self.daymonthyear = newdaymonthyear
        self.sep = " "

    def show(self):
        #TODO centralize in a class
        return self.daymonthyear.show(self.sep)

    def inverse(self):
        #TODO centralize in a class
        return self.daymonthyear.inverse(self.sep)
    
    def mmddyyyy(self):
        #TODO centralize in a class
        return self.daymonthyear.mmddyyyy(self.sep)
   

    def replace(self, old_sep):
        '''@return the substitution from dash to space separator'''
        return re.sub(old_sep, self.sep, self.data)

    def from_slash(self):
        return Space(self.replace ( "/" ))


class TestSpace(unittest.TestCase):

    def test_mmddyyyy(self):
        year = "2020"
        month = "06"
        day = "10"
        dayMonthYear = Space(DayMonthYear(day, month, year)).mmddyyyy()
        expected = "06 10 2020"
        self.assertEqual( dayMonthYear, expected)


class Dash:
    '''@overview: decorator with one dash'''
    def __init__(self, newdaymonthyear):
        self.daymonthyear = newdaymonthyear
        self.sep = "-"

    def show(self):
        return self.daymonthyear.show( self.sep )

    def inverse(self):
        return self.daymonthyear.inverse(self.sep)


class TestDayMonthYear(unittest.TestCase):

    def test_show_slash(self):
        year = "2020"
        month = "06"
        day = "10"
        dayMonthYear = Slash(DayMonthYear(day, month, year)).show()
        expected = "10/06/2020"
        self.assertEqual( dayMonthYear, expected)


    def test_show_space(self):
        year = "2020"
        month = "06"
        day = "10"
        dayMonthYear = Space ( ( DayMonthYear(day, month, year) ) ).show()
        expected = "10 06 2020"
        self.assertEqual( dayMonthYear, expected)

    def test_inverse_dash(self):
        year = "2020"
        month = "06"
        day = "10"
        dayMonthYear = Dash(DayMonthYear(day, month, year)).inverse()
        expected = "2020-06-10"
        self.assertEqual( dayMonthYear, expected)
