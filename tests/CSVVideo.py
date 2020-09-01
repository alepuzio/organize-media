import unittest
from PersonalLogging import PersonalLogging
from DayMonthYear import Space
from DayMonthYear import Slash



class CSVVideo:
    '''@overview: class that format the rows of the data of a video'''
    def __init__(self, newini, newcsv):
        self.log = PersonalLogging("CSVVideo")
        self.ini = newini
        self.manualcsv = newcsv
        self.staticcsv = CSVVideoStatic()

    
    def data(self):
        '''@return list fo the row to be printed
        "OriginalFilename","Copyright","Price","name","City","Region","Country,""Created","ClipSource","SpecifySource","FrameRendering","AspectRatio","Keywords","KeywordsCheckbox","PublicBin","Description"       
        '''
        result = []
        result.append( self.manualcsv.fileName() )#originalfilename 
        result.append( self.ini.copyright() )  #copyright
        result.append( self.ini.price() )#price
        result.append( self.name() ) #name
        result.append( self.ini.city() ) #city
        result.append( self.ini.region() ) #Region
        result.append( self.ini.country() ) #Country
        result.append( self.manualcsv.created() ) #Created
        result.append( self.staticcsv.clipsource() )  #clipsoucre
        result.append( self.ini.specifysource() ) #specififedsource
        result.append( self.staticcsv.framerendering() )        #framerendering
        result.append( self.staticcsv.aspectratio() )        #aspectratio
        result.append( self.manualcsv.keywords() )#keyword 
        result.append( self.staticcsv.keywordsCheckbox() )#keywordsCheckbox
        result.append( self.staticcsv.publicBin() )#publicbin
        result.append( self.manualcsv.description() ) #description
        result.append( self.ini.imagetype()  )#imagetype
        return ",".join(result)

    def name(self):#TODO create class
        '''@return name as concatenation fo Description, date creation , city, country'''
        result = "\"{0}, {1} - {2}: {3}\"".format(self.ini.city(), self.ini.country(), Space(self.manualcsv.created()).from_dash(), self.manualcsv.description())
        return result[0:79]

    def __str__(self):
        return "CSVVideo:[{0}]".format(self.ini)

    def __repr__(self):
        return "[{0}]".format(self.data())

class CSVVideoStatic:
    '''@overview: static value of a video in row CSV
    '''
    def __init__(self):
        self.values = {"keywordsCheckbox": "keywordscheckbox-static", 
                "publicBin":  "publicBin-static", 
                "clipSource":"other", 
                "frameRendering":"unkwon",
                "aspectRatio":"a16:9 native" }

    def keywordsCheckbox(self):
        '''@return list of static values'''
        return self.values["keywordsCheckbox"]

    def publicBin(self):
        return self.values["publicBin"]

    def clipsource(self):
        return self.values["clipSource"]

    def framerendering(self):
        return self.values["frameRendering"]

    def aspectratio(self):
        return self.values["aspectRatio"]




class TestCSVImage(unittest.TestCase):

    def test_data(self):
        print ( "Hard work to create fake object " ) 
        pass

    def test_substring_slice(self):
        more_than_80_char =  "111234567890 1234567890 234567890 1234567890 1234567890 1234567890 1234567890 1234567890 1234567890 123456789012345678901234567890234567890 "
        res = more_than_80_char[0:79] 
        print("res_more_than_80_char(" + str(len(more_than_80_char)) + "):" + res)
        self.assertTrue( res )
        less_than_80_char =  "11234567890" 
        res = less_than_80_char[0:79] 
        print("res_less_than_80_char(" + str(len (less_than_80_char)) + ") :" + res)
        self.assertTrue( res )
