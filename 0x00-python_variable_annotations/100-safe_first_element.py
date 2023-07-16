#!/usr/bin/env python3
""" Assign the correct duck type annotations """
from typing import Sequence, Any, Union


# The types of the elements of the input are not know
def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """
        safe_first_element - list of elements
        Arguments:
            lst - sequence of any type
        Return:
            any type
    """
    if lst:
        return lst[0]
    else:
        return None
