#!/usr/bin/env python3
"""asynchronous coroutine"""
import asyncio
from random import uniform


async def wait_random(max_delay: int = 1) -> float:
    """asynchronous coroutine that takes in an integer argument"""
    delay: float = uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
