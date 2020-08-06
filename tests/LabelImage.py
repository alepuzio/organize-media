import unittest

class LabelImage:
    '''@overview: list of fields'''
    
    def __init__(self):
        pass

    def csv(self):
        '''@return the fields as a string. The originay fields are:
        Clipid,OriginalFilename,Copyright,Price,name,City,Region,Country,Created,SpecifySource" ,"Keywords","KeywordsCheckbox","PublicBin","Description"  ,"ImageType
        '''
        result = ["OriginalFilename","Copyright" ,"Price","name" ,"City" , "Region" ,"Country", "Created" ,"SpecifySource" ,"Keywords","KeywordsCheckbox","PublicBin","Description"  ,"ImageType"  ]
        return ",".join ( result )


class TestLabelImage(unittest.TestCase):

    def test_csv(self):
        var = LabelImage()
        result = var.csv()
        expected =  "Clipid,OriginalFilename,Copyright,Price,name,City,Region,Country,Created,SpecifySource,Keywords,KeywordsCheckbox,PublicBin,Description,ImageType"
        self.assertEqual(result, expected)
