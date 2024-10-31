import networkx as nx
import random
import numpy as np
# import matplotlib.pyplot as plt

f = open("com-dblp.txt")
line = f.readline()
print(line)  # Undirected graph: ../../data/output/dblp.ungraph.txt
line = f.readline()
print(line)  # DBLP
line = f.readline()
print(line)  # Nodes: 317080 Edges: 1049866
line = f.readline()
print(
    line
)  # FromNodeId	ToNodeId (There is an undirected edge between FromNodeId and ToNodeId)

g = nx.Graph()
for i in range(1049866):
    line = f.readline()
    line = line[:-1]
    line = line.split("\t")
    # print(line)
    a = int(line[0])
    b = int(line[1])
    # print(a)
    # print(b)
    g.add_edge(a, b)
print("#####")
# #
# # #
# # # set an attribute "count" to all nodes
V = list(g.nodes)
for i in range(len(V)):
    node = V[i]
    g.nodes[node]["count"] = 0

# randomly choose a starting node
node_index = random.randint(0, len(V) - 1)
node = V[node_index]
g.nodes[node]["count"] += 1

M = 2 * 10000000
for i in range(M):
    nbr = list(g[node])
    nbr_index = random.randint(0, len(nbr) - 1)
    next_node = nbr[nbr_index]
    node = next_node
    g.nodes[node]["count"] += 1

total_diff = 0
D = 1049866 * 2
for i in range(len(V)):
    node = V[i]
    nbr = list(g[node])
    count = g.nodes[node]["count"]
    diff = np.abs(len(nbr) / D - count / M)
    total_diff += diff

print(M)
print(total_diff)
