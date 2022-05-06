import pprint


def vertical_seam_carving(energies: "list[list[int]]", width: int, height: int):
    history = [[0 for i in range(width)] for j in range(height)]
    dp = energies

    # Start from second last row and iterate upwards
    for i in range(height - 2, -1, -1):
        for j in range(width):
            predecessors = []

            # if position is at the left edge
            if j == 0:
                predecessors = [
                    (dp[i + 1][j], (i + 1, j)),
                    (dp[i + 1][j + 1], (i + 1, j + 1)),
                ]
            # if position is at the right edge
            elif j == len(dp[0]) - 1:
                predecessors = [
                    (dp[i + 1][j], (i + 1, j)),
                    (dp[i + 1][j - 1], (i + 1, j - 1)),
                ]
            # if position is in the middle
            else:
                predecessors = [
                    (dp[i + 1][j - 1], (i + 1, j - 1)),
                    (dp[i + 1][j], (i + 1, j)),
                    (dp[i + 1][j + 1], (i + 1, j + 1)),
                ]

            dp[i][j] += min(predecessors)[0]
            # Link the current position to the predecessor with the lowest energy
            history[i][j] = min(predecessors)[1]

    # Initialise a trail array to reconstruct the path
    trail = [[0 for i in range(width)] for j in range(height)]

    end_point = dp[0].index(min(dp[0]))
    trail[0][end_point] = 1
    path = history[0][end_point]

    # Iterate through the predecessors in the history array and mark optimal path with 1
    while type(path) == tuple:
        i, j = path
        trail[i][j] = 1
        path = history[i][j]

    print("Best Vertical Seam:")
    for row in trail:
        print(row)
    print("")


def vertical_seam_carving_traced(energies: "list[list[int]]", width: int, height: int):
    pp = pprint.PrettyPrinter(indent=2)

    print("Start:")
    history = [[0 for i in range(width)] for j in range(height)]
    print("history")
    pp.pprint(history)
    dp = energies
    print("dp")
    pp.pprint(dp)

    print("start loop")
    # Start from second last row and iterate upwards
    for i in range(height - 2, -1, -1):
        for j in range(width):
            predecessors = []

            # if position is at the left edge
            if j == 0:
                predecessors = [
                    (dp[i + 1][j], (i + 1, j)),
                    (dp[i + 1][j + 1], (i + 1, j + 1)),
                ]
            # if position is at the right edge
            elif j == len(dp[0]) - 1:
                predecessors = [
                    (dp[i + 1][j], (i + 1, j)),
                    (dp[i + 1][j - 1], (i + 1, j - 1)),
                ]
            # if position is in the middle
            else:
                predecessors = [
                    (dp[i + 1][j - 1], (i + 1, j - 1)),
                    (dp[i + 1][j], (i + 1, j)),
                    (dp[i + 1][j + 1], (i + 1, j + 1)),
                ]

            dp[i][j] += min(predecessors)[0]
            print("dp")
            pp.pprint(dp)
            # Link the current position to the predecessor with the lowest energy
            history[i][j] = min(predecessors)[1]
            print("history")
            pp.pprint(history)

    # Initialise a trail array to reconstruct the path
    trail = [[0 for i in range(width)] for j in range(height)]

    end_point = dp[0].index(min(dp[0]))
    trail[0][end_point] = 1
    path = history[0][end_point]

    # Iterate through the predecessors in the history array and mark optimal path with 1
    while type(path) == tuple:
        i, j = path
        trail[i][j] = 1
        path = history[i][j]

    print("Best Vertical Seam:")
    for row in trail:
        print(row)
    print("")


def horizontal_seam_carving(energies: "list[list[int]]", width: int, height: int):
    history = [[0 for i in range(width)] for j in range(height)]
    dp = energies

    # Start from second last column and iterate upwards
    for i in range(width - 2, -1, -1):
        for j in range(height):
            predecessors = []
            # if position is at the top edge
            if j == 0:
                predecessors = [
                    (dp[j][i + 1], (j, i + 1)),
                    (dp[j + 1][i + 1], (j + 1, i + 1)),
                ]
            # if position is at the bottom edge
            elif j == height - 1:
                predecessors = [
                    (dp[j][i + 1], (j, i + 1)),
                    (dp[j - 1][i + 1], (j - 1, i + 1)),
                ]
            # if position is in the middle
            else:
                predecessors = [
                    (dp[j][i + 1], (j, i + 1)),
                    (dp[j - 1][i + 1], (j - 1, i + 1)),
                    (dp[j + 1][i + 1], (j + 1, i + 1)),
                ]

            dp[j][i] += min(predecessors)[0]
            # Link the current position to the predecessor with the lowest energy
            history[j][i] = min(predecessors)[1]

    # Initialise a trail array to reconstruct the path
    trail = [[0 for i in range(width)] for j in range(height)]

    smallest_exit = min([row[0] for row in dp])
    end_point = [row[0] for row in dp].index(smallest_exit)
    trail[end_point][0] = 1
    path = history[end_point][0]

    # Iterate through the predecessors in the history array and mark optimal path with 1
    while type(path) == tuple:
        i, j = path
        trail[i][j] = 1
        path = history[i][j]

    print("Best Horizontal Seam:")
    for row in trail:
        print(row)
    print("")


def horizontal_seam_carving_traced(
    energies: "list[list[int]]", width: int, height: int
):
    pp = pprint.PrettyPrinter(indent=2)

    print("Start:")
    history = [[0 for i in range(width)] for j in range(height)]
    print("history")
    pp.pprint(history)
    dp = energies
    print("dp")
    pp.pprint(dp)

    # Start from second last column and iterate upwards
    for i in range(width - 2, -1, -1):
        for j in range(height):
            predecessors = []
            # if position is at the top edge
            if j == 0:
                predecessors = [
                    (dp[j][i + 1], (j, i + 1)),
                    (dp[j + 1][i + 1], (j + 1, i + 1)),
                ]
            # if position is at the bottom edge
            elif j == height - 1:
                predecessors = [
                    (dp[j][i + 1], (j, i + 1)),
                    (dp[j - 1][i + 1], (j - 1, i + 1)),
                ]
            # if position is in the middle
            else:
                predecessors = [
                    (dp[j][i + 1], (j, i + 1)),
                    (dp[j - 1][i + 1], (j - 1, i + 1)),
                    (dp[j + 1][i + 1], (j + 1, i + 1)),
                ]

            dp[j][i] += min(predecessors)[0]
            print("dp")
            pp.pprint(dp)
            # Link the current position to the predecessor with the lowest energy
            history[j][i] = min(predecessors)[1]
            print("history")
            pp.pprint(history)

    # Initialise a trail array to reconstruct the path
    trail = [[0 for i in range(width)] for j in range(height)]

    smallest_exit = min([row[0] for row in dp])
    end_point = [row[0] for row in dp].index(smallest_exit)
    trail[end_point][0] = 1
    path = history[end_point][0]

    # Iterate through the predecessors in the history array and mark optimal path with 1
    while type(path) == tuple:
        i, j = path
        trail[i][j] = 1
        path = history[i][j]

    print("Best Horizontal Seam:")
    for row in trail:
        print(row)
    print("")


# Example.
if __name__ == "__main__":
    energies = [
        [0, 75, 6, 3, 75],
        [3, 0, 75, 75, 75],
        [75, 75, 0, 2, 75],
        [-50, 1, 1, 0, -5],
        [75, 4, 75, 2, 7],
    ]
    vertical_seam_carving_traced(energies, len(energies[0]), len(energies))
    horizontal_seam_carving_traced(energies, len(energies[0]), len(energies))
