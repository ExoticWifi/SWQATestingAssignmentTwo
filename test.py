import unittest

from assignmentTwo import *

"""
Testing the main menu functionality
"""
class TestSum(unittest.TestCase):
    def testBMI(self):
        data = 1
        result = menu(data)
        self.assertEqual(result, 5)


    def testRetirement(self):
        data = 2
        result = menu(data)
        self.assertEqual(result, 3)

    def testQuit(self):
        data = 3
        result = menu(data)
        self.assertEqual(result, 2)

    def testValidInput(self):
        data = 4
        result = menu(data)
        self.assertEqual(result, 1)

if __name__ == '__main__':
    unittest.main()
