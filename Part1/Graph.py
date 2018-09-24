import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()

G.add_nodes_from([1,2,3,4,5])

G.add_edge(1,2)
G.add_edge(1,3)
G.add_edge(1,4)
G.add_edge(2,4)
G.add_edge(3,4)
G.add_edge(4,5)
G.add_edge(2,5)

nx.draw(G)

plt.show()