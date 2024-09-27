"""
Queue Abstract Data Type Implementation

This module contains an implementation of a Queue Abstract Data Type.

Author: Aflah Hanif Amarlyadi
Date: 2024-09-27
License: MIT
"""

from abc import ABC, abstractmethod
from typing import TypeVar, Generic

T = TypeVar('T')


class QueueADT(ABC, Generic[T]):
    """
    An abstract base class for the Queue Abstract Data Type.

    Attributes:
        length (int): The current number of items in the queue.
    """

    def __init__(self) -> None:
        """
        Initialises an empty queue.
        """
        self.length = 0

    @abstractmethod
    def enqueue(self, item: T) -> None:
        """
        Adds an item to the rear of the queue.

        Args:
            item (T): The item to be added to the queue.
        """
        pass

    @abstractmethod
    def dequeue(self) -> T:
        """
        Removes and returns the item at the front of the queue.

        Returns:
            T: The item removed from the front of the queue.
        """
        pass

    @abstractmethod
    def peek(self) -> T:
        """
        Returns the item at the front of the queue without removing it.

        Returns:
            T: The item at the front of the queue.
        """
        pass

    def clear(self) -> None:
        """
        Clears the queue.
        """
        self.length = 0

    @abstractmethod
    def is_full(self) -> bool:
        """
        Checks if the queue is full.

        Returns:
            bool: True if the queue is full, otherwise False.
        """
        pass

    def is_empty(self) -> bool:
        """
        Checks if the queue is empty.

        Returns:
            bool: True if the queue is empty, otherwise False.
        """
        return len(self) == 0

    def __len__(self) -> int:
        """
        Returns the number of items in the queue.

        Returns:
            int: The number of items in the queue.
        """
        return self.length
