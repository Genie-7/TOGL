"""Create graphs with a pre-defined number of cycles"""

import argparse

import numpy as np


def make_vertex_chain(start, n, edges):
    """Create chain of vertices, starting from a given index."""
    v = start

    for i in range(n):
        edges.append((v, v + 1))
        v += 1

    return edges, v


def make_cycle_graph(
    n_cycles,
    min_length,
    max_length,
    n_pre=10,
    n_mid=5,
    n_post=10
):
    """Create random graph with pre-defined number of cycles."""
    # No edges and no vertices by default. This will be updated by the
    # cycle creation procedure.
    v = 0
    edges = []

    edges, v = make_vertex_chain(v, np.random.randint(2, n_pre), edges)

    for i in range(n_cycles):
        cycle_len = np.random.randint(min_length, max_length + 1)

        v_start = v
        edges, v = make_vertex_chain(v, cycle_len - 1, edges)
        edges.append((v, v_start))

        edges, v = make_vertex_chain(v, np.random.randint(2, n_mid), edges)

    edges, v = make_vertex_chain(v, np.random.randint(2, n_post), edges)
    return edges, v + 1


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '-n', '--n-cycles',
        type=int,
        help='Number of cycles'
    )

    parser.add_argument(
        '-m', '--n-graphs',
        type=int,
        help='Number of graphs to generate'
    )

    parser.add_argument(
        '-l', '--min-length',
        type=int,
        help='Minimum length of cycle'
    )

    parser.add_argument(
        '-L', '--max-length',
        type=int,
        help='Maximum length of cycle'
    )

    args = parser.parse_args()

    edges, n_vertices = make_cycle_graph(10, 10, 20)

    print(f'*vertices {n_vertices}')
    print('*edges')

    for u, v in edges:
        print(f'{u+1} {v+1}')
