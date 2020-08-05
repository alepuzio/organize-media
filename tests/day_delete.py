import os
import platform
import time
import unittest
from datetime import datetime


class Day:
    '''@overview: this class incapsulate the data about the year'''

    def __init__(self, newformattedtimestamp):
        self.timefile = newformattedtimestamp


    def show(self):
        '''@return creationday as 'dd' '''
        date = self.timefile
        tmp = date.split(" ")
        return tmp[2]

    def __eq__(self, other):
        return self.timefile == other.timefile 

    def __repr__(self):
        return "Day[" + self.show() + "]"

class TestDay(unittest.TestCase):

    def test_complete(self):
        time = "Wed Jun 10 17:04:28 2020"
        year = Day(time)
        expected = "10"
        self.assertEqual(year.show(), expected)
                
    def test_eq(self):
        time_one = "Wed Jun 10 17:04:28 2020"
        time_two = "Wed Jun 10 17:04:28 2020"
        year_one = Day(time_one)
        year_two = Day(time_two)
        self.assertEqual(year_one, year_two)
    

