# %%

# | is a vertical pipe connecting north and south.
# - is a horizontal pipe connecting east and west.
# L is a 90-degree bend connecting north and east.
# J is a 90-degree bend connecting north and west.
# 7 is a 90-degree bend connecting south and west.
# F is a 90-degree bend connecting south and east.
# . is ground; there is no pipe in this tile.
# S is the starting position of the animal; 
#   there is a pipe on this tile, but your sketch doesn't show 
#   what shape the pipe has.

M = """
7-F7-
.FJ|7
SJLL7
|F--J
LJ.LJ
""".strip().splitlines()

with open("input.txt") as f:
    M = f.read().strip().splitlines()

sx = len(M[0])
sy = len(M)

G = {} # (x, y): [(x, y), (x, y)]

for x in range(sx):
    for y in range(sy):
        G[(y, x)] = []
        match M[y][x]:
            case '|':
                # up
                if y - 1 >= 0 and M[y-1][x] in ['S', '|', '7', 'F']:
                    G[(y, x)].append((y-1, x))

                # down
                if y + 1 < sy and M[y+1][x] in ['S', '|', 'L', 'J']:
                    G[(y, x)].append((y+1, x))

            case '-':
                # left
                if x - 1 >= 0 and M[y][x-1] in ['S', '-', 'L', 'F']:
                    G[(y, x)].append((y, x-1))

                # right
                if x + 1 < sx and M[y][x+1] in ['S', '-', '7', 'J']:
                    G[(y, x)].append((y, x+1))
            
            case 'L':
                # up
                if y - 1 >= 0 and M[y-1][x] in ['S', '|', '7', 'F']:
                    G[(y, x)].append((y-1, x))

                # right
                if x + 1 < sx and M[y][x+1] in ['S', '-', '7', 'J']:
                    G[(y, x)].append((y, x+1))

            case 'J':
                # up
                if y - 1 >= 0 and M[y-1][x] in ['S', '|', '7', 'F']:
                    G[(y, x)].append((y-1, x))

                # left
                if x - 1 >= 0 and M[y][x-1] in ['S', '-', 'L', 'F']:
                    G[(y, x)].append((y, x-1))
                
            case '7':
                # left
                if x - 1 >= 0 and M[y][x-1] in ['S', '-', 'L', 'F']:
                    G[(y, x)].append((y, x-1))
                
                # down
                if y + 1 < sy and M[y+1][x] in ['S', '|', 'L', 'J']:
                    G[(y, x)].append((y+1, x))
                
            case 'F':
                # down
                if y + 1 < sy and M[y+1][x] in ['S', '|', 'L', 'J']:
                    G[(y, x)].append((y+1, x))

                # right
                if x + 1 < sx and M[y][x+1] in ['S', '-', '7', 'J']:
                    G[(y, x)].append((y, x+1))

            case '.':
                continue
            case 'S':
                # up
                if y - 1 >= 0 and M[y-1][x] in ['S', '|', '7', 'F']:
                    G[(y, x)].append((y-1, x))

                # down
                if y + 1 < sy and M[y+1][x] in ['S', '|', 'L', 'J']:
                    G[(y, x)].append((y+1, x))

                # left
                if x - 1 >= 0 and M[y][x-1] in ['S', '-', 'L', 'F']:
                    G[(y, x)].append((y, x-1))

                # right
                if x + 1 < sx and M[y][x+1] in ['S', '-', '7', 'J']:
                    G[(y, x)].append((y, x+1))
            
                start = (y, x)


# walk the graph
steps = 1
prev_step = start
cur_step = G[start][0]
while cur_step != start:
    steps += 1
    a, b = G[cur_step]
    prev_step, cur_step = cur_step, a if a != prev_step else b

print("steps", steps)
print("answer", steps // 2 + steps % 1)



# %%
