import unittest

class LabelImage:
    '''@overview: list of fields'''
    
    def __init__(self):
        self.columns = ["OriginalFilename","Copyright" ,"Price","name" ,"City" , "Region" ,"Country", "Created" ,"SpecifySource" ,"Keywords","KeywordsCheckbox","PublicBin","Description"  ,"ImageType"  ]
        
    def csv(self):
        '''@return the fields as a string. 
        '''
        return ",".join ( self.columns )


class LabelVideo:
    '''@overview: list of fields of the video'''
    
    def __init__(self):
        self.columns = [
                "OriginalFilename","Copyright","Price","name","City","Region","Country","Created","ClipSource","SpecifySource","FrameRendering","AspectRatio","Keywords","KeywordsCheckbox","PublicBin","Description"       
 ]

    def csv(self):
        '''@return the fields as a string.
        '''
        return ",".join ( self.columns )

class TestLabel(unittest.TestCase):

    def test_images(self):
        var = LabelImage()
        result = var.csv()
        expected =  "Clipid,OriginalFilename,Copyright,Price,name,City,Region,Country,Created,SpecifySource,Keywords,KeywordsCheckbox,PublicBin,Description,ImageType"
        self.assertEqual(result, expected)
    
    def test_video(self):
        var = LabelVideo()
        result = var.csv()
        expected =  "OriginalFilename,Copyright,Price,name,City,Region,Country,Created,SpecifySource,Keywords,KeywordsCheckbox,PublicBin,Description,ImageType"
        self.assertEqual(result, expected)
