from cse163_utils import assert_equals
from time_graph import TimeGraph
import numpy as np
import math


# Step 1A: Implement my_get_primes.
def my_get_primes(max):
    """
    Return a set of all the prime numbers lower than max. (max is exclusive)
    """
    # Your implementation goes here
    primes = []
    for n in range(2, max):
        factor = False
        for i in range(1, n):
            if n % i == 0 and (i != 1) and (i != n):
                factor = True
        if not factor:
            primes.append(n)
    return primes


def sieve_get_primes(max):
    """
    Return a set of all the prime numbers lower than max. (max is exclusive)

    Implement using the Sieve of Eratosthenes. See Instructions.
    """
    # Your implementation goes here
    primes = [True] * max
    indexer = 2
    while indexer * indexer <= max:
        if primes[indexer]:
            for i in range(indexer * indexer, max, indexer):
                primes[i] = False
        indexer += 1

    allprime = []
    for num in range(2, max):
        if primes[num]:
            allprime.append(num)

    return allprime


def webs_get_primes(bound):
    """
    Return a set of all the prime numbers lower than max. (max is exclusive)
    Put a "plagiarized" implementation here. Find it yourself!
    """
    #
    sieve = np.ones(bound, dtype=bool)  # default all prime
    sieve[:2] = False  # 0, 1 is not prime

    sqrt_bound = math.ceil(math.sqrt(bound))

    for i in range(2, sqrt_bound):
        if sieve[i]:
            inc = i if i == 2 else 2 * i
            sieve[i * i:bound:inc] = False

    return np.arange(bound)[sieve]


# Test my_get_primes
def test_set_of_primes():
    fiddy = {2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47}
    assert_equals(fiddy, sieve_get_primes(50))
    print("set_of_primes Success")


def graph_prime_performance():
    timer = TimeGraph()
    timer.time_and_graph(webs_get_primes)


def main():
    # once your implementation of getting primes is complete,
    # graph its performance
    # test_set_of_primes()
    graph_prime_performance()
    # print(webs_get_primes(50))


if __name__ == "__main__":
    main()
