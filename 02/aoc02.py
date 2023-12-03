# Determine which games would have been possible if the bag had been loaded 
# with only 12 red cubes, 13 green cubes, and 14 blue cubes. What is the sum
# of the IDs of those games?


# %%

RED   = 12
GREEN = 13
BLUE  = 14

with open("input.txt") as f:
    rows = f.read().splitlines()


sum = 0

for row in rows:
    r, g, b = 0, 0, 0

    game_no, row = row.split(":")

    game_no = game_no.removeprefix("Game")
    game_no = int(game_no)

    games = row.split(";")
    games = [game.strip().split(",") for game in games]

    games = [[reversed(a.strip().split(" ")) for a in game] for game in games]
    games = [{k:int(v) for k,v in dict(game).items()} for game in games]
    
    # print(games)

    for game in games:
        if not (game.get("red", 0) <= RED and game.get("blue", 0) <= BLUE and game.get("green", 0) <= GREEN):
            break
    else:
        sum += game_no

print(sum)



# %%

# What is the fewest number of cubes of each color that could have been in the bag to make the game possible?


with open("input.txt") as f:
    rows = f.read().splitlines()


sum = 0

for row in rows:

    game_no, row = row.split(":")

    game_no = game_no.removeprefix("Game")
    game_no = int(game_no)

    games = row.split(";")
    games = [game.strip().split(",") for game in games]

    games = [[reversed(a.strip().split(" ")) for a in game] for game in games]
    games = [{k:int(v) for k,v in dict(game).items()} for game in games]
    
    # print(games)

    r = max([game.get("red", 0) for game in games])
    g = max([game.get("green", 0) for game in games])
    b = max([game.get("blue", 0) for game in games])

    sum += r * g * b

print(sum)
# %%
