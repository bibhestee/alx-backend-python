#!/usr/bin/env python3
""" Measure runtime of async concurrent coroutine """
import asyncio
from typing import List
import time
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """ measure_time - measures the total execution time for wait_n
        Arguments:
            n (int) - number of times to spawn wait random
            max_delay (int) - delayed seconds duration.
        Return:
            total time / n
    """
    start = time.time()
    asyncio.run(wait_n(n, max_delay))
    stop = time.time()
    total_time = stop - start
    return total_time/n
