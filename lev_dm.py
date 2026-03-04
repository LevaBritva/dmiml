import matplotlib.pyplot as plt
import networkx as nx
import numpy as np
from scipy.sparse.csgraph import floyd_warshall
from scipy.sparse import csr_array

n = 5
A = [(1,3), (2,3), (2,1), (5,4), (1,5), (2,3)]

R = np.zeros((n, n), dtype=int)
for pair in A:
    R[pair[0]-1, pair[1]-1] = 1

print("Матрица отношения:")
print(R)

G = nx.DiGraph()
G.add_nodes_from(range(1, n + 1))
G.add_edges_from(A)

plt.figure(figsize=(5, 5))
nx.draw(
    G,
    with_labels=True,
    arrows=True,
    node_color='lightblue',
    node_size=700
)
plt.show()


def reflexive(M):
    for i in range(n):
        if M[i, i] != 1:
            return False
    return True

def irreflexive(M):
    for i in range(n):
        if M[i, i] == 1:
            return False
    return True

def symmetric(M):
    return np.array_equal(M, M.T)

def antisymmetric(M):
    for i in range(n):
        for j in range(n):
            if i != j and M[i, j] == 1 and M[j, i] == 1:
                return False
    return True

def asymmetric(M):
    if not irreflexive(M):
        return False
    for i in range(n):
        for j in range(n):
            if M[i, j] and M[j, i]:
                return False
    return True

def transitive(M):
    graph = csr_array(M)
    dist = floyd_warshall(graph, directed=True)
    for i in range(n):
        for j in range(n):
            if dist[i, j] < np.inf and dist[i, j] != 1:
                if M[i, j] == 0:
                    return False
    return True

def total(M):
    for i in range(n):
        for j in range(n):
            if i != j:
                if not (M[i, j] or M[j, i]):
                    return False
    return True

print("\nСвойства отношения:")
print("Рефлексивное:", "да" if reflexive(R) else "нет")
print("Антирефлексивное:", "да" if irreflexive(R) else "нет")
print("Симметричное:", "да" if symmetric(R) else "нет")
print("Антисимметричное:", "да" if antisymmetric(R) else "нет")
print("Асимметричное:", "да" if asymmetric(R) else "нет")
print("Транзитивное:", "да" if transitive(R) else "нет")
print("Линейное (полное):", "да" if total(R) else "нет")