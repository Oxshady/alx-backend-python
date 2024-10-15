#!/usr/bin/env python3
"""Module to measure runtime"""
import asyncio
from time import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """measure time"""
    async_queue = []
    for i in range(4):
        async_queue.append(async_comprehension())
    start = time()
    await asyncio.gather(*async_queue)
    return time() - start
