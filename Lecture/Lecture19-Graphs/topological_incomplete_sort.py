def topological_sort(g):
    """Return a list of verticies of directed acyclic graph g in topological order.

    If graph g has a cycle, the result will be incomplete.
    """

    topo = []  # vertices in topological order
    ready = []  # list of vertices that hav eno remaining constraints
    incount = {}  # keep track of in-degree for each vertex

    for u in g.vertices():
        incount[u] = g.degree(u, False)  # param requests incoming degree
        if incount[u] == 0:  # u has no incoming edges, it is free of constraints
            ready.append(u)

    while len(ready) > 0:
        u = ready.pop()  # u is free of constraints
        topo.append(u)  # adding u to topological sort

        for e in g.incident_edges(u):
            v = e.opposite(u)
            incount[v] -= 1  # vertex v has one less constraint, without vertex u
            if incount[v] == 0:
                ready.append(v)

    return topo


if __name__ == '__main__':
    from graph_examples import figure_14_12_smaller as smaller_example

    g = smaller_example()
    print("Number of vertices is", g.vertex_count())
    print("Number of edges is", g.edge_count())
    topo = topological_sort(g)
    print("Topo order", [str(v) for v in topo])

    from graph_examples import figure_14_12 as example

    g = example()
    print("Number of vertices is", g.vertex_count())
    print("Number of edges is", g.edge_count())
    topo = topological_sort(g)
    print("Topo order", [str(v) for v in topo])

    from graph_examples import figure_14_12_smaller_wcycle as cycle_example

    g = cycle_example()
    print("Number of vertices is", g.vertex_count())
    print("Number of edges is", g.edge_count())
    topo = topological_sort(g)
    print("Topo order", [str(v) for v in topo])
