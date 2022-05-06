import pprint


def viterbi(
    obs: "list[int]",
    states: "list[int]",
    start_p: "list[list[float]]",
    trans_p: "list[list[float]]",
    emit_p: "list[list[float]]",
) -> "list[int]":
    """
    params:
        obs: observed sentence. Passed as a list of indices referring to the language.
        states: list of possible states
        start_p: list of probabilities for each start state
        trans_p: 2d array representing the transmition matrix
        emit_p: 2d array representing the emition matrix
    """

    n = len(obs)
    # initialise our most likely path and table for reverse lookup.
    mlp = [[None for _ in range(0, len(states))] for _ in range(0, len(obs))]
    prev = [[None for _ in range(0, len(states))] for _ in range(0, len(obs))]

    # initialise our base cases
    for state in states:
        mlp[0][state] = start_p[state] * emit_p[state][obs[0]]
        prev[0][state] = -1

    # calculate the transition costs.
    for i in range(1, n):
        for state in states:
            mlp[i][state] = 0
            prev[i][state] = -1
            for state_star in states:
                # Transition cost holds the probability of transitioning
                # from state_star to state multiplied by the probability of the observation
                transition_cost = trans_p[state_star][state] * emit_p[state][obs[i]]
                if transition_cost * mlp[i - 1][state_star] > mlp[i][state]:
                    mlp[i][state] = transition_cost * mlp[i - 1][state_star]
                    prev[i][state] = state_star

    backtrack_states = [max(enumerate(mlp[n - 1]), key=lambda x: x[1])[0]]
    for i in range(n - 1, 0, -1):
        prev_node = prev[i][backtrack_states[0]]
        backtrack_states = [prev_node] + backtrack_states

    # # Uncomment to return max probability
    # for state in states:
    #     if mlp[n, state] > max:
    #         max = mlp[n, state]

    return backtrack_states


def viterbi_traced(
    obs: "list[int]",
    states: "list[int]",
    start_p: "list[list[float]]",
    trans_p: "list[list[float]]",
    emit_p: "list[list[float]]",
) -> "list[int]":
    """
    params:
        obs: observed sentence. Passed as a list of indices referring to the language.
        states: list of possible states
        start_p: list of probabilities for each start state
        trans_p: 2d array representing the transmition matrix
        emit_p: 2d array representing the emition matrix
    """

    print("Start:")
    pp = pprint.PrettyPrinter(indent=2)

    n = len(obs)
    # initialise our most likely path and table for reverse lookup.
    mlp = [[None for _ in range(0, len(states))] for _ in range(0, len(obs))]
    prev = [[None for _ in range(0, len(states))] for _ in range(0, len(obs))]

    # initialise our base cases
    for state in states:
        mlp[0][state] = start_p[state] * emit_p[state][obs[0]]
        prev[0][state] = -1

    print("mlp")
    pp.pprint(mlp)
    print("prev")
    pp.pprint(prev)

    print("loop")
    # calculate the transition costs.
    for i in range(1, n):
        for state in states:
            mlp[i][state] = 0
            prev[i][state] = -1
            for state_star in states:
                # Transition cost holds the probability of transitioning
                # from state_star to state multiplied by the probability of the observation
                transition_cost = trans_p[state_star][state] * emit_p[state][obs[i]]
                if transition_cost * mlp[i - 1][state_star] > mlp[i][state]:
                    mlp[i][state] = transition_cost * mlp[i - 1][state_star]
                    prev[i][state] = state_star
                print("mlp")
                pp.pprint(mlp)
                print("prev")
                pp.pprint(prev)

    backtrack_states = [max(enumerate(mlp[n - 1]), key=lambda x: x[1])[0]]
    for i in range(n - 1, 0, -1):
        prev_node = prev[i][backtrack_states[0]]
        backtrack_states = [prev_node] + backtrack_states

    # # Uncomment to return max probability
    # for state in states:
    #     if mlp[n, state] > max:
    #         max = mlp[n, state]

    return backtrack_states


if __name__ == "__main__":
    state_names = ["DT", "N", "V", "Adj"]
    state_indices = list(range(0, len(state_names)))
    sentence = "The old man the lifeboats"
    language = ["lifeboats", "man", "old", "the", "other"]
    trans_p = [
        [0, 0.6, 0, 0.4],
        [0.05, 0.3, 0.4, 0.25],
        [0.4, 0.3, 0.1, 0.2],
        [0.1, 0.5, 0.2, 0.2],
    ]

    emit_p = [
        [0, 0, 0, 0.5, 0.5],
        [0.2, 0.3, 0.2, 0, 0.3],
        [0, 0.1, 0, 0, 0.9],
        [0, 0, 0.4, 0, 0.6],
    ]

    start_p = [0.4, 0.3, 0.2, 0.1]

    indices = []
    for word in sentence.lower().split(" "):
        indices.append(language.index(word))

    # as viterbi returns a list of indices, we need to convert it to a list of words
    grammar = []
    for i in viterbi_traced(indices, state_indices, start_p, trans_p, emit_p):
        grammar.append(state_names[i])
    print(grammar)
