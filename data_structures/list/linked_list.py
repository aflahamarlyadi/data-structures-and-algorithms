"""
Linked List Data Structure Implementation

This module contains an implementation of a Linked List data structure.

Author: Aflah Hanif Amarlyadi
Date: 2024-09-12
License: MIT
"""

from __future__ import annotations
from typing import TypeVar, Generic
from data_structures.list.list_adt import ListADT

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


class LinkedListIterator(Generic[T]):
    """
    An iterator for the linked list.

    Attributes:
        current (Node[T]): The current node in the iteration.
    """

    def __init__(self, node: Node[T]) -> None:
        """
        Initializes the linked list iterator.

        Args:
            node (Node[T]): The starting node of the iteration.
        """
        self.current = node

    def __iter__(self) -> LinkedListIterator[T]:
        """
        Returns the iterator object.

        Returns:
            LinkedListIterator[T]: The iterator object itself.
        """
        return self

    def __next__(self) -> T:
        """
        Returns the next item in the iteration.

        Returns:
            T: The data of the current node.

        Raises:
            StopIteration: If the iteration has reached the end of the list.
        """
        if self.current is None:
            raise StopIteration

        item = self.current.data
        self.current = self.current.link
        return item


class LinkedList(ListADT[T]):
    """
    A singly linked list implementation.

    Attributes:
        head (Node[T]): The head node of the list.
    """

    def __init__(self) -> None:
        """
        Initialises an empty linked list.
        """
        super().__init__()
        self.head = None

    def __iter__(self) -> LinkedListIterator[T]:
        """
        Returns an iterator for the linked list.

        Returns:
            LinkedListIterator[T]: An iterator for the linked list.
        """
        return LinkedListIterator(self.head)

    def __setitem__(self, index: int, item: T) -> None:
        """
        Sets the item at the specified index.

        Args:
            index (int): The index at which to set the item.
            item (T): The item to set at the specified index.

        Raises:
            IndexError: If the index is out of range.

        Time Complexity:
            O(index)
        """
        node_at_index = self._get_node(index)
        node_at_index.data = item

    def __getitem__(self, index: int) -> T:
        """
        Gets the item at the specified index.

        Args:
            index (int): The index of the item to retrieve.

        Returns:
            T: The item at the specified index.

        Raises:
            IndexError: If the index is out of range.

        Time Complexity:
            O(index)
        """
        node_at_index = self._get_node(index)
        return node_at_index.data

    def _get_node(self, index: int) -> Node[T]:
        """
        Gets the node at the specified index.

        Args:
            index (int): The index of the node to retrieve.

        Returns:
            Node[T]: The node at the specified index.

        Raises:
            IndexError: If the index is out of range.

        Time Complexity:
            O(index)
        """
        if index < 0:
            index += len(self)

        if index < 0 or index >= len(self):
            raise IndexError("Index out of range")

        current = self.head
        for _ in range(index):
            current = current.link
        return current

    def insert(self, index: int, item: T) -> None:
        """
        Inserts an item to the list at the specified index.

        Args:
            index (int): The index at which to insert the item.
            item (T): The item to insert to the list.

        Raises:
            IndexError: If the index is out of range.

        Time Complexity:
            O(index)
        """
        new_node = Node(item)

        if index == 0:
            new_node.link = self.head
            self.head = new_node
        else:
            previous_node = self._get_node(index - 1)
            new_node.link = previous_node.link
            previous_node.link = new_node

        self.length += 1

    def pop(self, index: int = None) -> T:
        """
        Removes the item at the specified index from the list.
        If the index is not specified, the last item will be removed.

        Args:
            index (int): The index of the item to remove. Default is None.

        Returns:
            T: The item that was removed from the list.

        Raises:
            IndexError: If the index is out of bounds.
            ValueError: If the list is empty.

        Time Complexity:
            Best Case: O(1)
            Worst Case: O(n)
        """
        index = len(self) - 1 if index is None else index

        if index < 0 or index >= len(self):
            raise IndexError("Index out of bounds")

        if self.is_empty():
            raise ValueError("List is empty")
        elif index == 0:
            item = self.head.data
            self.head = self.head.link
        else:
            previous_node = self._get_node(index - 1)
            item = previous_node.link.data
            previous_node.link = previous_node.link.link

        self.length -= 1
        return item

    def index(self, item: T) -> int:
        """
        Returns the index of the first occurrence of the specified item in the list.

        Args:
            item (T): The item to find the index of.

        Returns:
            int: The index of the item in the list.

        Raises:
            ValueError: If the item is not in the list.

        Time Complexity:
            O(n)
        """
        current = self.head
        index = 0

        while current is not None and current.data != item:
            current = current.link
            index += 1

        if current is None:
            raise ValueError(f"{item} is not in list")
        else:
            return index

    def is_full(self) -> bool:
        """
        Checks if the list is full.

        Returns:
            bool: False.

        Time Complexity:
            O(1)
        """
        return False

    def clear(self) -> None:
        """
        Clears the list.

        Time Complexity:
            O(1)
        """
        super().clear()
        self.head = None

    def __contains__(self, item: T) -> bool:
        """
        Checks if the list contains the specified item.

        Args:
            item (T): The item to check for.

        Returns:
            bool: True if the item is in the list, otherwise False.

        Time Complexity:
            O(n)
        """
        current = self.head
        while current is not None:
            if current.data == item:
                return True
            current = current.link
        return False
