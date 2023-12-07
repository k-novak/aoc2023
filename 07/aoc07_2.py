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


order = {k:v for v, k in enumerate(reversed(['A', 'K', 'Q', 'T', '9', '8', '7', '6', '5', '4', '3', '2', 'J']))}

class Card:
    def __init__(self, cards, value) -> None:
        self.cards = cards
        self.value = value

        num_J = cards.count("J")
        cards = cards.replace("J", "")

        qty = {k:0 for k, v in order.items()}
        for card in cards:
            qty[card] += 1
        qty = [v for k, v in qty.items() if v != 0]

        # The complex if elif else can be reduced to a decision table:
        decision_table = [
            [0, 1, 3, 5, 6, 6],
            [1, 3, 5, 6],
            [2, 4],
            [3, 5, 6],
            [4],
            [5, 6],
            [6]
        ]
        if 5 in qty:                    # 6: Five of a kind
            self.rank = decision_table[6][num_J]
        elif 4 in qty:                  # 5: Four of a kind
            self.rank = decision_table[5][num_J]
        elif 3 in qty and 2 in qty:     # 4: Full house
            self.rank = decision_table[4][num_J]
        elif 3 in qty:                  # 3: Three of a kind
            self.rank = decision_table[3][num_J]
        elif qty.count(2) == 2:         # 2: Two pair
            self.rank = decision_table[2][num_J]
        elif qty.count(2) == 1:         # 1: One pair
            self.rank = decision_table[1][num_J]
        else:                           # 0: High card or no card (5J)
            self.rank = decision_table[0][num_J]

        # if 5 in qty:                    # 6: Five of a kind
        #     self.rank = 6
        # elif 4 in qty:                  # 5: Four of a kind
        #     if num_J != 0:
        #         self.rank = 6
        #     else:
        #         self.rank = 5
        # elif 3 in qty and 2 in qty:     # 4: Full house
        #     self.rank = 4
        # elif 3 in qty:                  # 3: Three of a kind
        #     if num_J == 1:
        #         self.rank = 5
        #     elif num_J == 2:
        #         self.rank = 6
        #     else:
        #         self.rank = 3
        # elif qty.count(2) == 2:         # 2: Two pair
        #     if num_J == 1:
        #         self.rank = 4
        #     else:
        #         self.rank = 2
        # elif qty.count(2) == 1:         # 1: One pair
        #     if num_J == 1:
        #         self.rank = 3
        #     elif num_J == 2:
        #         self.rank = 5
        #     elif num_J == 3:
        #         self.rank = 6
        #     else:
        #         self.rank = 1
        # else:                           # 0: High card or no card (5J)
        #     if num_J == 1:
        #         self.rank = 1
        #     elif num_J == 2:
        #         self.rank = 3
        #     elif num_J == 3:
        #         self.rank = 5
        #     elif num_J == 4:
        #         self.rank = 6
        #     elif num_J == 5:
        #         self.rank = 6
        #     else:
        #         self.rank = 0

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


