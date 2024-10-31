import networkx as nx
import numpy as np
import pickle
import random

alpha = 0.15

# open the graph which we created in A2Q3.0
f = open("graph.pickle", 'rb')
g = pickle.load(f)

# set an attribute "s" to all node
V = list(g.nodes)
for i in range(len(V)):
    v = V[i]
    g.nodes[v]["s"] = 0


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
        # count
        g.nodes[v]["s"] += 1
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

# calculate the difference between pi and alpha * s
total_diff = 0
for i in range(len(V)):
    v = V[i]
    real_pi = g.nodes[v]["real_pi"]
    s_v = g.nodes[v]["s"]
    diff = np.abs(real_pi - alpha * s_v/M)
    total_diff += diff

print("M:", M)
print("total_diff= ", total_diff)

# the result are:
# M = 2 * n
# total_diff = 0.2617900633502739
# M = 4 * n
# total_diff = 0.1847371630417072
# M = 6 * n
# total_diff = 0.15137008965272244
# M = 8 * n
# total_diff = 0.13051422851130293
# M = 10 * n
# total_diff = 0.11647763142652445

# more result
# M = 100 * n
# total_diff = 0.03692385477490199
# M = 1000 * n
# total_diff = 0.011701718361304785
