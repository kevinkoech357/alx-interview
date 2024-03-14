#!/usr/bin/python3

"""
Find the winner in a competition of
removing prime nums and their multiples.
"""


def isWinner(x, nums):
    """
    Return name of the winner.
    """

    if not nums or x < 1:
        return None

    def generate_primes(n):
        primes = [True] * (n + 1)
        primes[0], primes[1] = False, False
        for i in range(2, int(n**0.5) + 1):
            if primes[i]:
                for j in range(i * i, n + 1, i):
                    primes[j] = False
        return [i for i in range(2, n + 1) if primes[i]]

    # Function to determine the winner for each round
    def determine_winner(n):
        primes = generate_primes(n)
        if not primes:
            return "Ben"
        if n in primes:
            return "Maria" if len(primes) % 2 == 0 else "Ben"
        return "Maria"

    # Count the number of wins for each player
    maria_wins = 0
    ben_wins = 0
    for n in nums:
        winner = determine_winner(n)
        if winner == "Maria":
            maria_wins += 1
        else:
            ben_wins += 1

    # Determine the overall winner
    if maria_wins == ben_wins:
        return None
    elif maria_wins > ben_wins:
        return "Maria"
    else:
        return "Ben"
