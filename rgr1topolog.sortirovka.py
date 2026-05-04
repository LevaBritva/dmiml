from collections import deque

def covering(m, n):
    c = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if i != j and m[i][j] == 1:
                flag = False
                for k in range(n):
                    if k != i and k != j:
                        if m[i][k] == 1 and m[k][j] == 1:
                            flag = True
                            break
                if not flag:
                    c[i][j] = 1
    return c


def tsort(c, labels):
    n = len(labels)
    indeg = [0]*n

    for i in range(n):
        for j in range(n):
            if c[i][j] == 1:
                indeg[j] += 1

    q = deque()
    for i in range(n):
        if indeg[i] == 0:
            q.append(i)

    order = []

    while len(q) > 0:
        v = q.popleft()
        order.append(v)

        for j in range(n):
            if c[v][j] == 1:
                indeg[j] -= 1
                if indeg[j] == 0:
                    q.append(j)

    return order