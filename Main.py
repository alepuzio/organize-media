import sys
from organizemedia.personal_logging import PersonalLogging
from tests.test_control import Control

#class Main:
 
 #'''@overview entry point of the application'''

if __name__ == '__main__':
    controls = Control(sys.argv)
    operation= controls.act()
    operation.run()
