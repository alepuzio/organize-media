import unittest


class Field:
    '''@overview: class abotu a single field'''
    
    def __init__(self, new_value):
        self.value = new_value

    def csv(self):
        '''@return the field offo the CSV'''
        return "%s, " %(self.value)

    def __str__(self):
        return "Field({0})".format(self.value)
    
    def __repr__(self):
        return "Field( {0} ) -> [ {1} ]".format(self.value, self.csv() )

class TestField (unittest.TestCase):

    def test_show(self):
        value = "Created"
        var = Field(value)
        result = var.csv()
        expected = "Created, "
        self.assertEqual(result, expected)


