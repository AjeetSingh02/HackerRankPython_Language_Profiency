from collections import OrderedDict
od, distinct = OrderedDict(), 0
for _ in range(int(input())):
    word = input()
    if word in od:
        od[word] += 1
    else:
        distinct += 1
        od[word] = 1
print(distinct)
for v in od.values():
    print(v, end=" ")
