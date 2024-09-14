#!/usr/bin/env python3
'''More involved type annotations '''


from typing import Mapping, Any, Union, TypeVar, Optional, Iterable, Sequence
T = TypeVar('T')


def safely_get_value(dct: Mapping, key: Any,
                     default: Union[T, None] = None) -> Union[Any, T]:
    '''it is a function to find values of keys of some set'''
    if key in dct:
        return dct[key]
    else:
        return default
