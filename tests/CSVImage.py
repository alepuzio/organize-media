import unittest
from PersonalLogging import PersonalLogging
#from Field import Field

class CSVImage:
    '''@overview: class that format the rows of the data'''
    def __init__(self, newini, newcsv):
        self.log = PersonalLogging("CSVImage")
        self.ini = newini
        self.manualcsv = newcsv
        self.staticcsv = CSVImageStatic()

    
    def data(self):
        '''@return list fo the row to be printed'''
        result = []
        #result.append( Field("numero_clip")
        
        
        result.append( self.manualcsv.fileName() )#filename 
        result.append( self.ini.copyright() )  #copyright
        result.append( self.ini.price() )#price
        #result.append( #self.compounedName(filename) ) #name
        result.append( self.ini.city() ) #city
        result.append( self.ini.region() ) #Region
        result.append( self.ini.country() ) #Country
        result.append( self.manualcsv.created() ) #Created
        #result.append( Field( self.formattedData(da ) )#created
        result.append( self.ini.specifysource() ) #specififedsource
        result.append( self.manualcsv.keywords() )#keyword 
        result.append( self.staticcsv.keywordsCheckbox() )#keywordsCheckbox
        result.append( self.staticcsv.publicBin() )#publicbin
        result.append( self.manualcsv.description() ) #description
        result.append( self.ini.imagetype()  )#imagetype
        return ",".join(result)

    def compounedName(self):
        '''@return name as concatenation fo Description, date creation , city, country'''
        pass
        #     return "{0}, {1} - {2}: {3}".format(self.ini.city(), self.ini.country(), self.manualecsv.date(), self.manualcsv.description())

    def __str__(self):
        return "CSVImage:[{0}]".format(self.ini)

    def __repr__(self):
        return "[{0}]".format(self.data())

class CSVImageStatic:
    '''@overview: static value of a image in row CSV
    '''
    def __init__(self):
        pass

    def keywordsCheckbox(self):
        '''@return list of static values'''
        return "keywordscheckbox-static"

    def publicBin(self):
        return "publicBin-static"


        '''
Clipid: 102140997
OriginalFilename: _MG_5231.jpg	
Copyright:	Alessandro Puzielli
Price	:5
name	:Lisbon, Portugal - 12 08 2018: convent of the Grace in the night	
City	:Lisbon
Region	:
Country	:
Created	:2018-12-08
SpecifySource	:CANON EOS 1200D
Keywords: lisbon, portugal, december, light, architecture, city, building, travel, sky, landmark, evening, urban, water, center, blue, tower, skyline, view, cityscape, church, convent, tourism, downtown, dusk, river, monastery, reflection, landscape, illuminated, tour tourism, background, park, culture, scenic, town, famous, new, religion, hotel, history	

KeywordsCheckbox	: KMI0804	
PublicBin:	
Description:	convent of the Grace in the night in Lisbon (Portugal)	
ImageType:photo
Alessandro Puzielli	5	
Lisbon	
Portugal
2018-12-08	
	

'''
class TestCSVImage(unittest.TestCase):

    def test_data(self):
        print ( "Hard work to create fake object " ) 
        pass
