"""
Set Abstract Data Type Implementation

This module contains an implementation of a Set Abstract Data Type.

Author: Aflah Hanif Amarlyadi
Date: 2024-09-12
License: MIT
"""

from __future__ import annotations
from abc import ABC, abstractmethod
from typing import TypeVar, Generic

T = TypeVar('T')


class SetADT(ABC, Generic[T]):
    """
    An abstract base class for the Set Abstract Data Type.
    """

    @abstractmethod
    def add(self, item: T) -> None:
        """
        Adds an item to the set.

        Args:
            item (T): The item to be added to the set.
        """
        pass

    @abstractmethod
    def remove(self, item: T) -> None:
        """
        Removes an item from the set.

        Args:
            item (T): The item to be removed from the set.
        """
        pass

    @abstractmethod
    def union(self, other: SetADT[T]) -> SetADT[T]:
        """
        Returns a new set that is the union of this set and another set.

        Args:
            other (SetADT[T]): The other set to perform the union with.

        Returns:
            SetADT[T]: A new set that contains all unique elements from both sets.
        """
        pass

    @abstractmethod
    def intersection(self, other: SetADT[T]) -> SetADT[T]:
        """
        Returns a new set that is the intersection of this set and another set.

        Args:
            other (SetADT[T]): The other set to perform the intersection with.

        Returns:
            SetADT[T]: A new set that contains only the elements that are in both sets.
        """
        pass

    @abstractmethod
    def difference(self, other: SetADT[T]) -> SetADT[T]:
        """
        Returns a new set that is the difference of this set and another set.

        Args:
            other (SetADT[T]): The other set to perform the difference with.

        Returns:
            SetADT[T]: A new set that contains the elements that are in this set but not in the other set.
        """
        pass

    @abstractmethod
    def clear(self) -> None:
        """
        Clears the set.
        """
        pass

    @abstractmethod
    def is_empty(self) -> bool:
        """
        Checks if the set is empty.

        Returns:
            bool: True if the set is empty, otherwise False.
        """
        pass

    @abstractmethod
    def __len__(self) -> int:
        """
        Returns the number of items in the set.

        Returns:
            int: The number of items in the set.
        """
        pass

    @abstractmethod
    def __contains__(self, item: T) -> bool:
        """
        Checks if the set contains the specified item.

        Args:
            item (T): The item to check for.

        Returns:
            bool: True if the item is in the set, otherwise False.
        """
        pass
