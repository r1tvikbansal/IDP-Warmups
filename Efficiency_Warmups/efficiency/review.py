# find primes up to n
# add a timer
# graph time as n grows (use lesson code or numpy)
# provide the graphing code
# guess at what O() is and do theoretical guess as well
# do they match up

import pandas as pd
import random
from time_graph import TimeGraph


def limit_list_to_range_fast(n):
    # generate a random list of size n
    # then, create a range that grows linearly with n
    items = [random.randrange(0, 1000000) for n in range(n)]
    low = 0
    high = 100 * n
    list_to_range_fast(items, low, high)


def limit_list_to_range_slow(n):
    # generate a random list of size n
    # then, use a range of that grows linearly with n
    items = [random.randrange(0, 1000000) for n in range(n)]
    low = 0
    high = 100 * n
    list_to_range_slow(items, low, high)


def get_species_count_fns():
    """
    Create a closure that loads the data set that is
    held in memory for subsequent calls to run_species_count methods.
    We do it this way so that we don't have to continually reload the data
    or use a global.
    """
    data = pd.read_csv("pokemon_expanded.csv").to_dict("records")

    def species_count_set(n):
        rows = min(n // 100, len(data))
        df = data[0:rows]
        return get_species_count_set(df)

    def species_count_list(n):
        rows = min(n // 100, len(data))
        df = data[0:rows]
        return get_species_count_list(df)

    return species_count_set, species_count_list


def get_list_slow(n):
    result = []
    for num in range(1, n):
        result.insert(0, num)
    return result


def get_list_med(n):
    result = []
    for num in range(n - 1, 0, -1):
        result.append(num)
    return result


def get_list_fast(n):
    return [num for num in range(n - 1, 0, -1)]


def get_sum(n):
    sum = 0
    for i in range(n):
        for j in range(n):
            sum += j
    return sum


def list_to_range_slow(items, low, high):
    return [n for n in range(low, high) if n in items]


def list_to_range_fast(items, low, high):
    return [n for n in items if n >= low and n < high]


def get_species_count_set(data):
    """
    From HW3: species_count returns the number of unique Pokemon
    species (determined by the name attribute) found in
    the dataset. The data is a list of dictionaries.
    """
    unique = set()
    for pokemon in data:
        unique.add(pokemon["name"])

    return len(unique)


def get_species_count_list(data):
    """
    Use a list solution to demonstrate slower performance than a set
    """
    unique = []
    for pokemon in data:
        if pokemon["name"] not in unique:
            unique.append(pokemon["name"])


def time_and_graph_stuff(timer):
    timer.time_and_graph(get_list_slow, max_iters=8)
    timer.time_and_graph(get_list_med, max_iters=16)
    timer.time_and_graph(get_list_fast, max_iters=18)

    # data only has 3000 rows so can't run 3000 * 100 as max n 300,000
    species_set, species_list = get_species_count_fns()
    timer.time_and_graph(species_set, max_iters=13)
    timer.time_and_graph(species_list, max_iters=13)

    timer.time_and_graph(get_sum, max_iters=7)
    timer.time_and_graph(limit_list_to_range_fast, max_iters=14)
    timer.time_and_graph(limit_list_to_range_slow, max_iters=4)


if __name__ == "__main__":
    # run this next line once to get the graphs, then comment it out
    timer = TimeGraph()
    time_and_graph_stuff(timer)
