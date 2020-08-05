import unittest
from Month import Month
from Year import Year


class YearMonth:
    '''@overview: this class incapsulate the data about the year
        TODO control if logic duplicated in another class or method
    '''

    def __init__(self, newyear, newmonth):
        self.year = newyear
        self.month = newmonth


    def show(self):
        '''@return creation year as 'yyyymm' '''
        return str(self.year) + str(self.month.single_number())


    def __repr__(self):
        return "YearMonth[" + str(self.year) +"][" + str(self.month) +  "]"


class TestYearMonth(unittest.TestCase):

    def test_show(self):
        year = "2020"
        month = Month("Jun")
        yearMonth = YearMonth(year, month)
        expected = "202006"
        self.assertEqual(yearMonth.show(), expected)



