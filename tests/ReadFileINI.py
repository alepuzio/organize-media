import unittest
import os
from PersonalLogging import PersonalLogging
from Extension import Extension
from QuotationMark import QuotationMark
from QuotationMark import QuotationMark

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
        path =  self.dir + os.sep + "common.ini" #TODO concatenation of string to improve
        exists = os.path.exists(path)
        if exists :
            config.read(path)
            #TODO centralize in an object
            path = self.dir.split ( os.sep )
            path.reverse()
            extension = Extension ( path[0] )#TODO put control if the path finish in \ or \\
            
            file_ini = ReadFileINI(self.dir)
            if extension.image(): #TODO: create decorator and class
                self.log.print("reo file immagine")
                file_ini = Image ( ReadINI ( config ) ) 
            elif extension.video():
                self.log.print("creo file video")
                file_ini = Video ( ReadINI ( config ) ) 
            else:
                raise Exception ("Unkown type of file:{0}".format(extension) ) 
        else:
            raise Error( "The file [[0}] is not present, I stop the elaboration".format(path) )
        return file_ini

class Image:
    '''@overview: this class contains the configuration about the images'''
    def __init__(self, new_read_ini):
        self.name = 'Image'
        self.read = new_read_ini

    def copyright(self):
        return  QuotationMark( self.read.copyright(self.name) ).string()

    def city(self):
        return self.read.city(self.name)
    
    def price(self):
        return self.read.price(self.name)
    
    def specifysource(self):
        return QuotationMark ( self.read.specifysource(self.name) ).string()
    
    def region(self):
        return self.read.region(self.name)
    
    def imagetype(self):
        return 'photo'

    def country(self):
        return self.read.country(self.name)
   
    def __str__(self):
       return "Image:[{0}]".format(self.name)

class Video:
    '''@overview: this class contains the configuration about the videos'''
    def __init__(self, new_read_ini):
        self.name = 'Video'
        self.read = new_read_ini

    def copyright(self):
        return QuotationMark( self.read.copyright(self.name) ).string()

    def city(self):
        return self.read.city(self.name)
    
    def price(self):
        return self.read.price(self.name)
    
    def specifysource(self):
        return QuotationMark ( self.read.specifysource(self.name) ).string()
    
    def region(self):
        return self.read.region(self.name)
    
    def imagetype(self):
        return 'video'

    def country(self):
        return self.read.country(self.name)


    def __str__(self):
       return "Video:[{0}]".format(self.name)


class ReadINI:
    '''@overview: this class contains the configuration'''
    def __init__(self, new_config ):
        self.config = new_config

    def copyright(self, name):
        return self.config.get(name, 'Copyright' )
    
    def city(self, name):
        return self.config.get(name,'City')
    
    def price(self, name):
        return self.config.get(name, 'Price')
    
    def specifysource(self, name):
        return self.config.get(name,'SpecifySource')
    
    def region(self, name):
        return self.config.get(name,'Region')
    
    def imagetype(self, name):
        return self.config.get(name,'ImageType')

    def country(self, name ):
        return self.config.get(name,'Country')
   
    def __str__(self):
       return "ReadINI:[{0}]".format(self.copyright())
