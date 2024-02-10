import unittest
from main.py import greet

class TestGreet(unittest.TestCase):
    def test_greet(self):
        self.assertEqual(greet(), "Hello, World!")

if __name__ == "__main__":
    unittest.main()
