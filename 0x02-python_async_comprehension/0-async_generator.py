#!/usr/bin/env python3
""" Async generators coroutine """
import asyncio
import random


async def async_generator():
    """
        async_generator - The coroutine will loop 10 times,
            each time asynchronously wait 1 second,
            then yield a random number between 0 and 10.
        Return:
            yield values
    """
    for i in range(10):
        await asyncio.sleep(1)
        yield random.triangular(0, 10)
