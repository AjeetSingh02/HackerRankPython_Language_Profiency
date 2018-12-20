from collections import deque
d = deque()
for _ in range(int(input())):
    cmd, *arg = input().split()
    getattr(d,cmd)(*arg)
print(*[item for item in d])
