import networkx as nx
import pickle
import numpy as np

alpha = 0.15
f = open("com-dblp.txt")
line = f.readline()
print(line)
line = f.readline()
print(line)
line = f.readline()
print(line)
line = f.readline()
print(line)

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

# set an attribute "old_pi" and "new_pi" to all nodes
V = list(g.nodes)
n = len(V)
for i in range(len(V)):
    v = V[i]
    g.nodes[v]["old_pi"] = 1/n
    g.nodes[v]["new_pi"] = 1/n

# power iterations
iterations_count = 0
while True:
    iterations_count += 1
    # iterate
    for i in range(len(V)):
        v = V[i]
        g.nodes[v]["old_pi"] = g.nodes[v]["new_pi"]
        g.nodes[v]["new_pi"] = 0
    for i in range(len(V)):
        v = V[i]
        temp = 0
        for u in g.neighbors(v):
            temp += g.nodes[u]["old_pi"] / len(list(g.neighbors(u)))
        g.nodes[v]["new_pi"] = (1-alpha) * temp + alpha/n
    # check convergence
    tol = 0
    for i in range(len(V)):
        v = V[i]
        tol += np.abs(g.nodes[v]["old_pi"] - g.nodes[v]["new_pi"])
    print("iteration: ", iterations_count)
    print(tol)
    if tol < 1e-9:
        print("converge")
        break

# set an attribute "real_pi" to all nodes
for i in range(len(V)):
    v = V[i]
    g.nodes[v]["real_pi"] = g.nodes[v]["new_pi"]

# we store our graph
f = open("graph.pickle", 'wb')
pickle.dump(g, f)
f.close()
