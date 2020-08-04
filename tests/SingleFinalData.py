from PersonalLogging import PersonalLogging
from AsString import AsString
import os
import unittest
from Month import Month
from Media import Media
from MonthFinal import MonthFinal
from OriginalFile import OriginalFile

class SingleFinalData:
    '''@ovewview this class represent the final data necessaryt ot run the copy of the original file'''

    def __init__(self, newroot, neworiginaltupla):
       self.log = PersonalLogging("SingleFinalData", False)
       self.root = newroot
       self.originaltupla = neworiginaltupla


    def tupla(self):
        '''trasform data of the original file in tupla'''
        self.log.print("tupla iniziale:\n" + AsString(self.originaltupla).show())
        year = self.originaltupla[0]
        self.log.print("year:" + year.show())
        month = self.originaltupla[1]
        self.log.print("month:" + month.show()) 
        month = MonthFinal ( month )
        topic = self.originaltupla[2] 
        filename = self.originaltupla[3]
        extension = self.originaltupla[4]
        root = self.root
        media = Media(self.originaltupla[4]).directory()
        day = self.originaltupla[6]
        return (root, year, month, topic, media, filename, extension, day)

    def physicalFile(self):
        '''@return the complete path as String'''
        data = self.tupla()
        listdata = [data[0], data[1].show(), data[2].show(), data[3].show(), data[4], data[5].show()]
        path = os.sep.join(listdata[0:6])
        return AsString(path + "." + data[6].show() ).show()
    
    def physicalPath(self):
        '''@return the complete path as String, no filename and extension'''
        data = self.tupla()
        listdata = [data[0], data[1].show(), data[2].show(), data[3].show(), data[4], data[5].show()]
        path = os.sep.join(listdata[0:5])
        return AsString(path).show()
        
    def __repr__(self):
        return "SingleFinalData[" + self.physicalFile() + "]\n>>>" + str(self.tupla())

    def __eq__(self, other):
        return self.physicalFile() == other.physicalFile()

