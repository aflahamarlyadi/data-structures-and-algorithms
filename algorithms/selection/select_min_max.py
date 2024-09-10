"""
Select Min Max Implementation

This module contains an implementation of the Select Min Max algorithm.

Author: Aflah Hanif Amarlyadi
Date: 2024-09-10
License: MIT
"""

from typing import List, Tuple, TypeVar

T = TypeVar('T')


def select_min_max(array: List[T]) -> Tuple[T, T]:
    """
    Finds the minimum and maximum values in the list with 1.5n comparisons.

    This approach compare elements in pairs by comparing the smaller with the current minimum 
    and the larger with the current maximum, resulting in 1.5n comparisons for n elements.

    Args:
        array (List[T]): The input list.

    Returns:
        Tuple[T, T]: A tuple containing the minimum and maximum values in the list.

    Raises:
        ValueError: If the input list is empty.

    Time Complexity:
        O(n)

    Space Complexity:
        O(1)

    Examples:
    >>> select_min_max([3, 2, 6, 8, 7, 9, 8, 2])
    (2, 9)
    >>> select_min_max([1])
    (1, 1)
    """
    n = len(array)

    if n == 0:
        raise ValueError("Array must contain at least one element")
    
    minimum = array[0]
    maximum = array[0]
    
    start = 0 if n % 2 == 0 else 1
    
    for i in range(start, n, 2):
        if array[i] < array[i + 1]:
            if array[i] < minimum:
                minimum = array[i]
            if array[i + 1] > maximum:
                maximum = array[i + 1]
        else:
            if array[i] > maximum:
                maximum = array[i]
            if array[i + 1] < minimum:
                minimum = array[i + 1]

    return minimum, maximum


def select_min_max_naive(array: List[T]) -> Tuple[T, T]:
    """
    Finds the minimum and maximum values in the list with 2n comparisons.

    This naive approach compares each element with both the current minimum and maximum, 
    resulting in 2n comparisons for n elements.

    Args:
        array (List[T]): The input list.

    Returns:
        Tuple[T, T]: A tuple containing the minimum and maximum values in the list.

    Raises:
        ValueError: If the input list is empty.

    Time Complexity:
        O(n)

    Space Complexity:
        O(1)

    Examples:
    >>> select_min_max_naive([3, 2, 6, 8, 7, 9, 8, 2])
    (2, 9)
    >>> select_min_max_naive([1])
    (1, 1)
    """
    n = len(array)

    if n == 0:
        raise ValueError("Array must contain at least one element")

    minimum = array[0]
    maximum = array[0]

    for i in range(1, n):
        if array[i] < minimum:
            minimum = array[i]
        if array[i] > maximum:
            maximum = array[i]

    return minimum, maximum


if __name__ == "__main__":
    import doctest
    doctest.testmod()
