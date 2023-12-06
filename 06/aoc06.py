# %%

txt = """
Time:        44     89     96     91
Distance:   277   1136   1890   1768
""".strip().splitlines()


# txt = """
# Time:      7  15   30
# Distance:  9  40  200
# """.strip().splitlines()

time, distance = [list(map(int, line.split()[1:])) for line in txt]
ans = 1
for t, d in zip(time, distance):
    counter = 0
    for p in range(1, t):
        if (t - p) * p > d:
            counter += 1
    ans *= counter
print(ans)


# %%

txt = """
Time:        44     89     96     91
Distance:   277   1136   1890   1768
""".strip().splitlines()


# txt = """
# Time:      7  15   30
# Distance:  9  40  200
# """.strip().splitlines()

t, d = [int(line.split(":")[-1].replace(" ", "")) for line in txt]
ans = 1
counter = 0
for p in range(1, t):
    if (t - p) * p > d:
        counter += 1
ans *= counter
print(ans)
# %%
