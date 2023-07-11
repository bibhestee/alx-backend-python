#!/usr/bin/env python3
""" Asyncio Task """
import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task :
    """
        task_wait_random - create an asyncio task and return it

        Arguments:
            max_delay (int) - delayed seconds duration.
        Return:
            asyncio.Task
    """
    return asyncio.Task(wait_random(max_delay))
