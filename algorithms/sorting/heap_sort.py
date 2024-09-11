"""
Heap Sort Algorithm Implementation

This module contains an implementation of the Heap Sort algorithm.

Author: Aflah Hanif Amarlyadi
Date: 2024-09-11
License: MIT
"""

from typing import List, TypeVar

T = TypeVar('T')


def heap_sort(array: List[T]) -> List[T]:
    """
    Sorts a list in ascending order using the Heap Sort algorithm.

    Heap Sort is a comparison-based sorting algorithm that uses a binary heap data structure.
    It first builds a max heap from the input list, then repeatedly extracts the maximum element
    from the heap and rebuilds the heap until all elements are sorted.

    Args:
        array (List[T]): The list to be sorted.

    Returns:
        List[T]: The sorted list.

    Time Complexity:
        Best Case: O(n) - occurs when the entire list consists of identical elements.
        Average Case: O(n log n)
        Worst Case: O(n log n)

    Space Complexity:
        O(1) - sorting is done in-place, only a constant amount of extra memory is used.

    Stability:
        Heap Sort is unstable, it does not maintain the relative order of equal elements.

    Examples:
    >>> heap_sort([])
    []
    >>> heap_sort([1])
    [1]
    >>> heap_sort([1, 2, 3, 4, 5, 1, 2, 3, 4, 5])
    [1, 1, 2, 2, 3, 3, 4, 4, 5, 5]
    >>> heap_sort([1, 2, 3, 4, 5, 0, -1, -2, -3, -4, -5])
    [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]
    >>> heap_sort([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    >>> heap_sort([10, 9, 8, 7, 6, 5, 4, 3, 2, 1])
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    >>> heap_sort(['A', 'a', 'B', 'b', 'C', 'c', 'D', 'd', 'E', 'e'])
    ['A', 'B', 'C', 'D', 'E', 'a', 'b', 'c', 'd', 'e']
    """
    def heapify(array: List[T]) -> None:
        """
        Converts the given array into a max heap.

        Args:
            array (List[T]): The array to convert into a max heap.
        """
        n = len(array)
        for i in range(n // 2 - 1, -1, -1):
            fall(array, i, n)

    def fall(array: List[T], index: int, n: int) -> None:
        """
        Moves the element at the given index down to maintain the max heap property.

        Args:
            array (List[T]): The array representing the heap.
            index (int): The index of the element to fall.
            n (int): The number of elements in the heap portion of the array.
        """
        while index * 2 + 1 < n:
            left = index * 2 + 1
            right = index * 2 + 2
            largest = index

            if left < n and array[left] > array[largest]:
                largest = left
            if right < n and array[right] > array[largest]:
                largest = right

            if largest != index:
                array[index], array[largest] = array[largest], array[index]
                index = largest
            else:
                break

    n = len(array)

    heapify(array)

    for i in range(n - 1, 0, -1):
        array[0], array[i] = array[i], array[0]
        fall(array, 0, i)

    return array


if __name__ == '__main__':
    import doctest
    doctest.testmod()
