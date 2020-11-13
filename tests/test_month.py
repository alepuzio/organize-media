import datetime
import platform
import pytest

from src.personal_logging import PersonalLogging


class Month:
    """ @overview this class has the dat aof year and month"""

    def __init__(self, newformattedtimestamp):
        self.timefile = newformattedtimestamp
        self.log = PersonalLogging("Month", False)

    def name(self):
        """@return creation month as string """
        date = self.timefile
        self.log.print("Month.show():" + str(date))
        tmp = date.split(" ")
        return self.timefile

    def single_number(self):
        """@return number of the month"""
        #TODO rename to 'number'
        translateMonths= {"Jan":"01", "Feb":"02", "Mar":"03", "Apr":"04", "May":"05", "Jun":"06", "Jul":"07", "Aug":"08","Sep":"09", "Oct":"10","Nov":"11", "Dec":"12" }
        return str ( translateMonths[self.name()] )

    def __eq__(self, other):
        return self.timefile == other.timefile 

    def __repr__(self):
        return "Month[" + self.single_number() +"][" + self.name() +"]" 

def test_number():
    result = Month("Jun").single_number()
    assert (result== "06")

def test_name():
    result = Month("Jun").name()
    assert(result == "Jun")
                
def test_eq():
    time_one = "Jul"
    time_two = "Jul"
    month_one = Month(time_one)
    month_two = Month(time_two)
    assert(month_one== month_two)
    

