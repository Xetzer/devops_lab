import unittest
import pcheck

class TestUM(unittest.TestCase):
 
    def setUp(self):
        pass
 
    def dicttest(self):
        #self.assertEqual( multiply(3,4), 12)
        self.assertEqual(pcheck.virt_env, "venv3.5")

if __name__ == '__main__':
    unittest.main()
