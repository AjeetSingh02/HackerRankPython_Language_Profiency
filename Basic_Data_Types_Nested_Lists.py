if __name__ == '__main__':
    students, scores = [], []
    for _ in range(int(input())):
        name, score = input(), float(input())
        students.append([name,score])
        scores.append(score)
    sec_high_score = sorted(list(set(scores)))[1]
    names = []
    for data in students:
        if data[1] == sec_high_score:
            names.append(data[0])
    names = sorted(names)
    for name in names:
        print(name)
