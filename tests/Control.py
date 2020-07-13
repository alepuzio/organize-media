import sys
#import os
import unittest
#from Filesystem import FileSystem
from PersonalLogging import PersonalLogging
#from GroupOriginalFiles import GroupOriginalFiles
#from DecomposeOriginalFile import DecomposeOriginalFile
#from GroupFinalData import GroupFinalData


class Control:
    '''@overview the class control the params'''
    def __init__(self, args):
        self.args = args
        self.log = PersonalLogging("Control", False)

    def act(self):
        '''@return true if the paramers are correct'''
        numberParams = len(self.args)
        correctNumberParams =  (3 == numberParams)
        if not correctNumberParams:
            self.log.print("The params have to be:")

            self.log.print("1) name of the program: Main.py ")
            self.log.print("2) root where there are the original files")
            self.log.print("2) root where to copy the read files")
            self.log.print("Now theese are [" + str(numberParams) +"]:" + str(self.args))
        result = correctNumberParams
        return result

    #TODO mettere controllo che il path passato deve avere il sepratore os.sep corretto
    # altrimenti ci saranno problemi con i file

class TestControl(unittest.TestCase):
    '''the class control the params'''
    def test_act_1_params_ko(self):
        control = Control(["./"])
        result = control.act()
        expected = False
        self.assertEqual(expected, result)

    def test_act_2_params_ko(self):
        control = Control(["./", "./aa"])
        result = control.act()
        expected = False
        self.assertEqual(expected, result)
 
    def test_act_3_params_ok(self):
        control = Control(["Main.py", "./", "./aa"])
        result = control.act()
        expected = True
        self.assertEqual(expected, result)
