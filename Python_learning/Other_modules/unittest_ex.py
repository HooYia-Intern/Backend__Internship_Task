import unittest

class TestMathOperations(unittest.TestCase):
    
    def test_addition(self):
        self.assertEqual(2 + 3, 5)
        self.assertEqual(-1 + 1, 0)
    
    def test_subtraction(self):
        self.assertEqual(10 - 5, 5)
        self.assertNotEqual(2 - 2, 1)
    
    def test_multiplication(self):
        self.assertEqual(3 * 3, 9)
        self.assertTrue(5 * 0 == 0)
    
    def test_division(self):
        self.assertEqual(10 / 2, 5)
        with self.assertRaises(ZeroDivisionError):
            1 / 0

def main():
    unittest.main()

if __name__ == '__main__':
    main()
