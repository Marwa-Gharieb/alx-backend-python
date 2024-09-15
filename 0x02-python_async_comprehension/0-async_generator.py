#!/usr/bin/env python3
'''Async Generator'''
import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    '''Loops 10 times,waits 1 second, and yields a random number '''
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
