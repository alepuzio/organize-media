import unittest
import os
from Extension import Extension

class Position:
    '''@overview: class thant manage the physical data of the file abotu the path'''

    def __init__(self, newabsolutepath, newfilename):
        self.absolutepath = newabsolutepath
        self.filename = newfilename

    def root(self):
        '''@return the expected path of the topic'''    
        path = self.absolutepath.split(os.sep)
        index_second_to_last = len(path) -1
        return os.sep.join(path[ 0 : index_second_to_last ] )

    def name(self):
        '''@return the name of the file, wit no extension'''
        name = self.filename.split(".")
        return  name[0]

    def extension(self):
        '''@return the extension of the file'''
        pieces = self.filename.split(".")
        if ( 0 == len (pieces) ) :
            self.log.warn( "No extension:" + str(pieces) )
            file_extension = "UNSUPPORTED-EXTENSION"
        else:
            file_extension = pieces[1]
        return  Extension ( file_extension )

    def topic(self):
        '''@return the topic of a file, meaning the last part of the subdirectory'''
        listdirectory = self.absolutepath.split(os.sep)
        listdirectory.reverse()
        return listdirectory[0]

    def __eq__(self, other):
        return self.absolutepath == other.absolutepath

    def __repr__(self):
        return "Position[{0}][{1}][{2}][{3}]".format(self.root(), self.topic(), self.name(), self.extension() )

    def __str__(self):
        return "Position[{0}][{1}]".format(self.absolutepath, self.filename) 

class TestRoot(unittest.TestCase):

    def test_root(self):
        path = "c:\\path\\absolute\\with\\no\\topic"
        name = "vecchia.jpg"
        result = Position(path, name).root()
        expected = "c:\\path\\absolute\\with\\no"
        self.assertEqual(result, expected)

    def test_filename(self):
        path = "c:\\path\\absolute\\with\\no\\topic"
        name = "vecchia.jpg"
        r = Position(path, name)
        result = r.name()
        expected = "vecchia"
        self.assertEqual(result , expected)

    def test_extension(self):
        path = "c:\\path\\absolute\\with\\no\\topic"
        name = "vecchia.jpg"
        result = Position(path, name).extension()
        expected = Extension("jpg")
        self.assertEqual(result , expected)
   
    def test_topic(self):
        path = "c:\\path\\absolute\\with\\topic\\lugano"
        name = "vecchia.jpg"
        result = Position(path, name).topic()
        expected = "lugano"
        self.assertEqual(result, expected)


    def test_str(self):
        path = "c:\\path\\absolute\\with\\topic\\lugano"
        name = "vecchia.jpg"
        result = Position(path, name)
        expected = "Position"
        self.assertEqual(str(result), expected)




