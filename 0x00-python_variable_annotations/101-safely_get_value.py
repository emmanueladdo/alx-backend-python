#!/usr/bin/env python3
"""
This module reolve the code
"""
from typing import TypeVar, Mapping, Any, Union

T = TypeVar('T')


def safely_get_value(dct: Mapping, key: Any,
                     default: Union[T, None] = None) -> Union[Any, T]:
    """
    Safely gets the value associated with the given key from the dictionary.

    Parameters:
    - dct (Mapping): The input dictionary.
    - key (Any): The key to look up in the dictionary.
    - default (Union[T, None], optional): The default
    - value to return if the key is not found. Defaults to None.

    Returns:
    - Union[Any, T]: The value associated with the key if it exists,
    otherwise the default value.
    """
    if key in dct:
        return dct[key]
    else:
        return default
