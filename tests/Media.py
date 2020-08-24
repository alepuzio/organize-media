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
        '''@return the name of the directory about the media'''
        pieces = self.extension.name().split(".")
        pieces.reverse();
        return  pieces[0].upper() 

    def __eq__(self, other):
        return self.extension == other.extension

    def __str__(self):
        return "Media[" + str(self.extension) + "]"

    def __repr__(self):
        return "Media[" + str(self.extension) + "]->[" + self.directory() +"]"

class TestMedia(unittest.TestCase):

    def test_media(self):
        extension = Extension("generic_image_raw.CR2")
        result = Media(extension).directory()
        expected = "CR2"
        self.assertEqual(result, expected)


