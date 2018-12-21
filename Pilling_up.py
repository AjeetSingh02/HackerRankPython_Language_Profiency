from collections import deque
for _ in range(int(input())):
    d, f = deque(), 0
    n = input()
    d.extend(list(map(int,input().split())))
    last_dim = max([d[0],d[-1]])
    while len(d) > 0:
        if d[0] > d[-1]:
            current_dim = d.popleft()
        else:
            current_dim = d.pop()
        if current_dim > last_dim:
            f = 1
            print("No")
            break
        last_dim = current_dim
    if f == 0:
        print("Yes")

