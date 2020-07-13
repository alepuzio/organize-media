import unittest
import os


class Topic:
    '''@overview: class that manage the topic of a file'''

    def __init__(self, newabsolutepath):
        self.absolutepath = newabsolutepath

    def show(self):
        '''print the topic of a file, meaning the last part of the subdirectory'''
        listdirectory = self.absolutepath.split(os.sep)
        listdirectory.reverse()
        result = listdirectory[0]
        return result

    def __eq__(self, other):
        return self.absolutepath == self.absolutepath

    def __repr__(self):
        return "Topic[" + self.show()  + "]"


class TestTopic(unittest.TestCase):
    
    def test_show(self):
        filetmp = Topic("c:\\aaa\\lugano")
        result = filetmp.show()
        expected = "lugano"
        self.assertEqual(result, expected)

                
    def test_eq(self):
        dir_one = "\\subdir\\topic"
        dir_two = "\\subdir\\topic"
        topic_one = Topic(dir_one)
        topic_two = Topic(dir_two)
        self.assertEqual(topic_one, topic_two)
    

