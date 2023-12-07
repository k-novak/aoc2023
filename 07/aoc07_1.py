# %%
from collections import defaultdict

txt = """
32T3K 765
T55J5 684
KK677 28
KTJJT 220
QQQJA 483
""".strip().splitlines()

with open("input.txt") as f:
    txt = f.read().strip().splitlines()


order = {k:v for v, k in enumerate(reversed(['A', 'K', 'Q', 'J', 'T', '9', '8', '7', '6', '5', '4', '3', '2']))}

class Card:
    def __init__(self, cards, value) -> None:
        self.cards = cards
        self.value = value

        qty = {k:0 for k, v in order.items()}
        for card in cards:
            qty[card] += 1
        qty = [v for k, v in qty.items() if v != 0]

        if 5 in qty:
            self.rank = 6
        elif 4 in qty:
            self.rank = 5
        elif 3 in qty and 2 in qty:
            self.rank = 4
        elif 3 in qty:
            self.rank = 3
        elif qty.count(2) == 2:
            self.rank = 2
        elif qty.count(2) == 1:
            self.rank = 1
        else:
            self.rank = 0

    def __lt__(self, other):
        if self.rank < other.rank:
            return True
        elif self.rank == other.rank:
            for s, o in zip(self.cards, other.cards):
                if order[s] < order[o]:
                    return True
                elif order[s] > order[o]:
                    return False
            else:
                raise "identical hands"
        else:
            return False


hands = [line.split() for line in txt]
hands = [Card(line[0], int(line[1])) for line in hands]
hands = sorted(hands)

ans = 0
for i, hand in enumerate(hands):
    ans += (i + 1) * hand.value

print(ans)




# %%
