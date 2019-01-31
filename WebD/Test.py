import networkx as nx
import matplotlib.pyplot as plt

list=[]
G = nx.Graph()
#plt.ion()

options = {
    'node_color': 'yellow',
    'node_size': 100,
    'width': 3,
    'arrowstyle': '-|>',
    'arrowsize': 12,
}

for i in range (2):
    list.append((i,i))
    G.add_edges_from(list)
    plt.figure(figsize=(5,5))
    nx.draw(G,with_labels=True,**options)
    #plt.show()
    plt.pause(1)
    #plt.clf()
    plt.close()


nx.draw(G,with_labels=True,**options)
plt.show()

#plt.waitforbuttonpress()