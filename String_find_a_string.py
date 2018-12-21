def count_substring(string, sub_string):
    l = []
    a = string
    b = sub_string
    for i in range(0,len(a)-len(b)+1):
        l.append(a[i:i+len(b)])
    return l.count(b)
    
if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    count = count_substring(string, sub_string)
    print(count)
