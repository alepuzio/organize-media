import unittest
from Field import Field

class LabelImage:
    '''@overview: list of fields'''
    
    def __init__(self):
        pass

    def csv_old(self):
        '''@return the list of the fields'''
        result = []
#        # result.append( Field("Clipid" )
#        # result.append( Field("OriginalFilename"   )
 #       # result.append( Field("Copyright" )
        # result.append( Field("Price" )
        # result.append( Field("name" )
        # result.append( Field("City" )
        # result.append( Field("Region" )
        # result.append( Field("Country" )
        # result.append( Field("Created" )
        # result.append( Field("SpecifySource" )
        # result.append( Field("Keywords" )
        # result.append( Field("KeywordsCheckbox"  )
        # result.append( Field("PublicBin" )
        # result.append( Field("Description"   )
        # result.append( Field("ImageType"  )
        return result

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
