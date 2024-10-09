import random
import numpy as np


def load_graph(file_path):
    edges = []
    with open(file_path, "r") as file:
        for line in file:
            if line.startswith("#"):
                continue  # Skip comment lines
            parts = line.strip().split()
            if len(parts) == 2:
                from_node, to_node = map(int, parts)
                edges.append((from_node, to_node))
    return edges

def calculate_normalized_degrees(graph_edges):
    node_degrees = {}
    for from_node, to_node in graph_edges:
        if from_node not in node_degrees:
            node_degrees[from_node] = 0
        if to_node not in node_degrees:
            node_degrees[to_node] = 0
        node_degrees[from_node] += 1
        node_degrees[to_node] += 1

    total_degrees = sum(node_degrees.values())
    normalized_degrees = {
        node: degree / total_degrees for node, degree in node_degrees.items()
    }
    return normalized_degrees

def simulate_random_walk(graph_edges, num_steps, seed=42):
    random.seed(seed)

    neighbors = {}
    for from_node, to_node in graph_edges:
        if from_node not in neighbors:
            neighbors[from_node] = []
        if to_node not in neighbors:
            neighbors[to_node] = []
        neighbors[from_node].append(to_node)
        neighbors[to_node].append(from_node)

    # Start from a random node
    current_node = random.choice(list(neighbors.keys()))
    visit_counts = {node: 0 for node in neighbors.keys()}

    for _ in range(num_steps):
        visit_counts[current_node] += 1
        current_node = random.choice(neighbors[current_node])

    return visit_counts

def calculate_empirical_frequencies(visit_counts, num_steps):
    empirical_frequencies = {
        node: count / num_steps for node, count in visit_counts.items()
    }
    return empirical_frequencies

def calculate_l1_distance(vector1, vector2):
    return np.sum(
        np.abs(np.array(list(vector1.values())) - np.array(list(vector2.values())))
    )

# Load the graph
file_path = "com-dblp.txt"
graph_edges = load_graph(file_path)

# Calculate the normalized degree vector
normalized_degrees = calculate_normalized_degrees(graph_edges)

# Simulate the random walk
num_steps = 1000000  # Number of steps in the random walk
visit_counts = simulate_random_walk(graph_edges, num_steps)

# Calculate the empirical frequency vector
empirical_frequencies = calculate_empirical_frequencies(visit_counts, num_steps)

# Calculate the L1 distance between the normalized degree vector and the empirical frequency vector
l1_distance = calculate_l1_distance(normalized_degrees, empirical_frequencies)

# Print the L1 distance rounded to three decimal places
print(f"L1 Distance: {l1_distance:.3f}")