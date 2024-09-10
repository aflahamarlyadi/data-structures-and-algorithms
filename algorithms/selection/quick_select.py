"""
Quick Select Algorithm Implementation

This module contains an implementation of the Quick Select algorithm.

Author: Aflah Hanif Amarlyadi
Date: 2024-09-10
License: MIT
"""

from typing import List, TypeVar
import random

T = TypeVar('T')


def quick_select(array: List[T], k: int, low: int = 0, high: int = None) -> T:
    """
    Finds the k-th smallest element from the list using the Quick Select algorithm with randomised pivot selection.

    Quick Select is a selection algorithm to find the k-th smallest element in an unordered list by partitioning the list 
    around a randomly chosen pivot, then recursively searching only the side of the partition that contains the k-th element.

    Args:
        array (List[T]): The input list.
        k (int): The k-th smallest element to find.
        low (int, optional): The lower index of the sublist. Defaults to 0.
        high (int, optional): The upper index of the sublist. Defaults to None.
    
    Returns:
        T: The k-th smallest element in the list.
    
    Time Complexity:
        O(n)

    Space Complexity:
        O(log n) - additional space is used for the recursive call stack.

    Example:
    >>> quick_select([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 0)
    0
    >>> quick_select([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 1)
    1
    >>> quick_select([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 2)
    2
    >>> quick_select([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 3)
    3
    >>> quick_select([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 4)
    4
    >>> quick_select([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 5)
    5
    >>> quick_select([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 6)
    6
    >>> quick_select([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 7)
    7
    >>> quick_select([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 8)
    8
    >>> quick_select([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 9)
    9
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
        pivot = random.randint(low, high)
        array[low], array[pivot] = array[pivot], array[low]
        i, j = low, high
        
        while i <= j:
            while i <= j and array[i] <= array[low]:
                i += 1
            while i <= j and array[j] > array[low]:
                j -= 1
            if i <= j:
                array[i], array[j] = array[j], array[i]
        
        array[low], array[j] = array[j], array[low]
        return j

    n = len(array)

    high = n-1 if high is None else high
    
    if low >= high:
        return array[k]
    
    mid = partition(array, low, high)

    if k < mid:
        return quick_select(array, k, low, mid-1)
    elif k > mid:
        return quick_select(array, k, mid+1, high)
    else:
        return array[k]


if __name__ == '__main__':
    import doctest
    doctest.testmod()
