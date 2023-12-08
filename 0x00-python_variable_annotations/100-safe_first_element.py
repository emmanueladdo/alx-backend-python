#!/usr/bin/env python3
"""
This module contains code with correct duck-typed annotations
"""
from typing import Any, Sequence, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """
    Returns the first element of the input sequence if it is non-empty,
    otherwise returns None.

    Parameters:
    - lst (Sequence[Any]): The input sequence.

    Returns:
    - Union[Any, None]: The first element of the sequence or None
    if the sequence is empty.
    """
    if lst:
        return lst[0]
    else:
        return None
