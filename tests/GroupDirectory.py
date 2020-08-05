import unittest
import os
from PersonalLogging import PersonalLogging
from OriginalFile import OriginalFile
from SingleFinalData import SingleFinalData
from SafeDirectory import SafeDirectory
from YearMonth import YearMonth

class GroupDirectory:
    '''@overivew: this class create the new directory  fro mthe final data tupla'''

    def __init__(self, new_list_finaltupla):
        self.list_final_tupla = new_list_finaltupla
        self.logging = PersonalLogging("GroupDirectory", True)

    def various_directory(self):
        '''@return  the list of the new directory with complete path'''
        result = []
        for filetmp in self.list_final_tupla:
            self.logging.print("filetmp:" + str(filetmp))
            data_tmp = filetmp.tupla()
            data = ( data_tmp[0], data_tmp[1],  YearMonth(data_tmp[1], data_tmp[2]).show(),  data_tmp[3], data_tmp[4].directory(), data_tmp[5] )
            self.logging.print("data" + ">" + str(data) )
            limit = len(data)
            for place in range(1, limit ):
                result.append(os.sep.join(data[0:place]))
        return result

    def unique(self, listtmp):
        '''@return the list with 1 occurrence for every element'''
        result = set()
        listtmp.sort()
        for tmp in listtmp:
            result.add(tmp)
        return result

    def createDirectories(self, list_dir):
        '''crete all not existing directory'''
        for element in list_dir:
            possible_dir = SafeDirectory(element)
            possible_dir.create()
        self.logging.print("The directories are created on filesystem")


    def write(self):
        '''create the directory and doesn't modifiy the existing'''
        list_dir = self.various_directory()
        to_write = self.unique(list_dir)
        self.createDirectories(to_write)
        return to_write

