def brute_force_shortest_path(graph, start, end, max_depth=10):
    """
    Find the shortest path between start and end nodes using Dijkstra's algorithm.
    More efficient than brute force approach.
    
    Args:
        graph: Dictionary representing the graph {node: {neighbor: distance}}
        start: Starting node
        end: Target node
        max_depth: Maximum path length (not used in Dijkstra's but kept for compatibility)
    
    Returns:
        Tuple of (shortest_path, distance)
    """
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    previous = {node: None for node in graph}
    unvisited = set(graph.keys())
    
    while unvisited:
        current = min(unvisited, key=lambda x: distances[x])
        
        if current == end:
            break
            
        if distances[current] == float('inf'):
            break
            
        unvisited.remove(current)
        
        for neighbor, weight in graph[current].items():
            if neighbor in unvisited:
                distance = distances[current] + weight
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    previous[neighbor] = current
    
    if distances[end] == float('inf'):
        return None, float('inf')
        
    path = []
    current = end
    while current is not None:
        path.append(current)
        current = previous[current]
    path.reverse()
    
    return path, distances[end]