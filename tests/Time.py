import time
import unittest
from datetime import datetime
from Month import Month
import re

class Time:
    '''@overview: this class incapsulate the data about the datetime of a file'''

    def __init__(self, newdatetime):
        self.datetime = newdatetime

    def year(self):
        '''@return creation year as 'yyyy' '''
        date = self.prepare()
        tmp = date.split(" ")
        return tmp[4]

    def day(self):
        '''@return creationday as 'dd' '''
        date = self.prepare()
        tmp = date.split(" ")
        res = None
        if 1 == len(tmp[2]):
            res = "0{0}".format(tmp[2])
        else:
            res = tmp[2]
        return res

    def month(self):
        '''@return creationday as 'mm' '''
        date = self.prepare()
        tmp = date.split(" ")
        return Month(tmp[1])

    def yearMonth ( self ) :
        '''@return yyyymm '''
        year = self.year()
        month = self.month().single_number()
        return str(year) + str(month)


    def prepare(self):
        '''@return datetime in format DAY-OF-WEEK-space-month-name-space-dayofmonth-space-hours:minutes:second-space-year because of the different valeu in different OS'''
        date = self.datetime
        ##remove doubel space 
        return re.sub(' +', ' ', date)
        

    def __eq__( self, other ) :
        return self.datetime == other.datetime 

    def __repr__(self):
        return "Time[" + self.datetime + "]"


    def __str__(self):
        return "Time[" + self.datetime + "]"
class TestDatetime(unittest.TestCase):

    def test_year(self):
        time = "Wed Jun 10 17:04:28 2020"
        year = Time(time)
        expected = "2020"
        self.assertEqual(year.year(), expected) 
        time = "Mon Aug  3 17:04:28 2020"
        year = Time(time)
        expected = "2020"
        self.assertEqual(year.year(), expected)


    def test_yearmonth(self):
        time = "Wed Jun 10 17:04:28 2020"
        year = Time(time)
        expected = "202006"
        self.assertEqual(year.yearMonth(), expected)

    def test_eq(self):
        time_one = "Wed Jun 10 17:04:28 2020"
        time_two = "Wed Jun 10 17:04:28 2020"
        year_one = Time(time_one)
        year_two = Time(time_two)
        self.assertEqual(year_one, year_two)
    
    def test_day(self):
        time = "Wed Jun 10 17:04:28 2020"
        year = Time(time)
        expected = "10"
        self.assertEqual(year.day(), expected)
        time = "Wed Jun 5 17:04:28 2020"
        year = Time(time)
        expected = "05"
        self.assertEqual(year.day(), expected)



    def test_Month(self):
        time = "Wed Jun 10 17:04:28 2020"
        year = Time(time)
        expected = Month("Jun")
        self.assertEqual(year.month(), expected)

