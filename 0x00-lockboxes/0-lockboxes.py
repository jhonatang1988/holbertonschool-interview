#!/usr/bin/env python3
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
            if boxes[i][j] > i:
                visited.append(boxes[i][j])

    if max(visited) == len(boxes) - 1:
        return True
    else:
        return False
