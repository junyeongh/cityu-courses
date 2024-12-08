from collections import defaultdict, deque
# Find a flow of maximum value to the following network:

# (start, end, weight)
graph = [
    (0, 1, 16),
    (0, 2, 13),
    (1, 2, 10),
    (1, 3, 12),
    (2, 1, 4),
    (2, 4, 14),
    (3, 2, 9),
    (3, 5, 20),
    (4, 3, 7),
    (4, 5, 4),
]


def bfs(capacity, flow, source, sink, parent):
    visited = set()
    queue = deque([source])
    visited.add(source)

    while queue:
        u = queue.popleft()

        for v in capacity[u]:
            if v not in visited and capacity[u][v] - flow[u][v] > 0:
                queue.append(v)
                visited.add(v)
                parent[v] = u
                if v == sink:
                    return True
    return False


def max_flow(graph: list[tuple[int, int, int]], source: int, sink: int) -> tuple[int, list[list[int]]]:
    capacity = defaultdict(lambda: defaultdict(int))

    for u, v, w in graph:
        capacity[u][v] = w

    flow = defaultdict(lambda: defaultdict(int))
    parent = {}
    max_flow_value = 0
    paths = []

    while bfs(capacity, flow, source, sink, parent):
        path_flow = float("Inf")
        s = sink
        path = []

        while s != source:
            path_flow = min(path_flow, capacity[parent[s]][s] - flow[parent[s]][s])
            path.append(s)
            s = parent[s]
        path.append(source)
        path.reverse()
        paths.append(path)

        v = sink
        while v != source:
            u = parent[v]
            flow[u][v] += path_flow
            flow[v][u] -= path_flow
            v = parent[v]

        max_flow_value += path_flow

    return max_flow_value, paths


# Example usage
source = 0
sink = 5
max_flow_value, paths = max_flow(graph, source, sink)
print("The maximum possible flow is:", max_flow_value)
print("The paths of flow are:", paths)
