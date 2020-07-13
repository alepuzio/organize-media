import unittest
import os

class Root:
    '''@overview: class thant manage the root'''

    def __init__(self, newabsolutepath):
        self.absolutepath = newabsolutepath


    def show(self):
        '''@return the path expect of the topic'''    
        path = self.absolutepath.split(os.sep)
        index_second_to_last = len(path) -1
        return os.sep.join(path[ 0 : index_second_to_last ] )

    def __eq__(self, other):
        return self.absolutepath == other.absolutepath

    def __repr__(self):
        return "Root[" + self.show() + "]"

class TestRoot(unittest.TestCase):


    def test_show(self):
        path = "c:\\path\\absolute\\with\\no\\topic"
        result = Root(path).show()
        expected = "c:\\path\\absolute\\with\\no"
        self.assertEqual(result, expected)

