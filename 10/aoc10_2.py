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
FF7FSF7F7F7F7F7F---7
L|LJ||||||||||||F--J
FL-7LJLJ||||||LJL-77
F--JF--7||LJLJ7F7FJ-
L---JF-JLJ.||-FJLJJ7
|F|F-JF---7F7-L7L|7|
|FFJF7L7F-JF7|JL---7
7-L-JL7||F7|L7F-7F7|
L.L7LFJ|||||FJL7||LJ
L7JLJL-JLJLJL--JLJ.L
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

steps = [start, G[start][0]]
while steps[-1] != start:
    a, b = G[steps[-1]]
    steps.append(a if a != steps[-2] else b)

# print the loop
# for y in range(sy):
#     for x in range(sx):
#         if (y, x) in steps:
#             print(M[y][x], end='')
#             # print(' ', end='')
#         else:
#             print(' ', end='')
#             # print('O', end='')
#     print()

ans = 0
for y in range(sy):
    for x in range(sx):
        if (y, x) in steps:
            # print('__', end=", ")
            continue
        counter = 0
        for i in range(x, sx):
            if (y, i) in steps and M[y][i] in ['|', 'L', 'J']:
            # if (y, i) in steps and M[y][i] in ['|', '7', 'F']:
                counter += 1
        # print(f"{counter:2d}", end=", ")
        if counter % 2 == 1:
            ans += 1

print(ans)

# %%

# the idea is: where to cast a ray to count, how many times the loop is crossed
# F7: this is peak shaped loop
# LJ: this a valley shaped loop
# if we imagine, that each tiles is a square and the pipes are along the axes of the square,
# then if the ray goes above the centerline, it will cross only |, L and J
# if under the centerline, it will cross only |, F and 7

# in my case S is equivalent with a '7' so my solution worked (351)
# but if S is equivalent with L or J or |, then the answer would be incorrect (358)

# a step should be added, where S is converted to the equivalent tile (|, L, J, F, 7)