from itertools import combinations_with_replacement
from functools import reduce
inp = input().split(" ")
string = sorted(inp[0])
l = list(combinations_with_replacement(string,int(inp[1])))
temp = [reduce(lambda x,y:x+y,tup) for tup in l]
for ele in temp:
    print(ele)
