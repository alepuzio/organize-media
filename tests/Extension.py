import unittest
from PersonalLogging import PersonalLogging


class Extension:
    '''@overview: this class extract the extension of the read file'''
    
    def __init__(self, new_extension):
        self.ext = new_extension
        self.log = PersonalLogging("Extension", True)
        
    def __repr__ (self):
         return "Extension[" + str(self.media()) +"][" + self.name() +"]"
    
    def name(self):
        return self.ext

    def media(self):
        '''@return True se il fiel e' img o video'''
        typeFile = self.name().upper()
        print ("type: " + typeFile) 
        allowedExtensions = ["CR2", "JPG", "MOV"]
        return  (typeFile in allowedExtensions)


    def __eq__(self, other):
        return (self.ext == other.ext)


class TestExtension(unittest.TestCase):
    
    def test_show(self):
        absolutepath = "jpg"
        result = Extension(absolutepath).name().upper()
        expected = "JPG"
        self.assertEqual(result, expected)
    
    def test_media_supported(self):
        absolutepath = "jpg"
        result = Extension(absolutepath).media()
        self.assertTrue(result)
    
    def test_media_unsupported(self):
        absolutepath = "jpg2"
        result = Extension(absolutepath).media()
        self.assertFalse(result)


    def test_equal(self):
        absolutepath_one = "jpg"
        absolutepath_two = "jpg"
        result_one = Extension(absolutepath_one)
        result_two = Extension(absolutepath_two)
        self.assertEqual(result_one, result_two)


