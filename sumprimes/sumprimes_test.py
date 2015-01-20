import unittest
from sumprimes import isprime

class TestIsPrime(unittest.TestCase):
    def test_isprime_1(self):
        self.assertTrue(isprime(3))
        
    def test_isprime_2(self):
        self.assertTrue(isprime(409))
        
    def test_isprime_3(self):
        self.assertFalse(isprime(408))

if __name__ == '__main__':
    unittest.main()