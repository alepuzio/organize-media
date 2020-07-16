import unittest
from PersonalLogging import PersonalLogging


class ImageData:
    '''#overview: class that prepare the data to print'''

    def __init__(self, new_list_filename, new_path):
        self.list_filename = new_list_filename
        self.logging = PersonalLogging("ImageData", True)
        self.path = new_path

    def path(self):
        '''@return path where write the CSV file, no filename or extension'''
        return self.path

    def rows(self):
        '''@return list of the rows of data ofr the CSV file'''
        result = []
        for current in self.list_filename:
            
Clipid	OriginalFilename	Copyright	Price	name	City	Region	Country	Created	SpecifySource	Keywords	KeywordsCheckbox	PublicBin	Description	ImageType





class TestImageData(unittest.TestCase):

    def test_path(self):
        filename = "vecchia.jpg"
        list_filenames = []
        list_filenames.append(filename)
        path = "C:\\users\\output"
        var = ImageData(list_filenames, path)
        result = var.path()
        expected = "C:\\users\\output"
        self.assertEqual(result, expected)


    def test_rows(self)
        filename = "vecchia.jpg"
        list_filenames = []
        list_filenames.append(filename)
        path = "C:\\users\\output"
        var = ImageData(list_filenames, path)
        result = var.rows()
        expected = "a,b,c,d,e,g"
        self.assertEqual(result[0], expected[0])
