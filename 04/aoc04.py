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

from collections import defaultdict

with open("input.txt") as f:
    rows = f.read().splitlines()

# sample data must return 30!
# rows = """
# Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
# Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
# Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
# Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
# Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
# Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11
# """
# rows = rows.strip().splitlines()

cards = defaultdict(int)

for row in rows:

    # extract data from row
    a, b = row.split(":")
    _, card_no = a.split()
    card_no = int(card_no)
    winning, numbers = b.split("|")
    winning = winning.split()
    numbers = numbers.split()

    winning = set([int(cell) for cell in winning])
    numbers = set([int(cell) for cell in numbers])

    # number of common elements
    c = len(winning & numbers)
    print(c)

    cards[card_no] += 1

    for i in range(1, c+1):
        cards[card_no + i] += cards[card_no]

print(sum(cards.values())) # 9924412
# %%
