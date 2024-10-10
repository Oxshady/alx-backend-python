#!/usr/bin/env python3
"""Type-annotated function sum_mixed_list which takes a list mxd_lst of"""

from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """Return the sum of all elements of mxd_lst"""
    return sum(mxd_lst)

