def minion_game(string):
    word, cons, vow = string, 0, 0
    for i in range(len(word)):
        if word[i] in ('A','E','I','O','U'):
            vow += (len(word)-i)        
        else:
            cons += (len(word)-i)
    if cons > vow:
        print("Stuart"+" " + str(cons))
    elif cons < vow:
        print("Kevin"+" " + str(vow))
    else:
        print("Draw")

if __name__ == '__main__':
    s = input()
    minion_game(s)
