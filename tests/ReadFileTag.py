import os
import unittest

from PersonalLogging import PersonalLogging


class ReadFileTag:
    '''@overview: it contains the properties in file of tag and number:w
    '''

    def __init__(self, new_dir):
        self.dir = new_dir
        self.log = PersonalLogging("ReadFileTag")

    def read(self):
        path =  NameDraft( self.dir).name()  #TODO concatenation of string to improve
        result = []
        exists = os.path.exists(path)
        if exists :
            with open(path, newline = '') as file_tags:
                number_row = 0;
                name = "UNOKWN_NAME"
                provvisory_tag = "UNKWON_TAGS"
                while True:
                    name = file_tags.readline()
                    provvisory_tag = file_tags.readline()
                    if not name or not provvisory_tag:
                        break
                    result.append (   Tag(name.rstrip(), provvisory_tag.rstrip()) )

        else:
            raise Exception("The file [{0}] is not present, I stop the elaboration ".format ( path ) ) 
        return result 
    

class Tag:
    '''@overview: this class contains the data of a tag'''

    def __init__(self, new_name, new_tags):
        self.name = new_name
        self.tags = new_tags
        
    def label(self):
        return self.name
   
    def rating(self):
        return float( self.tags.split( "\t" )[2] )
    
    def __str__(self):
        return "Tag-{0}-{1}".format(self.name, self.tags)
    
    def __repr__(self):
        return "Tag:{0}{1}".format(self.name, self.tags)

class TestTag(unittest.TestCase):
 
    def test_label(self):
        single = Tag("name", "12 23.4 1234 ")
        result = single.label()
        expected = "name"
        self.assertEqual(result, expected)
   
    def test_rating(self):
        single = Tag("name", "12 23.4 1234 ")
        result = single.rating()
        expected = "1234"
        self.assertEqual(result, expected)




