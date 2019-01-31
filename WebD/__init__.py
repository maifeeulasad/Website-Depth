import networkx as nx
import matplotlib.pyplot as plt

class Data:
    mo=''
    links={}
    l=[]
    child_links=[]
    outer_links=[]

    @staticmethod
    def get_links_as_list():
        res=[]
        for x in Data.links:
            tem=Data.links[x]
            for y in tem:
                print(y)
                res.insert(0,(x,y))
                if y not in Data.child_links and y.startswith(Data.mo):
                    Data.child_links.insert(0,y)
                elif y not in Data.outer_links:
                    if y.startswith(Data.mo):
                        pass
                    else:
                        Data.outer_links.insert(0, y)
        Data.l=res
        return res

    @staticmethod
    def visualize():
        Data.get_links_as_list()
        G = nx.cubical_graph()
        pos = nx.spring_layout(G)
        nx.draw_networkx_nodes(G,
                               20,
                               nodelist=Data.child_links,
                               node_color='r',
                               node_size=500,
                               alpha=0.5)
        nx.draw_networkx_nodes(G,
                               20,
                               nodelist=Data.outer_links,
                               node_color='b',
                               node_size=500,
                               alpha=0.5)
        nx.draw_networkx_edges(G,
                               20,
                               width=1.0,
                               alpha=0.5)
        nx.draw_networkx_edges(G,
                               20,
                               edgelist=Data.l,
                               width=8,
                               alpha=0.5,
                               edge_color='r')

        '''
        
        nx.draw_networkx_edges(G, pos, width=1.0, alpha=0.5)
        nx.draw_networkx_edges(G, pos,
                               edgelist=[(0, 1), (1, 2), (2, 3), (3, 0)],
                               width=8, alpha=0.5, edge_color='r')
        nx.draw_networkx_edges(G, pos,
                               edgelist=[(4, 5), (5, 6), (6, 7), (7, 4)],
                               width=8, alpha=0.5, edge_color='b')
                               

        # some math labels
        labels = {}
        labels[0] = r'$a$'
        labels[1] = r'$b$'
        labels[2] = r'$c$'
        labels[3] = r'$d$'
        labels[4] = r'$\alpha$'
        labels[5] = r'$\beta$'
        labels[6] = r'$\gamma$'
        labels[7] = r'$\delta$'
                
        nx.draw_networkx_labels(G, pos, labels, font_size=16)

        '''

        plt.axis('off')
        plt.show()  # display