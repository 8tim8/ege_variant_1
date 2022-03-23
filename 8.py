from itertools import *

s = 'ДЕЙКСТРА'
comb = permutations(s, r=6)
k = 0
for i in comb:
    s = ''.join(i)
    if 'ЙД' in s or 'ЙК' in s or 'ЙС' in s or 'ЙТ' in s or 'ЙР' in s:
        k += 1
print(k)
