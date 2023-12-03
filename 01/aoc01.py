# %% solultion of the first part of the task! works!
with open("input.txt") as f:
    rows = f.read().splitlines()

sum = 0

for row in rows:

    for c in row:
        if c.isdigit():
            a = int(c)
            break

    for c in row[::-1]:
        if c.isdigit():
            b = int(c)
            break
        
    sum += a * 10 + b

print(sum)
# %% parsing from left to right, does not work
with open("input.txt") as f:
    rows = f.read().splitlines()
sum = 0
for ROW in rows:
    buff = []
    row = ROW
    while row:
        c, row = row[0], row[1:]
        if c.isdigit():
            buff.append(int(c))
            continue

        if c == 'o' and len(row) >= 2 and row[:2] == "ne":
            buff.append(1)
            row = row[2:]
            continue

        if c == 't':
            if len(row) >= 2 and row[:2] == "wo":
                buff.append(2)
                row = row[2:]
                continue
            elif len(row) >= 4 and row[:4] == 'hree':
                buff.append(3)
                row = row[4:]
                continue
        
        if c == 'f' and len(row) >= 3:
            if row[:3] == "our":
                buff.append(4)
                row = row[3:]
                continue
            elif row[:3] == 'ive':
                buff.append(5)
                row = row[3:]
                continue

        if c == 's':
            if len(row) >= 2 and row[:2] == "ix":
                buff.append(6)
                row = row[2:]
                continue
            elif len(row) >= 4 and row[:4] == "even":
                buff.append(7)
                row = row[4:]
                continue
        if c == 'e' and len(row) >= 4 and row[:4] == "ight":
            buff.append(8)
            row = row[4:]
            continue

        if c == 'n' and len(row) >= 3 and row[:3] == "ine":
            buff.append(9)
            row = row[3:]
            continue

    sum += 10 * buff[0] + buff[-1]

print(sum)            
        

# %% replace the text with digits, does not work

with open("input.txt") as f:
    rows = f.read().splitlines()

sum = 0

for row in rows:

    row = row.replace("one", "1")
    row = row.replace("two", "2")
    row = row.replace("three", "3")
    row = row.replace("four", "4")
    row = row.replace("five", "5")
    row = row.replace("six", "6")
    row = row.replace("seven", "7")
    row = row.replace("eight", "8")
    row = row.replace("nine", "9")

    for c in row:
        if c.isdigit():
            a = int(c)
            break

    for c in row[::-1]:
        if c.isdigit():
            b = int(c)
            break
        
    sum += a * 10 + b

print(sum)
# %% parse left to right till the first digit is found, then parse right to left

# this worked!!!
# I assume the trick was to parse the last digit from the back to avoid a problem like: "sevenine"
# This is seven if I parse from the left to right, nine if I parse from right to left.

# Yes, I was right: 8nine37bpkmtghhnc2hnreightwohvs --> eightwo

with open("input.txt") as f:
    rows = f.read().splitlines()
    
d = {
    "1": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, 
    "one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9,
}

sum = 0
for row in rows:
    flag = True
    S = row
    while S and flag:
        for k, v in d.items():
            if S.startswith(k):
                sum += 10 * v
                flag = False
                break
        else:
            S = S[1:]

    flag = True
    S = row
    while row and flag:
        for k, v in d.items():
            if row.endswith(k):
                sum += v
                flag = False
                break
        else:
            row = row[:-1]

print(sum)
# %%
