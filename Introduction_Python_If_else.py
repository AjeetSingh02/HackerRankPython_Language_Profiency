N = int(input())
if N %2 == 0 and (N in range(2,6) or N > 20):
    print("Not Weird")
else:
    print("Weird") 

