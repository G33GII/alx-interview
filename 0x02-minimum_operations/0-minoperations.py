#!/usr/bin/python3
"""
Main file for testing
"""


def prime_factors(n):
    """
    Helper function to calculate prime factors of n.

    :param n: Number to factorize
    :return: List of prime factors
    """
    factors = []
    factor = 2
    while factor * factor <= n:
        while n % factor == 0:
            factors.append(factor)
            n //= factor
        factor += 1
    if n > 1:
        factors.append(n)
    return factors


def minOperations(n):
    """
    Calculates the fewest number of operations needed to
    result in exactly n H characters.

    :param n: Target number of H characters
    :return: Minimum number of operations, or 0 if n is impossible to achieve
    """
    if n <= 1:
        return 0

    factors = prime_factors(n)
    return sum(factors)
