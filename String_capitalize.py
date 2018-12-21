def solve(s):
    name = s[0].upper() + s[1:]
    newName = ""    
    flag = 0
    for letter in name:
        if flag == 0:
            newName += letter
            if letter == " ":
                flag = 1
        else:
            if letter.isalnum():
                newName += letter.upper()
                flag = 0
            else:
                newName += letter
    return newName
