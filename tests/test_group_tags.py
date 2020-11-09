#import os
import pytest

from organizemedia.personal_logging import PersonalLogging
from .test_read_file_tag import Tag

class GroupTags:
    '''@overview: it contains the tags with every rating
    '''

    def __init__(self, new_list):
        self.tags = new_list
        self.log = PersonalLogging("GroupTags")

    def mean(self):
        '''@return  the rating mean of the list of tags'''
        return sum ( tmp.rating() for tmp in self.tags)/len(self.tags) 

    def median (self):
        '''@return  the rating median of the list of tags
            from https://www.geeksforgeeks.org/finding-mean-median-mode-in-python-without-libraries/
        '''
        n_num = [ tmp.rating() for tmp in  self.tags]
        n_num.sort() 
        number_element = len(n_num)
        if number_element % 2 == 0: 
            median1 = n_num[number_element//2] 
            median2 = n_num[number_element//2 - 1] 
            median = (median1 + median2)/2
        else: 
            median = n_num[number_element//2] 
        return median 


    def calculate(self):
        '''@return list of good tags to sell'''
        elements = [ tmp.label()  for tmp in  self.tags]
        elements.sort()
        self.log.print("At beginning, there are {0} tags".format( len(elements)  ) )  
        mean = round ( self.mean()) 
        choosen_tags = [tmp.name for tmp in self.tags if tmp.rating() > mean] #filter only element with higher rating than mean
        return CorrectTags(choosen_tags).control()

class CorrectTags:
    
    def __init__(self, new_list_tags):
        self.tags = new_list_tags

    def control(self):
        number_tags = len(self.tags)
        str_tags = str ( self.tags)
        if number_tags < 10:#TODO correct magic number
            raise Exception ("The input tags are {0}, too few. Please add some other tags".format( number_tags ).upper())
        if ":" in str_tags:
            raise Exception("There' a comma in tags are {0}, please remove it".format( str_tags) ) 
        else:
            self.log.warn ("There are {0} tags about the keywords".format( number_tags ) ) 
        return self.tags
        


class FailFirst:

    def __init__(self, new_origin):
        self.origin = new_origin

    def mean(self):
        return self.origin.mean()
    
    def median (self):
        return self.origin.median()

    def calculate(self):
        number_tags = len(self.origin.tags)
        if (0 == number_tags):
            raise Exception ("No Tags in mean, please write the file")
        else:
            return self.origin.calculate()
 


def test_calculate_by_mean_ok ():
    tags = []
    for i in range(20):
        values =  str(i) + " " + str(i+1) + " " + str(i+3)
        tags.append( Tag("{0}".format(i), values ) )  
    var = GroupTags(tags) 
    result = var.calculate()
    expected = ['10', '11', '12', '13', '14', '15', '16', '17', '18', '19'] 
    assert result == expected

def test_calculate_by_median_ok ():
    tags = []
    for i in range(5):
        values =  str(i) + " " + str(i+1) + " " + str(i+3)
        tags.append( Tag("{0}".format(i), values ) )  
    var = GroupTags(tags) 
    result = var.calculate()
    expected = ['3', '4']
    assert result == expected
