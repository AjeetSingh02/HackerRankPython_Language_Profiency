def print_rangoli(size):
    dash = "-"
    N = size
    alphabets = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    alpha = alphabets[:N]
    temp = []

    for j in range(N):
        res = ""
        for i in range(len(alpha)-1,j,-1):
            res += alpha[i] + dash
        for i in range(j,len(alpha)):
            res += alpha[i] + dash
        res = res[0:len(res)-1]
        
        temp.append(res.center(4*(N-1) + 1,"-"))
        
    for i in temp[::-1]:
        print(i)
    for i in temp[1:]:
        print(i)

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
