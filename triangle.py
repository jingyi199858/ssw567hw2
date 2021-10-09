# -*- coding: utf-8 -*-
"""
Created on Thu Jan 14 13:44:00 2016
Updated Jan 21, 2018

The primary goal of this file is to demonstrate a simple python program to classify triangles

@author: jrr
@author: rk
"""


def classify_triangle(a_values, b_values, c_values):
    """Your correct code goes here...  Fix the faulty logic below until the code passes all of
    you test cases.
    This function returns a string with the type of triangle from three integer values
    corresponding to the lengths of the three sides of the Triangle.
    return:
        If all three sides are equal, return 'Equilateral'
        If exactly one pair of sides are equal, return 'Isoceles'
        If no pair of  sides are equal, return 'Scalene'
        If not a valid triangle, then return 'NotATriangle'
        If the sum of any two sides equals the squate of the third side, then return 'Right'
      BEWARE: there may be a bug or two in this code"""
    # require that the input values be >= 0 and <= 200
    if a_values > 200 or b_values > 200 or c_values > 200:
        return 'InvalidInput'

    # Defect Found in original script1
    if a_values <= 0 or b_values <= 0 or c_values <= 0:
        return 'InvalidInput'  # verify that all 3 inputs are integers
    # Python's "isinstance(object,type) returns True if the object is of the specified type
    if not (isinstance(a_values, int) and isinstance(b_values, int) and isinstance(c_values, int)):
        return 'InvalidInput'  # This information was not in the requirements spec but
    # is important for correctness
    # the sum of any two sides must be strictly less than the third side
    # of the specified shape is not a triangle

    # Defect Found in original scipt2
    if (a_values >= (b_values + c_values)) \
            or (b_values >= (a_values + c_values)) \
            or (c_values >= (a_values + b_values)):
        return 'NotATriangle'
    # now we know that we have a valid triangle
    # Defect 3
    if a_values == b_values and b_values == c_values and c_values == a_values:
        result = 'Equilateral'
    # Defect 4
    elif ((a_values * a_values) + (b_values * b_values)) == (c_values * c_values) \
            or ((a_values * a_values) + (c_values * c_values)) == (b_values * b_values) \
            or ((b_values * b_values) + (c_values * c_values) == (a_values * a_values)):
        result = 'Right'
    # Defect 5
    elif b_values not in (a_values, c_values):
        result = 'Scalene'
    else:
        result = 'Isoceles'
    return result
