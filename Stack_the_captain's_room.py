from collections import Counter
input()
l = map(int,input().split())
temp = Counter(l)
t = [k for k in temp.elements() if temp[k] == 1]
print(t[0])
