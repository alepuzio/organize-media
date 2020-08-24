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


class LabelVideo:
    '''@overview: list of fields of the video'''
    
    def __init__(self):
        pass

    def csv(self):
        '''@return the fields as a string. The originay fields are:
Clipid,OriginalFilename,Copyright,Price,name,City,Region,Country,
Created,ClipSource,SpecifySource,FrameRendering,AspectRatio,Keywords,
KeywordsCheckbox,PublicBin,Description        '''
        result = [
"OriginalFilename","Copyright","Price","name","City","Region","Country,""Created","ClipSource","SpecifySource","FrameRendering","AspectRatio","Keywords","KeywordsCheckbox","PublicBin","Description"       
 ]
        return ",".join ( result )

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
