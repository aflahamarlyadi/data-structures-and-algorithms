"""
Median of Medians Algorithm Implementation

This module contains an implementation of the Median of Medians algorithm.

Author: Aflah Hanif Amarlyadi
Date: 2024-09-10
License: MIT
"""

from typing import List, TypeVar

T = TypeVar('T')


def median_of_medians(array: List[int]) -> int:
    """
    Finds the approximate median of an list of integers using the Median of Medians algorithm.

    The median of medians algorithm guarantees a good approximation of the median, 
    for use as a pivot in the Quick Select algorithm.

    Args:
        array (List[int]): The input list.

    Returns:
        int: The approximate median of the list.

    Time Complexity:
        O(n)

    Space Complexity:
        O(n)
    """
    def median_of_five(array: List[int]) -> int:
        """
        Finds the median of list of up to 5 integers.

        Args:
            array (List[int]): A list of integers.

        Returns:
            int: The median value of the list.
        """
        n = len(array)

        array = sorted(array)
        median = n // 2

        return array[median]
    
    n = len(array)
    
    if n < 5:
        return median_of_five(array)
    
    medians = []
    i = 0
    while i < n:
        j = min(i+5, n)
        median = median_of_five(array[i:j])
        medians.append(median)
        i += 5
    
    return median_of_medians(medians)
