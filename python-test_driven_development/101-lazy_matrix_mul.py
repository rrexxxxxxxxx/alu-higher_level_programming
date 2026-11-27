#!/usr/bin/python3
"""This module defines lazy_matrix_mul, which multiplies with NumPy."""
import numpy


def lazy_matrix_mul(m_a, m_b):
    """Check m_a and m_b, then return their product computed by NumPy."""
    for name, m in (("m_a", m_a), ("m_b", m_b)):
        if not isinstance(m, list):
            raise TypeError("{} must be a list".format(name))
        if not all(isinstance(row, list) for row in m):
            raise TypeError("{} must be a list of lists".format(name))
    for name, m in (("m_a", m_a), ("m_b", m_b)):
        if m == [] or m == [[]]:
            raise ValueError("{} can't be empty".format(name))
    for name, m in (("m_a", m_a), ("m_b", m_b)):
        for row in m:
            for x in row:
                if type(x) not in (int, float):
                    raise TypeError("{} should contain only integers or "
                                    "floats".format(name))
    for name, m in (("m_a", m_a), ("m_b", m_b)):
        if any(len(row) != len(m[0]) for row in m):
            raise TypeError("each row of {} must should be of the same "
                            "size".format(name))
    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")
    return numpy.matmul(m_a, m_b)
