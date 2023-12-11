# %%

from itertools import cycle
from math import lcm

example1 = """
RL

AAA = (BBB, CCC)
BBB = (DDD, EEE)
CCC = (ZZZ, GGG)
DDD = (DDD, DDD)
EEE = (EEE, EEE)
GGG = (GGG, GGG)
ZZZ = (ZZZ, ZZZ)
""".strip().splitlines()

example2 = """
LLR

AAA = (BBB, BBB)
BBB = (AAA, ZZZ)z
ZZZ = (ZZZ, ZZZ)
""".strip().splitlines()

example3 = """
LR

11A = (11B, XXX)
11B = (XXX, 11Z)
11Z = (11B, XXX)
22A = (22B, XXX)
22B = (22C, 22C)
22C = (22Z, 22Z)
22Z = (22B, 22B)
XXX = (XXX, XXX)
""".strip().splitlines()

with open("input.txt") as f:
    puzzle = f.read().strip().splitlines()

inp = puzzle

nodes = {line[:3]:(line[7:10], line[12:15]) for line in inp[2:]}

results = []
for node in [node for node in nodes.keys() if node[-1] == "A"]:
    print(node, end=" ")
    ans = 0
    for i in cycle(inp[0]):
        ans += 1
        node = nodes[node][0] if i == "L" else nodes[node][1]

        if node[-1] == "Z":
            break
    print(ans, node)
    results.append(ans)

print("solution:", lcm(*results))
# %%

"""
There are 6 nodes ending with Z.
Number of steps necessary to complete if only one path is traced:
15871
19637
12643
14257
21251
19099

LCM of the 6 number is 16187743689077, and this is the solution.

"""