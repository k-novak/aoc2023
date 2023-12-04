# %%
with open("input.txt") as f:
    rows = f.read().splitlines()

sum = 0
for row in rows:
    a, b = row.split(":")
    winning, numbers = b.split("|")
    winning = winning.split()
    numbers = numbers.split()

    winning = set([int(cell) for cell in winning])
    numbers = set([int(cell) for cell in numbers])

    c = len(winning & numbers)
    if c > 0:
        sum += 2**(c-1)
print(sum)
# %%
