import networkx as nx
import matplotlib.pyplot as plt

class Data:
    links={}

    @staticmethod
    def get_links_as_list():
        res=[]
        for x in Data.links:
            tem=Data.links[x]
            for y in tem:
                res.insert(0,(x,y))
        return res

    @staticmethod
    def hello():
        print("hello")


    @staticmethod
    def visualize():

        G = nx.MultiDiGraph()

        G.add_edges_from(Data.get_links_as_list())

        plt.figure(figsize=(5, 5))
        nx.draw(G, with_labels=True)
        plt.show()


