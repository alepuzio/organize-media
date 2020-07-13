import os
import platform
import time
import unittest
from datetime import datetime


class Year:
    '''@overview: this class incapsulate the data about the year
    '''

    def __init__(self, newformattedtimestamp):
        self.timefile = newformattedtimestamp


    def show(self):
        '''@return creation year as 'yyyy' '''
        date = self.timefile
        tmp = date.split(" ")
        return tmp[4]

    def __eq__(self, other):
        return self.timefile == other.timefile 

    def __repr__(self):
        return "Year[" + self.show() + "]"

class TestYear(unittest.TestCase):

    def test_complete(self):
        time = "Wed Jun 10 17:04:28 2020"
        year = Year(time)
        expected = "2020"
        self.assertEqual(year.show(), expected)
                
    def test_eq(self):
        time_one = "Wed Jun 10 17:04:28 2020"
        time_two = "Wed Jun 10 17:04:28 2020"
        year_one = Year(time_one)
        year_two = Year(time_two)
        self.assertEqual(year_one, year_two)
    

