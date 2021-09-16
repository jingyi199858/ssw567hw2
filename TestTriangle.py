# -*- coding: utf-8 -*-
"""
Updated Jan 21, 2018
The primary goal of this file is to demonstrate a simple unittest implementation

@author: jrr
@author: rk
"""

import unittest

from Triangle import classifyTriangle


# This code implements the unit test functionality
# https://docs.python.org/3/library/unittest.html has a nice description of the framework

class TestTriangles(unittest.TestCase):
    result = []

    # define multiple sets of tests as functions with names that begin

    def testTriangle1(self):
        self.result.append((1, (3, 4, 5), 'Right', classifyTriangle(3, 4, 5)))
        print(len(self.result), self.result)
        self.assertEqual(classifyTriangle(3, 4, 5), 'Right', '3,4,5 is a Right triangle')

    def testTriangle2(self):
        self.result.append((2, (5, 3, 4), 'Right', classifyTriangle(5, 3, 4)))
        print(len(self.result), self.result)
        self.assertEqual(classifyTriangle(5, 3, 4), 'Right', '5,3,4 is a Right triangle')

    def testTriangle3(self):
        self.result.append((3, (5, 4, 3), 'Right', classifyTriangle(5, 4, 3)))
        print(len(self.result), self.result)
        self.assertEqual(classifyTriangle(5, 4, 3), 'Right', '5,4,3 is a Right triangle')

    def testTriangle4(self):
        self.result.append((4, (5, 12, 13), 'Right', classifyTriangle(5, 12, 13)))
        print(len(self.result), self.result)
        self.assertEqual(classifyTriangle(5, 12, 13), 'Right', '5,12,13 is a Right triangle')

    def testTriangle5(self):
        self.result.append((5, (8, 15, 17), 'Right', classifyTriangle(8, 15, 17)))
        print(len(self.result), self.result)
        self.assertEqual(classifyTriangle(8, 15, 17), 'Right', '8,15,17 is a Right triangle')

    def testTriangle6(self):
        self.result.append((6, (1, 1, 1), 'Equilateral', classifyTriangle(1, 1, 1)))
        print(len(self.result), self.result)
        self.assertEqual(classifyTriangle(1, 1, 1), 'Equilateral', '1,1,1 should be equilateral')

    def testTriangle7(self):
        self.result.append((7, (199, 199, 199), 'Equilateral', classifyTriangle(199, 199, 199)))
        print(len(self.result), self.result)
        self.assertEqual(classifyTriangle(199, 199, 199), 'Equilateral', '199,199,199 should be equilateral')

    def testTriangle8(self):
        self.result.append((8, (10, 10, 10), 'Equilateral', classifyTriangle(10, 10, 10)))
        print(len(self.result), self.result)
        self.assertEqual(classifyTriangle(10, 10, 10), 'Equilateral', '10,10,10 should be equilateral')

    def testTriangle9(self):
        self.result.append((9, (7, 9, 5), 'Scalene', classifyTriangle(7, 9, 5)))
        print(len(self.result), self.result)
        self.assertEqual(classifyTriangle(7, 9, 5), 'Scalene', '7,9,5 is Scalene')

    def testTriangle10(self):
        self.result.append((10, (0, 9, 5), 'InvalidInput', classifyTriangle(0, 9, 5)))
        print(len(self.result), self.result)
        self.assertEqual(classifyTriangle(0, 9, 5), 'InvalidInput', '0,9,5 is not triangle')

    def testTriangle11(self):
        self.result.append((11, (1, 9, 5), 'NotATriangle', classifyTriangle(1, 9, 5)))
        print(len(self.result), self.result)
        self.assertEqual(classifyTriangle(1, 9, 5), 'NotATriangle', '1,9,5 is not triangle')

    def testTriangle12(self):
        self.result.append((12, (7, 9, 9), 'Isoceles', classifyTriangle(7, 9, 9)))
        print(len(self.result), self.result)
        self.assertEqual(classifyTriangle(7, 9, 9), 'Isoceles', '7,9,9 is Isoceles')

    def testTriangle13(self):
        self.result.append((13, (7, 1, 1), 'NotATriangle', classifyTriangle(7, 1, 1)))
        print(len(self.result), self.result)
        self.assertEqual(classifyTriangle(7, 1, 1), 'NotATriangle', '7,1,1 is not a triangle')

    def testTriangle14(self):
        self.result.append((14, (0, 0, 0), 'InvalidInput', classifyTriangle(0, 0, 0)))
        print(len(self.result), self.result)
        self.assertEqual(classifyTriangle(0, 0, 0), 'InvalidInput', '0,0,0 is not a triangle')

    def testTriangle15(self):
        self.result.append((15, (1, 1, 0), 'InvalidInput', classifyTriangle(1, 1, 0)))
        print(len(self.result), self.result)
        self.assertEqual(classifyTriangle(1, 1, 0), 'InvalidInput', '1,1,0 is not a triangle')

    def testTriangle16(self):
        self.result.append((16, (1, 0, 0), 'InvalidInput', classifyTriangle(1, 0, 0)))
        print(len(self.result), self.result)
        self.assertEqual(classifyTriangle(1, 0, 0), 'InvalidInput', '1,0,0 is not a triangle')

    def testTriangle17(self):
        self.result.append((17, (1, 2, 16), 'NotATriangle', classifyTriangle(1, 2, 16)))
        print(len(self.result), self.result)
        self.assertEqual(classifyTriangle(1, 2, 16), 'NotATriangle', '1,2,16 is not a triangle')

    def testTriangle18(self):
        self.result.append((18, (201, 201, 201), 'InvalidInput', classifyTriangle(201, 201, 201)))
        print(len(self.result), self.result)
        self.assertEqual(classifyTriangle(201, 201, 201), 'InvalidInput', '201,201,201 out of bound')

    def testTriangle19(self):
        self.result.append((19, (199, 199, 201), 'InvalidInput', classifyTriangle(199, 199, 201)))
        print(len(self.result), self.result)
        self.assertEqual(classifyTriangle(199, 199, 201), 'InvalidInput', '199,199,201 out of bound')

    def testTriangle20(self):
        self.result.append((20, (4.5, 6.7, 8.7), 'InvalidInput', classifyTriangle(4.5, 6.7, 8.7)))
        print(len(self.result), self.result)
        self.assertEqual(classifyTriangle(4.5, 6.7, 8.7), 'InvalidInput', 'must be int')

    def testTriangle21(self):
        self.result.append((21, (-1, -4.5, -10), 'InvalidInput', classifyTriangle(-1, -4.5, -10)))
        print(len(self.result), self.result)
        self.assertEqual(classifyTriangle(-1, -4.5, -10), 'InvalidInput', 'must be positive')

    def testTriangle22(self):
        self.result.append((22, (-4, -5, -6), 'InvalidInput', classifyTriangle(-4, -5, -6)))
        print(len(self.result), self.result)
        self.assertEqual(classifyTriangle(-4, -5, -6), 'InvalidInput', 'must be positive')

    def testTriangle23(self):
        self.result.append((23, (16, 1, 2), 'NotATriangle', classifyTriangle(16, 1, 2)))
        print(len(self.result), self.result)
        self.assertEqual(classifyTriangle(16, 1, 2), 'NotATriangle', '16,1,2 is not a triangle')

    def testTriangle24(self):
        self.result.append((24, (1, 16, 2), 'NotATriangle', classifyTriangle(1, 16, 2)))
        print(len(self.result), self.result)
        self.assertEqual(classifyTriangle(1, 16, 2), 'NotATriangle', '1,16,2 is not a triangle')


if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()
