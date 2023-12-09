# %%

inp = """
0 3 6 9 12 15
1 3 6 10 15 21
10 13 16 21 30 45
""".strip().splitlines()

with open("input.txt") as f:
    inp = f.read().strip().splitlines()

inp = [[int(value) for value in line.split()] for line in inp]

ans = 0
for i in inp:
    hist = [i]
    while not all(value == 0 for value in hist[-1]):
        hist.append([b - a for a, b in zip(hist[-1][:-1], hist[-1][1:])])

    hist[-1].append(0)
    hist.reverse()

    for a, b in zip(hist[:-1], hist[1:]):
        b.insert(0, b[0] - a[0])

    ans += hist[-1][0]

print(ans)
# %%
