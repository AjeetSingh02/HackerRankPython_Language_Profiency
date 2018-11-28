from itertools import combinations
from functools import reduce
inp = input().split(" ")

l = [list(combinations(inp[0],i)) for i in range(1,int(inp[1])+1)]
for small_list in l:
    temp = []
    for tup in small_list:
        sortTup = sorted(tup)
        s = [reduce(lambda x,y:x+y, sortTup)]
        temp.append(s[0])
    temp.sort()
    for ele in temp:
        print(ele)

