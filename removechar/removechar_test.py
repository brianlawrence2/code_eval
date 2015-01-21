import unittest
from removechar import removechars

class TestRemoveChars(unittest.TestCase):
    def test_removechars_1(self):
        self.assertEqual(removechars('hello world, obc'), 'hell wrld')
        
if __name__ == '__main__':
    unittest.main()