import unittest
from PersonalLogging import PersonalLogging


class Extension:
    '''@overview: this class extract the extension of the read file'''
    
    def __init__(self, newfile):
        self.file = newfile
        self.log = PersonalLogging("Extension", False)
        
    def __repr__ (self):
         return "Extension[" + str(self.media()) +"][" + self.show() +"]"
    
    def show(self):
        pieces = self.file.split(".")
        if ( 1 < len (pieces)) :
            file_extension = pieces[1]
        else:
            self.log.warn( "non ha estensione :" + str(pieces) )
            file_extension = "UNSUPPORTED-EXTENSION"
        return file_extension

    def media(self):
        '''@return True se il fiel e' img o video'''
        typeFile = self.show().upper()
        allowedExtensions = ["CR2", "JPG", "MOV"]
        return  (typeFile in allowedExtensions)


    def __eq__(self, other):
        return (self.file == other.file)


class TestExtension(unittest.TestCase):
    
    def test_show(self):
        absolutepath = "ecchia.jpg"
        result = Extension(absolutepath).show()
        expected = "jpg"
        self.assertEqual(result, expected)
    
    def test_media_supported(self):
        absolutepath = "ecchia.jpg"
        result = Extension(absolutepath).media()
        self.assertTrue(result)
    
    def test_media_unsupported(self):
        absolutepath = "ecchia.jpg2"
        result = Extension(absolutepath).media()
        self.assertFalse(result)


    def test_equal(self):
        absolutepath_one = "ecchia.jpg"
        absolutepath_two = "ecchia.jpg"
        result_one = Extension(absolutepath_one)
        result_two = Extension(absolutepath_two)
        self.assertEqual(result_one, result_two)


