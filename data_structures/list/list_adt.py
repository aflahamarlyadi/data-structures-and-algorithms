"""
List Abstract Data Type Implementation

This module contains an implementation of a List Abstract Data Type.

Author: Aflah Hanif Amarlyadi
Date: 2024-09-12
License: MIT
"""

from abc import ABC, abstractmethod
from typing import TypeVar, Generic

T = TypeVar('T')


class ListADT(ABC, Generic[T]):
    """
    An abstract base class for the List Abstract Data Type.

    Attributes:
        length (int): The number of items in the list.
    """

    def __init__(self) -> None:
        """
        Initialises an empty list.
        """
        self.length = 0

    @abstractmethod
    def __setitem__(self, index: int, item: T) -> None:
        """
        Sets the item at the specified index.

        Args:
            index (int): The index at which to set the item.
            item (T): The item to set at the specified index.
        """
        pass

    @abstractmethod
    def __getitem__(self, index: int) -> T:
        """
        Gets the item at the specified index.

        Args:
            index (int): The index from which to retrieve the item.

        Returns:
            T: The item at the specified index.
        """
        pass

    def append(self, item: T) -> None:
        """
        Appends an item to the end of the list.

        Args:
            item (T): The item to append to the list.
        """
        self.insert(len(self), item)

    @abstractmethod
    def insert(self, index: int, item: T) -> None:
        """
        Inserts an item to the list at the specified index.

        Args:
            index (int): The index at which to insert the item.
            item (T): The item to insert to the list.
        """
        pass

    def remove(self, item: T) -> None:
        """
        Removes the first occurrence of the specified item from the list.

        Args:
            item (T): The item to remove from the list.
        """
        index = self.index(item)
        self.pop(index)

    @abstractmethod
    def pop(self, index: int = None) -> T:
        """
        Removes the item at the specified index from the list.
        If the index is not specified, the last item will be removed.

        Args:
            index (int): The index of the item to remove. Default is None.

        Returns:
            T: The item that was removed.
        """
        pass

    @abstractmethod
    def index(self, item: T) -> int:
        """
        Returns the index of the first occurrence of the specified item in the list.

        Args:
            item (T): The item to find the index of.

        Returns:
            int: The index of the item in the list.
        """
        pass

    @abstractmethod
    def is_full(self) -> bool:
        """
        Checks if the list is full.

        Returns:
            bool: True if the list is full, otherwise False.
        """
        pass

    def is_empty(self) -> bool:
        """
        Checks if the list is empty.

        Returns:
            bool: True if the list is empty, otherwise False.
        """
        return len(self) == 0

    def clear(self) -> None:
        """
        Clears the list.
        """
        self.length = 0

    def __len__(self) -> int:
        """
        Returns the number of items in the list.

        Returns:
            int: The length of the list.
        """
        return self.length

    def __str__(self) -> str:
        """
        Returns a string representation of the list.

        Returns:
            str: A string showing the items of the list.
        """
        return "[" + ", ".join([str(self[i]) for i in range(len(self))]) + "]"
