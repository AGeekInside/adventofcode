from re import I
import click

from icecream import ic
import networkx as nx

def read_map(inputfile):

    map = nx.Graph()

    nodes_to_add = []
    edges_to_add = []

    for line in inputfile.readlines():
        nodes = line.split('-')
        if nodes[0].strip() == 'start':
            nodes[0] = 'StarT'
        if nodes[0].strip() == 'end':
            nodes[0] = 'EnD'
        if nodes[1].strip() == 'start':
            nodes[1] = 'StarT'
        if nodes[1].strip() == 'end':
            nodes[1] = 'EnD'

        edges_to_add.append((nodes[0].strip(), nodes[1].strip()))
        for node in nodes:
            node = node.strip()
            match node:
                case 'start':
                    nodes_to_add.append(('StarT', {'type': 'start'}))
                case 'end':
                    nodes_to_add.append(('EnD', {'type': 'end'}))
                case _:
                    if node.islower():
                        nodes_to_add.append((node, {'type': 'small'}))
                    else:
                        nodes_to_add.append((node, {'type': 'big'}))
    map.add_nodes_from(nodes_to_add)
    map.add_edges_from(edges_to_add)
    return map


def find_paths(start, path, small_twice):
    ic(start)
    ic(path)
    ic(small_twice)
    
    path.append(start)

    if 'EnD' in path:
        paths.append(path)
        return path

    for adj_node in map[start]:
        if not small_twice:
            if adj_node.islower() and adj_node in path:
                small_twice = True
                continue
            find_paths(adj_node, list(path), small_twice)



@click.command()
@click.argument('inputfile', type=click.File('r'))
def driver(inputfile):
    global map
    map = read_map(inputfile)

    ic(map.nodes)
    ic(map.edges)

    global paths
    paths = []

    find_paths('StarT', [], False)
    # ic(paths)
    ic(len(paths))

if __name__ == "__main__":
    driver()