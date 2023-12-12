#!/usr/bin/env python3
"""
Import async_comprehension from the previous file
write a measure_runtime coroutine that will execute
async_comprehension four times in parallel using asyncio.gather.
measure_runtime should measure the total runtime and return it.
"""

import asyncio
from typing import List

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    Coroutine that collects 10 random numbers using async comprehension over
    async_generator and returns the list of 10 random numbers.
    """
    return [result async for result in async_generator()]
