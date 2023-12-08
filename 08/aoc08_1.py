# %%

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
BBB = (AAA, ZZZ)
ZZZ = (ZZZ, ZZZ)""".strip().splitlines()

with open("input.txt") as f:
    puzzle = f.read().strip().splitlines()

inp = puzzle


nodes = {line[:3]:(line[7:10], line[12:15]) for line in inp[2:]}

def instructions():
    while 1:
        for i in inp[0]:
            yield i

ans = 0
cur = "AAA"
for i in instructions():
    ans += 1
    L, R = nodes[cur]
    cur = L if i == "L" else R
    if cur == "ZZZ":
        break
print(ans)
# %%
