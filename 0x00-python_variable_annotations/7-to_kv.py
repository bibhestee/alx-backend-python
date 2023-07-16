#!/usr/bin/env python3
""" A function that takes two args and returns a tuple """
from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """ to_kv - takes a string k and an int OR float v as arguments
            and returns a tuple.
            The first element of the tuple is the string k.
            The second element is the square of the int/float v and
            is annotate as a float.
        Arguments:
            k (str) - first argument
            v (int/float) - second argument
        Return:
           a tuple
    """
    return (k, v)
