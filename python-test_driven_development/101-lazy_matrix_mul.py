#!/usr/bin/python3
"""This module defines lazy_matrix_mul, which multiplies with NumPy."""
import numpy


def lazy_matrix_mul(m_a, m_b):
    """Return the product of the matrices m_a and m_b using NumPy."""
    return numpy.matmul(m_a, m_b)
