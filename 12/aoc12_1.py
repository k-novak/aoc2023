# %%

s = "???.### 1,1,3"
p, g = s.split()
g = [int(num) for num in g.split(',')]


from itertools import permutations 
perm = {"".join(p) for p in permutations('##.', r=3)}
for i in list(perm): 
    print (i) 




# %%
