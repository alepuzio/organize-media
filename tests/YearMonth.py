import unittest
from Month import Month
from Year import Year


class YearMonth:
    '''@overview: this class incapsulate the data about the year'''

    def __init__(self, newyear, newmonth):
        self.year = newyear
        self.month = Month(newmonth)


    def show(self):
        '''@return creation year as 'yyyymm' '''
        return str(self.year) + str(self.month.single_number())


    def __repr__(self):
        return "YearMonth[" + str(self.year) +"][" + str(self.month) +  "]"


class TestYearMonth(unittest.TestCase):

    def test_show(self):
        year = "2020"
        month = "06"
        yearMonth = YearMonth(year, month)
        expected = "202006"
        self.assertEqual(yearMonth.show(), expected)



