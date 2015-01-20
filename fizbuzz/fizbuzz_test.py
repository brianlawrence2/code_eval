import unittest
from fizbuzz import fizzbuzzer, fizzbuzz

class TestFizzBuzz(unittest.TestCase):
    def test_1(self):
        self.assertEqual(fizzbuzz(2,14,14), 'FB')

class TestFizzBuzzer(unittest.TestCase):
    
    def test_1(self):
        self.assertEqual(fizzbuzzer(3,5,10), '1 2 F 4 B F 7 8 F B')
        
    def test_2(self):
        self.assertEqual(fizzbuzzer(2,7,15), '1 F 3 F 5 F B F 9 F 11 F 13 FB 15')
        
    def test_3(self):
        self.assertEqual(fizzbuzzer(1,2,10), 'F FB F FB F FB F FB F FB')
        
    def test_4(self):
        self.assertEqual(fizzbuzzer(2,1,10), 'B FB B FB B FB B FB B FB')
        
    def test_5(self):
        self.assertEqual(fizzbuzzer(1,1,10), 'FB FB FB FB FB FB FB FB FB FB')
        
    def test_6(self):
        self.assertEqual(fizzbuzzer(100,101,10), '1 2 3 4 5 6 7 8 9 10')
        
    def test_7(self):
        self.assertEqual(fizzbuzzer(2,2,10), '1 FB 3 FB 5 FB 7 FB 9 FB')
        
if __name__ == '__main__':
    unittest.main()