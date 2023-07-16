#!/usr/bin/env python3
""" Type annotation requiring TypeVar """
from typing import Mapping, Any, Union, TypeVar
T = TypeVar('T')
Default = Union[T, None]
Ret = Union[Any, T]


def safely_get_value(dct: Mapping, key: Any, default: Default = None) -> Ret:
    """
        safely_get_value - Type var annotation
        Arguments:
            dct - Mapping type
            key - Any type
            default - TypeVar or None
        Return:
            Any type or TypeVar
    """
    if key in dct:
        return dct[key]
    else:
        return default
