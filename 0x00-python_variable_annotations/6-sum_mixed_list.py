#!/usr/bin/env python3
"""
Function that somes mixed lists and returns mixed list
"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    Calculate the sum of a list of integers and floats.

    Parameters:
        mxd_lst (List[Union[int, float]]): A list containing int and floats.

    Returns:
        float: The sum of the elements in the mixed list.
    """
    return sum(mxd_lst)
