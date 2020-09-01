import unittest
from PersonalLogging import PersonalLogging
from DayMonthYear import Space
from DayMonthYear import Slash



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
        result.append( self.name() ) #name
        result.append( self.ini.city() ) #city
        result.append( self.ini.region() ) #Region
        result.append( self.ini.country() ) #Country
        result.append( self.manualcsv.created() ) #Created
        result.append( self.ini.specifysource() ) #specififedsource
        result.append( self.manualcsv.keywords() )#keyword 
        result.append( self.staticcsv.keywordsCheckbox() )#keywordsCheckbox
        result.append( self.staticcsv.publicBin() )#publicbin
        result.append( self.manualcsv.description() ) #description
        result.append( self.ini.imagetype()  )#imagetype
        return ",".join(result)

    def name(self):
        '''@return name as concatenation fo Description, date creation , city, country'''
        result = "\"{0}, {1} - {2}: {3}\"".format(self.ini.city(), self.ini.country(), Space(self.manualcsv.created()).from_dash(), self.manualcsv.description())
        return result[0:79]

    def __str__(self):
        return "CSVImage:[{0}]".format(self.ini)

    def __repr__(self):
        return "[{0}]".format(self.data())

class CSVImageStatic:
    '''@overview: static value of a image in row CSV
    '''
    def __init__(self):
        pass #TODO put the value inside, as CSVVideoStatic

    def keywordsCheckbox(self):
        '''@return list of static values'''
        return "keywordscheckbox-static"

    def publicBin(self):
        return "publicBin-static"

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
