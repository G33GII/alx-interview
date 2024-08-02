#!/usr/bin/python3
"""
This module provides a function to determine if all boxes can be unlocked.

The main function `canUnlockAll` checks if all
boxes in a list of lists can be
unlocked starting from the first box.
"""


def canUnlockAll(boxes):
    """
    Determines if all boxes can be unlocked.

    Args:
        boxes (list of lists): A list where each element is a
        list containing keys to other boxes.

    Returns:
        bool: True if all boxes can be unlocked, False otherwise.
    """
    n = len(boxes)
    unlocked = set([0])  # Start with the first box unlocked
    keys = set(boxes[0])  # Keys from the first box

    while keys:
        new_key = keys.pop()
        if new_key < n and new_key not in unlocked:
            unlocked.add(new_key)
            keys.update(boxes[new_key])

    return len(unlocked) == n
