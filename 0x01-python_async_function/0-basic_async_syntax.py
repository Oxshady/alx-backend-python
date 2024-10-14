#!/usr/bin/env python3
"""asynchronous coroutine"""
import asyncio
from random import uniform


async def wait_random(max_delay=10):
    """asynchronous coroutine that takes in an integer argument"""
    return uniform(0, max_delay)
