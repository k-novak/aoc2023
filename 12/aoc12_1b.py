# %%

# s = "???????##?????##???? 1,1,11,3"
# inp = ".??..??...?##. 1,1,3"
# inp = "???.### 1,1,3"

with open("input.txt") as f:
    INP = f.read().strip().splitlines()


ans = 0

for inp in INP:
    pattern, groups = inp.split()
    groups = [int(num) for num in groups.split(',')]


    # print("pattern", pattern)
    # print("groups ", groups)


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

print(ans)
