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
        elements = [ tmp.label()  for tmp in  self.tags]
        elements.sort()
        self.log.print("There are {0} tags".format( len(elements)  ) )  
        mean = round ( self.mean()) 
        choosen_tags = [tmp.name for tmp in self.tags if tmp.rating() > mean] #filter only element with more than mean
        number_tags = len(choosen_tags)
        #TODO keep in mind using recursion instead of the if-else cascade
        if number_tags < 10:
            raise Exception("The input tags are {0}, too few. Please add some other tags".format( number_tags ))
        else:
            correct_tags = True
        
        self.log.warn ("There are {0} tags about the keywords".format( len(choosen_tags ) ) )
        return choosen_tags

        '''
        elif number_tags > 30:
            correction = round (mean * 1.5)
            self.log.warn ("There are {0} tags over the mean {1}, too much, I'm calculating using the new mean {2}".format(number_tags, mean, correction ) )
            choosen_tags =  [tmp.name for tmp in self.tags if tmp.rating() > correction ] 
        elif number_tags < 15:
            correction = round(mean * 0.5)
            self.log.warn ("There are {0} tags over the mean {1}, too few: I'm calculating using mean {2}".format(number_tags, mean, correction ) )
            choosen_tags =  [tmp.name for tmp in self.tags if tmp.rating() > correction ] 
        elif number_tags < 7:
            median = round(self.median())
            self.log.warn ("There are {0} tags over the mean {1}, too few: I'm calculating using median {2}".format(number_tags, mean, median ) )
            choosen_tags = [tmp.name for tmp in self.tags if tmp.rating() > median] # filter element with more than median
        '''
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
