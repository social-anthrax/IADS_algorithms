from typing import List
from enum import Enum, auto
import pprint

class NT:
    def __init__(self, l: Enum, r: Enum):
        self.l = l
        self.r = r

class Rule:
    def __init__(self, LHS: Enum, RHS, terminal: bool = False): # RHS: NT or String
        self.LHS = LHS
        self.RHS = RHS
        self.terminal = terminal

def cyk(s: List, G: "list[Rule]") -> "list[list[list[Enum]]]":  # G should really be a set of Rules but I cba to fix it rn
    n = len(s)
    table = [[[] for _ in range(n - 1)] for _ in range(n - 1)]
    
    for j in range(1, n + 1):   # columns
        for rule in G:
            if rule.terminal:
                if s[j - 1] == rule.RHS:
                    table[j - 1][j].append(rule.LHS)  # diagonal cell
        
        for i in range(j - 2, -1, -1):  # rows
            for k in range(i + 1, j):   # possible splits
                for rule in G:
                    if not rule.terminal:
                        if rule.RHS.l in table[i][k] and rule.RHS.r in table[k][j]:
                            table[i][j].append(rule.LHS)
    
    for i in range(len(table)):
        del table[i][0]
    del table[-1]
    
    return table

def cyk_parser(s: List, G: "list[Rule]") -> "list[list[list[tuple(Enum, tuple(int, int), tuple(int, int))]]]":  # G should really be a set of Rules but I cba to fix it rn
    n = len(s)
    table = [[[] for _ in range(n + 1)] for _ in range(n + 1)]
    
    for j in range(1, n + 1):   # columns
        for rule in G:
            if rule.terminal:
                if s[j - 1] == rule.RHS:
                    table[j - 1][j].append((rule.LHS, (j - 1, j), (j - 1, j)))  # diagonal cell
        
        for i in range(j - 2, -1, -1):  # rows
            for k in range(i + 1, j):   # possible splits
                for rule in G:
                    if not rule.terminal:
                        if any([rule.RHS.l == x[0] for x in table[i][k]]) and any([rule.RHS.r == x[0] for x in table[k][j]]):
                            table[i][j].append((rule.LHS, (i, k), (k, j)))
    
    for i in range(len(table)):
        del table[i][0]
    del table[-1]
    
    return table

def cyk_traced(s: List, G: "list[Rule]") -> "list[list[list[Enum]]]":
    print("Start:", s)
    n = len(s)
    table = [[[] for _ in range(n + 1)] for _ in range(n + 1)]
    
    for j in range(1, n + 1):   # columns
        for rule in G:
            if rule.terminal:
                if s[j - 1] == rule.RHS:
                    print(n, j)
                    table[j - 1][j].append(rule.LHS)  # diagonal cell
                    print("diag", rule.LHS, j - 1, j)
        
        for i in range(j - 2, -1, -1):  # rows
            for k in range(i + 1, j):   # possible splits
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

    pp = pprint.PrettyPrinter(indent=2)
    pp.pprint(table)
    return table

def cyk_parser_traced(s: List, G: "list[Rule]") -> "list[list[list[tuple(Enum, tuple(int, int), tuple(int, int))]]]":
    print("Start:", s)
    n = len(s)
    table = [[[] for _ in range(n + 1)] for _ in range(n + 1)]
    
    for j in range(1, n + 1):   # columns
        for rule in G:
            if rule.terminal:
                if s[j - 1] == rule.RHS:
                    print(n, j)
                    table[j - 1][j].append((rule.LHS, (j - 1, j), (j - 1, j)))  # diagonal cell
                    print("diag", rule.LHS, j - 1, j)
        
        for i in range(j - 2, -1, -1):  # rows
            for k in range(i + 1, j):   # possible splits
                for rule in G:
                    if not rule.terminal:
                        if any([rule.RHS.l == x[0] for x in table[i][k]]) and any([rule.RHS.r == x[0] for x in table[k][j]]):
                            table[i][j].append((rule.LHS, (i, k), (k, j)))
                            print("non-diag", rule.LHS, i, j)
                            print("non-diag l", rule.RHS.l, i, k)
                            print("non-diag r", rule.RHS.r, k, j)
    
    for i in range(len(table)):
        del table[i][0]
    del table[-1]

    pp = pprint.PrettyPrinter(indent=2)
    pp.pprint(table)
    return table

if __name__ == "__main__":
    class NTs(Enum):
        NP = auto()
        Nom = auto()
        AP = auto()
        A = auto()
        Det = auto()
        Adv = auto()

    grammarRules = [
        Rule(NTs.NP, NT(NTs.Det, NTs.Nom)),
        Rule(NTs.Nom, "book", True),
        Rule(NTs.Nom, "orange", True),
        Rule(NTs.Nom, NT(NTs.AP, NTs.Nom)),
        Rule(NTs.AP, "heavy", True),
        Rule(NTs.AP, "orange", True),
        Rule(NTs.AP, NT(NTs.Adv, NTs.A)),
        Rule(NTs.A, "heavy", True),
        Rule(NTs.A, "orange", True),
        Rule(NTs.Det, "my", True),
        Rule(NTs.Adv, "very", True)
    ]

    cyk_parser_traced(["my", "very", "heavy", "orange", "book"], grammarRules)
    cyk_traced(["my", "very", "heavy", "orange", "book"], grammarRules)
