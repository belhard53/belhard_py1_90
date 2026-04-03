import unittest

from func_for_test import circle_area
from math import pi


class TestCirclrArea(unittest.TestCase):
    def setUp(self):
        print(123)
    
    def test_area(self):
        self.assertEqual(circle_area(3), pi*3**2)
        self.assertEqual(circle_area(1), pi*1**2)
        self.assertEqual(circle_area(0), pi*0**2)
        self.assertEqual(circle_area(1.5), pi*1.5**2)
        
    def test_value(self):
        self.assertRaises(ValueError, circle_area, -1)
        self.assertRaises(ValueError, circle_area, -5)
        
    def test_type(self):
        self.assertRaises(TypeError, circle_area, "222")
        self.assertRaises(TypeError, circle_area, True)
        self.assertRaises(TypeError, circle_area, [1,2])
        self.assertRaises(TypeError, circle_area, {1:1, 2:22})
        self.assertRaises(TypeError, circle_area, 3+1j)
        
# unittest.main()
