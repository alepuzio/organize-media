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



