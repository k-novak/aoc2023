# %%
from itertools import permutations 

inp = """
???.### 1,1,3
.??..??...?##. 1,1,3
?#?#?#?#?#?#?#? 1,3,1,6
????.#...#... 4,1,1
????.######..#####. 1,6,5
?###???????? 3,2,1
""".strip().splitlines()

with open("input.txt") as f:
    inp = f.read().strip().splitlines()

ans = 0
for num, s in enumerate(inp):
    print(num)
    p, g = s.split()
    g = [int(num) for num in g.split(',')]

    failed = sum(g) - p.count('#')
    good   = p.count('?') - failed
    idx = [i for i, c in enumerate(p) if c == '?']

    perms = {"".join(p) for p in permutations('#' * failed + '.' * good, r=failed + good)}

    for perm in perms:
        ns = p
        for i, c in zip(idx, perm):
            ns = ns[:i] + c + ns[i+1:]
        if g == [len(sub) for sub in ns.replace('.', ' ').split()]:
            ans += 1

print(ans)



# %%
