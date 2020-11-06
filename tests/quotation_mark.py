import unittest

class QuotationMark:

    def __init__(self, new_string):
        self.value =new_string
        self.sep = "\""

    def string(self):
        return '{0}{1}{2}'.format(self.sep, self.value, self.sep)


class TestQuotationMark(unittest.TestCase):

    def test_string(self):
        value = "value"
        result = QuotationMark (value).string()
        expected = "\"value\""
        self.assertEqual(result, expected)

