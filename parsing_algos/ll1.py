from typing import List
from queue import LifoQueue
from enum import Enum, auto
import pprint

class LngElem:
    def __init__(self, val, terminal: bool = False):
        self.val = val
        self.terminal = terminal

class Rule:
    def __init__(self, LHS: LngElem, RHS: "list[LngElem]", terminal: bool = False):   # different from the CYK version!
        self.LHS = LHS
        self.RHS = RHS
        self.terminal = terminal

def ll1_parse(table: "dict[Enum, list[Rule]]", S: Enum, in_str: str, parse_cols: dict) -> bool:
    i = 0
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
            else:   # rule x -> beta
                stack.get()
                for symbol in reversed(table[x][parse_cols[in_str[pos]]].RHS):
                    stack.put(symbol)
        else:   # Match case (x is terminal)
            if x == in_str[pos]:
                stack.get()
                pos += 1
            else:
                if not x in terminals:
                    return Exception("Error 2: terminal expected", x, "found")
                return Exception("Error 2: expected", x, "found", in_str[pos])
        i = i + 1
        # if i > 2: break
    if in_str[pos] == "$":
        return True
    else:
        return Exception("Error 3: stack empty before string empty")

def ll1_parse_traced(table: "dict[Enum, list[Rule]]", S: Enum, in_str: str, parse_cols: dict) -> bool:
    i = 0
    terminals = parse_cols
    if S in terminals:
        return Exception("Error: start symbol is terminal")
    pos = 0
    stack = LifoQueue()
    stack.put(S)
    while not stack.empty():
        x = stack.queue[-1]
        print("x", x)
        if x not in terminals:  # Lookup case
            print("RHS", table[x][parse_cols[in_str[pos]]].RHS)
            if table[x][parse_cols[in_str[pos]]] == None:
                return Exception("Error 1: looked up blank cell")
            else:   # rule x -> beta
                got = stack.get()
                print("got", got)
                for symbol in reversed(table[x][parse_cols[in_str[pos]]].RHS):
                    stack.put(symbol)
        else:   # Match case (x is terminal)
            if x == in_str[pos]:
                stack.get()
                pos += 1
            else:
                if not x in terminals:
                    return Exception("Error 2: terminal expected", x, "found")
                return Exception("Error 2: expected", x, "found", in_str[pos])
        print("stack", stack.queue)
        i = i + 1
        # if i > 2: break
    if in_str[pos] == "$":
        return True
    else:
        return Exception("Error 3: stack empty before string empty")

def ll1_parse_lightly_traced(table: "dict[Enum, list[Rule]]", S: Enum, in_str: str, parse_cols: dict) -> bool:
    i = 0
    terminals = parse_cols
    if S in terminals:
        return Exception("Error: start symbol is terminal")
    pos = 0
    stack = LifoQueue()
    stack.put(S)
    while not stack.empty():
        x = stack.queue[-1]
        # print("x", x)
        if x not in terminals:  # Lookup case
            # print("RHS", table[x][parse_cols[in_str[pos]]].RHS)
            if table[x][parse_cols[in_str[pos]]] == None:
                return Exception("Error 1: looked up blank cell")
            else:   # rule x -> beta
                got = stack.get()
                # print("got", got)
                for symbol in reversed(table[x][parse_cols[in_str[pos]]].RHS):
                    stack.put(symbol)
        else:   # Match case (x is terminal)
            if x == in_str[pos]:
                stack.get()
                pos += 1
            else:
                if not x in terminals:
                    return Exception("Error 2: terminal expected", x, "found")
                return Exception("Error 2: expected", x, "found", in_str[pos])
        print("stack", stack.queue)
        i = i + 1
        # if i > 2: break
    if in_str[pos] == "$":
        return True
    else:
        return Exception("Error 3: stack empty before string empty")

if __name__ == "__main__":
    class NTs(Enum):
        S = auto()
        T = auto()

    # S = LngElem(NTs.S)
    # T = LngElem(NTs.T)
    # empty = LngElem("")

    # leftBracket = LngElem("(", True)
    # rightBracket = LngElem(")", True)
    # final = LngElem("$", True)

    # parse_rows = {S: 0, T: 1}
    # parse_cols = {leftBracket.val: 0, rightBracket.val: 1, final.val: 2}
    parse_cols = {"(": 0, ")": 1, "$": 2}

    parseTable = {
        NTs.S: [
            Rule(NTs.S, [NTs.T, NTs.S]),
            Rule(NTs.S, []),
            Rule(NTs.S, [])
        ],

        NTs.T: [
            Rule(NTs.T, ["(", NTs.S, ")"]),
            None,
            None
        ]
    }

    print(ll1_parse_traced(parseTable, NTs.S, ")$", parse_cols))
    print(ll1_parse_traced(parseTable, NTs.S, "($", parse_cols))
    print(ll1_parse_lightly_traced(parseTable, NTs.S, "(())$", parse_cols))
