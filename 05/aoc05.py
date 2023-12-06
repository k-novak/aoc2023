# %%

txt = """
seeds: 79 14 55 13

seed-to-soil map:
50 98 2
52 50 48

soil-to-fertilizer map:
0 15 37
37 52 2
39 0 15

fertilizer-to-water map:
49 53 8
0 11 42
42 0 7
57 7 4

water-to-light map:
88 18 7
18 25 70

light-to-temperature map:
45 77 23
81 45 19
68 64 13

temperature-to-humidity map:
0 69 1
1 0 69

humidity-to-location map:
60 56 37
56 93 4
""".strip().split("\n\n")

with open("input.txt") as f:
    txt = f.read().strip().split("\n\n")

[
    seeds, 
    seed_to_soil, 
    soil_to_fertilizer, 
    fertilizer_to_water, 
    water_to_light, 
    light_to_temperature, 
    temperatrue_to_humidity, 
    humidity_to_location
] = txt

seeds = [int(i) for i in seeds.split(":")[1].split()]

def extract(text):
    return [[int(i) for i in lst.split()] for lst in text.split(":")[1].strip().split("\n")]

seed_to_soil = extract(seed_to_soil)
soil_to_fertilizer = extract(soil_to_fertilizer)
fertilizer_to_water = extract(fertilizer_to_water)
water_to_light = extract(water_to_light)
light_to_temperature = extract(light_to_temperature)
temperatrue_to_humidity = extract(temperatrue_to_humidity)
humidity_to_location = extract(humidity_to_location)

def contains(num, a, b):
    return num >= a and num <= b

def map_to(source, m):
    for d, s, l in m:
        if contains(source, s, s + l - 1):
            delta = source - s
            return d + delta
    else:
        return source

end_loc = []
for a in seeds:
    a = map_to(a, seed_to_soil)
    a = map_to(a, soil_to_fertilizer)
    a = map_to(a, fertilizer_to_water)
    a = map_to(a, water_to_light)
    a = map_to(a, light_to_temperature)
    a = map_to(a, temperatrue_to_humidity)
    a = map_to(a, humidity_to_location)
    end_loc.append(a)

print(min(end_loc))


# %%

txt = """
seeds: 79 14 55 13

seed-to-soil map:
50 98 2
52 50 48

soil-to-fertilizer map:
0 15 37
37 52 2
39 0 15

fertilizer-to-water map:
49 53 8
0 11 42
42 0 7
57 7 4

water-to-light map:
88 18 7
18 25 70

light-to-temperature map:
45 77 23
81 45 19
68 64 13

temperature-to-humidity map:
0 69 1
1 0 69

humidity-to-location map:
60 56 37
56 93 4
""".strip().split("\n\n")

with open("input.txt") as f:
    txt = f.read().strip().split("\n\n")

[
    seeds, 
    seed_to_soil, 
    soil_to_fertilizer, 
    fertilizer_to_water, 
    water_to_light, 
    light_to_temperature, 
    temperatrue_to_humidity, 
    humidity_to_location
] = txt

seeds = [int(i) for i in seeds.split(":")[1].split()]
it = iter(seeds)
seeds = list(zip(it,it))

def extract(text):
    return [[int(i) for i in lst.split()] for lst in text.split(":")[1].strip().split("\n")]

def sort_mapping(mapping):
    return sorted(mapping, key=lambda x: x[1])

seed_to_soil = sort_mapping(extract(seed_to_soil))
soil_to_fertilizer = sort_mapping(extract(soil_to_fertilizer))
fertilizer_to_water = sort_mapping(extract(fertilizer_to_water))
water_to_light = sort_mapping(extract(water_to_light))
light_to_temperature = sort_mapping(extract(light_to_temperature))
temperatrue_to_humidity = sort_mapping(extract(temperatrue_to_humidity))
humidity_to_location = sort_mapping(extract(humidity_to_location))

def intersection(A, B):
    a1, al = A
    b1, bl = B

    a2 = a1 + al - 1
    b2 = b1 + bl - 1

    if max(a1, b1) < min(a2, b2) + 1: # there is intersection
        return [max(a1, b1), min(a2, b2) - max(a1, b1) + 1]
    return []

def subtract(r, sections):
    output = []
    sections = sorted(sections, key=lambda x:x[0])

    if r[0] < sections[0][0]:
        output.append( (r[0], sections[0][0] - r[0]) )
    if sections[-1][0] + sections[-1][1] < r[0] + r[1]:
        output.append( (sections[-1][0] + sections[-1][1],  r[0] + r[1] - (sections[-1][0] + sections[-1][1])) )
    for s1, s2 in zip(sections[:-1], sections[1:]):
        output.append( (s1[0]+s1[1], s2[0]-(s1[0]+s1[1])) )
    return output


def f(ranges, mapping):

    has_intersection = []
    output = []
    for r in ranges:
        for m in mapping:
            i = intersection(r, m[1:])
            if i:
                has_intersection.append(i)
                output.append( (m[0] + i[0] - m[1], i[1]) )


    # remove has_intersection from all input ranges and see what remains, that maps directly
    for r in ranges:
        collect = []
        for i in has_intersection:
            # map r-i directly
            ii = intersection(r, i)
            if ii:
                collect.append(ii)
        
        if collect:
            output.extend(subtract(r, collect))
        else:
            output.append(r)

    return output

a = f(seeds, seed_to_soil           )
# print(len(a), len(set(a)))
a = f(a    , soil_to_fertilizer     )
# print(len(a), len(set(a)))
a = f(a    , fertilizer_to_water    )
# print(len(a), len(set(a)))
a = f(a    , water_to_light         )
# print(len(a), len(set(a)))
a = f(a    , light_to_temperature   )
# print(len(a), len(set(a)))
a = f(a    , temperatrue_to_humidity)
# print(len(a), len(set(a)))
a = f(a    , humidity_to_location   )
# print(len(a), len(set(a)))

a = sorted(a, key=lambda x:x[0])
print(a[0][0])

for i in a:
    print(i)

# %%


# there are zere length intervals in the result
# if i remove them, then the result is: 52210644

# no time to remove this bug or understand where i add zero length intervals

# (24333950, 0)
# (44804161, 0)
# (52210644, 9617565)
# (77864446, 1688301)
# (79552747, 22836171)
# (102388918, 16974983)
# (119363901, 8969493)
# (132197744, 0)
# (144922528, 29802073)
# (169908659, 0)
# (175513302, 36303828)
# (179967997, 0)
# (194189667, 0)
# (195510987, 0)
# (198333073, 0)
# (275428333, 50219275)
# (340994526, 18764957)
# (414853363, 22778075)