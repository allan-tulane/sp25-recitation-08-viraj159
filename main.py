from collections import deque
from heapq import heappush, heappop 

def shortest_shortest_path(graph, source):
    """
    Params: 
      graph.....a graph represented as a dict where each key is a vertex
                and the value is a set of (vertex, weight) tuples (as in the test case)
      source....the source node
      
    Returns:
      a dict where each key is a vertex and the value is a tuple of
      (shortest path weight, shortest path number of edges). See test case for example.
    """
    heap = []
    heappush(heap, (0, 0, source))  # (weight, edge_count, node)
    best = {}

    while heap:
        weight, edge_count, node = heappop(heap)
        
        # If we've already found a better path, skip
        if node in best:
            continue
        
        best[node] = (weight, edge_count)

        for neighbor, w in graph.get(node, []):
            if neighbor not in best:
                heappush(heap, (weight + w, edge_count + 1, neighbor))

    return best
    

    
    
def bfs_path(graph, source):
    """
    Returns:
      a dict where each key is a vertex and the value is the parent of 
      that vertex in the shortest path tree.
    """
    parents = {}
    visited = set([source])
    queue = [source]

    while queue:
        node = queue.pop(0)  # less efficient than deque.popleft()

        for neighbor in graph.get(node, set()):
            if neighbor not in visited:
                visited.add(neighbor)
                parents[neighbor] = node
                queue.append(neighbor)
    
    return parents

def get_sample_graph():
     return {'s': {'a', 'b'},
            'a': {'b'},
            'b': {'c'},
            'c': {'a', 'd'},
            'd': {}
            }


    
def get_path(parents, destination):
    """
    Returns:
      The shortest path from the source node to this destination node 
      (excluding the destination node itself). See test_get_path for an example.
    """
    path = []
    while destination in parents:
        parent = parents[destination]
        path.append(parent)
        destination = parent
    path.reverse()
    return '->'.join(path)

