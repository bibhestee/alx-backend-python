#!/usr/bin/env python3
""" Use mypy module to check annotation """
from typing import Tuple, List


def zoom_array(lst: Tuple, factor: int = 2) -> List:
    """
        zoom_array - zoom array
        Arguments:
            lst - tuple
            factor - int
        Return:
            list
    """
    zoomed_in = [
        item for item in lst
        for i in range(factor)
    ]
    return zoomed_in


array = (12, 72, 91)

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, 3)
