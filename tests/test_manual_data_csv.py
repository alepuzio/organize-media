import pytest

from src.personal_logging import PersonalLogging
from src.safe_file import SafeFile
from src.file_to_write import FileToWrite

from .test_day_month_year  import DayMonthYear
from .test_day_month_year import Slash
from .test_extension import Extension
from .test_month import Month
from .test_position import PositionFake

class ManualDataCSV:
    """@overview: class for the partial csv fil"""
    
    def __init__(self, new_safe_file):
        self.safefile = new_safe_file
        self.logging = PersonalLogging("ManualDataCSV")

    def data(self, map_file_single_data):
        """
        @return list of data file
        """
        list_rows = []
        list_rows.append("Day,Month,Year,OriginalFilename,Description,Keywords,\n") 
        for tmp_file in map_file_single_data.keys():
            tmp_value = map_file_single_data[tmp_file]
            list_rows.append( "%s,%s,%s,%s\t,%s\t,%s\n" % (tmp_value.tupla().time.day()  , tmp_value.tupla().time.month().single_number(), tmp_value.tupla().time.year()  , self.filename ( tmp_value.tupla() ), "  ", "  "))

        return self.safefile.safe(list_rows)
        
    
    def time(self, tmp_value):
        """@return the day mm year of the file"""
        year = tmp_value.time.year()
        month = tmp_value.time.month().single_number()
        day = tmp_value.time.day()
        time = DayMonthYear(day, month, year)
        return time


    def filename(self, tmp_value):
        """@return thefilename and extensione of the file"""
        filename = "%s.%s"  % (tmp_value.position.name(), tmp_value.position.extension().name() )
        return filename


"""
Test area TODO code again after use ad-hoc class instead of tuplas
def test_filename():
    tmp_value = ( "2020", Month("Jun"), "30", "topic", "filename", Extension("jpg") )
    result = ManualDataCSV(None).filename(tmp_value)
    expected = "filename.jpg"
    assert (result == expected)


    def st_time(self):
        tmp_value = ( "2020", Month("Jun"), "30", "topic", "filename", Extension("jpg") )
        result = ManualDataCSV(None).time(tmp_value)
        expected = "30/03/2020"
        assert (result == expected)
"""
