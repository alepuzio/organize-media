import unittest
from Month import Month
from Year import Year
from Day import Day

class DayMonthYear:
    '''@overview: this class incapsulate the data about the year'''

    def __init__(self, newday, newmonth , newyear ):
        self.year = newyear
        self.month = newmonth
        self.day = newday

    def show(self):
        '''@return creation year as 'dd/mm/yyyy' '''
        return "/" .join ( [self.day.show(), self.month.show() , self.year.show()] )

    def __repr__(self):
        return "DayMonthYear[" + self.day.show() +"][" + self.month.show() +  "][" + self.year.show() + "]"


class TestDayYearMonth(unittest.TestCase):

    def test_show(self):
        time = "Wed Jun 10 17:04:28 2020"
        year = Year(time)
        month = Month (time)
        day = Day(time)
        dayMonthYear = DayMonthYear(day, month, year)
        expected = "10/06/2020"
        self.assertEqual( dayMonthYear.show(), expected)



