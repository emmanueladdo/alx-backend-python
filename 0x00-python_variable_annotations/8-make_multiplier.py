#!/usr/bin/env python3
"""

"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Takes a float `multiplier` and returns a
    function that multiplies a float by `multiplier`.

    Parameters:
        multiplier (float): The multiplier value.

    Returns:
        Callable[[float], float]: A function that
        takes a float and returns its product with `multiplier`.
    """
    def multiplier_function(x: float) -> float:
        return x * multiplier

    return multiplier_function
