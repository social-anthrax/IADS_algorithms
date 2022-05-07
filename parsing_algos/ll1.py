from typing import List
from queue import LifoQueue
from enum import Enum, auto
import pprint


class LngElem:
    def __init__(self, val, terminal: bool = False):
        self.val = val
        self.terminal = terminal


class Rule:
    def __init__(
        self, LHS: LngElem, RHS: "list[LngElem]", terminal: bool = False
    ):  # different from the CYK version!
        self.LHS = LHS
        self.RHS = RHS
        self.terminal = terminal


def ll1_parse(
    table: "dict[Enum, list[Rule]]", S: Enum, in_str: str, parse_cols: dict
) -> bool:
    terminals = parse_cols
    if S in terminals:
        return Exception("Error: start symbol is terminal")
    pos = 0
    stack = LifoQueue()
    stack.put(S)
    while not stack.empty():
        x = stack.queue[-1]
        if x not in terminals:  # Lookup case
            if table[x][parse_cols[in_str[pos]]] == None:
                return Exception("Error 1: looked up blank cell")
            else:  # rule x -> beta
                stack.get()
                for symbol in reversed(table[x][parse_cols[in_str[pos]]].RHS):
                    stack.put(symbol)
        else:  # Match case (x is terminal)
            if x == in_str[pos]:
                stack.get()
                pos += 1
            else:
                if not x in terminals:
                    return Exception("Error 2: terminal expected", x, "found")
                return Exception("Error 2: expected", x, "found", in_str[pos])
    if in_str[pos] == "$":
        return True
    else:
        return Exception("Error 3: stack empty before string empty")


def ll1_parse_traced(
    table: "dict[Enum, list[Rule]]", S: Enum, in_str: str, parse_cols: dict
) -> bool:
    terminals = parse_cols
    if S in terminals:
        return Exception("Error: start symbol is terminal")
    pos = 0
    stack = LifoQueue()
    stack.put(S)
    while not stack.empty():
        x = stack.queue[-1]
        if x not in terminals:  # Lookup case
            if table[x][parse_cols[in_str[pos]]] == None:
                return Exception("Error 1: looked up blank cell")
            else:  # rule x -> beta
                got = stack.get()
                print(
                    f"Lookup: {in_str[pos]}, {got} => {table[x][parse_cols[in_str[pos]]].RHS}"
                )
                for symbol in reversed(table[x][parse_cols[in_str[pos]]].RHS):
                    stack.put(symbol)
        else:  # Match case (x is terminal)
            if x == in_str[pos]:
                print(f"matched: {stack.get()}")  # removes item from stack
                pos += 1
            else:
                if not x in terminals:
                    return Exception("Error 2: terminal expected", x, "found")
                return Exception("Error 2: expected", x, "found", in_str[pos])
        print(f"input: {in_str[pos:]}")
        print("stack", stack.queue[::-1])
        print("-" * 10)
    if in_str[pos] == "$":
        return True
    else:
        return Exception("Error 3: stack empty before string empty")


def ll1_parse_lightly_traced(
    table: "dict[Enum, list[Rule]]", S: Enum, in_str: str, parse_cols: dict
) -> bool:
    terminals = parse_cols
    if S in terminals:
        return Exception("Error: start symbol is terminal")
    pos = 0
    stack = LifoQueue()
    stack.put(S)
    while not stack.empty():
        x = stack.queue[-1]
        if x not in terminals:  # Lookup case (X is a non terminal)
            if table[x][parse_cols[in_str[pos]]] == None:
                return Exception("Error 1: looked up blank cell")
            else:  # rule x -> beta
                got = stack.get()
                for symbol in reversed(table[x][parse_cols[in_str[pos]]].RHS):
                    stack.put(symbol)
        else:  # Match case (x is terminal)
            if x == in_str[pos]:
                stack.get()
                pos += 1
            else:
                if not x in terminals:
                    return Exception("Error 2: terminal expected", x, "found")
                return Exception("Error 2: expected", x, "found", in_str[pos])
        print("stack", stack.queue)
    if in_str[pos] == "$":
        return True
    else:
        return Exception("Error 3: stack empty before string empty")


if __name__ == "__main__":

    class NTs(Enum):
        S = auto()
        T = auto()

    parse_cols = {"(": 0, ")": 1, "$": 2}

    """
    e = epsilon
    __|____(_____|____)___|___$____|
    S | S -> TS  | S -> e | S -> e |
    T | T -> (S) |        |        |
    """

    parseTable = {
        NTs.S: [Rule(NTs.S, [NTs.T, NTs.S]), Rule(NTs.S, []), Rule(NTs.S, [])],
        NTs.T: [Rule(NTs.T, ["(", NTs.S, ")"]), None, None],
    }

    print(ll1_parse_traced(parseTable, NTs.S, "(())$", parse_cols))
    # print(ll1_parse_traced(parseTable, NTs.S, ")$", parse_cols))
    # print(ll1_parse_traced(parseTable, NTs.S, "($", parse_cols))
    # print(ll1_parse_lightly_traced(parseTable, NTs.S, "(())$", parse_cols))
