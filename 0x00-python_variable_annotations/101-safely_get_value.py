#!/usr/bin/env python3
"""Type-annotated function safely_get_value
that takes a dict and a key as arguments"""
from typing import Union, Any, Mapping, TypeVar

T = TypeVar("T")


def safely_get_value(
    dct: Mapping, key: Any, default: Union[T, None] = None
) -> Union[Any, T]:
    """Return the value of key in dct if it exists,
    otherwise return default"""
    if key in dct:
        return dct[key]
    else:
        return default
