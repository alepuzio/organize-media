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
        return "\"" + self.config.get('Image', 'Copyright' ) + "\""
    
    def city(self):
        return self.config.get('Image','City')
    
    def price(self):
        return self.config.get('Image', 'Price')
    
    def specifysource(self):
        return "\"" + self.config.get('Image','SpecifySource') + "\""
    
    def region(self):
        return self.config.get('Image','Region')
    
    def imagetype(self):
        return self.config.get('Image','ImageType')

    def country(self):
        return self.config.get('Image','Country')
   
    def __str__(self):
       return "ReadINI:[{0}]".format(self.copyright())
