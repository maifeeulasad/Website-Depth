import networkx as nx
import matplotlib.pyplot as plt

class Data:
    G = nx.Graph();
    mo=''
    links={}
    color_list = []

    @staticmethod
    def simple_name(url):
        if len(url)>15:
            return "..."+url[-5:]
        return url


    @staticmethod
    def get_links_as_list():
        labels = {}
        for x in Data.links:
            tem=Data.links[x]
            for y in tem:
                print(y)
                Data.G.add_node(y)
                if y.startswith(Data.mo):
                    Data.color_list.append('green')
                else:
                    Data.color_list.append('red')

                labels[y] = y
                #Data.G.add_edge(x, y)

        pos = nx.spring_layout(Data.G, scale=0.5)
        nx.draw(Data.G, pos,node_color=Data.color_list, labels= labels,  font_size=2)
        plt.axis('off')


        plt.show()

        return

    @staticmethod
    def visualize():

        '''

        Data.G.add_node('A')
        Data.G.add_node('B')
        Data.G.add_node('C')
        Data.G.add_node('D')
        Data.G.add_edge('A', 'B', weight=1)
        Data.G.add_edge('C', 'B', weight=1)
        Data.G.add_edge('B', 'D', weight=30)

        pos = nx.spring_layout(Data.G, scale=2)

        #color_map=['blue','red','green','red']
        #e_map=['blue','red','red']

        #nx.draw(Data.G, pos, node_color=color_map,edge_color=e_map, font_size=8)
        nx.draw(Data.G, pos, font_size=8)
        plt.axis('off')

        plt.show()


        :return:
        '''


        '''
        
        nx.draw_networkx_edges(Data.G, pos, width=1.0, alpha=0.5)
        nx.draw_networkx_edges(Data.G, pos,
                               edgelist=[(0, 1), (1, 2), (2, 3), (3, 0)],
                               width=8, alpha=0.5, edge_color='r')
        nx.draw_networkx_edges(Data.G, pos,
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
                
        nx.draw_networkx_labels(Data.G, pos, labels, font_size=16)

        '''

