from itertools import combinations
n, l, k = int(input()), input().split(), int(input())
c = list(combinations(l,k))
f = list(filter(lambda x:"a" in x,c))
print(round((len(f)/len(c)),3))
