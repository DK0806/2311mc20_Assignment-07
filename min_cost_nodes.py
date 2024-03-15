def min_cost_nodes(nodes, edges):
    # Convert edge list to adjacency list
    graph = {node: [] for node in nodes}
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)
    
    visited = set()
    selected = set()
    
    def dfs(node):
        if node in visited:
            return
        visited.add(node)
        
        is_adj_selected = any(neighbor in selected for neighbor in graph[node])
        if not is_adj_selected:
            selected.add(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                dfs(neighbor)
    
    for node in nodes:
        if node not in visited:
            dfs(node)
    
    return selected


nodes = {"A": -2, "B": -3, "C": -4, "D": -5}
edges = {("A", "B"), ("B", "C"), ("A", "D"), ("C", "D")}
min_cost_nodes(nodes, edges)

