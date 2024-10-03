#!/usr/bin/python3


def sieve_of_eratosthenes(limit):
    primes = [True] * (limit + 1)
    primes[0] = primes[1] = False
    for i in range(2, int(limit ** 0.5) + 1):
        if primes[i]:
            for j in range(i * i, limit + 1, i):
                primes[j] = False
    return [i for i in range(2, limit + 1) if primes[i]]


def isWinner(x, nums):
    # Precompute prime numbers up to the maximum possible value of n
    max_n = max(nums)
    primes = sieve_of_eratosthenes(max_n)

    maria_wins, ben_wins = 0, 0

    for n in nums:
        available_nums = list(range(1, n + 1))
        primes_in_range = [p for p in primes if p <= n]
        current_player = 0  # Maria starts

        while primes_in_range:
            prime = primes_in_range.pop(0)
            available_nums = [num for num in available_nums
                              if num % prime != 0]
            primes_in_range = [p for p in primes_in_range
                               if p in available_nums]
            current_player = 1 - current_player

        if current_player == 0:
            ben_wins += 1
        else:
            maria_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
