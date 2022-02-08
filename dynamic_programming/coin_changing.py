# File: coin_changing.py
# COIN CHANGING PROBLEMS.

import sys
import time

sys.setrecursionlimit(1000000)

# Some coin systems:

lecture_coins = [1, 5, 7]

sterling_coins = [1, 2, 5, 10, 20, 50, 100, 200]


# Problem (1): Minimum number of coins (as in Lecture 17).

c_list = sterling_coins  # global variable, can set as desired


# Plain recursive implementation.
# fewest_coins should be implemented recursively, returning just smallest number of coins.


def fewest_coins(v: int) -> int:
    if v in c_list:
        return 1
    return 1 + min(fewest_coins(v - c_i) for c_i in c_list if c_i < v)


# slightly different method which returns a list of actual coins (which constitute a
# minimum-sized solution).


def fewest_coins_list(v: int) -> "list[int]":
    if v in c_list:
        return [v]
    return min(
        ([c_i] + fewest_coins_list(v - c_i) for c_i in c_list if c_i < v), key=len
    )


# Memoization operation, exactly as in our lecture:


def memoize(f):
    memo = {}

    def check(v):
        if v not in memo:
            memo[v] = f(v)
        return memo[v]

    return check


# memoize : (int->int) -> (int->int)
# f : int->int,  check : int->int

# To get the optimization of the recursion:

#   fewest_coins = memoize(fewest_coins)
#   fewest_coins_list = memoize(fewest_coins_list)

# NB. Can't change c_list after doing this!
# We would need to reload the file within the Python interpreter to use with new c_list.

# You should also implement and experiment with a dynamic programming solution,
# as given towards the end of slide-set 17.


INF = 1_000_000_000


def fewest_coins_dp(v):
    k = len(c_list)
    c = c_list  #
    C = [INF for _ in range(v + 1)]
    P = [INF for _ in range(v + 1)]
    C[0] = 0
    for w in range(1, v + 1):
        for i in range(1, k):
            if c[i] <= w and (C[w - c[i]] + 1) < C[w]:
                C[w] = 1 + C[w - c[i]]
                P[w] = i
    return C[v]


def fewest_coins_list_dp(v):
    k = len(c_list)
    c = c_list
    S = [0 for _ in range(k)]
    C = [INF for _ in range(v + 1)]
    P = [INF for _ in range(v + 1)]
    C[0] = 0
    for w in range(1, v + 1):
        for i in range(k):
            if c[i] <= w and (C[w - c[i]] + 1) < C[w]:
                C[w] = 1 + C[w - c[i]]
                P[w] = i
    temp = v  # stores the quantity
    while v > 0:
        i = P[v]
        S[i] = S[i] + 1
        v = v - c[i]
    return S


if __name__ == "__main__":
    small_target = 50
    medium_target = 2_500
    target = 10_000_000
    start = time.time()
    sol = fewest_coins(small_target)
    print(f"naive counting {small_target} takes {time.time() - start:.2f} seconds.")
    print(f" ==> {sol} coins are needed.")
    # start = time.time()
    # print(fewest_coins_list(small_target))
    # print(f"naive listing {small_target} takes {time.time() - start:.2f} seconds.")

    fewest_coins = memoize(fewest_coins)
    # fewest_coins_list = memoize(fewest_coins_list)

    start = time.time()
    sol = fewest_coins(medium_target)
    print(f"memoised counting {medium_target} takes {time.time() - start:.2f} seconds.")
    print(f" ==> {sol} coins are needed.")
    # start = time.time()
    # print(fewest_coins_list(medium_target))
    # print(f"memoised listing {medium_target} takes {time.time() - start:.2f} seconds.")

    start = time.time()
    sol = fewest_coins_dp(target)
    print(
        f"dynamic programming counting {target} takes {time.time() - start:.2f} seconds."
    )
    print(f" ==> {sol} coins are needed.")
    # start = time.time()
    # print(fewest_coins_list_dp(target))
    # print(f"dynamic programming listing {target} takes {time.time() - start:.2f} seconds.")
