# %%

# s = "???????##?????##???? 1,1,11,3"
# inp = ".??..??...?##. 1,1,3"
# inp = "???.### 1,1,3"

with open("input.txt") as f:
    INP = f.read().strip().splitlines()


def calc(pattern, groups):
    ans = 0

    if pattern[0] == '?':
        S = ['#', '.']
    else:
        S = [pattern[0]]

    while S:
        v = S.pop()
        # print(f"{v:30}", end='')
        w = [s.count('#') for s in v.replace('.', ' ').split()]

        if w > groups:
            # print("w > groups")
            continue

        if len(v) == len(pattern):
            if w == groups:
                ans += 1
            continue

        # go deeper
        if pattern[len(v)] == '?':
            # print("extend")
            S.append(v + '.')
            S.append(v + '#')
        else:
            # print("take over", pattern[len(v)])
            S.append(v + pattern[len(v)])
    return ans

INP = """
???.### 1,1,3
.??..??...?##. 1,1,3
?#?#?#?#?#?#?#? 1,3,1,6
????.#...#... 4,1,1
????.######..#####. 1,6,5
?###???????? 3,2,1
""".strip().splitlines()

for inp in INP[:10]:
    pattern, groups = inp.split()
    groups = [int(num) for num in groups.split(',')]
    a = calc(pattern + "?", groups)
    b = calc(pattern, groups)
    c = calc("?" + pattern, groups)

    print(f"{a:2} {b:2} {c:2}")

# %%
