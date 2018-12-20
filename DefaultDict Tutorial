from collections import defaultdict
n,m = map(int,input().split())
dict_n = defaultdict(list)
counter = 1
for _ in range(n):
    dict_n[input()].append(counter)
    counter += 1
for _ in range(m):
    word = input()
    if word in dict_n:
        print(" ".join(map(str,dict_n[word])))
    else:
        print(-1)
