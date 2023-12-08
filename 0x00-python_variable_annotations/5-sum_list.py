#!/usr/bin/env python3
"""
Takes list as argument and return sum as float
"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """
    Calculate the sum of a list of floats.

    Parameters:
        input_list (List[float]): A list of floats.

    Returns:
        float: The sum of the elements in the input list.
    """
    return sum(input_list)
