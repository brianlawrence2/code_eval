import unittest
from primepal import isprime, ispal, largest_prime_pal

class TestIsPrime(unittest.TestCase):
    def test_isprime_1(self):
        self.assertTrue(isprime(3))
        
    def test_isprime_2(self):
        self.assertTrue(isprime(409))
        
    def test_isprime_3(self):
        self.assertFalse(isprime(408))
        
class TestIsPal(unittest.TestCase):
    def test_ispal_1(self):
        self.assertTrue(ispal(101))
        
    def test_ispal_2(self):
        self.assertFalse(ispal(122))
        
class TestLargestPrimePal(unittest.TestCase):
    def test_largest_prime_pal_1(self):
        self.assertEqual(largest_prime_pal(102), 101)

    def test_largest_prime_pal_2(self):
        self.assertEqual(largest_prime_pal(1000), 929)
            
if __name__ == '__main__':
    unittest.main()