from cse163_utils import assert_equals
from time_graph import TimeGraph


# Step 1A: Implement my_get_primes.
def my_get_primes(max):
    """
    Return a set of all the prime numbers lower than max. (max is exclusive)
    """
    # Your implementation goes here
    return {2, 3, 5, 7}


def sieve_get_primes(max):
    """
    Return a set of all the prime numbers lower than max. (max is exclusive)

    Implement using the Sieve of Eratosthenes. See Instructions.
    """
    # Your implementation goes here
    return {2, 3, 5, 7}


def webs_get_primes(max):
    """
    Return a set of all the prime numbers lower than max. (max is exclusive)
    Put a "plagiarized" implementation here. Find it yourself!
    """
    #
    return {2, 3, 5, 7}


# Test my_get_primes
def test_set_of_primes():
    fiddy = {2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47}
    assert_equals(fiddy, my_get_primes(50))
    print("set_of_primes Success")


def graph_prime_performance():
    timer = TimeGraph()
    timer.time_and_graph(my_get_primes)


def main():
    # once your implementation of getting primes is complete,
    # graph its performance
    test_set_of_primes()
    graph_prime_performance()


if __name__ == "__main__":
    main()
