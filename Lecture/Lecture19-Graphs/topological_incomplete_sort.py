def topological_sort(g):
    """Return a list of verticies of directed acyclic graph g in topological order.

    If graph g has a cycle, the result will be incomplete.
    """


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
