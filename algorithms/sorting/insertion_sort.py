"""
Insertion Sort Algorithm Implementation

This module contains an implementation of the Insertion Sort algorithm.

Author: Aflah Hanif Amarlyadi
Date: 2024-09-11
License: MIT
"""

from typing import List, TypeVar

T = TypeVar('T')


def insertion_sort(array: List[T]) -> List[T]:
    """
    Sorts a list in ascending order using the Insertion Sort algorithm.

    Insertion Sort is a comparison-based sorting algorithm that builds the final sorted array one element at a time. 
    It is particularly efficient for small data sets or nearly sorted data.

    Args:
        array (List[T]): The list to be sorted.

    Returns:
        List[T]: The sorted list.

    Time Complexity:
        Best Case: O(n) - occurs when the list is already sorted.
        Average Case: O(n^2)
        Worst Case: O(n^2) - occurs when the list is sorted in reverse.

    Space Complexity:
        O(1) - sorting is done in-place, only a constant amount of extra memory is used.

    Stability:
        Insertion Sort is stable, maintaining the relative order of equal elements.

    Examples:
    >>> insertion_sort([])
    []
    >>> insertion_sort([1])
    [1]
    >>> insertion_sort([1, 2, 3, 4, 5, 1, 2, 3, 4, 5])
    [1, 1, 2, 2, 3, 3, 4, 4, 5, 5]
    >>> insertion_sort([1, 2, 3, 4, 5, 0, -1, -2, -3, -4, -5])
    [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]
    >>> insertion_sort([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    >>> insertion_sort([10, 9, 8, 7, 6, 5, 4, 3, 2, 1])
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    >>> insertion_sort(['A', 'a', 'B', 'b', 'C', 'c', 'D', 'd', 'E', 'e'])
    ['A', 'B', 'C', 'D', 'E', 'a', 'b', 'c', 'd', 'e']
    """
    n = len(array)

    for i in range(1, n):
        key = array[i]
        j = i - 1
        
        while j >= 0 and key < array[j]:
            array[j+1] = array[j]
            j -= 1
        
        array[j+1] = key
    
    return array


if __name__ == "__main__":
    import doctest
    doctest.testmod()
