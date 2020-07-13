import unittest

class Filename:
    '''@overview: class that manage the filename with no extension'''

    def __init__(self, newfile):
        self.file = newfile


    def show(self):
        '''@return the name of the file, wit no extension'''
        listfilename = self.file.split(".")
        return  listfilename[0]
    
    def __eq__(self, other):
        return self.file == other.file

    def __repr__(self):
        return "Filename[" + self.show() + "]"

class TestFilename(unittest.TestCase):


    def test_show(self):
        filename = Filename("vecchia.jpg")
        result = filename.show()
        expected = "vecchia"
        self.assertEqual(result , expected)

                
    def t_eq(self):
        filename_one = Filename("vecchia.jpg")
        filename_two = Filename("vecchia.jpg")
        self.assertEqual(filename_one, filename_two)
    

