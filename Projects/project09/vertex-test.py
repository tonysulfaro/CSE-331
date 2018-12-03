from Graph import Graph

vertex = Graph.Vertex(1)

vertex.add_edge(2)
vertex.add_edge(3)
vertex.add_edge(4)

assert(vertex.degree() == 3)
assert(vertex.visited is False)

vertex.visit()

assert(vertex.visited is True)

edge1 = vertex.get_edge(2)
edge_none = vertex.get_edge(5)

assert(edge1.source == vertex and edge1.destination == 2)
assert(edge_none is None)