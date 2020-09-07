from PersonalLogging import PersonalLogging
from AsString import AsString
import os
import unittest
from Month import Month
from Media import Media
from OriginalFile import OriginalFile
from YearMonth import YearMonth 
from Position import Position
from Time import Time
from TimeFile import TimeFile
from InitialData import InitialData



class SingleFinalData:
    '''@ovewview this class represent the final data necessaryt ot run the copy of the original file'''

    def __init__(self, newroot, neworiginaltupla):
       self.log = PersonalLogging("SingleFinalData", False)
       self.root = newroot
       self.originaltupla = neworiginaltupla

    def tupla(self):
        '''@return  data of the original file as tupla'''
        self.log.print("tupla iniziale:\n" + AsString(self.originaltupla.tupla()[0]).show())
        year = self.originaltupla.time.year()
        month = self.originaltupla.time.month()
        topic = self.originaltupla.position.topic() 
        filename = self.originaltupla.position.name()
        extension = self.originaltupla.position.extension()
        root = self.root
        media = Media(extension)

        day = self.originaltupla.time.day()
        return (root, year, month, topic, media, filename, extension, day)

    def physicalFile(self):
        '''@return the complete path as String'''
        data = self.tupla()
        #listdata = [data[0], data[1], YearMonth(data[1], data[2]).show(), data[3], "original", data[4].directory() , data[5], data[6].name()]
        listdata = [data[0], data[1], YearMonth(data[1], data[2]).show(), data[3],  data[4].directory() , data[5], data[6].name()]
        path = os.sep.join(listdata[0:6])
        self.log.print("path: {0}".format( path ) )
        return AsString(path + "." + data[6].name() ).show()
    
    def physicalPath(self):
        '''@return the complete path as String, no filename and extension'''
        data = self.tupla()
        listdata = [data[0], data[1], data[2].name(), data[3], data[4].directory() , data[5] ]
        path = os.sep.join(listdata[0:5])
        return AsString(path).show()
        
    def __repr__(self):
        return "SingleFinalData[" + self.physicalFile() + "]\n>>>" + str(self.tupla())

    def __eq__(self, other):
        return self.physicalFile() == other.physicalFile()


