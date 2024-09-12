"""
Referential Array Data Structure Implementation

This module contains an implementation of a Referential Array data structure.

Author: Aflah Hanif Amarlyadi
Date: 2024-09-12
License: MIT
"""

from ctypes import py_object
from typing import TypeVar, Generic

T = TypeVar('T')


class ReferentialArray(Generic[T]):
    """
    A fixed-size array that stores references to objects.
    """
    def __init__(self, length: int) -> None:
        """
        Initialise the array with a given length.

        Args:
            length (int): The length of the array.

        Raises:
            ValueError: If the length is less than or equal to 0.
        """
        if length <= 0:
            raise ValueError("Array length should be larger than 0.")
        self.array = (length * py_object)()
        self.array[:] = [None for _ in range(length)]

    def __len__(self) -> int:
        """
        Get the length of the array.

        Returns:
            int: The length of the array.
        """
        return len(self.array)

    def __getitem__(self, index: int) -> T:
        """
        Get the item at the given index.

        Args:
            index (int): The index of the item.

        Returns:
            T: The item at the given index.

        Raises:
            IndexError: If the index is out of bounds (handled by Python).
        """
        return self.array[index]

    def __setitem__(self, index: int, value: T) -> None:
        """
        Set the item at the given index.

        Args:
            index (int): The index where the value should be set.
            value (T): The value to set at the given index.

        Raises:
            IndexError: If the index is out of bounds (handled by Python).
        """
        self.array[index] = value
