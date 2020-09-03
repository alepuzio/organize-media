import os
import unittest

from PersonalLogging import PersonalLogging

from ReadFileTag import Tag
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
        mean = self.mean()
        choosen_tags = [tmp.name for tmp in self.tags if tmp.rating() > mean] #filter only element with more than mean
        if len(choosen_tags) < 10:
            print("median")
            median = self.median()
            choosen_tags = [tmp.name for tmp in self.tags if tmp.rating() > median] # filter element with more than median
        return choosen_tags

class TestGroupTags(unittest.TestCase):

    def test_calculate_by_mean(self):
        tags = []
        for i in range(20):
            values =  str(i) + " " + str(i+1) + " " + str(i+3)
            tags.append( Tag("{0}".format(i), values ) )  
        var = GroupTags(tags) 
        result = var.calculate()
        expected = ['10', '11', '12', '13', '14', '15', '16', '17', '18', '19'] 
        self.assertEqual(result, expected)

    def test_calculate_by_median(self):
        tags = []
        for i in range(5):
            values =  str(i) + " " + str(i+1) + " " + str(i+3)
            tags.append( Tag("{0}".format(i), values ) )  
        var = GroupTags(tags) 
        result = var.calculate()
        expected = ['3', '4']
        self.assertEqual(result, expected)
