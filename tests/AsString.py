import unittest

class AsString:
    '''@overview questa classe mostra i dati come stringhe'''
    def __init__(self, newobjecttocast):
        self.objecttocast = newobjecttocast

    def show(self):
        '''return the object as a string'''
        return str(self.objecttocast)


class TestAsString(unittest.TestCase):
    
    def test_show(self):
        '''test the correct cas in string'''
        var = "onestring"
        result = AsString(var).show()
        self.assertEqual(result, "onestring")
