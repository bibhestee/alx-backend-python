#!/usr/bin/env python3
""" Correct typed annotation """
from typing import Iterable, Sequence, Tuple, List


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """ element_length - calculate the length of the list.
        Arguments:
            lst - list
        Return:
            length of the lists
    """
    return [(i, len(i)) for i in lst]
