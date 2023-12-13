#!/usr/bin/env python3
"""
Module to define the async_comprehension
function and the measure_runtime coroutine.
"""

import asyncio
import time

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    Measure the total runtime by executing
    async_comprehension four times in parallel using asyncio.gather.
    """

    start = time.perf_counter()
    result = await asyncio.gather(*(async_comprehension() for _ in range(4)))
    total_time = time.perf_counter() - start
    return total_time
