import os
import unittest
from PersonalLogging import PersonalLogging
class AbsolutePath:
    '''@overview: leggo il path assoluto del file passato'''

    def __init__(self, newrelativepath):
        self.relativepath = newrelativepath
        self.logging = PersonalLogging("AbsolutePath", True)

    def absolute(self):
        return os.path.abspath(self.relativepath)


class TestAbsolutePath(unittest.TestCase):

    def test_absolute_exists(self):
        relativepath = ".\\resources\\lugano\\vecchia.jpg"
        toRead = AbsolutePath(relativepath)
        expected = "C:\\Users\\alepu\\Documents\\repo-github\\organize-media\\tests\\resources\\lugano\\vecchia.jpg"
        self.assertEquals(toRead.absolute(), expected)

