#!/usr/bin/env python3
""" Multiple coroutines at the same time with async """

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> list[float]:
    """ Wait n - spawn wait random n times
        Arguments:
            n (int) - number of times to spawn wait random
            max_delay (int) - delayed seconds duration.
        Return:
            list of delayed values
    """
    delays = []
    for i in range(n+1):
        delays.append(await wait_random(max_delay))
    delays.sort()
    return delays
