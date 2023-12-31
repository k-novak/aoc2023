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

empty_rows = [y for y, row in enumerate(inp) if '#' not in row]
empty_cols = sorted(list(set.intersection(*[set([x for x, ch in enumerate(row) if ch == '.']) for row in inp])))

# expand
for y in reversed(empty_rows):
    inp.insert(y, '.' * len(inp[0]))

for x in reversed(empty_cols):
    for y, row in enumerate(inp):
        inp[y] = row[:x] + '.' + row[x:]


# collect galaxies
G = []
for y in range(len(inp)):
    for x in range(len(inp[0])):
        if inp[y][x] == '#':
            G.append((y, x))

# calculate distances
ans = 0
for i, (x1, y1) in enumerate(G[:-1]):
    for (x2, y2) in G[i+1:]:
        ans += abs(x1 - x2) + abs(y1 - y2)
        
print(ans)

# %%
