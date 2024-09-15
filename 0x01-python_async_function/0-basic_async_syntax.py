#!/usr/bin/env python3
'''The basics of async '''
import random
import asyncio


async def wait_random(max_delay: int = 10) -> float:
    '''function picks a random float'''
    await asyncio.sleep(1)
    max_delay = random.uniform(0.0, 10.0)
    return max_delay
