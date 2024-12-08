from collections import defaultdict


class Graph:
    def __init__(self, vertices):
        self.graph = defaultdict(list)
        self.ROW = vertices

    def add_edge(self, u, v, w):
        self.graph[u].append((v, w))

    def bfs(self, s, t, parent):
        visited = [False] * self.ROW
        queue = [s]
        visited[s] = True

        while queue:
            u = queue.pop(0)

            for v, w in self.graph[u]:
                if not visited[v] and w > 0:
                    queue.append(v)
                    visited[v] = True
                    parent[v] = u

        return visited[t]

    def ford_fulkerson(self, source, sink):
        parent = [-1] * self.ROW
        max_flow = 0

        while self.bfs(source, sink, parent):
            path_flow = float("Inf")
            s = sink

            while s != source:
                for v, w in self.graph[parent[s]]:
                    if v == s:
                        path_flow = min(path_flow, w)
                s = parent[s]

            max_flow += path_flow
            v = sink

            while v != source:
                u = parent[v]
                for i, (vertex, weight) in enumerate(self.graph[u]):
                    if vertex == v:
                        self.graph[u][i] = (vertex, weight - path_flow)
                for i, (vertex, weight) in enumerate(self.graph[v]):
                    if vertex == u:
                        self.graph[v][i] = (vertex, weight + path_flow)
                v = parent[v]

        return max_flow

    def display_graph(self):
        for u in self.graph:
            for v, w in self.graph[u]:
                print(f"{u} -> {v} (weight {w})")


# 예제 사용법
g = Graph(6)
g.add_edge(0, 1, 16)
g.add_edge(0, 2, 13)
g.add_edge(1, 2, 10)
g.add_edge(1, 3, 12)
g.add_edge(2, 1, 4)
g.add_edge(2, 4, 14)
g.add_edge(3, 2, 9)
g.add_edge(3, 5, 20)
g.add_edge(4, 3, 7)
g.add_edge(4, 5, 4)

source = 0
sink = 5

print(f"Max flow: {g.ford_fulkerson(source, sink)}")
print(g.display_graph())
