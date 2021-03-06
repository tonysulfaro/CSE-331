######################################################################
# PROJECT: Graphs, and all the frustrations that come with them haha
# Author: Tony Sulfaro
######################################################################

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
            """
            add vertex to vertices list
            :param vertex: vertex to add
            :return: None
            """
            self.vertices.append(vertex)

        def remove_vertex(self):
            """
            pop last vertex from vertices list
            :return: None
            """
            if self.is_empty():
                return None
            self.vertices.pop()

        def last_vertex(self):
            """
            get but do not remove last vertex in vertices list
            :return:
            """
            if self.is_empty():
                return None
            return self.vertices[-1]

        def is_empty(self):
            """
            check if vertices is empty
            :return: Bool - is empty
            """
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
            """
            add edge to vertex
            :param destination: adj-vertex to self
            :return: None
            """
            new_edge = Graph.Edge(self, destination)
            if new_edge not in self.edges:
                self.edges.append(new_edge)

        def degree(self):
            """
            how many edges a vertex has
            :return: int - degree
            """
            return len(self.edges)

        def get_edge(self, destination):
            """
            search for particular edge on vertex
            :param destination: key to look for in adj-vertex
            :return: edge if found, None if not found
            """
            for edge in self.edges:
                if edge.destination == destination:
                    return edge
            return None

        def get_edges(self):
            """
            return edge list for vertex
            :return: List(Edge)
            """
            return self.edges

        def set_fake(self):
            """
            mark vertex as fake
            :return: None
            """
            self.fake = True

        def visit(self):
            """
            mark vertex as visited
            :return:
            """
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
        """
        try to retrieve vertex from dict
        :param ID: Vertex to search for
        :return: Vertex if found, None if not
        """
        try:
            return self.adj_list[ID]
        except KeyError:
            return None

    def construct_graph(self):
        """
        generate graph from file or with function provided in generate_edges
        :return: None
        """

        def add_new_edge(vertex, adj_vertex):
            """
            adds new edge to graph if edge DNE [vertex]->[adj_vertex]
            :param vertex: starting vertex to add edge to its edge list
            :param adj_vertex: vertex that is adjacent to vertex
            :return: None
            """

            new_vertex = self.Vertex(vertex)
            new_adj_vertex = self.Vertex(adj_vertex)

            # Edge: connects a source (Vertex object) with a destination (Vertex id)

            # both vertex and adj_vertex not in graph
            if self.get_vertex(vertex) is None and self.get_vertex(adj_vertex) is None:
                new_vertex.add_edge(adj_vertex)
                self.adj_list[vertex] = new_vertex  # add new vertex,adj_node to graph
                self.adj_list[adj_vertex] = new_adj_vertex

            # vertex exists in graph but adj_vertex does not
            elif self.get_vertex(vertex) and self.get_vertex(adj_vertex) is None:
                self.adj_list[adj_vertex] = new_adj_vertex
                self.adj_list[vertex].add_edge(adj_vertex)  # append new edge and adj_node to graph vertex

            # vertex DNE in graph but adj_vertex does
            elif self.get_vertex(vertex) is None and self.get_vertex(adj_vertex):
                new_vertex.add_edge(adj_vertex)
                self.adj_list[vertex] = new_vertex

            # both vertices exist in adj_list
            elif self.get_vertex(vertex) and self.get_vertex(adj_vertex):
                vert = self.get_vertex(vertex)
                test_edge = self.Edge(vert, adj_vertex)
                if test_edge not in self.adj_list[vertex].edges:
                    self.adj_list[vertex].edges.append(test_edge)  # add new edge if it DNE

        if self.filename:
            # Construct graph from file
            fp = open(self.filename, 'r', encoding='ascii')
            for line in fp:
                line = line.split()  # [vertex, adjacent-vertex]

                vertex = int(line[0])
                adj_vertex = int(line[1])
                add_new_edge(vertex, adj_vertex)
        else:
            # no file provided, use built in function
            if self.size <= 0:
                raise GraphError('bad size')
            if not 0 < self.connectedness <= 1:  # has to be (0,1]
                raise GraphError('something is wrong with connectedness, whatever that means')

            edges = self.generate_edges()

            # add edges from generate_edges()
            for edge in edges:
                vertex = edge[0]
                adj_vertex = edge[1]
                add_new_edge(vertex, adj_vertex)

    def BFS(self, start, target):
        """
        check distances from start node until target is found or not found
        :param start: ID of vertex to start search at
        :param target: target ID to stop search and return path at
        :return: Path - path taken to get from start to target
        """

        def BFS_List(start, target):

            stack = [(start, [start])]  # initialize stack to save visited vertices
            while stack:
                (vertex, path) = stack.pop()  # get list element
                vert = self.get_vertex(vertex)
                new_edges = []
                for edge in vert.edges:  # get new edges for vertex
                    if edge.destination not in path:
                        new_edges.append(edge)
                vert.edges = new_edges
                for next in vert.edges:
                    if next.destination == target:
                        yield path + [next.destination]
                    else:
                        stack.append((next.destination, path + [next.destination]))

        path = self.Path([])
        path_result = BFS_List(start, target)  # after getting traversal in list form, convert to Path
        print(path_result)
        for vertex_id in path_result:
            for item in vertex_id:
                path.add_vertex(item)
                if item == target:
                    return path

    def DFS(self, start, target, path=Path()):
        """
        depth first search on graph
        :param start: int - start node
        :param target: int - target node
        :param path: path to get from start to target
        :return: None
        """
        # path.add_vertex(start)
        vert = self.adj_list[start]
        vert.visit()
        print(path)

        for edge in vert.edges:  # for every outgoing edge from u

            if target in path.vertices:
                return path

            v = edge.destination

            for edge in vert.edges:  # if vertex in adj_edges then add it to path along with self and return
                if edge.destination == target:
                    path.add_vertex(start)
                    path.add_vertex(edge.destination)
                    return path
            if v == target:  # path has been found
                path.add_vertex(edge.destination)
                print('found', path)
                return path
            if v not in path.vertices:  # v is an unvisited vertex
                path.add_vertex(start)
                # path.add_vertex(edge.destination)  # e is the tree edge that discovered v
                self.DFS(v, target, path)  # recursively explore from v

        if target not in path.vertices:
            path.remove_vertex()
        else:
            return path


def fake_emails(graph, mark_fake=False):
    """
    finds fake emails
    * if a vertex has a degree 0 then it is a likely candidate for a fake email address
    * given, email messages are coming into the vertex, but no email messages are sent from it
    :param graph: graph to find fakes and modify in place
    :param mark_fake: weather or not to mark vertices as fake
    :return: List - Fake vertices
    """

    fakes = []

    # get fake emails for a vertex
    def check_fake_emails(start, emails=list()):
        """
        * Given a start Vertex ID, find all fake email addressses that can be reached from that ID
        * remove the edge connecting to the fake address.
        :param start: starting vertex ID
        :param emails: emails that are fake
        :return: emails - list of fake emails that can be reached
        """

        # for vertex in verticies
        # if an edge.destination in emails:
        # remove edge from source to fake email

        # get a traversal of all vertices that can be reached from start
        def dfs_traversal(graph, start, visited=None):
            """
            return DFS traversal of the graph starting at start
            :param graph: graph to traverse on
            :param start: where to start
            :param visited: set of vertices that have been visited
            :return: visited - set
            """
            if visited is None:
                visited = set()
            visited.add(start)
            vert = graph.get_vertex(start)
            for edge in vert.edges:  # get edges for vertex
                if edge.destination not in visited:  # add unique ones to visited
                    visited.add(edge.destination)
                    dfs_traversal(graph, edge.destination, visited)  # repeat again
            return visited

        visited = dfs_traversal(graph, start)

        # remove edges from vertices that are fake
        for vertex_id in visited:  # remove edges that are to fake vertices
            vert = graph.get_vertex(vertex_id)
            new_edges = []
            for edge in vert.edges:  # add in only the realist of edges, no fakes
                if edge.destination not in emails:
                    new_edges.append(edge)
            vert.edges = new_edges

    for vertex_id, vertex in graph.adj_list.items():  # iterate through vertices

        if vertex.degree() == 0:  # found fake vertex
            fakes.append(vertex_id)

    for vertex_id, vertex in graph.adj_list.items():  # remove fake edges for each vertex
        vertex.visit()
        check_fake_emails(vertex_id, fakes)  # remove edges for vertex
        if vertex.degree() == 0 and mark_fake and vertex_id in fakes:
            vertex.set_fake()
    return fakes


if __name__ == '__main__':
    # test = Graph(size=60, connectedness=0.3)
    test = Graph(20, connectedness=0.1)
    test = Graph(filename='test_construction_simple.txt')
    test.construct_graph()
    # print(test.DFS(2, 44))
    # print('shortest path:', test.BFS(0, 16))
    print(test)
    print(fake_emails(test, True))
    print(test)
