#!/usr/bin/env python3
'''Let's duck type an iterable object'''


from typing import Iterable, Sequence, Tuple, List


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    '''iterable function returns the number of iteration and list len'''
    return [(i, len(i)) for i in lst]
