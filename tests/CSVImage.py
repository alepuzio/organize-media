import unittest

class CSVImage:
	'''@overview: class that format the rows of the data'''

    def __init__(self, new_list_rows):
        self.list_rows = list_rows
    
    def format(self):
        '''@return list fo the row to be printed'''
        result = []
        result.append("numero_clip")
        result.append(filename)
        result.append( "Alessandro Puzielli") #copyright
        result.append(Field("5" ) #price
        result.append(Field(self.compounedName(filename) ) #name
        result.append( ) #city
        result.append( ) #Region
        result.append( ) #Country
        result.append( self.formattedData(da ) )#created
        result.append( Field("CANON EOS 1200D") ) #specififedsource
        result.append(  )#keyword 
        result.append( ) #keywordsCheckbox
        result.append( ) #description
        result.append(Field("photo" ) )#imagetype
        return result

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

    def test_format(self)
        list_files = []
	list_files.append("filename.extension")
	var = CSVImage(list_files)
        result = var.format()
        expected = []
        expected.append("c,ghu, hod")
        self.assertEqual(len(result), len(expected))

