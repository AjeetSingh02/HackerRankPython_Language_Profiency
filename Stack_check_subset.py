n = int(input())
for i in range(n):
    input()
    A = list(map(int, input().split()))
    input()
    B = list(map(int,input().split()))
    print(all(ele in B for ele in A))
