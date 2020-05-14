class Graph:
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            raise IndexError("Vertex does not exist in this graph")


def earliest_ancestor(ancestors, starting_node):
    g = Graph()
    collection = [starting_node]

    g.add_vertex(starting_node)
    for v in ancestors:
        if v[0] not in g.vertices:
            g.add_vertex(v[0])
        if v[1] not in g.vertices:
            g.add_vertex(v[1])

    print(g.vertices)
    
    for e in ancestors:
        g.add_edge(e[1], e[0])

    #set of the vertex is its ancestor
    #if vertices[x] is empty means that's the end of the line
    
    
    return g.vertices


ancestors = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]


ancestors = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]
print(earliest_ancestor(t))