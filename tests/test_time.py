import time
import pytest
import re

from datetime import datetime
from .test_month import Month

class Time:
    """@overview: this class incapsulate the data about the datetime of a file"""

    def __init__(self, newdatetime):
        self.datetime = newdatetime

    def year(self):
        """@return creation year as 'yyyy' """
        date = self.prepare()
        tmp = date.split(" ")
        return tmp[4]

    def day(self):
        """@return creationday as 'dd' """
        date = self.prepare()
        tmp = date.split(" ")
        res = None
        if 1 == len(tmp[2]):
            res = "0{0}".format(tmp[2])
        else:
            res = tmp[2]
        return res

    def month(self):
        """@return creationday as 'JUN, Jan, Apr, etc' """
        date = self.prepare()
        tmp = date.split(" ")
        return Month(tmp[1])

    def yearMonth ( self ) :
        """@return yyyymm """
        year = self.year()
        month = self.month().single_number()
        return str(year) + str(month)


    def prepare(self):
        """@return datetime in format DAY-OF-WEEK-space-month-name-space-dayofmonth-space-hours:minutes:second-space-year because of the different valeu in different OS"""
        date = self.datetime
        #remove double space 
        return re.sub(' +', ' ', date)
        

    def __eq__( self, other ) :
        return self.datetime == other.datetime 

    def __repr__(self):
        return "Time[" + self.datetime + "]"


    def __str__(self):
        return "Time[" + self.datetime + "]"


def test_year_in_year_OK():
    time = "Wed Jun 10 17:04:28 2020"
    year = Time(time)
    expected = "2020"
    assert year.year()== expected 

def test_yearmonth_OK():
    time = "Wed Jun 10 17:04:28 2020"
    year = Time(time)
    expected = "202006"
    assert year.yearMonth()== expected

def test_eq_OK():
    time_one = "Wed Jun 10 17:04:28 2020"
    time_two = "Wed Jun 10 17:04:28 2020"
    year_one = Time(time_one)
    year_two = Time(time_two)
    assert year_one == year_two

def test_day_OK():
    time = "Wed Jun 10 17:04:28 2020"
    year = Time(time)
    expected = "10"
    assert year.day()== expected

def test_day_OK():    
    time = "Wed Jun 26 17:04:28 2020"
    year = Time(time)
    expected = "26"
    assert year.day()== expected

def test_Month_OK():
    time = "Wed Jun 10 17:04:28 2020"
    year = Time(time)
    expected = Month("Jun")
    assert year.month()== expected

