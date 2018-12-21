N, X = map(int,input().split())
unzip = []
for _ in range(X):
   unzip.append(map(float,input().split()))
for tup in zip(*unzip):
    print("{0:.1f}".format(sum(tup)/X))
