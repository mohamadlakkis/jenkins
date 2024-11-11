import unittest
from app import greet 
def test_greet(self):
    self.assertEqual(greet("World"), "Hello, World from FirstName LastName!")


if __name__ == "__main__":
    unittest.main()
    