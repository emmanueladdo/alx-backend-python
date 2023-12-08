#!/usr/bin/env python3
"""
The module contains a type-annotated function to_kv that takes a string k and
 an int OR float v as arguments and returns a tuple. The first element of the
 tuple is the string k. The second element is the square of the int/float v
 and should be annotated as a float
"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Takes a string `k` and an int/float `v` and returns a tuple.
    Parameters:
        k (str): The input string.
        v (Union[int, float]): The input integer or float.
    Returns:
        Tuple[str, float]: A tuple containing `k` and the square of
        `v` (annotated as a float).
    """
    return k, float(v ** 2)
