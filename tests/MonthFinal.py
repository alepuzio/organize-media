import unittest
from Month import Month 

class MonthFinal:
    '''@overview: this class incapsulate the data about the month'''

    def __init__(self, newmonth):
        self.month = newmonth


    def show(self):
        '''@return creation year as 'yyyymm' '''
        return self.month.single_number()


    def __repr__(self):
        return "Month[" + self.month.show() +  "]"


class TestFinalMonth(unittest.TestCase):

    def test_show(self):
        time = "Wed Jun 10 17:04:28 2020"
        month = MonthFinal ( Month (time) ) 
        expected = "06"
        self.assertEqual(month.show(), expected)



