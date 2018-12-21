if __name__ == '__main__':
    l = []
    for _ in range(int(input())):
        s = input().split()
        cmd, args = s[0], s[1:]
        if cmd !="print":
            cmd += "("+ ",".join(args) +")"
            eval("l."+cmd)
        else:
            print(l)
