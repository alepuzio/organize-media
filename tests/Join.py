import sys
import unittest
from PersonalLogging import PersonalLogging
from Write import Write
from Copy import Copy
from ReadFileINI import ReadFileINI
from ReadFileCSV import ReadFileCSV
        
    #TODO mettere controllo che il path passato deve avere il sepratore os.sep corretto
    # altrimenti ci saranno problemi con i file


class Join:
    '''@overview: class to join CSV and INI file'''
    def __init__(self, new_args ):
        self.directory = new_args[0]

    def __repr__(self):
        return 'Join(%s)' % (self.directory)

    def __str__(self):
        return "Join(%s)" % (self.directory)

    def __eq__(self, other):
        return self.directory == other.directory
    
    def run(self):
        '''run the join between data of INI file and CSV file'''
        
        '''take the dir'''
        '''put the ini inside an object'''

        properties_ini = ReadFileINI(self.directory).read()# has INI 
        # print("properties.ini:{0}".format( str(properties_ini)))
        '''TODO control that every property has a value, othrwise exception'''
        '''read the CSV'''
        
        properties_csv = ReadFileCSV(self.directory).read()# has INI 
        print("properties.csv:{0}".format( str(properties_csv)))
        '''
        every row-obejct is put inside another object with the optional data and the INI object
         
        this object will be in another list'''
        
        '''the list is passed to a class that creates the file'''
        '''this object is formatted as CSV'''
 
