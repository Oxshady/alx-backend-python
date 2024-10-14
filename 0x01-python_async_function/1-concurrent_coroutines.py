#!/usr/bin/env python3
"""asynchronous coroutine"""
import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """async routine"""
    delays = [wait_random(max_delay) for i in range(n)]
    result = [await delay for delay in asyncio.as_completed(delays)]
    return result
