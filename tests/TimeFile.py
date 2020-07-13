import os
import platform
import time
import unittest
from datetime import datetime


class TimeFile:
    '''@overview: this class incapsulate the data bout time and date 
    '''

    def __init__(self, newabsolutepath):
        self.absolutepath = newabsolutepath

    
    def complete(self):
        ''' @return datetime of the creation file'''
        return time.ctime(os.path.getctime(self.absolutepath ))


class TestTimeFile(unittest.TestCase):

    def test_complete(self):
        absolutePath = ".\\resources\\lugano\\vecchia.jpg"
        timefile = TimeFile(absolutePath)
        expected = "Wed Jun 10 17:04:28 2020"
        self.assertEqual(timefile.complete(), expected)
