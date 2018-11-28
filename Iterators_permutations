from itertools import permutations
from functools import reduce

inp = input().split(" ")
l = list(permutations(inp[0],int(inp[1])))
li = [reduce(lambda x,y:x+y, tup) for tup in l]

li.sort()
for ele in li:
    print(ele)
