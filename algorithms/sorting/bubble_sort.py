"""
Bubble Sort Algorithm Implementation

This module contains an implementation of the Bubble Sort algorithm.

Author: Aflah Hanif Amarlyadi
Date: 2024-09-11
License: MIT
"""

from typing import List, TypeVar

T = TypeVar('T')


def bubble_sort(array: List[T]) -> List[T]:
    """
    Sorts a list in ascending order using the Bubble Sort algorithm.

    Bubble Sort is a comparison-based sorting algorithm that repeatedly steps through the list,
    compares adjacent elements, and swaps them if they are in the wrong order. The pass through
    the list is repeated until the list is sorted.

    Args:
        array (List[T]): The list to be sorted.

    Returns:
        List[T]: The sorted list.

    Time Complexity:
        Best Case: O(n) - occurs when the list is already sorted.
        Average Case: O(n^2).
        Worst Case: O(n^2) - occurs when the list is sorted in reverse.

    Space Complexity:
        O(1) - sorting is done in-place, only a constant amount of extra memory is used.

    Stability:
        Bubble Sort is stable, it maintains the relative order of equal elements.

    Examples:
    >>> bubble_sort([])
    []
    >>> bubble_sort([1])
    [1]
    >>> bubble_sort([1, 2, 3, 4, 5, 1, 2, 3, 4, 5])
    [1, 1, 2, 2, 3, 3, 4, 4, 5, 5]
    >>> bubble_sort([1, 2, 3, 4, 5, 0, -1, -2, -3, -4, -5])
    [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]
    >>> bubble_sort([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    >>> bubble_sort([10, 9, 8, 7, 6, 5, 4, 3, 2, 1])
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    >>> bubble_sort(['A', 'a', 'B', 'b', 'C', 'c', 'D', 'd', 'E', 'e'])
    ['A', 'B', 'C', 'D', 'E', 'a', 'b', 'c', 'd', 'e']
    """
    n = len(array)

    for i in range(n):
        swapped = False

        for j in range(n-i-1):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
                swapped = True

        if not swapped:
            break
    
    return array


if __name__ == "__main__":
    import doctest
    doctest.testmod()
