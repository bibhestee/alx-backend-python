#!/usr/bin/env python3
""" A function that takes ta float multiplier """
from typing import Callable


def multiply(a: float) -> float:
    return a * a


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """ make_multiplier - takes a float multiplier as argument and
                returns a function that multiplies a float by multiplier.
        Arguments:
            multiplier - float
        Return:
           a callable that multiplies a float by multiplier
    """
    return multiply
