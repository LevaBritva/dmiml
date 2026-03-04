import numpy as np
import matplotlib.pyplot as plt
import networkx as nx

divisors = [1, 2, 3, 4, 6, 8, 12, 24]
n = len(divisors)

data = np.zeros((n, n), dtype=int)
for i, a in enumerate(divisors):
    for j, b in enumerate(divisors):
        if a != b:
            if b % a == 0:
                data[i, j] = 1

G = nx.from_numpy_array(data, create_using=nx.DiGraph)
H = nx.transitive_reduction(G)

mapping = {idx: val for idx, val in enumerate(divisors)}
H = nx.relabel_nodes(H, mapping)

layer_nodes = {
    0: [1],
    1: [2, 3],
    2: [4, 6],
    3: [8, 12],
    4: [24]
}

pos = {}
for layer in layer_nodes:
    nodes = layer_nodes[layer]
    count = len(nodes)
    for k, node in enumerate(nodes):
        offset = (k - (count - 1) / 2) * 1.5
        pos[node] = (offset, -layer)

plt.figure(figsize=(4, 4))
nx.draw(
    H,
    pos,
    with_labels=True,
    node_color='pink',
    node_size=800,
    arrows=True,
    font_size=12
)
plt.show()