from collections import OrderedDict
od = OrderedDict()
for _ in range(int(input())):
    line = input().split()
    item, price = " ".join(line[:-1]), int(line[-1])
    if item in od:
        od[item] += price
    else:
        od[item] = price
for k,v in od.items():
    print(" ".join([k,str(v)]))
