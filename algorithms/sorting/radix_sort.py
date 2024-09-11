"""
Radix Sort Algorithm Implementation

This module contains implementations of the Radix Sort algorithm.

Author: Aflah Hanif Amarlyadi
Date: 2024-09-11
License: MIT
"""

from typing import List, TypeVar

T = TypeVar('T')


def radix_sort(array: List[int], k: int = 10) -> List[int]:
    """
    Sorts a list of non-negative integers in ascending order using the Radix Sort algorithm.

    Radix Sort is a non-comparison based sorting algorithm that sorts integers by processing
    their digits from least significant to most significant. It uses counting sort as a
    subroutine to sort numbers based on each digit.

    Args:
        array (List[int]): The list of non-negative integers to be sorted.
        k (int, optional): The base of the number system used for counting sort. Defaults to 10.

    Returns:
        List[int]: The sorted list.

    Raises:
        ValueError: If the input list contains negative integers.

    Time Complexity:
        O(d(n + k)) - where d is the number of digits in the maximum integer, n is the number of elements, 
        and k is the range of each digit.

    Space Complexity:
        O(n + k) - where n is the number of elements and k is the range of each digit.

    Stability:
        This implementation of Radix Sort is stable, it maintains the relative order of equal elements.

    Examples:
    >>> radix_sort([])
    []
    >>> radix_sort([1])
    [1]
    >>> radix_sort([1, 10, 100, 1000, 10000, 100000, 1, 10, 100, 1000, 10000, 100000])
    [1, 1, 10, 10, 100, 100, 1000, 1000, 10000, 10000, 100000, 100000]
    >>> radix_sort([1, 10, 100, 1000, 10000, 100000, 200000, 20000, 2000, 200, 20, 2])
    [1, 2, 10, 20, 100, 200, 1000, 2000, 10000, 20000, 100000, 200000]
    """
    def counting_sort(array: List[int], k: int, exponent: int) -> List[int]:
        """
        Performs counting sort on the array based on the digit represented by the given exponent.

        Args:
            array (List[int]): The list of non-negative integers to be sorted.
            exponent (int): The exponent corresponding to the digit to be sorted.

        Returns:
            array (List[int]): The list sorted by the current digit.
        """
        n = len(array)

        if n == 0:
            return array

        count = [[] for _ in range(k)]

        for num in array:
            digit = (num // exponent) % k
            count[digit].append(num)

        index = 0
        for num_list in count:
            for num in num_list:
                array[index] = num
                index += 1

        return array

    n = len(array)

    if n == 0:
        return array

    maximum = array[0]

    for num in array:
        if num < 0:
            raise ValueError("Array must not contain any negative integers.")
        if num > maximum:
            maximum = num

    exp = 1
    while maximum // exp > 0:
        counting_sort(array, k, exp)
        exp *= 10

    return array


def radix_sort_str(array: List[str]) -> List[str]:
    """
    Sorts a list of strings in ascending order using the Radix Sort algorithm.

    This version of Radix Sort sorts strings by treating them as sequences of ASCII characters.
    It sorts from the rightmost character to the leftmost, based on their ASCII values.

    Args:
        array (List[str]): The list to be sorted.

    Returns:
        List[str]: The sorted list.

    Time Complexity:
        O(nk) - where n is the number of strings and k is the length of the longest string.

    Space Complexity:
        O(n) - where n is the number of elements.
    
    Stability:
        This implementation of Radix Sort is stable, it maintains the relative order of equal elements.

    Examples:
    >>> radix_sort_str([])
    []
    >>> radix_sort_str(['a'])
    ['a']
    """
    def counting_sort_chr(array: List[str], position: int) -> List[str]:
        """
        Performs counting sort on the list based on the character at the given position.

        Args:
            array (List[str]): The list of strings to be sorted.
            position (int): The position of the character to sort by.

        Returns:
            array (List[str]): The list sorted by the current character.
        """
        n = len(array)
        count = [[] for _ in range(95)]

        for string in array:
            char_index = ord(string[position]) - 32 if position < len(string) else 0
            count[char_index].append(string)

        index = 0
        for char_list in count:
            for string in char_list:
                array[index] = string
                index += 1

        return array

    if not array:
        return array

    max_length = len(max(array))

    for pos in range(max_length - 1, -1, -1):
        counting_sort_chr(array, pos)

    return array


if __name__ == "__main__":
    import doctest
    doctest.testmod()
