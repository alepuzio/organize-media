import sys
import unittest
from PersonalLogging import PersonalLogging
from Control import Control

#class Main:
 
 #'''@overview entry point of the application'''

if __name__ == '__main__':
    controls = Control(sys.argv)
    operation= controls.act()
    operation.run()
