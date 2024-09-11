"""
Selection Sort Algorithm Implementation

This module contains an implementation of the Selection Sort algorithm.

Author: Aflah Hanif Amarlyadi
Date: 2024-09-11
License: MIT
"""

from typing import List, TypeVar

T = TypeVar('T')


def selection_sort(array: List[T]) -> List[T]:
    """
    Sorts a list in ascending order using the Selection Sort algorithm.

    Selection Sort is a comparison-based sorting algorithm that repeatedly selects the minimum element 
    from the unsorted portion of the list and swaps it with the first element of the unsorted portion. 
    This process is repeated for the entire list until the list is sorted.

    Args:
        array (List[T]): The list to be sorted.

    Returns:
        List[T]: The sorted list.

    Time Complexity:
        O(n^2)

    Space Complexity:
        O(1) - sorting is done in-place, only a constant amount of extra memory is used.

    Stability:
        Selection Sort is not stable, it does not maintain the relative order of equal elements.

    Examples:
    >>> selection_sort([])
    []
    >>> selection_sort([1])
    [1]
    >>> selection_sort([1, 2, 3, 4, 5, 1, 2, 3, 4, 5])
    [1, 1, 2, 2, 3, 3, 4, 4, 5, 5]
    >>> selection_sort([1, 2, 3, 4, 5, 0, -1, -2, -3, -4, -5])
    [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]
    >>> selection_sort([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    >>> selection_sort([10, 9, 8, 7, 6, 5, 4, 3, 2, 1])
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    >>> selection_sort(['A', 'a', 'B', 'b', 'C', 'c', 'D', 'd', 'E', 'e'])
    ['A', 'B', 'C', 'D', 'E', 'a', 'b', 'c', 'd', 'e']
    """
    n = len(array)

    for i in range(n-1):
        min_index = i
        for j in range(i+1, n):
            if array[j] < array[min_index]:
                min_index = j
        
        if min_index != i:
            array[i], array[min_index] = array[min_index], array[i]

    return array


if __name__ == "__main__":
    import doctest
    doctest.testmod()
