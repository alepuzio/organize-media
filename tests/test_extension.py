import pytest
from organizemedia.personal_logging import PersonalLogging

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
        '''@return True if the file has one of these extensions'''
        return  self.image() or self.video()

    def allowed_extension(self, type_file, allowed_extensions):
        '''@return True if the file has one of these extensions'''
        return  (type_file in allowed_extensions)

    def image(self):
        '''@return True if the file is an img '''
        typeFile = self.name().upper()
        allowedExtensions = ["CR2", "JPG"]
        return  self.allowed_extension ( typeFile , allowedExtensions)
    
    def video ( self):
        '''@return True if the file is a video '''
        typeFile = self.name().upper()
        allowedExtensions = ["MOV"]
        return  self.allowed_extension ( typeFile , allowedExtensions)

    def __eq__(self, other):
        return (self.ext == other.ext)


    
def test_show():
    unkown_extension = "jpg"
    result = Extension(unkown_extension).name().upper()
    expected = "JPG"
    assert result == expected
    
def test_image_supported():
    unkown_extension = "jpg"
    result = Extension(unkown_extension).image()
    assert True == result
    
def test_video_supported():
    unkown_extension = "mov"
    result = Extension(unkown_extension).video()
    assert True == result


def test_equal():
    unkown_extension_one = "jpg"
    unkown_extension_two = "jpg"
    result_one = Extension(unkown_extension_one)
    result_two = Extension(unkown_extension_two)
    assert result_one == result_two


