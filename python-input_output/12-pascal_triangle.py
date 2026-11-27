#!/usr/bin/python3
"""This module defines pascal_triangle."""


def pascal_triangle(n):
    """Return a list of lists of integers for Pascal's triangle of n rows.

    Returns an empty list if n <= 0.
    """
    if n <= 0:
        return []
    triangle = [[1]]
    for _ in range(n - 1):
        prev = triangle[-1]
        row = [1]
        for i in range(1, len(prev)):
            row.append(prev[i - 1] + prev[i])
        row.append(1)
        triangle.append(row)
    return triangle
