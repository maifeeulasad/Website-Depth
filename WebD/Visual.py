import networkx as nx
import matplotlib.pyplot as plt

G = nx.MultiDiGraph()

G.add_edges_from([
    (1, 2),
    (2, 3),
    (3, 2),
    (2, 1),
])

plt.figure(figsize=(2,2))
nx.draw(G)
plt.show()