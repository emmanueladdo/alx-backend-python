#!/usr/bin/env pyhton3
"""
Takes list as argument and return sum as float
 input_list of floats as argument and returns their sum as a float
"""
from typing import List

from typing import List


def sum_list(input_list: List[float]) -> float:
    """adds a list of floats and return a float"""
    if not input_list:
        return 0
    return sum(input_list)
    