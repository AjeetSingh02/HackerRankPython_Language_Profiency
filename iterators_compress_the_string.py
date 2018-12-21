string, count = input(), 1
for i in range(len(string)):
    if i == (len(string) - 1):
        print("({0}, {1}) ".format(count,string[i]), end = "")
    elif string[i] != string[i+1]:
        print("({0}, {1}) ".format(count,string[i]), end = "")
        count = 1
    else:
        count += 1
