from PersonalLogging import PersonalLogging
from AsString import AsString
import os
import unittest
from Extension import Extension


class Media:
    '''@overview this class extract the type of media'''

    def __init__(self, newextension):
        self.extension = newextension
        self.log = PersonalLogging("Media", False)

    def directory(self):
        '''@return the name of the directory abotu the media'''
        pieces = self.extension.show().split(".")
        pieces.reverse();
        ext = pieces[0]
        self.log.warn("pieces[0]:" + str(ext))
        return  ext.upper() 

class TestMedia(unittest.TestCase):

    def test_media(self):
        extension = Extension("generic_image_raw.CR2")
        result = Media(extension).directory()
        expected = "CR2"
        self.assertEqual(result, expected)


