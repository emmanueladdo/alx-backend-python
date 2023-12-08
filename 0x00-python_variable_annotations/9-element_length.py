#!/usr/bin/env python3
"""
Annotate the below function’s
parameters and return values with the appropriate types
"""
from typing import List, Tuple


def element_length(lst: List[str]) -> List[Tuple[str, int]]:
    """
    Takes a list of strings `lst` and returns a list of tuples.
    Each tuple contains an element from the input list and its length.

    Parameters:
        lst (List[str]): The input list of strings.

    Returns:
        List[Tuple[str, int]]: A list of tuples, where each tuple
        contains a string from `lst` and its length.
    """
    return [(i, len(i)) for i in lst]
