#!/usr/bin/env python3
""" A function that takes a list of floats and ints and returns a float """
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[float, int]]) -> float:
    """ sum_mixed_list - takes a list mxd_lst of integers and
                        floats and returns their sum as a float.
        Arguments:
            mxd_lst (list) - list of floats and ints
        Return:
           sum of the floats and ints
    """
    result = 0
    for num in mxd_lst:
        result += num
    return result
