#!/usr/bin/python3

"""
This file contains a function that creates
a pascal's triangle
"""


def pascal_triangle(n):
    """
    Creates pascals triangle.
    """
    results = []

    if n <= 0:
        return {}

    for _ in range(n):
        row = [1]
        if results:
            last_row = results[-1]
            row.extend([sum(pair) for pair in zip(last_row, last_row[1:])])
            row.append(1)
        results.append(row)
    return results
