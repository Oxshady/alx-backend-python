#!/usr/bin/env python3
"""
The coroutine will collect 10 random numbers using an async comprehensing over
"""
import asyncio
from random import uniform
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator[float, None]:
    """coroutine will collect 10 random numbers using an async comprehensing"""
    for _ in range(10):
        await asyncio.sleep(1)
        yield uniform(0, 10)
