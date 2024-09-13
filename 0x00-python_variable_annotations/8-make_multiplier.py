#!/usr/bin/env python3
''' Complex types - functions '''


from typing import Callable

def make_multiplier(multiplier: float) -> Callable[[float], float]:
    '''returns a function that multiplies a float by multiplier'''
    def func(cha: float) -> float:
        '''another function'''
        return cha*multiplier
    return func