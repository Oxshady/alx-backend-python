#!/usr/bin/env python3
"""asynchronous coroutine"""
import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random
def task_wait_random(n: int) -> asyncio.Task:
    """return async task"""
    return asyncio.create_task(wait_random(n))
