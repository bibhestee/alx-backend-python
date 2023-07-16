#!/usr/bin/env python3
""" A function that takes a list of floats and returns a float """
from typing import List


def sum_list(input_list: List[float]) -> float:
    """ sum_list - takes a list input_list of floats as argument
                    and returns their sum as a float.
        Arguments:
            input_list (list) - list of floats
        Return:
           sum of the floats
    """
    result = 0
    for num in input_list:
        result += num
    return result
