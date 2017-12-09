import unittest
import pcheck

class TestUM(unittest.TestCase):
 
    def setUp(self):
        pass
 
    def test_dict(self):
        #checks that dict is not empty
        self.assertTrue(pcheck.ddic)

if __name__ == '__main__':
    unittest.main()
