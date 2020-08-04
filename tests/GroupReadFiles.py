import unittest
import os
from OriginalFile import OriginalFile
from AbsolutePath import AbsolutePath
from PersonalLogging import PersonalLogging
from Extension import Extension


class GroupReadFiles:
    '''@overview: classe che riceve i file letti e li trasforma in OriginalFiles'''

    def __init__(self, new_list_readfiles):
        self.list_readfiles = new_list_readfiles
        self.logging = PersonalLogging("GroupReadFiles", False)

    def map(self):
        '''@return la mappa tra persorso assoluto del file letto e la class originalFile'''
        result = {}
        for filetmp in self.list_readfiles:
            self.logging.print("filetmp: " + str(filetmp))
            path = AbsolutePath(filetmp).absolute()
            tail, head = os.path.split(filetmp)
            if Extension(head).media():
                result[filetmp]= OriginalFile(tail, head)
            else:
                self.logging.warn("Il file [" + head + "] non verra processato")
        return result


