I = list(map(int,input().split(" ")))
N,M = I[0],I[1]
l = []
for i in range(1,N,2):
    factor = int((M - 3*i)/2)
    temp = factor * "-" + ".|." * i + factor * "-"
    l.append(temp)
    print(temp)     
factor = int((M-7)/2)
print(factor * "-" + "WELCOME" + factor * "-")
for _ in l[::-1]:
    print(_)

