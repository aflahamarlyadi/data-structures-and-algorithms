"""
Array Set Data Structure Implementation

This module contains an implementation of a Array Set data structure.

Author: Aflah Hanif Amarlyadi
Date: 2024-09-12
License: MIT
"""

from __future__ import annotations
from typing import TypeVar
from data_structures.set.set_adt import SetADT
from data_structures.array.referential_array import ReferentialArray

T = TypeVar('T')


class ArraySet(SetADT[T]):
    """
    A set implementation using an array.

    Attributes:
        MIN_CAPACITY (int): The minimum capacity of the set.
        array (ReferentialArray[T]): The array storing the items of the set.
    """
    MIN_CAPACITY = 1

    def __init__(self, max_capacity: int) -> None:
        """
        Initialises an empty set with the given maximum capacity.

        Args:
            max_capacity (int): The maximum capacity of the set. If less than MIN_CAPACITY, the set's capacity will be
            set to MIN_CAPACITY.
        """
        super().__init__()
        self.length = 0
        self.array = ReferentialArray(max(self.MIN_CAPACITY, max_capacity))

    def add(self, item: T) -> None:
        """
        Adds an item to the set.

        Args:
            item (T): The item to add to the set.

        Raises:
            Exception: If the set is full.

        Time Complexity:
            O(n)
        """
        if self.is_full():
            raise Exception("Set is full")
        if item not in self:
            self.array[self.length] = item
            self.length += 1

    def remove(self, item: T) -> None:
        """
        Removes an item from the set.

        Args:
            item (T): The item to remove from the set.

        Raises:
            KeyError: If the item is not in the set.

        Time Complexity:
            O(n)
        """
        for i in range(self.length):
            if item == self.array[i]:
                self.array[i] = self.array[self.length - 1]
                self.length -= 1
                break
        else:
            KeyError(f"{item} is not in set")

    def union(self, other: ArraySet[T]) -> ArraySet[T]:
        """
        Returns a new set that is the union of this set and another set.

        Args:
            other (ArraySet[T]): The other set to union with.

        Returns:
            ArraySet[T]: A new set containing all unique elements from both sets.

        Time Complexity:
            O(n + m)
        """
        union = ArraySet(len(self.array) + len(other.array))

        for the_set in [self, other]:
            for i in range(len(the_set)):
                union.add(the_set.array[i])

        return union

    def intersection(self, other: ArraySet[T]) -> ArraySet[T]:
        """
        Returns a new set that is the intersection of this set and another set.

        Args:
            other (ArraySet[T]): The other set to intersect with.

        Returns:
            ArraySet[T]: A new set containing only the elements present in both sets.

        Time Complexity:
            O(n * m)
        """
        intersection = ArraySet(min(len(self), len(other)))

        for i in range(len(self)):
            if self.array[i] in other:
                intersection.add(self.array[i])

        return intersection

    def difference(self, other: ArraySet[T]) -> ArraySet[T]:
        """
        Returns a new set that is the difference of this set and another set.

        Args:
            other (ArraySet[T]): The other set to differentiate with.

        Returns:
            ArraySet[T]: A new set containing elements present in this set but not in the other set.

        Time Complexity:
            O(n * m)
        """
        difference = ArraySet(len(self))

        for i in range(len(self)):
            if self.array[i] not in other:
                difference.add(self.array[i])

        return difference

    def is_full(self) -> bool:
        """
        Checks if the set is full.

        Returns:
            bool: True if the set is full, otherwise False.

        Time Complexity:
            O(1)
        """
        return len(self) == len(self.array)

    def clear(self) -> None:
        """
        Clears the set.

        Time Complexity:
            O(1)
        """
        self.length = 0

    def is_empty(self) -> bool:
        """
        Checks if the set is empty.

        Returns:
            bool: True if the set is empty, otherwise False.

        Time Complexity:
            O(1)
        """
        return len(self) == 0

    def __len__(self) -> int:
        """
        Returns the number of items in the set.

        Returns:
            int: The number of items in the set.

        Time Complexity:
            O(1)
        """
        return self.length

    def __contains__(self, item: T) -> bool:
        """
        Checks if the set contains the specified item.

        Args:
            item (T): The item to check for.

        Returns:
            bool: True if the item is in the set, otherwise False.

        Time Complexity:
            O(n)
        """
        for i in range(self.length):
            if item == self.array[i]:
                return True
        return False

    def __str__(self):
        """
        Returns a string representation of the set.

        Returns:
            str: A string showing the items of the set.
        """
        return "{" + ", ".join(str(self.array[i]) for i in range(self.length)) + "}"
