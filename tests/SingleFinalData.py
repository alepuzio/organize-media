from PersonalLogging import PersonalLogging
from AsString import AsString
import os
import unittest
from Month import Month
from Media import Media
#from MonthFinal import MonthFinal
from OriginalFile import OriginalFile

class SingleFinalData:
    '''@ovewview this class represent the final data necessaryt ot run the copy of the original file'''

    def __init__(self, newroot, neworiginaltupla):
       self.log = PersonalLogging("SingleFinalData", False)
       self.root = newroot
       self.originaltupla = neworiginaltupla


    def tupla(self):
        '''trasform data of the original file in tupla'''
        self.log.print("tupla iniziale:\n" + AsString(self.originaltupla.tupla()[0]).show())
        year = self.originaltupla.time.year()
        month = self.originaltupla.time.month()
        self.log.print("month:" + month.name()) 
        #month = MonthFinal ( month )
        topic = self.originaltupla.position.topic() 
        filename = self.originaltupla.position.name()
        extension = self.originaltupla.position.extension()
        root = self.root
        media = Media(extension).directory()
        day = self.originaltupla.time.day()
        return (root, year, month, topic, media, filename, extension, day)

    def physicalFile(self):
        '''@return the complete path as String'''
        data = self.tupla()
        listdata = [data[0], data[1], data[2].name(), data[3], data[4], data[5], data[6].name()]
        path = os.sep.join(listdata[0:6])
        return AsString(path + "." + data[6].name().upper() ).show()
    
    def physicalPath(self):
        '''@return the complete path as String, no filename and extension'''
        data = self.tupla()
        listdata = [data[0], data[1], data[2].name(), data[3], data[4], data[5]]
        path = os.sep.join(listdata[0:5])
        return AsString(path).show()
        
    def __repr__(self):
        return "SingleFinalData[" + self.physicalFile() + "]\n>>>" + str(self.tupla())

    def __eq__(self, other):
        return self.physicalFile() == other.physicalFile()

