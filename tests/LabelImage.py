import unittest
from Field import Field

class LabelImage:
    '''@overview: list of fields'''
    
    def __init__(self):
        pass

    def csv(self):
        '''@return the list of the fields'''
        result = []
        result.append( Field("Clipid").csv())
        result.append( Field("OriginalFilename"  ).csv())
        result.append( Field("Copyright").csv())
        result.append( Field("Price").csv())
        result.append( Field("name").csv())
        result.append( Field("City").csv())
        result.append( Field("Region").csv())
        result.append( Field("Country").csv())
        result.append( Field("Created").csv())
        result.append( Field("SpecifySource").csv())
        result.append( Field("Keywords").csv())
        result.append( Field("KeywordsCheckbox" ).csv())
        result.append( Field("PublicBin").csv())
        result.append( Field("Description"  ).csv())
        result.append( Field("ImageType" ).csv())
        return result
        '''
        '''
class TestLabelImage(unittest.TestCase):

    def test_csv(self):
        var = LabelImage()
        result = var.csv()
        expected = [
        "Clipid, ","OriginalFilename, ",     "Copyright, ",
        "Price, ","name, ", "City, ",
        "Region, ", "Country, " , "Created, ",       
        "SpecifySource, ", "Keywords, ",   "KeywordsCheckbox, ", 
        "PublicBin, ", "Description, ","ImageType, "
                ]
        self.assertEqual(result, expected)
