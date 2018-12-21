from itertools import product
first = list(map(int,input().split(" ")))
second = list(map(int,input().split(" ")))
l = list(product(first,second))
for tup in l:
    print(tup, end=" ")
