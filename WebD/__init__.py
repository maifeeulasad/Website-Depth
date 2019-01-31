import networkx as nx
import matplotlib.pyplot as plt

class Data:
    G = nx.Graph();
    mo=''
    links={}
    color_list = []
    e_color=[]
    labels = {}

    @staticmethod
    def simple_name(url):
        if len(url)>15:
            return "..."+url[-5:]
        return url

    @staticmethod
    def url_type(url1,url2):
        if url1.startswith(Data.mo) and url2.startswith(Data.mo):
            return 0
        elif not url1.startswith(Data.mo) and url2.startswith(Data.mo):
            return 1
        elif url1.startswith(Data.mo) and not url2.startswith(Data.mo):
            return -1

    @staticmethod
    def get_links_as_list():
        for x in Data.links:
            tem=Data.links[x]
            for y in tem:
                print(y)
                Data.G.add_node(y)
                if y.startswith(Data.mo):
                    Data.color_list.append('green')
                else:
                    Data.color_list.append('red')
                Data.labels[y] = y
                Data.G.add_edge(x, y)
                v=Data.url_type(x,y)
                if v==0 :
                    Data.e_color.append('green')
                else:
                    Data.e_color.append('red')




        return

    @staticmethod
    def visualize():
        pos = nx.spring_layout(Data.G, scale=0.2)
        nx.draw(Data.G, pos, node_color=Data.color_list, labels=Data.labels, width=0.5, font_size=2)
        plt.axis('off')
        plt.show()