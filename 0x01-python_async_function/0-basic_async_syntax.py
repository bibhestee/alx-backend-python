#!/usr/bin/env python3
""" Async coroutine """

import asyncio
import random


async def wait_random(max_delay=10):
    """ Wait random - waits for a delay and eventually return it
        Arguments:
            max_delay (int): delayed seconds duration.
        Return:
            random value generated
    """
    random_value = random.uniform(0, max_delay)
    await asyncio.sleep(random_value)
    return random_value
