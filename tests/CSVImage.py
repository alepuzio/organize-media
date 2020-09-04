import unittest
from PersonalLogging import PersonalLogging

from DayMonthYear import DayMonthYear 
from DayMonthYear import Space
from DayMonthYear import Slash

from QuotationMark import QuotationMark

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
        created = DayMonthYear ( self.manualcsv.day(), self.manualcsv.month(), self.manualcsv.year())
        
        result.append( self.name(created) ) #name
        result.append( self.ini.city() ) #city
        result.append( self.ini.region() ) #Region
        result.append( self.ini.country() ) #Country

        result.append( Slash(created).show()  ) #Created
        
        result.append( self.ini.specifysource() ) #specififedsource
        result.append( self.manualcsv.keywords() )#keyword 
        result.append( self.staticcsv.keywordsCheckbox() )#keywordsCheckbox
        result.append( self.staticcsv.publicBin() )#publicbin

        result.append( QuotationMark(self.manualcsv.description()).string() ) #description
        
        result.append( self.ini.imagetype()  )#imagetype
        return ",".join(result)

    def name(self, created):
        '''@return name as concatenation fo Description, date creation , city, country'''
        return Name(self.ini, self.manualcsv, created).string()

    def __str__(self):
        return "CSVImage:[{0}]".format(self.ini)

    def __repr__(self):
        return "[{0}]".format(self.data())

class Name:
    '''@overview: name fo the CSV final to upload'''
    
    def __init__(self, new_ini, new_manual, new_created):
        self.city = new_ini.city()
        self.country = new_ini.country()
        self.created = new_created
        self.description = new_manual.description()

    def string(self):
        '''@return the name as concatenation of elementary data'''
        result ="{0}, {1} - {2}: {3}".format(self.city, self.country, Space(self.created).mmddyyyy(), self.description )
        return QuotationMark ( result[0:79] ).string()


class TestName(unittest.TestCase):

    def test_string(self):
       pass 

class CSVImageStatic:
    '''@overview: static value of a image in row CSV
    '''
    def __init__(self):
        pass #TODO put the value inside, as CSVVideoStatic

    def keywordsCheckbox(self):
        '''@return list of static values'''
        return " " #"keywordscheckbox-static" #TODO delete

    def publicBin(self):
        return " "# "publicBin-static" #TODO delete

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
