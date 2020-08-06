import unittest
from PersonalLogging import PersonalLogging
from Field import Field

class CSVImage:
    '''@overview: class that format the rows of the data'''
    def __init__(self, newini, newcsv):
        self.log = PersonalLogging("CSVImage")
        self.ini = newini
        self.manualcsv = newcsv
        #self.staticsv = CSVImage()

    
    def data(self):
        '''@return list fo the row to be printed'''
        result = []
        #result.append( Field("numero_clip")
        
        
        result.append( self.manualcsv.fileName() ) 
        result.append( self.ini.copyright() )  #copyright
        #       result.append( Field( ) )#price
        # result.append( Field( self.compounedName(filename) ) #name
        #       result.append( Field( ) #city
        #      result.append( Field( ) #Region
        #     result.append( Field( ) #Country
        #     result.append( Field( self.formattedData(da ) )#created
        #    result.append( Field( Field("CANON EOS 1200D") ) #specififedsource
        #    result.append( Field(  )#keyword 
        #    result.append( Field( ) #keywordsCheckbox
        #        result.append( Field(self.manualcsv.description()  )) #description
        #       result.append( Field( Field( self.init.imagetype()  ) )#imagetype
        return ",".join(result)


    def compounedName(self):
        '''@return name as concatenation fo Description, date creation , city, country'''
        pass
        #     return "{0}, {1} - {2}: {3}".format(self.ini.city(), self.ini.country(), self.manualecsv.date(), self.manualcsv.description())

    def __str__(self):
        return "CSVImage:[{0}]".format(self.ini)


    def __repr__(self):
        return "[{0}]".format(self.data())

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
