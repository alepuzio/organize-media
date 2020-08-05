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

    def name(self):
        '''@return creation month as string '''
        date = self.timefile
        self.log.print("Month.show():" + str(date))
        tmp = date.split(" ")
        #return tmp[1]
        return self.timefile

    def single_number(self):
        '''@return number of the month'''
        #TODO rename to 'number'
        translateMonths= {"Jan":"01", "Feb":"02", "Mar":"03", "Apr":"04", "May":"05", "Jun":"06", "Jul":"07", "Aug":"08","Sep":"09", "Oct":"10","Nov":"11", "Dec":"12" }
        month = AsString ( translateMonths[self.name()] )
        return month.show()

    def __eq__(self, other):
        return self.timefile == other.timefile 

    def __repr__(self):
        return "Month[" + self.single_number() +"][" + self.name() +"]" 

class TestMonth(unittest.TestCase):

        def test_number(self):
            result = Month("Wed Jun 10 17:04:28 2020").single_number()
            self.assertEqual(result, "06")

        def test_name(self):
            result = Month("Wed Jun 10 17:04:28 2020").name()
            self.assertEqual(result, "Jun")
                
        def test_eq(self):
            time_one = "Wed Jun 10 17:04:28 2020"
            time_two = "Wed Jun 10 17:04:28 2020"
            month_one = Month(time_one)
            month_two = Month(time_two)
            self.assertEqual(month_one, month_two)
    

