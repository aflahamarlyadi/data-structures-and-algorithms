"""
Stack Abstract Data Type Implementation

This module contains an implementation of a Stack Abstract Data Type.

Author: Aflah Hanif Amarlyadi
Date: 2024-09-25
License: MIT
"""

from abc import ABC, abstractmethod
from typing import TypeVar, Generic

T = TypeVar('T')


class StackADT(ABC, Generic[T]):
    """
    An abstract base class for the Stack Abstract Data Type.

    Attributes:
        length (int): The current number of items in the stack.
    """

    def __init__(self) -> None:
        """
        Initialises an empty stack.
        """
        self.length = 0

    @abstractmethod
    def push(self, item: T) -> None:
        """
        Pushes an item to the top of the stack.

        Args:
            item (T): The item to add to the stack.
        """
        pass

    @abstractmethod
    def pop(self) -> T:
        """
        Pops the item at the top of the stack.

        Returns:
            T: The item removed from the top of the stack.
        """
        pass

    @abstractmethod
    def peek(self) -> T:
        """
        Returns the item at the top of the stack without popping it.

        Returns:
            T: The item at the top of the stack.
        """
        pass

    def clear(self) -> None:
        """
        Clears the stack.
        """
        self.length = 0

    @abstractmethod
    def is_full(self) -> bool:
        """
        Checks if the stack is full.

        Returns:
            bool: True if the stack is full, otherwise False.
        """
        pass

    def is_empty(self) -> bool:
        """
        Checks if the stack is empty.

        Returns:
            bool: True if the stack is empty, otherwise False.
        """
        return len(self) == 0

    def __len__(self) -> int:
        """
        Returns the number of items in the stack.

        Returns:
            int: The number of items in the stack.
        """
        return self.length
