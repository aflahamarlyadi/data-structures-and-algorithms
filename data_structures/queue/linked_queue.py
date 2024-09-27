"""
Linked Queue Data Structure Implementation

This module contains an implementation of an Linked Queue data structure.

Author: Aflah Hanif Amarlyadi
Date: 2024-09-27
License: MIT
"""

from typing import Generic, TypeVar
from data_structures.queue.queue_adt import QueueADT

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


class LinkedQueue(QueueADT[T]):
    """
    A queue implementation using a singly linked list.

    Attributes:
        front (Node): The front of the queue.
        rear (Node): The rear of the queue.
    """
    def __init__(self) -> None:
        """
        Initialises an empty linked queue.
        """
        super().__init__()
        self.front = None
        self.rear = None

    def enqueue(self, item: T) -> None:
        """
        Adds an item to the rear of the queue.

        Args:
            item (T): The item to add to the rear of the queue.

        Time Complexity:
            O(1)
        """
        new_node = Node(item)

        if self.is_empty():
            self.front = new_node
        else:
            self.rear.link = new_node

        self.rear = new_node
        self.length += 1

    def dequeue(self) -> T:
        """
        Removes and returns the item at the front of the queue.

        Returns:
            T: The item removed from the front of the queue.

        Raises:
            Exception: If the queue is empty.

        Time Complexity:
            O(1)
        """
        if self.is_empty():
            raise Exception("Queue is empty")

        item = self.front.data
        self.front = self.front.link
        self.length -= 1

        if self.is_empty():
            self.rear = None

        return item

    def peek(self) -> T:
        """
        Returns the item at the front of the queue without removing it.

        Returns:
            T: The item at the front of the queue.

        Raises:
            Exception: If the queue is empty.

        Time Complexity:
            O(1)
        """
        if self.is_empty():
            raise Exception("Queue is empty")

        return

    def clear(self) -> None:
        """
        Clears the queue.

        Time Complexity:
            O(1)
        """
        super().clear()
        self.front = None
        self.rear = None

    def is_full(self) -> bool:
        """
        Checks if the queue is full.

        Returns:
            bool: False.

        Time Complexity:
            O(1)
        """
        return False

    def is_empty(self) -> bool:
        """
        Checks if the queue is empty.

        Returns:
            bool: True if the queue is empty, otherwise False.

        Time Complexity:
            O(1)
        """
        return self.front is None

    def __str__(self) -> str:
        """
        Returns a string representation of the queue.

        Returns:
            str: A string showing the items in the queue from front to rear.
        """
        items = []
        current = self.front

        while current is not None:
            items.append(str(current.data))
            current = current.link

        return "[" + ", ".join(items) + "]"
