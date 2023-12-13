#!/usr/bin/env python3
"""
Module to define the async_comprehension
function and the measure_runtime coroutine.
"""

import asyncio
from typing import List


async def async_comprehension() -> List[float]:
    """
    Async function demonstrating async comprehension.
    """
    # Your implementation of async_comprehension here
    pass


async def measure_runtime() -> float:
    """
    Measure the total runtime by executing
    async_comprehension four times in parallel using asyncio.gather.
    """
    start_time = asyncio.get_event_loop().time()

    # Execute async_comprehension four times in parallel using asyncio.gather
    await asyncio.gather(
        async_comprehension(),
        async_comprehension(),
        async_comprehension(),
        async_comprehension()
    )

    end_time = asyncio.get_event_loop().time()
    total_runtime = end_time - start_time
    return total_runtime
