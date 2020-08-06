import unittest

class DayMonthYear:
    '''@overview: this class incapsulate the data about the year'''

    def __init__(self, newday, newmonth , newyear ):
        self.year = newyear
        self.month = newmonth
        self.day = newday

    def show(self, separator):
        '''@return creation year as 'ddseparatormmseparatoryyyy'
           @param separator = string
        '''
        return separator.join ( [self.day, self.month , self.year] )

    def __repr__(self):
        return "DayMonthYear[" + self.day +"][" + self.month +  "][" + self.year + "]"

class Slash:
    '''@overview: decorator with slash'''
    def __init__(self, newdaymonthyear):
        self.daymonthyear = newdaymonthyear

    def show(self):
        return self.daymonthyear.show("/")


class Space:
    '''@overview: decorator with one space'''
    def __init__(self, newdaymonthyear):
        self.daymonthyear = newdaymonthyear

    def show(self):
        return self.daymonthyear.show(" ")





class TestDayYearMonth(unittest.TestCase):

    def test_show_slash(self):
        year = "2020"
        month = "06"
        day = "10"
        dayMonthYear = Slash(DayMonthYear(day, month, year)).show()
        expected = "10/06/2020"
        self.assertEqual( dayMonthYear, expected)


    def test_show_space(self):
        year = "2020"
        month = "06"
        day = "10"
        dayMonthYear = Space(DayMonthYear(day, month, year)).show()
        expected = "10 06 2020"
        self.assertEqual( dayMonthYear, expected)

