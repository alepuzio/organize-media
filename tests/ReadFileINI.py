import unittest
import os
from PersonalLogging import PersonalLogging

class ReadFileINI:
    '''@overview: it contains the properties in file INI'''

    def __init__(self, new_dir):
        self.dir = new_dir
        self.log = PersonalLogging("ReadINI")

    def read(self):
        '''@return the object with the properties'''
        try:
            from configparser import ConfigParser
        except ImportError:
            from ConfigParser import ConfigParser  # ver. < 3.0
        config = ConfigParser()
        path =  self.dir + os.sep+ "common.ini" #TODO concatenation of string to improve
        config.read(path)
        return ReadINI(config)



class ReadINI:
    '''overview: this class contains the configuration'''


    def __init__(self, newconfig):
        self.config = newconfig

    def copyright(self):
        return config.get('Image', 'Copyright' )
    
    def city(self):
        return config.get('Image','City')
    
    def price(self):
        return config.getInt('Image', 'Price')
    
    def specifysource(self):
        return config.get('Image','SpecifySource')
    
    def region(self):
        return config.get('Image','Region')
    
    def imagetype(self):
        return config.get('Image','ImageType')
    
    def country(self):
        return config.get('Image','Country')
    
