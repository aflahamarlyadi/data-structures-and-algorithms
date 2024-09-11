"""
Counting Sort Algorithm Implementation

This module contains both stable and unstable implementations of the Counting Sort algorithm.

Author: Aflah Hanif Amarlyadi
Date: 2024-09-11
License: MIT
"""

from typing import List, TypeVar
from algorithms.selection.select_min_max import select_min_max

T = TypeVar('T')


def counting_sort(array: List[int]):
    """
    Sorts a list of integers in ascending order using the stable Counting Sort algorithm.

    Counting Sort is a non-comparison based sorting algorithm that sorts integers by counting the occurrences of each 
    distinct element in the list. It is particularly efficient when the range of the input (k) is not significantly 
    greater than the number of elements to be sorted (n).

    Args:
        array (List[int]): The list of integers to be sorted.

    Returns:
        List[int]: The sorted list of integers.

    Time Complexity:
        O(n + k) - where n is the number of elements and k is the range of input.

    Space Complexity:
        O(n + k) - where n is the number of elements and k is the range of input.

    Stability:
        This implementation of Counting Sort is stable, it maintains the relative order of equal elements.

    Examples:
    >>> counting_sort([])
    []
    >>> counting_sort([1])
    [1]
    >>> counting_sort([1, 2, 3, 4, 5, 1, 2, 3, 4, 5])
    [1, 1, 2, 2, 3, 3, 4, 4, 5, 5]
    >>> counting_sort([1, 2, 3, 4, 5, 0, -1, -2, -3, -4, -5])
    [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]
    >>> counting_sort([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    >>> counting_sort([10, 9, 8, 7, 6, 5, 4, 3, 2, 1])
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    """
    n = len(array)

    if n == 0:
        return array

    minimum, maximum = select_min_max(array)
    k = maximum - minimum + 1

    count = [[] for _ in range(k)]

    for num in array:
        count[num - minimum].append(num)

    index = 0
    for num_list in count:
        for num in num_list:
            array[index] = num
            index += 1

    return array


def counting_sort_chr(array: List[chr]):
    """
    Sorts a list of characters in ascending order using the stable Counting Sort algorithm.

    This version of Counting Sort sorts ASCII printable characters, which have a range from 32 (space) to 126 (tilde).

    Args:
        array (List[chr]): The list of characters to be sorted.

    Returns:
        List[chr]: The sorted list of characters.

    Time Complexity:
        O(n + k) - where n is the number of elements and k is the range of input.

    Space Complexity:
        O(n) - since the size of the count array is fixed and does not depend on the range of input.

    Stability:
        This implementation of Counting Sort is stable, it maintains the relative order of equal elements.

    Examples:
    >>> counting_sort_chr([])
    []
    >>> counting_sort_chr(['a'])
    ['a']
    >>> counting_sort_chr(['a', 'b', 'c', 'd', 'e', 'a', 'b', 'c', 'd', 'e'])
    ['a', 'a', 'b', 'b', 'c', 'c', 'd', 'd', 'e', 'e']
    >>> counting_sort_chr(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j'])
    ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
    >>> counting_sort_chr(['j', 'i', 'h', 'g', 'f', 'e', 'd', 'c', 'b', 'a'])
    ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
    >>> counting_sort_chr(['A', 'a', 'B', 'b', 'C', 'c', 'D', 'd', 'E', 'e'])
    ['A', 'B', 'C', 'D', 'E', 'a', 'b', 'c', 'd', 'e']
    """
    n = len(array)

    if n == 0:
        return array

    count = [[] for _ in range(95)]

    for char in array:
        count[ord(char) - 32].append(char)

    index = 0
    for char_list in count:
        for char in char_list:
            array[index] = char
            index += 1

    return array


def counting_sort_unstable(array: List[int]):
    """
    Sorts a list of integers in ascending order using the unstable Counting Sort algorithm.

    This version of Counting Sort requires less additional space compared to the stable version, 
    but the stability is sacrificed.

    Args:
        array (List[int]): The list of integers to be sorted.

    Returns:
        List[int]: The sorted list of integers.

    Time Complexity:
        O(n + k) - where n is the number of elements and k is the range of input.

    Space Complexity:
        O(k) - where k is the range of input.

    Stability:
        This implementation of Counting Sort is unstable, it does not maintain the relative order of equal elements.

    Examples:
    >>> counting_sort_unstable([])
    []
    >>> counting_sort_unstable([1])
    [1]
    >>> counting_sort_unstable([1, 2, 3, 4, 5, 1, 2, 3, 4, 5])
    [1, 1, 2, 2, 3, 3, 4, 4, 5, 5]
    >>> counting_sort_unstable([1, 2, 3, 4, 5, 0, -1, -2, -3, -4, -5])
    [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]
    >>> counting_sort_unstable([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    >>> counting_sort_unstable([10, 9, 8, 7, 6, 5, 4, 3, 2, 1])
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    """
    n = len(array)

    if n == 0:
        return array

    minimum, maximum = select_min_max(array)
    k = maximum - minimum + 1

    count = [0] * k

    for num in array:
        count[num - minimum] += 1

    index = 0
    for i in range(k):
        frequency = count[i]
        for _ in range(frequency):
            array[index] = i + minimum
            index += 1
    
    return array


def counting_sort_chr_unstable(array: List[chr]):
    """
    Sorts a list of characters in ascending order using the unstable Counting Sort algorithm.

    This version of Counting Sort sorts ASCII printable characters, which have a range from 32 (space) to 126 (tilde).
    It requires less additional space compared to the stable version, but the stability is sacrificed.

    Args:
        array (List[chr]): The list of characters to be sorted.

    Returns:
        List[chr]: The sorted list of characters.

    Time Complexity:
        O(n + k) - where n is the number of elements and k is the range of input.

    Space Complexity:
        O(1) - since the size of the count array is fixed and does not depend on the range of input.

    Stability:
        This implementation of Counting Sort is unstable, it does not maintain the relative order of equal elements.

    Examples:
    >>> counting_sort_chr_unstable([])
    []
    >>> counting_sort_chr_unstable(['a'])
    ['a']
    >>> counting_sort_chr_unstable(['a', 'b', 'c', 'd', 'e', 'a', 'b', 'c', 'd', 'e'])
    ['a', 'a', 'b', 'b', 'c', 'c', 'd', 'd', 'e', 'e']
    >>> counting_sort_chr_unstable(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j'])
    ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
    >>> counting_sort_chr_unstable(['j', 'i', 'h', 'g', 'f', 'e', 'd', 'c', 'b', 'a'])
    ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
    >>> counting_sort_chr_unstable(['A', 'a', 'B', 'b', 'C', 'c', 'D', 'd', 'E', 'e'])
    ['A', 'B', 'C', 'D', 'E', 'a', 'b', 'c', 'd', 'e']
    """
    n = len(array)

    if n == 0:
        return array

    count = [0] * 95

    for char in array:
        count[ord(char) - 32] += 1

    index = 0
    for i in range(95):
        frequency = count[i]
        for _ in range(frequency):
            array[index] = chr(i + 32)
            index += 1

    return array


if __name__ == "__main__":
    import doctest
    doctest.testmod()
