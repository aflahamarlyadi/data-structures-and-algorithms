"""
Quick Sort Algorithm Implementation

This module contains implementations of the Quick Sort algorithm with different partitioning schemes.

Author: Aflah Hanif Amarlyadi
Date: 2024-09-11
License: MIT
"""

from typing import List, Tuple, TypeVar
import random

T = TypeVar('T')


def quick_sort(array: List[T]) -> List[T]:
    """
    Sorts a list in ascending order using the Quick Sort algorithm.

    Quick Sort is a comparison-based sorting algorithm that uses a divide-and-conquer approach.
    It selects a pivot element and partitions the list into three sublists: elements less than the pivot,
    elements equal to the pivot, and elements greater than the pivot. It then recursively sorts the sublists.

    Args:
        array (List[T]): The list to be sorted.

    Returns:
        List[T]: The sorted list.

    Time Complexity:
        Best Case: O(n log n)
        Average: O(n log n)
        Worst Case: O(n^2) - occurs when the pivot selection consistently results in the smallest or largest element in
        the sublist, leading to highly unbalanced partitions.

    Space Complexity:
        O(n) - additional space is used for the temporary sublists during partitioning.

    Stability:
        This implementation of Quick Sort is stable, it maintains the relative order of equal elements.

    Examples:
    >>> quick_sort([])
    []
    >>> quick_sort([1])
    [1]
    >>> quick_sort([1, 2, 3, 4, 5, 1, 2, 3, 4, 5])
    [1, 1, 2, 2, 3, 3, 4, 4, 5, 5]
    >>> quick_sort([1, 2, 3, 4, 5, 0, -1, -2, -3, -4, -5])
    [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]
    >>> quick_sort([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    >>> quick_sort([10, 9, 8, 7, 6, 5, 4, 3, 2, 1])
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    >>> quick_sort(['A', 'a', 'B', 'b', 'C', 'c', 'D', 'd', 'E', 'e'])
    ['A', 'B', 'C', 'D', 'E', 'a', 'b', 'c', 'd', 'e']
    """
    n = len(array)

    if n <= 1:
        return array

    left = []
    middle = []
    right = []

    pivot = array[random.randint(0, n-1)]
    for x in array:
        if x < pivot:
            left.append(x)
        elif x > pivot:
            right.append(x)
        else:
            middle.append(x)

    return quick_sort(left) + middle + quick_sort(right)


def quick_sort_dnf(array: List[T], low: int = 0, high: int = None) -> List[T]:
    """
    Sorts a list in ascending order using the Quick Sort algorithm with Dutch National Flag partitioning scheme.

    This version of Quick Sort uses the Dutch National Flag partitioning scheme, which partitions the array into three parts: 
    elements less than the pivot, elements equal to the pivot, and elements greater than the pivot. It is generally more 
    efficient than Hoare's partitioning scheme for lists with many equal elements, as it avoids unnecessary recursive 
    calls on equal elements.

    Args:
        array (List[T]): The list to be sorted.
        low (int, optional): The lower index of the sublist. Defaults to 0.
        high (int, optional): The upper index of the sublist. Defaults to None.

    Returns:
        List[T]: The sorted list.

    Time Complexity:
        Best Case: O(n log n)
        Average Case: O(n log n)
        Worst Case: O(n^2) - occurs when the pivot selection consistently results in the smallest or largest element in
        the sublist, leading to highly unbalanced partitions.

    Space Complexity:
        O(log n) - additional space is used for the recursive call stack.

    Stability:
        This implementation of Quick Sort is unstable, it does not maintain the relative order of equal elements.

    Examples:
    >>> quick_sort_dnf([])
    []
    >>> quick_sort_dnf([1])
    [1]
    >>> quick_sort_dnf([1, 2, 3, 4, 5, 1, 2, 3, 4, 5])
    [1, 1, 2, 2, 3, 3, 4, 4, 5, 5]
    >>> quick_sort_dnf([1, 2, 3, 4, 5, 0, -1, -2, -3, -4, -5])
    [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]
    >>> quick_sort_dnf([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    >>> quick_sort_dnf([10, 9, 8, 7, 6, 5, 4, 3, 2, 1])
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    >>> quick_sort_dnf(['A', 'a', 'B', 'b', 'C', 'c', 'D', 'd', 'E', 'e'])
    ['A', 'B', 'C', 'D', 'E', 'a', 'b', 'c', 'd', 'e']
    """
    def partition(array: List[T], low: int, high: int) -> Tuple[int, int]:
        """
        Partitions the list with Dutch National Flag partitioning scheme.

        Args:
            array (List[T]): The list to partition.
            low (int): The lower index of the sublist.
            high (int): The upper index of the sublist.

        Returns:
            Tuple[int, int]: The indices where elements equal to the pivot start and end.
        """
        pivot = array[random.randint(low, high)]
        mid = low
        
        while mid <= high:
            if array[mid] < pivot:
                array[low], array[mid] = array[mid], array[low]
                low += 1
                mid += 1
            elif array[mid] == pivot:
                mid += 1
            else:
                array[mid], array[high] = array[high], array[mid]
                high -= 1
        
        return low, mid

    n = len(array)

    high = n-1 if high is None else high

    if low < high:
        left, right = partition(array, low, high)
        quick_sort_dnf(array, low, left - 1)
        quick_sort_dnf(array, right, high)

    return array


def quick_sort_hoare(array: List[T], low: int = 0, high: int = None) -> List[T]:
    """
    Sorts a list in ascending order using the Quick Sort algorithm with Hoare's partitioning scheme.

    This version of Quick Sort uses Hoare's partitioning scheme, which partitions the array into two parts: elements 
    less than the pivot and elements greater than the pivot. It is generally more efficient than Lomuto's scheme as it 
    performs fewer swaps. It uses two pointers that start at the ends of the array and move towards each other until 
    they overlap, swapping elements that are in the wrong partition.

    Args:
        array (List[T]): The list to be sorted.
        low (int, optional): The lower index of the sublist. Defaults to 0.
        high (int, optional): The upper index of the sublist. Defaults to None.

    Returns:
        List[T]: The sorted list.

    Time Complexity:
        Best Case: O(n log n)
        Average Case: O(n log n)
        Worst Case: O(n^2) - occurs when the pivot selection consistently results in the smallest or largest element in
        the sublist, leading to highly unbalanced partitions.

    Space Complexity:
        O(log n) - additional space is used for the recursive call stack.

    Stability:
        This implementation of Quick Sort is unstable, it does not maintain the relative order of equal elements.

    Examples:
    >>> quick_sort_hoare([])
    []
    >>> quick_sort_hoare([1])
    [1]
    >>> quick_sort_hoare([1, 2, 3, 4, 5, 1, 2, 3, 4, 5])
    [1, 1, 2, 2, 3, 3, 4, 4, 5, 5]
    >>> quick_sort_hoare([1, 2, 3, 4, 5, 0, -1, -2, -3, -4, -5])
    [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]
    >>> quick_sort_hoare([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    >>> quick_sort_hoare([10, 9, 8, 7, 6, 5, 4, 3, 2, 1])
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    >>> quick_sort_hoare(['A', 'a', 'B', 'b', 'C', 'c', 'D', 'd', 'E', 'e'])
    ['A', 'B', 'C', 'D', 'E', 'a', 'b', 'c', 'd', 'e']
    """
    def partition(array: List[T], low: int, high: int) -> int:
        """
        Partitions the list with Hoare's partitioning.

        Args:
            array (List[T]): The list to partition.
            low (int): The lower index of the sublist.
            high (int): The upper index of the sublist.

        Returns:
            int: The index of the sorted pivot.
        """
        pivot = array[random.randint(low, high)]
        i, j = low, high

        while True:
            while array[i] < pivot:
                i += 1
            while array[j] > pivot:
                j -= 1
            if i >= j:
                return j
            array[i], array[j] = array[j], array[i]
            i += 1
            j -= 1

    n = len(array)

    high = n-1 if high is None else high

    if low < high:
        mid = partition(array, low, high)
        quick_sort_hoare(array, low, mid)
        quick_sort_hoare(array, mid+1, high)

    return array


def quick_sort_lomuto(array: List[T], low: int = 0, high: int = None) -> List[T]:
    """
    Sorts a list in ascending order using the Quick Sort algorithm with Lomuto's partitioning scheme.

    This version of Quick Sort uses Lomuto's partitioning scheme, which partitions the array into two parts: elements 
    less than the pivot and elements greater than or equal to the pivot. It uses a single pointer that scans from left 
    to right, swapping elements smaller than the pivot to the left side of the array. After partitioning, the pivot is 
    guaranteed to be in its final sorted position.

    Args:
        array (List[T]): The list to be sorted.
        low (int, optional): The lower index of the sublist. Defaults to 0.
        high (int, optional): The upper index of the sublist. Defaults to None.

    Returns:
        List[T]: The sorted list.

    Time Complexity:
        Best Case: O(n log n)
        Average Case: O(n log n)
        Worst Case: O(n^2) - occurs when the pivot selection consistently results in the smallest or largest element in
        the sublist, leading to highly unbalanced partitions.

    Space Complexity:
        O(log n) - additional space is used for the recursive call stack.

    Stability:
        This implementation of Quick Sort is unstable, it does not maintain the relative order of equal elements.

    Examples:
    >>> quick_sort_lomuto([])
    []
    >>> quick_sort_lomuto([1])
    [1]
    >>> quick_sort_lomuto([1, 2, 3, 4, 5, 1, 2, 3, 4, 5])
    [1, 1, 2, 2, 3, 3, 4, 4, 5, 5]
    >>> quick_sort_lomuto([1, 2, 3, 4, 5, 0, -1, -2, -3, -4, -5])
    [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]
    >>> quick_sort_lomuto([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    >>> quick_sort_lomuto([10, 9, 8, 7, 6, 5, 4, 3, 2, 1])
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    >>> quick_sort_lomuto(['A', 'a', 'B', 'b', 'C', 'c', 'D', 'd', 'E', 'e'])
    ['A', 'B', 'C', 'D', 'E', 'a', 'b', 'c', 'd', 'e']
    """
    def lomuto_partition(array: List[T], low: int, high: int) -> int:
        """
        Partitions the list with Lomuto's partitioning scheme.

        Args:
            array (List[T]): The list to partition.
            low (int): The lower index of the sublist.
            high (int): The upper index of the sublist.

        Returns:
            int: The index of the sorted pivot.
        """
        pivot = random.randint(low, high)
        array[high], array[pivot] = array[pivot], array[high]

        i = low
        for j in range(low, high):
            if array[j] < array[high]:
                array[i], array[j] = array[j], array[i]
                i += 1

        array[high], array[i] = array[i], array[high]
        return i

    n = len(array)

    high = n-1 if high is None else high

    if low < high:
        mid = lomuto_partition(array, low, high)
        quick_sort_lomuto(array, low, mid-1)
        quick_sort_lomuto(array, mid+1, high)

    return array


if __name__ == "__main__":
    import doctest
    doctest.testmod()
