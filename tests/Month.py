import os
import re
from PersonalLogging import PersonalLogging
import time
import datetime
import platform
from AsString import AsString

import unittest



class Month:
    ''' @overview this class has the dat aof year and month'''


    def __init__(self, newformattedtimestamp):
        self.timefile = newformattedtimestamp
        self.log = PersonalLogging("Month", False)


    def show(self):
        '''@return creation month as string '''
        date = self.timefile
        self.log.print("Month.show():" + str(date))
        tmp = date.split(" ")
        return tmp[1]
    
    def single_number(self):
        '''@return number of the month'''
        translateMonths= {"Jan":"01", "Feb":"02", "Mar":"03", "Apr":"04", "May":"05", "Jun":"06", "Jul":"07", "Aug":"08","Sep":"09", "Oct":"10","Nov":"11", "Dec":"12" }
        month = AsString(translateMonths[self.show()])
        return month.show()

    def upper(self):
        '''@return name of the month in upeprcase'''
        return self.show().upper()

    def __eq__(self, other):
        return self.timefile == other.timefile 

    def __repr__(self):
        return "Month[" + self.single_number() +"][" + self.show() +"]" 

class TestMonth(unittest.TestCase):

        def test_upper(self):
            result = Month("Wed Jun 10 17:04:28 2020").upper()
            self.assertEqual(result, "JUN")

        def test_number(self):
            result = Month("Wed Jun 10 17:04:28 2020").single_number()
            self.assertEqual(result, "06")

        def test_show(self):
            result = Month("Wed Jun 10 17:04:28 2020").show()
            self.assertEqual(result, "Jun")

                
        def test_eq(self):
            time_one = "Wed Jun 10 17:04:28 2020"
            time_two = "Wed Jun 10 17:04:28 2020"
            month_one = Month(time_one)
            month_two = Month(time_two)
            self.assertEqual(month_one, month_two)
    

