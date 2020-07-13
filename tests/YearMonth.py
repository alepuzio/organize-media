import unittest
from Month import Month
from Year import Year


class YearMonth:
    '''@overview: this class incapsulate the data about the year'''

    def __init__(self, newyear, newmonth):
        self.year = newyear
        self.month = newmonth


    def show(self):
        '''@return creation year as 'yyyymm' '''
        return self.year.show() + self.month.single_number()


    def __repr__(self):
        return "YearMonth[" + self.year.show() +"][" + self.month.show() +  "]"


class TestYearMonth(unittest.TestCase):

    def test_show(self):
        time = "Wed Jun 10 17:04:28 2020"
        year = Year(time)
        month = Month (time)
        yearMonth = YearMonth(year, month)
        expected = "202006"
        self.assertEqual(yearMonth.show(), expected)



