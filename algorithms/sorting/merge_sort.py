"""
Merge Sort Algorithm Implementation

This module contains both iterative and recursive implementations of the Merge Sort algorithm.

Author: Aflah Hanif Amarlyadi
Date: 2024-09-11
License: MIT
"""

from typing import List, TypeVar

T = TypeVar('T')


def merge_sort_iterative(array: List[T]) -> List[T]:
    """
    Sorts a list in ascending order using the iterative Merge Sort algorithm.

    Merge Sort is a comparison-based sorting algorithm that uses a divide-and-conquer approach.
    It divides the list into smaller sublists, sorts them, and then merges them back together.
    The iterative version uses a bottom-up approach, starting with sublists of size 1 and
    iteratively merging them.

    Args:
        array (List[T]): The list to be sorted.

    Returns:
        List[T]: The sorted list.

    Time Complexity:
        O(n log n)

    Space Complexity:
        O(n) - additional space is used for the temporary sublists during merging.
    
    Stability:
        Merge Sort is stable, it maintains the relative order of equal elements.

    Examples:
    >>> merge_sort_iterative([])
    []
    >>> merge_sort_iterative([1])
    [1]
    >>> merge_sort_iterative([1, 2, 3, 4, 5, 1, 2, 3, 4, 5])
    [1, 1, 2, 2, 3, 3, 4, 4, 5, 5]
    >>> merge_sort_iterative([1, 2, 3, 4, 5, 0, -1, -2, -3, -4, -5])
    [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]
    >>> merge_sort_iterative([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    >>> merge_sort_iterative([10, 9, 8, 7, 6, 5, 4, 3, 2, 1])
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    >>> merge_sort_iterative(['A', 'a', 'B', 'b', 'C', 'c', 'D', 'd', 'E', 'e'])
    ['A', 'B', 'C', 'D', 'E', 'a', 'b', 'c', 'd', 'e']
    """
    def merge(left: List[T], right: List[T]) -> List[T]:
        """
        Merges two sorted lists into one sorted list.

        Args:
            left (List[T]): The first sorted list.
            right (List[T]): The second sorted list.

        Returns:
            List[T]: The merged sorted list.
        """
        merged = []
        n, m = len(left), len(right)
        i, j = 0, 0

        while i < n or j < m:
            if j == m or (i < n and left[i] <= right[j]):
                merged.append(left[i])
                i += 1
            else:
                merged.append(right[j])
                j += 1
        
        return merged

    n = len(array)

    if n <= 1:
        return array
    
    size = 1
    while size < n:
        for i in range(0, n, 2 * size):
            left = array[i:i + size]
            right = array[i + size:i + 2 * size]
            array[i:i + 2 * size] = merge(left, right)
        size *= 2

    return array


def merge_sort_recursive(array: List[T]) -> List[T]:
    """
    Sorts a list in ascending order using the recursive Merge Sort algorithm.

    Merge Sort is a comparison-based sorting algorithm that uses a divide-and-conquer approach.
    It divides the list into smaller sublists, sorts them, and then merges them back together.
    The recursive version uses a top-down approach, recursively dividing the list until
    sublists of size 1 are reached, then merging them.

    Args:
        array (List[T]): The list to be sorted.

    Returns:
        List[T]: The sorted list.

    Time Complexity:
        O(n log n)

    Space Complexity:
        O(n) - additional space is used for the temporary sublists during merging.

    Stability:
        Merge Sort is stable, it maintains the relative order of equal elements.

    Examples:
    >>> merge_sort_recursive([])
    []
    >>> merge_sort_recursive([1])
    [1]
    >>> merge_sort_recursive([1, 2, 3, 4, 5, 1, 2, 3, 4, 5])
    [1, 1, 2, 2, 3, 3, 4, 4, 5, 5]
    >>> merge_sort_recursive([1, 2, 3, 4, 5, 0, -1, -2, -3, -4, -5])
    [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]
    >>> merge_sort_recursive([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    >>> merge_sort_recursive([10, 9, 8, 7, 6, 5, 4, 3, 2, 1])
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    >>> merge_sort_recursive(['A', 'a', 'B', 'b', 'C', 'c', 'D', 'd', 'E', 'e'])
    ['A', 'B', 'C', 'D', 'E', 'a', 'b', 'c', 'd', 'e']
    """

    def merge(left: List[T], right: List[T]) -> List[T]:
        """
        Merges two sorted lists into one sorted list.

        Args:
            left (List[T]): The first sorted list.
            right (List[T]): The second sorted list.

        Returns:
            List[T]: The merged sorted list.
        """
        merged = []
        n, m = len(left), len(right)
        i, j = 0, 0

        while i < n or j < m:
            if j == m or (i < n and left[i] <= right[j]):
                merged.append(left[i])
                i += 1
            else:
                merged.append(right[j])
                j += 1

        return merged

    n = len(array)

    if n <= 1:
        return array

    mid = n // 2
    left = merge_sort_recursive(array[:mid])
    right = merge_sort_recursive(array[mid:])
    return merge(left, right)


if __name__ == "__main__":
    import doctest
    doctest.testmod()
