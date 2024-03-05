#!/usr/bin/python3

"""
Define a function that returns the perimeter
of the island described in grid.
"""


from typing import List


def island_perimeter(grid: List[int]) -> int:
    """
    0 represents water
    1 represents land
    Each cell is square, with a side length of 1

    Returns perimeter of island described in grid.
    """
    perimeter = 0

    if not grid:
        return 0

    rows = len(grid)
    cols = len(grid[0])

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                perimeter += 4

                # Check left side
                if j > 0 and grid[i][j - 1] == 1:
                    perimeter -= 2

                # Check top side
                if i > 0 and grid[i - 1][j] == 1:
                    perimeter -= 2

    return perimeter
