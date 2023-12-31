#!/usr/bin/env python3
"""
The module contains 
routine call t wait_n and takes two int
argument and with max_delay time
"""

import asyncio
import random
from typing import List


wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """returns list of all the delays(floats) in ASC order"""
    todos = [asyncio.create_task(wait_random(max_delay)) for _ in range(n)]
    return [await todo for todo in asyncio.as_completed(todos)]
