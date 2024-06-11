#!/usr/bin/env python3
"""
This module contains a function to measure the runtime of
executing async_comprehension four times in parallel.
"""

import asyncio
import time
from .1_async_comprehension import async_comprehension

async def measure_runtime() -> float:
    """
    Measures the runtime of running async_comprehension four times in parallel.

    Returns:
        float: The total runtime for executing the comprehensions in seconds.
    """
    start_time = time.perf_counter()
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    end_time = time.perf_counter()
    return end_time - start_time
