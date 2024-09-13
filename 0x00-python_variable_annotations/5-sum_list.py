#!/usr/bin/env python3
'''Complex types - list of floats '''

from typing import List


def sum_list(input_list: List[float]) -> float:
    result = 0
    for arg in input_list:
        result += arg
    return result
