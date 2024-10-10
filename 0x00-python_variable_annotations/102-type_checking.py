#!/usr/bin/env python3
"""	Annotate the below function's parameters
and return values with the appropriate types"""

from typing import Tuple, List


def zoom_array(lst: Tuple, factor: int = 2) -> List:
    """Return a list that is a zoomed-in version of lst"""
    zoomed_in: List = [item for item in lst for i in range(factor)]
    return zoomed_in
