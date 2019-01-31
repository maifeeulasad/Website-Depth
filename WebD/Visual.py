import networkx as nx
import matplotlib.pyplot as plt

G = nx.MultiDiGraph()

G.add_edges_from([
    (0, 2),
    (2, 3),
    (3, 2),
    (2, 1),
    (0, 1),
])

plt.figure(figsize=(5,5))
nx.draw(G,with_labels=True)
plt.show()