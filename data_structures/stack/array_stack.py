"""
Array Stack Data Structure Implementation

This module contains an implementation of an Array Stack data structure.

Author: Aflah Hanif Amarlyadi
Date: 2024-09-25
License: MIT
"""

from typing import TypeVar
from data_structures.stack.stack_adt import StackADT
from data_structures.array.referential_array import ReferentialArray

T = TypeVar('T')


class ArrayStack(StackADT[T]):
    """
    A stack implementation using an array.

    Attributes:
        MIN_CAPACITY (int): The minimum capacity of the stack.
        array (ReferentialArray[T]): The array storing the items of the stack.
    """

    MIN_CAPACITY = 1

    def __init__(self, max_capacity: int) -> None:
        """
        Initialises an empty stack with the given maximum capacity.

        Args:
            max_capacity (int): The maximum capacity of the stack. If less than MIN_CAPACITY, the stack's capacity will
            be set to MIN_CAPACITY.
        """
        super().__init__()
        self.array = ReferentialArray(max(self.MIN_CAPACITY, max_capacity))

    def push(self, item: T) -> None:
        """
        Pushes an item to the top of the stack.

        Args:
            item (T): The item to add to the stack.

        Raises:
            Exception: If the stack is full.

        Time Complexity:
            O(1)
        """
        if self.is_full():
            raise Exception("Stack is full")

        self.array[len(self)] = item
        self.length += 1

    def pop(self) -> T:
        """
        Pops the item at the top of the stack.

        Returns:
            T: The item removed from the top of the stack.

        Raises:
            Exception: If the stack is empty.

        Time Complexity:
            O(1)
        """
        if self.is_empty():
            raise Exception("Stack is empty")

        self.length -= 1
        return self.array[self.length]

    def peek(self) -> T:
        """
        Returns the item at the top of the stack without popping it.

        Returns:
            T: The item at the top of the stack.

        Raises:
            Exception: If the stack is empty.

        Time Complexity:
            O(1)
        """
        if self.is_empty():
            raise Exception("Stack is empty")

        return self.array[self.length - 1]

    def is_full(self) -> bool:
        """
        Checks if the stack is full.

        Returns:
            bool: True if the stack is full, otherwise False.

        Time Complexity:
            O(1)
        """
        return len(self) == len(self.array)

    def __str__(self) -> str:
        """
        Returns a string representation of the stack.

        Returns:
            str: A string showing the items in the stack from top to bottom.
        """
        return "[" + ", ".join(str(self.array[i]) for i in range(len(self) - 1, -1, -1)) + "]"
