import networkx as nx
import numpy as np
import pickle
import random

alpha = 0.15

# open the graph which we created in A2Q3.0
f = open("graph.pickle", 'rb')
g = pickle.load(f)

# set an attribute "f" to all node
V = list(g.nodes)
for i in range(len(V)):
    v = V[i]
    g.nodes[v]["f"] = 0


n = len(V)
# M is the number of random walks
M = 2 * n

for i in range(M):
    if i % n == 0:
        print(i/n)
    # randomly choose a start node
    node_index = random.randint(0, len(V) - 1)
    v = V[node_index]
    while True:
        # should we stop?
        r_num = random.random()
        if r_num < alpha:
            # we stop
            break
        else:
            # we jump
            nbr = list(g[v])
            nbr_index = random.randint(0, len(nbr)-1)
            next_node = nbr[nbr_index]
            v = next_node
    # count for the stop node
    g.nodes[v]["f"] += 1

# calculate the difference between pi and f
total_diff = 0
for i in range(len(V)):
    v = V[i]
    real_pi = g.nodes[v]["real_pi"]
    f_v = g.nodes[v]["f"]
    diff = np.abs(real_pi - f_v/M)
    total_diff += diff

print("M:", M)
print("total_diff= ", total_diff)

# the result are:
# M = 2 * n
# total_diff = 0.5421592861728463
# M = 4 * n
# total_diff = 0.38263823819566245
# M = 6 * n
# total_diff = 0.31120519857200024
# M = 8 * n
# total_diff = 0.2702356795501741
# M = 10 * n
# total_diff = 0.2415049875688257

# more result
# M = 100 * n
# total_diff = 0.07629566739282231
# M = 1000 * n
# total_diff = 0.024066841672824482
