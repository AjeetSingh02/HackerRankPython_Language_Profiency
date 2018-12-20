valChar = [".","-","+"]
for _ in range(int(input())):
    string, f = input(), 0
    if string.count(".") == 1 and (string[0].isnumeric() == True or string[0] in valChar) and string[-1] != ".":
        for char in string[1:]:
            if char != "." and char.isnumeric() == False:
                f = 1
                print("False")
                break
        if f == 0:
            print("True")     
    else:
        print("False")
