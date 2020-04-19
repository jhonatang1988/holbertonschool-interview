#!/usr/bin/python3
"""
check if all lockboxes can be access
"""


def canUnlockAll(boxes):
    """
    main
    """
    visited = []
    for i in range(len(boxes)):
        for j in range(len(boxes[i])):
            if i < boxes[i][j] < len(boxes):
                visited.append(boxes[i][j])
        if len(boxes[i]) == 0 and i == len(boxes) - 1:
            visited.append(0)
    if len(visited) == len(boxes):
        return True
    else:
        return False
