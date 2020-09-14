import unittest
import os
from OriginalFile import OriginalFile
from AbsolutePath import AbsolutePath
from PersonalLogging import PersonalLogging
from Extension import Extension
from SingleFinalData import SingleFinalData


class GroupOriginalFiles:
    '''@overview: classe che riceve gli OriginalFiles e li trasforma in FinalFiles'''

    def __init__(self, new_map_originalfiles):
        self.map_originalfiles = new_map_originalfiles
        self.logging = PersonalLogging("GroupOriginalFiles", False)

    def map(self, output_dir):
        '''@return la mappa tra persorso assoluto del file letto e dati disaggregati del file da copiare'''
        result = {}
        self.logging.print("map: " + str(self.map_originalfiles))
        for filetmp in self.map_originalfiles.keys():
           disaggregated_data = self.map_originalfiles[filetmp] 
           self.logging.print( "disaggregated_data: " + str(disaggregated_data) )
           var = SingleFinalData(output_dir, disaggregated_data.tupla())
           self.logging.print( "var: " + str(var))
           result[filetmp] = var
        #self.logging.print( "result: " + str(result) )
        return result


