#!/usr/bin/env python3
'''Complex types - mixed list '''

from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[float, int]]) -> float:
    '''return sum of list of floats and integers'''
    result = 0
    for arg in mxd_lst:
        result += arg
    return float(result)
