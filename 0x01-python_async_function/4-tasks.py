#!/inusr/bin/env python3
"""
async routine
"""
import asyncio
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """async routine"""
    delays = [task_wait_random(max_delay) for i in range(n)]
    result = [await delay for delay in asyncio.as_completed(delays)]
    return result
