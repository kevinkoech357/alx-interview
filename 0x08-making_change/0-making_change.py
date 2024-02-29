#!/usr/bin/python3

"""
Define a greedy algorithm that determines
the fewest number of coins
needed to sum up to total.
"""


def makeChange(coins, total):
    """
    Return: fewest number of coins needed to meet total
    """
    if total <= 0:
        return

    coins.sort(reverse=True)

    coin_count = 0
    N = total

    for coin in coins:
        while N >= coin:
            N -= coin
            coin_count += 1

        if N == 0:
            break

    if N != 0:
        return -1

    return coin_count
