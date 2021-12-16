from collections import defaultdict
from collections import deque


# using edges to create adjacency list
def create_adjacency_list(edges):
    # Using default dict to auto assign value to key
    graph = defaultdict(list)

    # Creating graph as dict of nodes and edge weights
    for (source, end, weight) in edges:
        # add both directions - undirected graph (back & forth)
        graph[source].append([end, weight])
        graph[end].append([source, weight])

    return graph


def shortest_path(n_edges, edges, source):
    # Creating adjacency list
    graph = create_adjacency_list(edges)

    # weights list of length of no of edges + 1 set to infinity
    weights = [float('INF')] * (n_edges + 1)

    # Source weight set to 0 (starting point)
    weights[source] = 0

    # create a queue to store start node and weight
    queue = deque()
    queue.append([source, 0])

    # stores visited nodes
    visited = set()

    # for as long as queue isn't empty run
    while queue:
        # Get next node from queue
        node, weight = queue.popleft()

        # If node is not visited run
        if node not in visited:
            # Add node to visited set
            visited.add(node)

            # Loop through adjacent node to node and weight of edge
            for adj_node, w in graph[node]:
                # Get current weight of edge btn node and adj_nod
                edge_weight = weights[adj_node]

                # Check to compare the current weight to edge weight btn node and adj node
                new_weight = weight + w
                if edge_weight > new_weight:
                    weights[adj_node] = new_weight

                    # Enqueue new node to queue
                    queue.append([adj_node, new_weight])

    # remove set weight of source node
    del weights[source]

    # set weight of inaccessible nodes to -1
    return [-1 if weight is float('INF') else weight for weight in weights[1:]]


if __name__ == '__main__':
    no_edges = 4
    edges = [[1, 2, 24],
             [1, 4, 20],
             [3, 1, 3],
             [4, 3, 12]]

    source_node = 1

    # Print output in 1/S -> node - Shortest Path Value: weight

    for i in range(2, no_edges + 1):
        print(str(source_node) + "/S -> ", str(i), " - Shortest Path Value: ",
              shortest_path(no_edges, edges, source_node)[i - 2])
