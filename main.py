def cpu_intensive_task():
    print(f"[CPU Task] Starting CPU-intensive graph algorithm task")
    iteration = 0
    while cpu_spike_active:
        iteration += 1
        # Reduced graph size and added rate limiting
        graph_size = 10
        graph = generate_large_graph(graph_size)
        
        start_node = random.randint(0, graph_size-1)
        end_node = random.randint(0, graph_size-1)
        while end_node == start_node:
            end_node = random.randint(0, graph_size-1)
        
        print(f"[CPU Task] Iteration {iteration}: Running optimized shortest path algorithm on graph with {graph_size} nodes from node {start_node} to {end_node}")
        
        start_time = time.time()
        path, distance = brute_force_shortest_path(graph, start_node, end_node, max_depth=5)
        elapsed = time.time() - start_time
        
        if path:
            print(f"[CPU Task] Found path with {len(path)} nodes and distance {distance} in {elapsed:.2f} seconds")
        else:
            print(f"[CPU Task] No path found after {elapsed:.2f} seconds")
            
        # Add delay between iterations to reduce CPU load
        time.sleep(0.5)
        
        # Break if iteration takes too long
        if elapsed > 2.0:
            print(f"[CPU Task] Iteration took too long ({elapsed:.2f}s), breaking")
            break