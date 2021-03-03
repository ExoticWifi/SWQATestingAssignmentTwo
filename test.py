import unittest

from assignmentTwo import *

"""
Testing the main menu functionality and input validation
"""
class TestMenu(unittest.TestCase):
    def testBMISelection(self):
        data = 1
        result = menu(data)
        self.assertEqual(result, 5)


    def testRetirementSelection(self):
        data = 2
        result = menu(data)
        self.assertEqual(result, 3)

    def testQuitSelection(self):
        data = 3
        result = menu(data)
        self.assertEqual(result, 2)

    def testValidInput(self):
        data = 4
        result = menu(data)
        self.assertEqual(result, 1)

"""
Testing BMI functionality and input validation
"""

class TestBMI(unittest.TestCase):
    def testValidInput(self):
        weight = 150
        heightFT = 6
        heightIN = 0
        data = (weight, heightFT, heightIN)
        result = bmi(data)
        self.assertEqual(result, 20.83)

    def testInvalidWeight(self):
        weight = "f"
        heightFT = 6
        heightIN = 0
        data = (weight, heightFT, heightIN)
        result = bmi(data)
        self.assertEqual(result, False)

    def testInvalidHeightFT(self):
        weight = 150
        heightFT = "six"
        heightIN = 0
        data = (weight, heightFT, heightIN)
        result = bmi(data)
        self.assertEqual(result, False)
    
    def testInvalidHeightFTTwo(self):
        weight = 150
        heightFT = -1
        heightIN = 0
        data = (weight, heightFT, heightIN)
        result = bmi(data)
        self.assertEqual(result, False)

    def testInvalidHeightFTThree(self):
        weight = 150
        heightFT = "6 feet"
        heightIN = 0
        data = (weight, heightFT, heightIN)
        result = bmi(data)
        self.assertEqual(result, False)

    def testInvalidHeightIN(self):
        weight = 150
        heightFT = 6
        heightIN = "zero"
        data = (weight, heightFT, heightIN)
        result = bmi(data)
        self.assertEqual(result, False)

    def testInvalidHeightINTwo(self):
        weight = 150
        heightFT = 6
        heightIN = -1
        data = (weight, heightFT, heightIN)
        result = bmi(data)
        self.assertEqual(result, False)
    
    def testInvalidHeightINThree(self):
        weight = 150
        heightFT = 6
        heightIN = 14
        data = (weight, heightFT, heightIN)
        result = bmi(data)
        self.assertEqual(result, False)

    def testInvalidHeightINFour(self):
        weight = 150
        heightFT = 6
        heightIN = "0 inches"
        data = (weight, heightFT, heightIN)
        result = bmi(data)
        self.assertEqual(result, False)
        

if __name__ == '__main__':
    unittest.main()
