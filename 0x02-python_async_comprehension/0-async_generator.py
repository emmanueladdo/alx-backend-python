#!/usr/bin/env python3
"""
The module is a coroutine called async_generator
that takes no arguments
"""

import asyncio
import random


async def async_generator():
    """
    Asynchronous generator that yields random numbers
    between 0 and 10.
    """
    for i in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
