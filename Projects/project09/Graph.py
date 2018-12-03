import random


# Custom Graph error
class GraphError(Exception): pass


class Graph:
    """
    Graph Class ADT
    """

    class Edge:
        """
        Class representing an Edge in the Graph
        """
        __slots__ = ['source', 'destination']

        def __init__(self, source, destination):
            """
            DO NOT EDIT THIS METHOD!
            Class representing an Edge in a graph
            :param source: Vertex where this edge originates
            :param destination: ID of Vertex where this edge ends
            """
            self.source = source
            self.destination = destination

        def __eq__(self, other):
            return self.source == other.source and self.destination == other.destination

        def __repr__(self):
            return f"Source: {self.source} Destination: {self.destination}"

        __str__ = __repr__

    class Path:
        """
        Class representing a Path through the Graph
        """
        __slots__ = ['vertices']

        def __init__(self, vertices=[]):
            """
            DO NOT EDIT THIS METHOD!
            Class representing a path in a graph
            :param vertices: Ordered list of vertices that compose the path
            """
            self.vertices = vertices

        def __eq__(self, other):
            return self.vertices == other.vertices

        def __repr__(self):
            return f"Path: {' -> '.join([str(v) for v in self.vertices])}\n"

        __str__ = __repr__

        def add_vertex(self, vertex):
            self.vertices.append(vertex)

        def remove_vertex(self):
            self.vertices.pop()

        def last_vertex(self):
            if self.is_empty():
                return None
            return self.vertices[-1]

        def is_empty(self):
            return len(self.vertices) == 0

    class Vertex:
        """
        Class representing a Vertex in the Graph
        """
        __slots__ = ['ID', 'edges', 'visited', 'fake']

        def __init__(self, ID):
            """
            Class representing a vertex in the graph
            :param ID : Unique ID of this vertex
            """
            self.edges = []
            self.ID = ID
            self.visited = False
            self.fake = False

        def __repr__(self):
            return f"Vertex: {self.ID}"

        __str__ = __repr__

        def __eq__(self, other):
            """
            DO NOT EDIT THIS METHOD
            :param other: Vertex to compare
            :return: Bool, True if same, otherwise False
            """
            if self.ID == other.ID and self.visited == other.visited:
                if self.fake == other.fake and len(self.edges) == len(other.edges):
                    edges = set((edge.source.ID, edge.destination) for edge in self.edges)
                    difference = [e for e in other.edges if (e.source.ID, e.destination) not in edges]
                    if len(difference) > 0:
                        return False
                    return True

        def add_edge(self, destination):
            new_edge = Graph.Edge(self, destination)
            if new_edge not in self.edges:
                self.edges.append(new_edge)

        def degree(self):
            return len(self.edges)

        def get_edge(self, destination):
            for edge in self.edges:
                if edge.destination == destination:
                    return edge
            return None

        def get_edges(self):
            return self.edges

        def set_fake(self):
            self.fake = True

        def visit(self):
            self.visited = True

    def __init__(self, size=0, connectedness=1, filename=None):
        """
        DO NOT EDIT THIS METHOD
        Construct a random DAG
        :param size: Number of vertices
        :param connectedness: Value from 0 - 1 with 1 being a fully connected graph
        :param: filename: The name of a file to use to construct the graph.
        """
        assert connectedness <= 1
        self.adj_list = {}
        self.size = size
        self.connectedness = connectedness
        self.filename = filename
        self.construct_graph()

    def __eq__(self, other):
        """
        DO NOT EDIT THIS METHOD
        Determines if 2 graphs are IDentical
        :param other: Graph Object
        :return: Bool, True if Graph objects are equal
        """
        if len(self.adj_list) == len(other.adj_list):
            for key, value in self.adj_list.items():
                if key in other.adj_list:
                    if not self.adj_list[key] == other.adj_list[key]:
                        return False
                else:
                    return False
            return True
        return False

    def generate_edges(self):
        """
        DO NOT EDIT THIS METHOD
        Generates directed edges between vertices to form a DAG
        :return: A generator object that returns a tuple of the form (source ID, destination ID)
        used to construct an edge
        """
        random.seed(10)
        for i in range(self.size):
            for j in range(i + 1, self.size):
                if random.randrange(0, 100) <= self.connectedness * 100:
                    yield [i, j]

    def get_vertex(self, ID):
        try:
            return self.adj_list[ID]
        except KeyError:
            return None

    def construct_graph(self):

        if self.size <= 0 and self.filename is None:
            raise GraphError('bad size')
        if self.connectedness < 0 and self.connectedness >= 1: # has to be > 0 and <= 1
            raise GraphError('something is wrong with connectedness, whatever that means')

        if self.filename:
            # Construct graph from file
            fp = open(self.filename, 'r', encoding='ascii')

            for line in fp:
                line = line.split()  # [vertex, adjacent-vertex]

                vertex = line[0]
                adj_vertex = line[1]

                new_vertex = self.Vertex(vertex)
                new_adj_vertex = self.Vertex(adj_vertex)

                # Edge: connects a source (Vertex object) with a destination (Vertex id)

                if self.get_vertex(vertex) is None and self.get_vertex(adj_vertex) is None:
                    new_vertex.add_edge(adj_vertex)
                    self.adj_list[vertex] = new_vertex  # add new vertex,adj_node to graph
                    self.adj_list[adj_vertex] = new_adj_vertex

                elif self.get_vertex(vertex) and self.get_vertex(adj_vertex) is None:
                    self.adj_list[adj_vertex] = new_adj_vertex
                    self.adj_list[vertex].add_edge(adj_vertex)  # append new edge and adj_node to graph vertex
                elif self.get_vertex(vertex) and self.get_vertex(adj_vertex):
                    vert = self.get_vertex(vertex)
                    test_edge = self.Edge(vert, adj_vertex)
                    if test_edge not in self.adj_list[vertex].edges:
                        self.adj_list[vertex].edges.append(test_edge)  # add new edge if it DNE

        else:
            self.generate_edges()

    def BFS(self, start, target):
        pass

    def DFS(self, start, target, path=Path()):
        pass


def fake_emails(graph, mark_fake=False):
    def check_fake_emails(start, emails=list()):
        pass

    pass


if __name__ == '__main__':
    test = Graph(filename='test_construction_simple.txt')
    test.construct_graph()
    print(test)
