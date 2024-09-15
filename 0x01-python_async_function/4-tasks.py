#!/usr/bin/env python3
'''tasks'''
import asyncio
from typing import List


task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    ''' a function that runs another function a specific times'''
    result = []
    result = await asyncio.gather(*(task_wait_random(max_delay)
                                    for i in range(n)))
    return sorted(result)
