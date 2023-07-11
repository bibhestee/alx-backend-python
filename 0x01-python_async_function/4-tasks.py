#!/usr/bin/env python3
""" Multiple task wait coroutines at the same time """
from typing import List
import asyncio
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """ task_wait_n - spawn wait random n times
        Arguments:
            n (int) - number of times to spawn wait random
            max_delay (int) - delayed seconds duration.
        Return:
            list of delayed values
    """
    done, pend = await asyncio.wait([task_wait_random(max_delay)
                                    for i in range(n)])
    results = [task.result() for task in done]
    return sorted(results)
