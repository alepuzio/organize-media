#import os
import platform
import time
import pytest
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

    def __repr__():
        return "Year[" + self.show() + "]"

#class TestYear(unittest.TestCase)

def test_show():
    time = "Wed Jun 10 17:04:28 2020"
    year = Year(time)
    expected = "2020"
    assert (year.show() == expected)
            
def test_eq():
    time_one = "Wed Jun 10 17:04:28 2020"
    time_two = "Wed Jun 10 17:04:28 2020"
    year_one = Year(time_one)
    year_two = Year(time_two)
    assert (year_one == year_two)
    

