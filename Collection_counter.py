from collections import Counter

number_of_shoes = int(input())
list_of_shoe_sizes = list(map(int, input().split(" ")))
number_of_customers = int(input())
total_count = 0
shoes = Counter(list_of_shoe_sizes)
for i in range(number_of_customers):
    inp = list(map(int, input().split(" ")))
    if inp[0] in list(shoes.keys()) and shoes[inp[0]] > 0:
        total_count += inp[1]
        shoes[inp[0]] -= 1
print(total_count)


