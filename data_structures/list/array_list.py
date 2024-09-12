"""
Array List Data Structure Implementation

This module contains an implementation of an Array List data structure.

Author: Aflah Hanif Amarlyadi
Date: 2024-09-12
License: MIT
"""

from typing import TypeVar
from data_structures.list.list_adt import ListADT
from data_structures.array.referential_array import ReferentialArray

T = TypeVar('T')


class ArrayList(ListADT[T]):
    """
    A list implementation using an array.

    Attributes:
        MIN_CAPACITY (int): The minimum capacity of the list.
        array (ReferentialArray[T]): The array storing the items of the list.
    """
    MIN_CAPACITY = 1

    def __init__(self, max_capacity: int) -> None:
        """
        Initialises an empty list with the given maximum capacity.

        Args:
            max_capacity (int): The maximum capacity of the list. If less than MIN_CAPACITY, the list's capacity will
            be set to MIN_CAPACITY.
        """
        super().__init__()
        self.array = ReferentialArray(max(self.MIN_CAPACITY, max_capacity))

    def __setitem__(self, index: int, item: T) -> None:
        """
        Sets the item at the specified index.

        Args:
            index (int): The index at which to set the item.
            item (T): The item to set at the specified index.

        Time Complexity:
            O(1)
        """
        if index < 0:
            index += len(self)

        if index < 0 or index >= len(self):
            raise IndexError("Index out of range")

        self.array[index] = item

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

    def insert(self, index: int, item: T) -> None:
        """
        Inserts an item to the list at the specified index.

        Args:
            index (int): The index at which to insert the item.
            item (T): The item to insert to the list.

        Raises:
            Exception: If the list is full.

        Time Complexity:
            O(index)
            + O(n) - occurs when resizing the array is needed, O(1) amortised.
        """
        if index < 0:
            index += len(self)

        if index < 0:
            index = 0
        elif index > len(self):
            index = len(self)

        if self.is_full():
            # Resize array
            new_array = ReferentialArray(2 * len(self.array))
            for i in range(len(self)):
                new_array[i] = self.array[i]
            self.array = new_array

        # Shuffle right
        for i in range(len(self), index, -1):
            self.array[i] = self.array[i - 1]

        self.array[index] = item
        self.length += 1

    def pop(self, index: int = None) -> T:
        """
        Removes the item at the specified index from the list.
        If the index is not specified, the last item will be removed.

        Args:
            index (int): The index of the item to remove. Default is None.

        Returns:
            T: The item that was removed from the list.

        Raises:
            IndexError: If the index is out of range.

        Time Complexity:
            O(index)
        """
        index = len(self)-1 if index is None else index

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
        Returns the index of the first occurrence of the specified item in the list.

        Args:
            item (T): The item to find the index of.

        Returns:
            int: The index of the item in the list.

        Raises:
            ValueError: If the item is not in the list.

        Time Complexity:
            O(n)
        """
        for i in range(len(self)):
            if item == self[i]:
                return i

        raise ValueError(f"{item} is not in list")

    def is_full(self) -> bool:
        """
        Checks if the list is full.

        Returns:
            bool: True if the list is full, otherwise False.

        Time Complexity:
            O(1)
        """
        return len(self) >= len(self.array)

    def __contains__(self, item: T) -> bool:
        """
        Checks if the list contains the specified item.

        Args:
            item (T): The item to check for.

        Returns:
            bool: True if the item is in the list, otherwise False.

        Time Complexity:
            O(n)
        """
        for i in range(len(self)):
            if self.array[i] == item:
                return True
        return False
