from collections import deque


class DirectedGraph:
    def __init__(self):
        self.vertices = []
        self.edges = {}

    def add_vertex(self, vertex):
        if vertex not in self.edges:
            self.vertices.append(vertex)
            self.edges[vertex] = []

    def add_edge(self, start, end):
        self.add_vertex(start)
        self.add_vertex(end)
        if end not in self.edges[start]:
            self.edges[start].append(end)


def bfs(graph, start):
    if start not in graph.edges:
        return []

    result = []
    visited = set()
    queue = deque([start])
    visited.add(start)

    while queue:
        vertex = queue.popleft()
        result.append(vertex)
        for neighbor in graph.edges[vertex]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
    return result


def edges_to_matrix(edges):
    vertices = []
    for start, end in edges:
        if start not in vertices:
            vertices.append(start)
        if end not in vertices:
            vertices.append(end)

    matrix = [[0] * len(vertices) for _ in range(len(vertices))]
    for start, end in edges:
        add_edge_matrix(vertices, matrix, start, end)
    return vertices, matrix


def add_vertex_matrix(vertices, matrix, vertex):
    if vertex in vertices:
        return
    vertices.append(vertex)
    for row in matrix:
        row.append(0)
    matrix.append([0] * len(vertices))


def add_edge_matrix(vertices, matrix, start, end):
    add_vertex_matrix(vertices, matrix, start)
    add_vertex_matrix(vertices, matrix, end)
    i = vertices.index(start)
    j = vertices.index(end)
    matrix[i][j] = 1


def edges_to_adj_list(edges):
    graph = {}
    for start, end in edges:
        add_edge_list(graph, start, end)
    return graph


def add_vertex_list(graph, vertex):
    if vertex not in graph:
        graph[vertex] = []


def add_edge_list(graph, start, end):
    add_vertex_list(graph, start)
    add_vertex_list(graph, end)
    if end not in graph[start]:
        graph[start].append(end)


def print_matrix(vertices, matrix):
    print("   ", " ".join(str(vertex) for vertex in vertices))
    for vertex, row in zip(vertices, matrix):
        print(vertex, "", " ".join(str(value) for value in row))


print("Задание 1. Ориентированный граф")
graph = DirectedGraph()
graph.add_vertex("A")
graph.add_edge("A", "B")
graph.add_edge("A", "C")
graph.add_edge("B", "D")
graph.add_edge("C", "D")
graph.add_edge("C", "E")
print("вершины:", graph.vertices)
print("ребра:", graph.edges)

print("\nЗадание 2. Обход в ширину (BFS)")
print("из A:", bfs(graph, "A"))
print("из C:", bfs(graph, "C"))

print("\nЗадание 3. Матрица смежности")
edges = [("A", "B"), ("A", "C"), ("B", "D"), ("C", "D"), ("C", "E")]
vertices, matrix = edges_to_matrix(edges)
print_matrix(vertices, matrix)

add_vertex_matrix(vertices, matrix, "F")
add_edge_matrix(vertices, matrix, "E", "F")
print("после вершины F и ребра E -> F:")
print_matrix(vertices, matrix)

print("\nЗадание 4. Список смежности")
adj = edges_to_adj_list(edges)
print("из ребер:", adj)
add_vertex_list(adj, "F")
add_edge_list(adj, "E", "F")
print("после вершины F и ребра E -> F:", adj)