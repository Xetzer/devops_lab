import unittest
import pcheck

class TestUM(unittest.TestCase):
 
    def setUp(self):
        pass
 
    def test_dict(self):
        '''Check that dictionary is not empty'''
        self.assertTrue(pcheck.dictionary)

if __name__ == '__main__':
    unittest.main()
