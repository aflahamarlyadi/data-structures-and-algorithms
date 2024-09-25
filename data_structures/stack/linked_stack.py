"""
Linked Stack Data Structure Implementation

This module contains an implementation of a Linked Stack data structure.

Author: Aflah Hanif Amarlyadi
Date: 2024-09-25
License: MIT
"""

from typing import Generic, TypeVar
from data_structures.stack.stack_adt import StackADT

T = TypeVar('T')


class Node(Generic[T]):
    """
    A node in a singly linked list.

    Attributes:
        data (T): The data stored in the node.
        link (Node[T]): A reference to the next node in the list.
    """

    def __init__(self, data: T = None) -> None:
        """
        Initialises a node with the given data.

        Args:
            data (T): The data to store in the node. Defaults to None.
        """
        self.data = data
        self.link = None


class LinkedStack(StackADT[T]):
    """
    A stack implementation using a singly linked list.

    Attributes:
        top (Node[T]): The top node of the stack.
    """

    def __init__(self) -> None:
        """
        Initialises an empty linked stack.
        """
        super().__init__()
        self.top = None

    def push(self, item: T) -> None:
        """
        Pushes an item onto the top of the stack.

        Args:
            item (T): The item to add to the stack.

        Time Complexity:
            O(1)
        """
        new_node = Node(item)
        new_node.link = self.top
        self.top = new_node
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

        item = self.top.data
        self.top = self.top.link
        self.length -= 1
        return item

    def peek(self) -> T:
        """
        Returns the item at the top of the stack without removing it.

        Returns:
            T: The item at the top of the stack.

        Raises:
            Exception: If the stack is empty.

        Time Complexity:
            O(1)
        """
        if self.is_empty():
            raise Exception("Stack is empty")

        return self.top.data

    def clear(self) -> None:
        """
        Clears the stack.

        Time Complexity:
            O(1)
        """
        super().clear()
        self.top = None

    def is_full(self) -> bool:
        """
        Checks if the stack is full.

        Returns:
            bool: False.

        Time Complexity:
            O(1)
        """
        return False

    def is_empty(self) -> bool:
        """
        Checks if the stack is empty.

        Returns:
            bool: True if the stack is empty, otherwise False.

        Time Complexity:
            O(1)
        """
        return self.top is None

    def __str__(self) -> str:
        """
        Returns a string representation of the stack.

        Returns:
            str: A string showing the items in the stack from top to bottom.
        """
        items = []
        current_node = self.top

        while current_node is not None:
            items.append(str(current_node.data))
            current_node = current_node.link

        return "[" + ", ".join(items) + "]"
