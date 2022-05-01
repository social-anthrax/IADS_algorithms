# Anonymous ArRay 2022 02 08

import numpy as np


def edit_distance(s: str, t: str):  # s : 1 to m -> 0 to m-1, t : 1 to n -> 0 to n-1
    m = len(s)
    n = len(t)

    # d = [[0 for j in range(n+1)] for i in range(m+1)]
    # a = [[0 for j in range(n+1)] for i in range(m+1)]
    d = np.ndarray((m + 1, n + 1)).astype(np.int64)
    a = np.ndarray((m + 1, n + 1)).astype(np.int64)
    # d = [ [0] * (n+1) for i in range(0,m+1) ]
    # a = [ [0] * (n+1) for i in range(0,m+1) ]

    for j in range(0, n + 1):
        d[0][j] = j
        a[0][j] = 2

    for i in range(0, m + 1):
        d[i][0] = i
        a[0][j] = 3

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s[i - 1] == t[j - 1]:
                d[i][j] = d[i - 1][j - 1]
                a[i][j] = 0
            else:
                d[i][j] = 1 + min(d[i][j - 1], d[i - 1][j], d[i - 1][j - 1])
                if d[i][j] == d[i - 1][j - 1] + 1:
                    a[i][j] = 1
                elif d[i][j] == d[i][j - 1] + 1:
                    a[i][j] = 2
                else:
                    a[i][j] = 3

    print("s1 : " + s)
    print("s2 : " + t)

    reconstruct_rec(s, t, a)
    # b,c = reconstruct(s,t,a)
    # print(b)
    # print(c)

def edit_distance_traced(s: str, t: str):  # s : 1 to m -> 0 to m-1, t : 1 to n -> 0 to n-1
    m = len(s)
    n = len(t)

    # d = [[0 for j in range(n+1)] for i in range(m+1)]
    # a = [[0 for j in range(n+1)] for i in range(m+1)]
    # d = np.ndarray((m + 1, n + 1)).astype(np.int64)
    # a = np.ndarray((m + 1, n + 1)).astype(np.int64)
    d = np.zeros((m + 1, n + 1)).astype(np.int64)
    a = np.zeros((m + 1, n + 1)).astype(np.int64)
    # d = [ [0] * (n+1) for i in range(0,m+1) ]
    # a = [ [0] * (n+1) for i in range(0,m+1) ]

    print("d", d)
    print("a", a)

    for j in range(0, n + 1):
        d[0][j] = j
        a[0][j] = 2
    
    for i in range(0, m + 1):
        d[i][0] = i
        a[0][n] = 3 # changed j to n

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s[i - 1] == t[j - 1]:
                d[i][j] = d[i - 1][j - 1]
                a[i][j] = 0
            else:
                d[i][j] = 1 + min(d[i][j - 1], d[i - 1][j], d[i - 1][j - 1])
                if d[i][j] == d[i - 1][j - 1] + 1:
                    a[i][j] = 1
                elif d[i][j] == d[i][j - 1] + 1:
                    a[i][j] = 2
                else:
                    a[i][j] = 3
            print("d", d)
            print("a", a)
            print("\n\n\n")

    print("s1 : " + s)
    print("s2 : " + t)

    reconstruct_rec(s, t, a)
    # b,c = reconstruct(s,t,a)
    # print(b)
    # print(c)


def reconstruct(s: str, t: str, a: np.ndarray):  # not working, fuck recursion
    b = ""
    c = ""
    m = len(s)
    n = len(t)

    for i in reversed(range(0, m)):
        if i == 0:
            c += t[:j]
            return b, c
        for j in reversed(range(0, n)):
            if j == 0:
                b += s[:i]
                return b, c

            if a[i][j] == 0 or a[i][j] == 1:
                b += s[i]
                c += t[j]
                i -= 1
                j -= 1
            elif a[i][j] == 2:
                b += "-"
                c += t[j]
                j -= 1
            elif a[i][j] == 3:
                b += s[i]
                c += "-"
                i -= 1


def reconstruct_rec(s: str, t: str, a: list):  # from editdist_sol.py
    def alignS(i, j):
        if (i == 0) and (j == 0):
            return ""
        elif i == 0:
            return alignS(i, j - 1) + "-"
        elif j == 0:
            return s[0:i]
        elif (a[i][j] == 0) or (a[i][j] == 1):
            return alignS(i - 1, j - 1) + s[i - 1]
        elif a[i][j] == 2:
            return alignS(i, j - 1) + "-"
        else:
            return alignS(i - 1, j) + s[i - 1]

    def alignT(i, j):
        if (i == 0) and (j == 0):
            return ""
        elif i == 0:
            return t[0:j]
        elif j == 0:
            return alignT(i - 1, j) + "-"
        elif (a[i][j] == 0) or (a[i][j] == 1):
            return alignT(i - 1, j - 1) + t[j - 1]
        elif a[i][j] == 2:
            return alignT(i, j - 1) + t[j - 1]
        else:
            return alignT(i - 1, j) + "-"

    m = len(s)
    n = len(t)
    ss = alignS(m, n)
    tt = alignT(m, n)

    print("s1 : " + ss)
    print("s2 : " + tt)


if __name__ == "__main__":
    # edit_distance("ACCGGTATCCTAGGAC", "ACCTATCT--TAGGAC")
    # edit_distance_traced("ACCGGTATCCTAGGAC", "ACCTATCT--TAGGAC")
    # edit_distance("ABCDE", "BCDED")
    # edit_distance_traced("ABCDE", "BCDED")
    # edit_distance("ACTGGT", "ATGGCT")
    edit_distance_traced("ACTGGT", "ATGGCT")
