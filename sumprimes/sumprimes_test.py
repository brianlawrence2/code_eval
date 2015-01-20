import unittest
from sumprimes import isprime, sumprimes

class TestIsPrime(unittest.TestCase):
    def test_isprime_1(self):
        self.assertTrue(isprime(3))
        
    def test_isprime_2(self):
        self.assertTrue(isprime(409))
        
    def test_isprime_3(self):
        self.assertFalse(isprime(408))
        
    def test_isprime_4(self):
        self.assertFalse(isprime(1))
        
class TestSumPrimes(unittest.TestCase):
    def test_sumprimes_1(self):
        self.assertEqual(sumprimes(3), 10)
        
    #def test_sumprimes_2(self):
    #    self.assertEqual(sumprimes(1000), 3682913)

if __name__ == '__main__':
    unittest.main()