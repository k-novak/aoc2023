# %%
import re

with open("input.txt") as f:
    rows = f.read().splitlines()

symbols = []
for row in rows:
    l = []
    for match in re.finditer(r'[^\d.]', row):
        l.append(match.start())
    symbols.append(l)

sum = 0
for i, row in enumerate(rows):
    print(i, "-------------------------")

    for match in re.finditer(r'\d+', row):

        begin = match.start() - 1
        end   = match.end() + 1

        if begin < 0:
            begin = 0
        if end > len(row):
            end = len(row)

        if set(range(begin, end)) &  set(symbols[i]):
            sum += int(match.group())
            print(match.group())
            continue

        if i > 0 and set(range(begin, end)) & set(symbols[i - 1]):
            sum += int(match.group())
            print(match.group())
            continue

        if i < len(symbols) - 1 and set(range(begin, end)) & set(symbols[i + 1]):
            sum += int(match.group())
            print(match.group())
    

print(sum)
# %%

import re

with open("input.txt") as f:
    rows = f.read().splitlines()

# numbers = []

# for i, row in enumerate(rows):
#     n = []
#     for match in re.finditer(r'\d+', row):
#         n.append(int(match.group()))
#     numbers.append(n)


sum = 0
for i, row in enumerate(rows):
    print(i, "-------------------------")


    for match in re.finditer(r'[*]', row):
        pos = match.start()

        N = []

        # parse previous line
        if i > 0:
            for M in re.finditer(r'\d+', rows[i-1]):
                if M.end() >= pos and M.start() <= pos+1:
                    N.append(int(M.group()))
        
        # parse next line
        if i < len(rows)-1:
            for M in re.finditer(r'\d+', rows[i+1]):
                if M.end() >= pos and M.start() <= pos+1:
                    N.append(int(M.group()))

        # parse left
        for M in re.finditer(r'\d+', rows[i]):
            if M.end() == pos:
                N.append(int(M.group()))
                
        # parse right
        for M in re.finditer(r'\d+', rows[i]):
            if M.start() == pos + 1:
                N.append(int(M.group()))

        print(N)
        if len(N) == 2:
            sum += N[0] * N[1]
    

print(sum)
# %%
