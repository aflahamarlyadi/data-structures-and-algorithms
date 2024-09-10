"""
Linear Search Algorithm Implementation

This module contains an implementation of the Linear Search algorithm.

Author: Aflah Hanif Amarlyadi
Date: 2024-09-10
License: MIT
"""

from typing import List, TypeVar

T = TypeVar('T')


def linear_search(array: List[T], item: T) -> int:
    """
    Searches for the specified item in a list using the Linear Search algorithm.

    Linear Search is a search algorithm that iterates through the list and compares 
    each element with the target value until the target is found or the end of the list 
    is reached.

    Args:
        array (List[T]): The list to search.
        item (T): The item to search in the list.

    Returns:
        int: The index of the item if found; otherwise, -1.

    Time Complexity:
        O(n)

    Space Complexity:
        O(1)

    Examples:
    >>> linear_search([], 0)
    -1
    >>> linear_search([3, 2, 6, 8, 7, 8, 9, 2], 9)
    6
    >>> linear_search([3, 2, 6, 8, 7, 8, 9, 2], 1)
    -1
    >>> linear_search(['a', 'b', 'c', 'd', 'e'], 'd')
    3
    >>> linear_search(['a', 'b', 'c', 'd', 'e'], 'f')
    -1
    """
    n = len(array)

    for i in range(n):
        if array[i] == item:
            return i
    
    return -1


if __name__ == "__main__":
    import doctest
    doctest.testmod()
