import pytest

class LabelImage:
    """
    @overview: list of fields
    """
    
    def __init__(self):
        self.columns = ["OriginalFilename","Copyright" ,"Price","name" ,"City" , "Region" ,"Country", "Created" ,"SpecifySource" ,"Keywords","KeywordsCheckbox","PublicBin","Description"  ,"ImageType"  ]
        
    def csv(self):
        """
        @return the fields as a string. 
        """
        return ",".join ( self.columns )


class LabelVideo:
    """
    @overview: list of fields of the video
    """
    
    def __init__(self):
        self.columns = [
                "OriginalFilename","Copyright","Price","name","City","Region","Country","Created","ClipSource","SpecifySource","FrameRendering","AspectRatio","Keywords","KeywordsCheckbox","PublicBin","Description"       
 ]

    def csv(self):
        """
        @return the fields as a string.
        """
        return ",".join ( self.columns )


def testImagesOK ( ) :
    var = LabelImage()
    result = var.csv()
    expected = "OriginalFilename,Copyright,Price,name,City,Region,Country,Created,SpecifySource,Keywords,KeywordsCheckbox,PublicBin,Description,ImageType"  
    assert result == expected
    
def testVideoOK ( ) :
    var = LabelVideo()
    result = var.csv()
    expected = "OriginalFilename,Copyright,Price,name,City,Region,Country,Created,ClipSource,SpecifySource,FrameRendering,AspectRatio,Keywords,KeywordsCheckbox,PublicBin,Description" 
    assert result == expected
