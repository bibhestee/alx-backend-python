#!/usr/bin/env python3
""" Async comprehension for coroutine """
async_generator = __import__('0-async_generator').async_generator
from typing import List


async def async_comprehension() -> List[float]:
    """
        async_comprehension - The coroutine will collect 10 random numbers
            using an async comprehensing over async_generator,
            then return the 10 random numbers.
        Return:
            yield values
    """
    return [value async for value in async_generator()]
