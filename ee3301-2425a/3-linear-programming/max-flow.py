import numpy as np
from scipy.optimize import linprog

# Define the network
edges = [
    (0, 1, 3), (0, 2, 2), (0, 3, 2),
    (1, 4, 5), (1, 5, 1),
    (2, 4, 3), (2, 5, 1), (2, 6, 1),
    (3, 5, 1),
    (4, 7, 4),
    (5, 7, 2),
    (6, 7, 4)
]

# Number of nodes
n_nodes = 8

# Create the objective function (we'll maximize the flow out of node 0)
c = np.zeros(len(edges))
for i, (u, v, _) in enumerate(edges):
    if u == 0:
        c[i] = -1  # Negative because linprog minimizes by default

# Create the equality constraints (flow conservation)
A_eq = np.zeros((n_nodes, len(edges)))
b_eq = np.zeros(n_nodes)

for i, (u, v, _) in enumerate(edges):
    A_eq[u, i] += 1
    A_eq[v, i] -= 1

# Set the flow conservation constraint for source and sink
A_eq = A_eq[1:-1]  # Remove constraints for source (0) and sink (7)
b_eq = b_eq[1:-1]

# Create the inequality constraints (capacity constraints)
A_ub = np.eye(len(edges))
b_ub = np.array([cap for _, _, cap in edges])

# Solve the linear programming problem
res = linprog(c, A_ub=A_ub, b_ub=b_ub, A_eq=A_eq, b_eq=b_eq, method='highs')

if res.success:
    max_flow = -res.fun  # Remember, we minimized the negative of the flow
    print(f"Maximum flow: {max_flow}")
    print("\nFlow on each edge:")
    for i, (u, v, cap) in enumerate(edges):
        print(f"Edge {u} -> {v}: {res.x[i]:.2f} / {cap}")
else:
    print("Failed to find a solution.")
