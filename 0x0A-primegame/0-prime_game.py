#!/usr/bin/python3

"""
Find the winner in a competition of
removing prime nums and their multiples.
"""


def isWinner(x, nums):
    maria_wins = 0
    ben_wins = 0

    for n in nums:
        primes = [True] * (n + 1)
        primes[0] = primes[1] = False

        for i in range(2, int(n**0.5) + 1):
            if primes[i]:
                for j in range(i * i, n + 1, i):
                    primes[j] = False

        remaining = [i for i in range(2, n + 1) if primes[i]]

        if not remaining:
            ben_wins += 1
        else:
            player = True
            while remaining:
                if player:
                    prime = remaining[0]
                    for i in range(prime, n + 1, prime):
                        if i in remaining:
                            remaining.remove(i)
                    player = False
                else:
                    if not remaining:
                        maria_wins += 1
                        break
                    prime = remaining[0]
                    for i in range(prime, n + 1, prime):
                        if i in remaining:
                            remaining.remove(i)
                    player = True
            if not player:
                ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
