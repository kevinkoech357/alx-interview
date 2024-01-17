#!/usr/bin/python3

"""
This file contains a function that attempts to
find the minimum operations needed to perform a specified task.
"""


def minOperations(n: int) -> int:
    """
    Use the concept of prime factorization to determine the minimum
    number of operations needed to achieve exactly n H characters.
    """
    if n <= 1:
        return 0

    def prime_factors(n):
        i = 2
        factors = []
        while i * i <= n:
            if n % i:
                i += 1
            else:
                n //= i
                factors.append(i)
        if n > 1:
            factors.append(n)
        return factors

    factors = prime_factors(n)

    if not factors:
        return 0

    operations = 0
    for factor in factors:
        operations += factor

    return operations
