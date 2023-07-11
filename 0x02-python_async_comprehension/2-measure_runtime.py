#!/usr/bin/env python3
""" Async comprehension parallel run runtime """
import time
import asyncio
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
        measure_runtime - measure the total runtime and return it.
        Return:
            total runtime
    """
    start = time.perf_counter()
    await asyncio.gather(async_comprehension(), async_comprehension(),
                         async_comprehension(), async_comprehension())
    stop = time.perf_counter()
    return stop - start
