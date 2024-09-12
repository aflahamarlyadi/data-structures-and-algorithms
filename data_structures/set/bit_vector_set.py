"""
Bit Vector Set Data Structure Implementation

This module contains an implementation of a Bit Vector Set data structure.

Author: Aflah Hanif Amarlyadi
Date: 2024-09-12
License: MIT
"""

from __future__ import annotations
from typing import TypeVar
from data_structures.set.set_adt import SetADT

T = TypeVar('T')


class BitVectorSet(SetADT[int]):
    """
    A set implementation using a bit vector to store integers.

    This class provides a space-efficient way to represent a set of non-negative integers using a bit vector.
    Each bit in the bit vector represents the presence or absence of an integer in the set.

    Attributes:
        bit_vector (int): An integer used as a bit vector to store set elements.
    """

    def __init__(self) -> None:
        """
        Initializes an empty set.
        """
        super().__init__()
        self.bit_vector = 0

    def add(self, item: int) -> None:
        """
        Adds an item to the set.

        Args:
            item (int): The non-negative integer to add to the set.

        Raises:
            ValueError: If the item is not a non-negative integer.

        Time Complexity:
            O(1)
        """
        if not isinstance(item, int) or item <= 0:
            raise ValueError("Item must be a positive integer.")
        self.bit_vector |= 1 << (item - 1)

    def remove(self, item: int) -> None:
        """
        Removes an item from the set.

        Args:
            item (int): The non-negative integer to remove from the set.

        Raises:
            ValueError: If the item is not a non-negative integer.
            KeyError: If the item is not found in the set.

        Time Complexity:
            O(1)
        """
        if not isinstance(item, int) or item <= 0:
            raise ValueError("Item must be a positive integer")
        if item in self:
            self.bit_vector ^= 1 << (item - 1)
        else:
            raise KeyError(f"{item} is not in the set")

    def union(self, other: BitVectorSet[int]) -> BitVectorSet[int]:
        """
        Returns a new set that is the union of this set and another set.

        Args:
            other (BitVectorSet[int]): The other set to union with.

        Returns:
            BitVectorSet[int]: A new set containing all elements present in either set.

        Time Complexity:
            O(1)
        """
        union = BitVectorSet()
        union.bit_vector = self.bit_vector | other.bit_vector
        return union

    def intersection(self, other: BitVectorSet[int]) -> BitVectorSet[int]:
        """
        Returns a new set that is the intersection of this set and another set.

        Args:
            other (BitVectorSet[int]): The other set to intersect with.

        Returns:
            BitVectorSet[int]: A new set containing only the elements present in both sets.

        Time Complexity:
            O(1)
        """
        intersection = BitVectorSet()
        intersection.bit_vector = self.bit_vector & other.bit_vector
        return intersection

    def difference(self, other: BitVectorSet[int]) -> BitVectorSet[int]:
        """
        Returns a new set that is the difference of this set and another set.

        Args:
            other (BitVectorSet[int]): The other set to differentiate with.

        Returns:
            BitVectorSet[int]: A new set containing elements present in this set but not in the other set.

        Time Complexity:
            O(1)
        """
        difference = BitVectorSet()
        difference.bit_vector = self.bit_vector & ~other.bit_vector
        return difference

    def clear(self) -> None:
        """
        Removes all items from the set.

        Time Complexity:
            O(1)
        """
        self.bit_vector = 0

    def is_empty(self) -> bool:
        """
        Checks if the set is empty.

        Returns:
            bool: True if the set is empty, otherwise False.

        Time Complexity:
            O(1)
        """
        return self.bit_vector == 0

    def __len__(self) -> int:
        """
        Returns the number of items in the set.

        Returns:
            int: The number of items in the set.

        Time Complexity:
            O(n), where n is the number of bits in the bit vector.
        """
        return bin(self.bit_vector).count('1')

    def __contains__(self, item: int) -> bool:
        """
        Checks if the set contains the specified item.

        Args:
            item (int): The non-negative integer to check for.

        Returns:
            bool: True if the item is in the set, otherwise False.

        Time Complexity:
            O(1)
        """
        if not isinstance(item, int) or item <= 0:
            return False
        return (self.bit_vector & (1 << (item - 1))) != 0

    def __str__(self) -> str:
        """
        Returns a string representation of the set.

        Returns:
            str: A string representation of the set elements.

        Time Complexity:
            O(n), where n is the number of bits in the bit vector.
        """
        elements = [str(i + 1) for i in range(self.bit_vector.bit_length()) if self.bit_vector & (1 << i)]
        return "{" + ", ".join(elements) + "}"
