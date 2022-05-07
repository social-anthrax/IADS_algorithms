from ast import arg, parse
from lib2to3.pgen2 import grammar
from typing import Dict, List
from enum import Enum, auto
import pprint
import pandas as pd


class NT:
    def __init__(self, l: Enum, r: Enum):
        self.l = l
        self.r = r


class Rule:
    def __init__(self, LHS: Enum, RHS, terminal: bool = False):  # RHS: NT or str
        self.LHS = LHS
        self.RHS = RHS
        self.terminal = terminal  # flag to mark node as terminal


def cyk(
    s: List, G: "list[Rule]"
) -> "list[list[list[Enum]]]":  # G should really be a set of Rules but I cba to fix it rn
    n = len(s)
    table = [[[] for _ in range(n - 1)] for _ in range(n - 1)]

    for j in range(1, n + 1):  # columns
        for rule in G:
            if rule.terminal:
                if s[j - 1] == rule.RHS:
                    table[j - 1][j].append(rule.LHS)  # diagonal cell

        for i in range(j - 2, -1, -1):  # rows
            for k in range(i + 1, j):  # possible splits
                for rule in G:
                    if not rule.terminal:
                        if rule.RHS.l in table[i][k] and rule.RHS.r in table[k][j]:
                            table[i][j].append(rule.LHS)

    for i in range(len(table)):
        del table[i][0]
    del table[-1]

    return table


def cyk_parser(
    s: List, G: "list[Rule]"
) -> "list[list[list[tuple[Enum, tuple[int, int], tuple[int, int]]]]]":  # G should really be a set of Rules but I cba to fix it rn
    n = len(s)
    table = [[[] for _ in range(n + 1)] for _ in range(n + 1)]

    for j in range(1, n + 1):  # columns
        for rule in G:
            if rule.terminal:
                if s[j - 1] == rule.RHS:
                    table[j - 1][j].append(
                        (rule.LHS, (j - 1, j), (j - 1, j))
                    )  # diagonal cell

        for i in range(j - 2, -1, -1):  # rows
            for k in range(i + 1, j):  # possible splits
                for rule in G:
                    if not rule.terminal:
                        if any([rule.RHS.l == x[0] for x in table[i][k]]) and any(
                            [rule.RHS.r == x[0] for x in table[k][j]]
                        ):
                            table[i][j].append((rule.LHS, (i, k), (k, j)))

    for i in range(len(table)):
        del table[i][0]
    del table[-1]

    return table


def cyk_traced(s: List, G: "list[Rule]") -> "list[list[list[Enum]]]":
    print("Start:", s)
    n = len(s)
    table = [[[] for _ in range(n + 1)] for _ in range(n + 1)]

    for j in range(1, n + 1):  # columns
        for rule in G:
            if rule.terminal:
                if s[j - 1] == rule.RHS:
                    print(n, j)
                    table[j - 1][j].append(rule.LHS)  # diagonal cell
                    print("diag", rule.LHS, j - 1, j)

        for i in range(j - 2, -1, -1):  # rows
            for k in range(i + 1, j):  # possible splits
                for rule in G:
                    if not rule.terminal:
                        if rule.RHS.l in table[i][k] and rule.RHS.r in table[k][j]:
                            table[i][j].append(rule.LHS)
                            print("non-diag", rule.LHS, i, j)
                            print("non-diag l", rule.RHS.l, i, k)
                            print("non-diag r", rule.RHS.r, k, j)

    for i in range(len(table)):
        del table[i][0]
    del table[-1]

    table = pd.DataFrame(table, s, s)
    print(table)
    return table


def cyk_parser_traced(s: List, G: "list[Rule]"):
    print("Start:", s)
    n = len(s)
    table = [[[] for _ in range(n + 1)] for _ in range(n + 1)]

    for j in range(1, n + 1):  # columns
        for rule in G:
            if rule.terminal:
                if s[j - 1] == rule.RHS:
                    print(n, j)
                    table[j - 1][j].append(
                        (rule.LHS, (j - 1, j), (j - 1, j))
                    )  # diagonal cell
                    print("diag", rule.LHS, j - 1, j)

        for i in range(j - 2, -1, -1):  # rows
            for k in range(i + 1, j):  # possible splits
                for rule in G:
                    if not rule.terminal:
                        if any([rule.RHS.l == x[0] for x in table[i][k]]) and any(
                            [rule.RHS.r == x[0] for x in table[k][j]]
                        ):
                            table[i][j].append((rule.LHS, (i, k), (k, j)))
                            print("non-diag", rule.LHS, i, j)
                            print("non-diag l", rule.RHS.l, i, k)
                            print("non-diag r", rule.RHS.r, k, j)

    for i in range(len(table)):
        del table[i][0]
    del table[-1]

    table = pd.DataFrame(table, s, s)
    print(table)
    return table


def parseFromFile(file: str, parse: str):
    grammarRules = extractGrammar(file)

    return cyk_parser_traced(parse.split(), grammarRules)

def cykFromFile(file: str, parse:str):
    grammarRules = extractGrammar(file)
    
    return cyk_traced(parse.split(), grammarRules)


def extractGrammar(file):
    content = []
    with open(file, "r") as f:
        content = f.readlines()

    ntsStrings = dict()
    rules = []
    for line in content:
        split = line.split("->")
        ntsStrings[split[0].strip()] = split[0].strip()
        rules.append([split[0].strip()] + split[1].split())

    NTs = Enum("NTs", ntsStrings)

    grammarRules = []
    for rule in rules:
        # case that rule is a terminal
        if len(rule) == 2:
            grammarRules.append(Rule(NTs(rule[0]), rule[1], True))
        else:
            grammarRules.append(Rule(NTs(rule[0]), NT(NTs(rule[1]), NTs(rule[2]))))
    return grammarRules





if __name__ == "__main__":
    from sys import argv

    # out = cyk_parser(["my", "very", "heavy", "orange", "book"], grammarRules)
    # print(pprint.pformat(out))
    # cyk_traced(["my", "very", "heavy", "orange", "book"], grammarRules)
    if len(argv) == 1:
        print("Call function using python3 cyk.py inputfile.txt \"String to parse\" outfile.md")
        print("For example")
        print("python3 cyk.py input.txt \"I ate the salad with a fork\" out1.md")
        print("An example input file is provided. The numbers next the terminal/ non terminals indicate where they were taken from")
        print("Remember that the left side is 0 indexed, the top is 1 indexed.")
    else:
        out = parseFromFile(argv[1], argv[2])
        if len(argv) == 3:
            
            out.to_markdown(argv[3])
        else:
            out.to_markdown("out.md")
    
