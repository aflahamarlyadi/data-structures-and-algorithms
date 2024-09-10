"""
Binary Search Algorithm Implementation

This module contains an implementation of the Binary Search algorithm.

Author: Aflah Hanif Amarlyadi
Date: 2024-09-10
License: MIT
"""

from typing import List, TypeVar

T = TypeVar('T')


def binary_search(array: List[T], item: T) -> int:
    """
    Searches for the specified item in a sorted list using the Binary Search algorithm.
    
    Binary Search is a search algorithm that finds the position of a target value within 
    a sorted list by repeatedly dividing the search interval in half. It compares the 
    middle element of the interval with the target value. If the target is less than 
    the middle element, the search continues in the lower half, otherwise, in the upper 
    half, until the target is found or it's determined that the target is not in the list.

    Args:
        array (List[T]): The sorted list to search.
        item (T): The item to search in the sorted list.

    Returns:
        int: The index of the item if found; otherwise, -1.

    Time Complexity:
        O(log n)

    Space Complexity:
        O(1)

    Examples:
    >>> binary_search([], 0)
    -1
    >>> binary_search([2, 2, 3, 6, 7, 8, 8, 9], 9)
    7
    >>> binary_search([2, 2, 3, 6, 7, 8, 8, 9], 1)
    -1
    >>> binary_search(['a', 'b', 'c', 'd', 'e'], 'd')
    3
    >>> binary_search(['a', 'b', 'c', 'd', 'e'], 'f')
    -1
    """
    n = len(array)
    
    low, high = 0, n-1

    while low <= high:
        mid = low + (high - low) // 2
        if array[mid] == item:
            return mid
        elif array[mid] < item:
            low = mid + 1
        else:
            high = mid - 1
    
    return -1


if __name__ == "__main__":
    import doctest
    doctest.testmod()
