import sys
import unittest
from PersonalLogging import PersonalLogging


class Control2:
    '''@overview the class control the params'''
    def __init__(self, new_args):
        self.arguments = new_args
        self.log = PersonalLogging("Control2", True)

    def act(self):
        '''@return true if the paramers are correct'''
        numberParams = len(self.arguments)
        correctNumberParams =  ( 3 < numberParams  )
        
        if not correctNumberParams:
            self.log.print("The params have to be:")
            self.log.print("1) name of the program: Main.py ")
            self.log.print("2) comand to run")
            self.log.print("3) directory")
            self.log.print("Now theese are [" + str(numberParams) +"]:" + str(self.arguments))
        else:
            opts = [opt for opt in self.arguments[1:] if opt.startswith("-")]
            args = [arg for arg in self.arguments[1:] if not arg.startswith("-")]
            var = None
            print("opts:" +  str(opts))
            print("args: " + str(args))
            if "-c" in opts:
                self.log.print("Copy(" + str(args) +")")
                var = Copy(args)
            elif "-w" in opts:
                self.log.print("Write")
                var = Write(args[1])
            elif "-j" in opts:
                self.log.print("Join")
                var = Join(args[1]) 
        return var

        
    #TODO mettere controllo che il path passato deve avere il sepratore os.sep corretto
    # altrimenti ci saranno problemi con i file

class Copy:
    '''@overview: class to copy file'''

    def __init__(self, one):
        print(one )
        self.source = one[0]
        self.dest = one[1]


    def __repr__(self):
        return 'Copy( source = %s, dest = %s )' % (self.source, self.dest)

    def __str__(self):
        return "Copy(%s,%s)" % (self.source, self.dest)

    def __eq__(self, other):
        return self.source == other.source and self.dest == other.dest

class Join:
    '''@overview: class to join CSV and INI file'''

    def __init__(self, new_directory):
        self.directory = new_directory



class TestControl(unittest.TestCase):
    '''the class control the params'''

 
    def test_act_3_params_ok(self):
        source  = "./aa"
        dest = "./f"
        control = Control2(["Main.py", "-c", source, dest])
        result = control.act()
        expected = Copy([source, dest])
        self.assertEqual(expected, result)
