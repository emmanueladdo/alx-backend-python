#!/usr/bin/env python3
"""
The module contains regular function with integers n and max_delay as
arguments that measures the total execution time for wait_n(n, max_delay),
returns total_time / n. The function should return a float.
time module is used to measure approximate elapsed time.
"""

import asyncio
import random
import time
from typing import List


wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int = 10) -> float:
    """
    takes n and max_delay as input to measure execution time are returns
    total_time / n
    """
    start = time.perf_counter()
    asyncio.run(wait_n(n, max_delay))
    elapsed = time.perf_counter() - start
    return elapsed / n
