#!/usr/bin/python3

"""
Define a function that determines if all the
boxes can be opened.
"""


def canUnlockAll(boxes):
    """
    Determine if all locked boxes can be opened.
    """
    n = len(boxes)

    # List to keep track of the unlocked status of each box
    unlocked = [False] * n
    unlocked[0] = True  # The first box is initially unlocked

    # List to keep track of keys found during the process
    keys_found = [0]

    # Set to keep track of visited boxes
    visited = set()
    visited.add(0)

    while keys_found:
        current_key = keys_found.pop()

        # Check if the current key opens any new boxes
        for key in boxes[current_key]:
            if key not in visited:
                visited.add(key)
                unlocked[key] = True
                keys_found.append(key)

    # Check if all boxes are unlocked
    return all(unlocked)
