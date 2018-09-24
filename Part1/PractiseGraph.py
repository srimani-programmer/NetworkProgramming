import networkx as nx
import matplotlib.pyplot as plt

g = nx.Graph()

g.add_nodes_from([1,2,3,4,5,6,7,8,9,10,11,12])

g.add_edge(1,2)
g.add_edge(2,3)
g.add_edge(3,4)
g.add_edge(4,5)
g.add_edge(5,6)
g.add_edge(5,12)
g.add_edge(7,8)
g.add_edge(8,9)
g.add_edge(9,10)
g.add_edge(10,11)
g.add_edge(11,12)
g.add_edge(12,1)

plt.title('Solve Me If You Can')
nx.draw(g)

plt.show()