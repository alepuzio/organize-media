import pytest
from .test_month import Month
from .test_year import Year

class YearMonth:
    """
    @overview: this class incapsulate the data about the year
        TODO control if logic duplicated in another class or method
    """

    def __init__(self, newyear, newmonth):
        self.year = newyear
        self.month = newmonth

    def show(self):
        """
        @return creation year as 'yyyymm' 
        """
        return str(self.year) + str(self.month.single_number())

    def __repr__(self):
        return "YearMonth[" + str(self.year) +"][" + str(self.month) +  "]"


def test_show():
    year = "2020"
    month = Month("Jun")
    yearMonth = YearMonth(year, month)
    expected = "202006"
    assert(yearMonth.show() == expected)



