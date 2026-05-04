def disj(a, b):
    res = [[0]*len(a[0]) for _ in range(len(a))]
    for i in range(len(a)):
        for j in range(len(a[0])):
            if a[i][j] == 1 or b[i][j] == 1:
                res[i][j] = 1
            else:
                res[i][j] = 0
    return res


def transp(a):
    res = [[0]*len(a) for _ in range(len(a[0]))]
    for i in range(len(a)):
        for j in range(len(a[0])):
            res[j][i] = a[i][j]
    return res


def inv(a):
    res = [[0]*len(a[0]) for _ in range(len(a))]
    for i in range(len(a)):
        for j in range(len(a[0])):
            if a[i][j] == 1:
                res[i][j] = 0
            else:
                res[i][j] = 1
    return res


def sub(a, b):
    res = [[0]*len(a[0]) for _ in range(len(a))]
    for i in range(len(a)):
        for j in range(len(a[0])):
            res[i][j] = a[i][j] & (1 - b[i][j])
    return res


def mul(a, b):
    res = [[0]*len(b[0]) for _ in range(len(a))]
    for i in range(len(a)):
        for j in range(len(b[0])):
            for k in range(len(b)):
                if a[i][k] == 1 and b[k][j] == 1:
                    res[i][j] = 1
                    break
    return res