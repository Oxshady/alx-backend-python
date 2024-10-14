#!/usr/bin/env python3
"""
This time, measure the total runtime of
wait_n(n, max_delay), and display the runtime.
"""
import asyncio
from time import time
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    start_time = time()
    asyncio.run(wait_n(n, max_delay))
    end_time = time()
    return end_time - start_time
