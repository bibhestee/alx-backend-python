#!/usr/bin/env python3
""" Multiple coroutines at the same time with async """
from typing import List
import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """ Wait n - spawn wait random n times
        Arguments:
            n (int) - number of times to spawn wait random
            max_delay (int) - delayed seconds duration.
        Return:
            list of delayed values
    """
    done, pending = await asyncio.wait([wait_random(max_delay) for i in range(n)])
    results = [task.result() for task in done]
    return sorted(results)
