import builtins; builtins.profile = builtins.__dict__.get('profile', lambda x: x)
from cse163_utils import assert_equals
from time_graph import TimeGraph

@profile
def my_hailstone_seq(n):
    """
    See instructions for more information.

    n = the max n value to include in the result.
    return a dictionary with the key = number, value = length of sequence.
      next = n / 2     if n is even
      next = n * 3 + 1 if n is odd
    End the sequence when n == 1
    """
    # Your implementation goes here
    ans = dict()
    for num in range(1, n + 1):
        nextnum = num
        steps = 1
        while nextnum != 1:
            if nextnum % 2 == 0:
                nextnum = nextnum / 2
            else:
                nextnum = nextnum * 3 + 1
            steps = steps + 1
        ans[num] = steps
    return ans


def dynamic_hailstone_seq(n):
    # Your implementation goes here
    ans = dict()
    for num in range(1, n + 1):
        nextnum = num
        steps = 1
        while nextnum != 1:
            if nextnum in ans:
                steps += ans[nextnum] - 1
                break
            if nextnum % 2 == 0:
                nextnum = nextnum / 2
            else:
                nextnum = nextnum * 3 + 1
            steps += 1
        ans[num] = steps
    return ans


# Test my_get_primes
def test_hailstone():
    fiddy = {1: 1, 2: 2, 3: 8, 4: 3, 5: 6, 6: 9, 7: 17, 8: 4, 9: 20, 10: 7, 11: 15, 12: 10, 13: 10,
             14: 18, 15: 18, 16: 5}
    assert_equals(fiddy, dynamic_hailstone_seq(16))
    print("set_of_hailstone Success")


def graph_prime_performance():
    timer = TimeGraph()
    timer.time_and_graph(dynamic_hailstone_seq)


def main():
    test_hailstone()
    graph_prime_performance()
    # print(webs_get_primes(50))


if __name__ == "__main__":
    main()
