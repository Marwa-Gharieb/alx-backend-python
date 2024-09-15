#!/usr/bin/env python3
'''Let's execute multiple coroutines at the same time with async'''
import asyncio
from typing import List


wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> list[float]:
    ''' a function that runs another function a specific times'''
    result = []
    result = await asyncio.gather(*(wait_random(max_delay) for i in range(n)))
    return sorted(result)
