"""
Linear Queue Data Structure Implementation

This module contains an implementation of an Linear Queue data structure.

Author: Aflah Hanif Amarlyadi
Date: 2024-09-27
License: MIT
"""

from typing import TypeVar
from data_structures.queue.queue_adt import QueueADT
from data_structures.array.referential_array import ReferentialArray

T = TypeVar('T')


class LinearQueue(QueueADT[T]):
    """
    A linear queue implementation using an array.

    Attributes:
        MIN_CAPACITY (int): The minimum capacity of the queue.
        front (int): The index of the item at the front of the queue.
        rear (int): The index of the first empty space at the rear of the queue.
        array (ReferentialArray[T]): The array storing the items of the queue.
    """
    MIN_CAPACITY = 1

    def __init__(self, max_capacity: int) -> None:
        """
        Initialises an empty linear queue with the given maximum capacity.

        Args:
            max_capacity (int): The maximum capacity of the queue. If less than MIN_CAPACITY, the queue's capacity will
            be set to MIN_CAPACITY.
        """
        super().__init__()
        self.front = 0
        self.rear = 0
        self.array = ReferentialArray(max(self.MIN_CAPACITY, max_capacity))

    def enqueue(self, item: T) -> None:
        """
        Adds an item to the rear of the queue.

        Args:
            item (T): The item to add to the rear of the queue.

        Raises:
            Exception: If the queue is full.

        Time Complexity:
            O(1)
        """
        if self.is_full():
            raise Exception("Queue is full")

        self.array[self.rear] = item
        self.length += 1
        self.rear += 1

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

        self.length -= 1
        item = self.array[self.front]
        self.front += 1
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

        return self.array[self.front]

    def clear(self) -> None:
        """
        Clears the queue.

        Time Complexity:
            O(1)
        """
        super().clear()
        self.front = 0
        self.rear = 0

    def is_full(self) -> bool:
        """
        Checks if the queue is full.

        Returns:
            bool: True if the queue is full, otherwise False.

        Time Complexity:
            O(1)
        """
        return self.rear == len(self.array)

    def __str__(self) -> str:
        """
        Returns a string representation of the queue.

        Returns:
            str: A string showing the items in the queue from front to rear.
        """
        return "[" + ", ".join(str(self.array[i]) for i in range(self.front, self.rear)) + "]"
