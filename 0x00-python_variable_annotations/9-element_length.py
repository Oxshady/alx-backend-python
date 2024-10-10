#!/usr/bin/env python3
"""Type-annotated function element_length that takes a list lst as argument"""
from typing import List, Tuple, Sequence


def element_length(lst: List[Sequence]) -> List[Tuple[Sequence, int]]:
    return [(i, len(i)) for i in lst]
