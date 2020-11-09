import sys
import unittest
from PersonalLogging import PersonalLogging
from Write import Write
from Copy import Copy
from Join import Join
from ListTag import ListTag

class Control:
    '''@overview the class control the params'''
    def __init__(self, new_args):
        self.arguments = new_args
        self.log = PersonalLogging("Control", True)

    def act(self):
        '''@return true if the paramers are correct'''
        var = None
        opts = [opt for opt in self.arguments[1:] if opt.startswith("-")]
        args = [arg for arg in self.arguments[1:] if not arg.startswith("-")]
        print("opts:" +  str(opts))
        print("args: " + str(args))
        if 0 == len(opts):
            self.log.warn("Mandatory flas:\n-c(copy the file from source dir to target dir);\n-w(rite) the file CSV and INI in one dir;\n -j(oin) the CSV and INI files in one in one dir")
            self.log.warn("Exit program")
        if "-c" in opts:
            self.log.print("Copy(" + str(args) +")")
            var = Copy(args)
        elif "-w" in opts:
            self.log.print("Write")
            var = Write(args)
        elif "-j" in opts:
            self.log.print("Join")
            var = Join(args) 
        elif "-l" in opts:
            self.log.print("List")
            var = ListTag(args) 
        else:
            self.log.warn("The flag [{0}] is unkown".format (opts) )

        return var

        
    #TODO mettere controllo che il path passato deve avere il sepratore os.sep corretto
    # altrimenti ci saranno problemi con i file

class TestControl(unittest.TestCase):
    '''the class control the params'''

 
    def test_copy_ok(self):
        source  = "./aa"
        dest = "./f"
        control = Control(["Main.py", "-c", source, dest])
        result = control.act()
        expected = Copy([source, dest])
        self.assertEqual(expected, result)

    def test_list_ok(self):
        print("********* test_list_ok***************")
        source  = "./aa"
        control = Control(["Main.py", "-l", source])
        result = control.act()
        expected = ListTag ( [source] )
        self.assertEqual(expected, result)

    def test_Join_ok(self):
        print("********* test_join_ok***************")
        source  = "./aa"
        control = Control(["Main.py", "-j", source])
        result = control.act()
        expected = Join([source])
        self.assertEqual(expected, result)

    def test_write_ok(self):
        print("********* test_write_ok***************")
        source  = "./aa"
        control = Control(["Main.py", "-w", source])
        result = control.act()
        expected = Write([source])
        self.assertEqual(expected, result)