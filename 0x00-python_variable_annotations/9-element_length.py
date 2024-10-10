#!/usr/bin/env python3
"""Type-annotated function element_length
that takes a list lst as argument"""
from typing import List, Tuple, Sequence, Iterable


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    return [(i, len(i)) for i in lst]
