# %%

inp = """
...#......
.......#..
#.........
..........
......#...
.#........
.........#
..........
.......#..
#...#.....
""".strip().splitlines()

with open("input.txt") as f:
    inp = f.read().strip().splitlines()

N = 1000000 # expansion factor
empty_rows = [y for y, row in enumerate(inp) if '#' not in row]
empty_cols = sorted(list(set.intersection(*[set([x for x, ch in enumerate(row) if ch == '.']) for row in inp])))

X = [N if i in empty_cols else x for i, x in enumerate([1] * len(inp[0]))]
Y = [N if i in empty_rows else y for i, y in enumerate([1] * len(inp))]


# collect galaxies
G = []
for y in range(len(inp)):
    for x in range(len(inp[0])):
        if inp[y][x] == '#':
            G.append((y, x))

# calculate distances
ans = 0
for i, g1 in enumerate(G[:-1]):
    for g2 in G[i+1:]:
        y1, x1 = g1
        y2, x2 = g2
        if x1 > x2: 
            x1, x2 = x2, x1
        if y1 > y2: 
            y1, y2 = y2, y1
        res = sum(X[x1:x2]) + sum(Y[y1:y2])
        ans += res
        
print(ans)

# %%
