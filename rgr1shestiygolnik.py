from itertools import product

r = [[0,1,2,3,4,5],[1,2,3,4,5,0],[2,3,4,5,0,1],[3,4,5,0,1,2],[4,5,0,1,2,3],[5,0,1,2,3,4]]
s = [[0,5,4,3,2,1],[2,1,0,5,4,3],[4,3,2,1,0,5],[1,0,5,4,3,2],[3,2,1,0,5,4],[5,4,3,2,1,0]]

G = r + s
names = ["r"+str(i) for i in range(6)] + ["s"+str(i) for i in range(6)]

def mul(a, b):
    res = []
    for i in range(6):
        res.append(a[b[i]])
    return res

def name_of(p):
    for i in range(len(G)):
        if G[i] == p:
            return names[i]

print("Таблица умножения группы D6:\n")

print("   ", "  ".join(names))
print("   " + "-" * 68)

table = []
for a in G:
    row = []
    for b in G:
        row.append(name_of(mul(a, b)))
    table.append(row)
    print(name_of(a), "|", "  ".join(row))


print("\nПроверка аксиом группы:")

closed = True
for row in table:
    for x in row:
        if x not in names:
            closed = False

neutral = True
for i in range(len(G)):
    if name_of(mul(G[0], G[i])) != names[i] or name_of(mul(G[i], G[0])) != names[i]:
        neutral = False

has_inverse = True
for a in G:
    ok = False
    for b in G:
        if mul(a, b) == G[0]:
            ok = True
            break
    if not ok:
        has_inverse = False

assoc = True
for a, b, c in product(G, repeat=3):
    if mul(mul(a, b), c) != mul(a, mul(b, c)):
        assoc = False

print("1. Замкнутость:", "да" if closed else "нет")
print("2. Нейтральный элемент:", "да" if neutral else "нет")
print("3. Обратные элементы:", "да" if has_inverse else "нет")
print("4. Ассоциативность:", "да" if assoc else "нет")

is_group = closed and neutral and has_inverse and assoc
print("\nЭто группа:", "ДА" if is_group else "НЕТ")

if is_group:
    abelian = True
    for a in G:
        for b in G:
            if mul(a, b) != mul(b, a):
                abelian = False

    print("Группа абелева:", "ДА" if abelian else "НЕТ")

    if not abelian:
        print("\nПример некоммутативности:")
        for a in G:
            for b in G:
                if mul(a, b) != mul(b, a):
                    print(name_of(a), "*", name_of(b), "!=", name_of(b), "*", name_of(a))
                    break
            else:
                continue
            break