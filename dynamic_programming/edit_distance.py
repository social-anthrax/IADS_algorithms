# Anonymous ArRay 2022 02 08
# Artemis Livingstone 2022 05 06


def prettyPrint(a: list[list]):
    for i in a:
        print(i)


def edit_distance(s: str, t: str):  # s : 1 to m -> 0 to m-1, t : 1 to n -> 0 to n-1
    m = len(s)
    n = len(t)

    d = [[-1 for _ in range(n + 1)] for _ in range(m + 1)]
    a = [[-1 for _ in range(n + 1)] for _ in range(m + 1)]

    for i in range(0, m + 1):
        d[i][0] = i
        a[i][0] = 3

    for j in range(0, n + 1):
        d[0][j] = j
        a[0][j] = 2

    # put marker to allow for easier reconstruction. - is used in the textbook
    a[0][0] = -1

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s[i - 1] == t[j - 1]:  # as strings are zero indexed
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

    print("d:")
    prettyPrint(d)
    print("")
    print("a:")
    prettyPrint(a)

    b, c, distance = reconstruct(s, t, a)
    print(f"b: {b}")
    print(f"c: {c}")
    print(f"Edit distance: {distance}")


def reconstruct(s: str, t: str, a: list[list]):
    b = ""
    c = ""
    i = len(s)
    j = len(t)

    marker = a[i][j]
    distance = 0
    while marker != -1:
        if marker == 0 or marker == 1:
            b += s[i - 1]
            c += t[j - 1]
            i -= 1
            j -= 1
            if marker == 1:
                distance += 1
        elif marker == 2:
            b += "-"
            c += t[j - 1]
            j -= 1
            distance += 1
        elif marker == 3:
            b += s[i - 1]
            c += "-"
            i -= 1
            distance += 1
        else:
            assert False

        marker = a[i][j]

    return (b[::-1], c[::-1], distance)


if __name__ == "__main__":
    # edit_distance("ACCGGTATCCTAGGAC", "ACCTATCT--TAGGAC")
    # edit_distance_traced("ACCGGTATCCTAGGAC", "ACCTATCT--TAGGAC")
    # edit_distance("ABCDE", "BCDED")
    # edit_distance_traced("ABCDE", "BCDED")
    # edit_distance("ACTGGT", "ATGGCT")
    import sys

    if len(sys.argv) != 3:
        print("Run with edit_distance.py string1 string2")

    edit_distance(sys.argv[1], sys.argv[2])
