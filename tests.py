#tests.py
import unittest
from calculator import add, subtract, multiply, divide, power, square_root

class TestCalculator(unittest.TestCase):
    
    def test_add(self):
        """Test addition function."""
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-1, 1), 0)
        self.assertEqual(add(0, 0), 0)
    
    def test_subtract(self):
        """Test subtraction function."""
        self.assertEqual(subtract(5, 3), 2)
        self.assertEqual(subtract(0, 5), -5)
    
    def test_multiply(self):
        """Test multiplication function."""
        self.assertEqual(multiply(3, 4), 12)
        self.assertEqual(multiply(-2, 5), -10)
        
    def test_divide(self):
        """Test division function."""
        self.assertEqual(divide(10, 2), 5)
        with self.assertRaises(ValueError):
            divide(5, 0)
    
    def test_power(self):
        """Test power function."""
        self.assertEqual(power(2, 3), 8)
        self.assertEqual(power(5, 0), 1)
    
    def test_square_root(self):
        """Test square root function."""
        self.assertEqual(square_root(16), 4)
        with self.assertRaises(ValueError):
            square_root(-1)
            
if __name__ == '__main__':
    unittest.main()