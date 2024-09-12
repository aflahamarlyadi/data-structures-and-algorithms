"""
Array Sorted List Data Structure Implementation

This module contains an implementation of an Array Sorted List data structure.

Author: Aflah Hanif Amarlyadi
Date: 2024-09-12
License: MIT
"""

from typing import TypeVar
from data_structures.list.sorted_list_adt import SortedListADT
from data_structures.array.referential_array import ReferentialArray

T = TypeVar('T')


class ArraySortedList(SortedListADT[T]):
    """
    A sorted list implementation using an array.

    Attributes:
        MIN_CAPACITY (int): The minimum capacity of the sorted list.
        array (ReferentialArray[T]): The array storing the items of the sorted list.
    """
    MIN_CAPACITY = 1

    def __init__(self, max_capacity: int) -> None:
        """
        Initialises an empty sorted list with the given maximum capacity.

        Args:
            max_capacity (int): The maximum capacity of the sorted list. If less than MIN_CAPACITY, the sorted list's
            capacity will be set to MIN_CAPACITY.
        """
        super().__init__()
        self.array = ReferentialArray(max(self.MIN_CAPACITY, max_capacity))

    def __getitem__(self, index: int) -> T:
        """
        Gets the item at the specified index.

        Args:
            index (int): The index of the item to retrieve.

        Returns:
            T: The item at the specified index.

        Time Complexity:
            O(1)
        """
        if index < 0:
            index += len(self)

        if index < 0 or index >= len(self):
            raise IndexError("Index out of range")

        return self.array[index]

    def _binary_search(self, item: T) -> int:
        """
        Searches for the specified item in a sorted list using the Binary Search algorithm.

        Args:
            item (T): The item to search in the sorted list.

        Returns:
            int: The index of the item.

        Time Complexity:
            O(log n)
        """
        low = 0
        high = len(self) - 1

        while low <= high:
            mid = low + (high - low) // 2
            if self[mid] == item:
                return mid
            elif self[mid] < item:
                low = mid + 1
            else:
                high = mid - 1

        return low

    def add(self, item: T) -> None:
        """
        """
        if self.is_full():
            # Resize array
            new_array = ReferentialArray(2 * len(self.array))
            for i in range(len(self)):
                new_array[i] = self.array[i]
            self.array = new_array

        index = self._binary_search(item)

        for i in range(len(self), index, -1):
            self.array[i] = self.array[i - 1]

        self.array[index] = item

        self.length += 1

    def pop(self, index: int = None) -> T:
        """
        Removes the item at the specified index from the sorted list.
        If the index is not specified, the last item will be removed.

        Args:
            index (int): The index of the item to remove. Default is None.

        Returns:
            T: The item that was removed from the sorted list.

        Raises:
            IndexError: If the index is out of range.
        """
        index = len(self) - 1 if index is None else index

        if index < 0 or index >= len(self):
            raise IndexError("Index out of range")

        item = self.array[index]
        self.length -= 1

        # Shuffle left
        for i in range(index, len(self)):
            self.array[i] = self.array[i + 1]

        return item

    def index(self, item: T) -> int:
        """
        Returns the index of the specified item in the sorted list.

        Args:
            item (T): The item to find the index of.

        Returns:
            int: The index of the item in the sorted list.

        Raises:
            ValueError: If the item is not in the list.

        Time Complexity:
            O(log n)
        """
        index = self._binary_search(item)

        if index < len(self) and self[index] == item:
            return index

        raise ValueError(f"{item} not in list")

    def is_full(self) -> bool:
        """
        Checks if the sorted list is full.

        Returns:
            bool: True if the sorted list is full, otherwise False.

        Time Complexity:
            O(1)
        """
        return len(self) >= len(self.array)

    def __contains__(self, item: T) -> bool:
        """
        Checks if the sorted list contains the specified item.

        Args:
            item (T): The item to check for.

        Returns:
            bool: True if the item is in the sorted list, otherwise False.

        Time Complexity:
            O(n)
        """
        for i in range(len(self)):
            if self.array[i] == item:
                return True
        return False
