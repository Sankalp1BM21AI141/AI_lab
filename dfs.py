def dfs_recursive(graph, current_node, visited):
    if current_node not in visited:
        visited.add(current_node)
        print(current_node)  # You can process the node here instead of just printing it

        for neighbor in graph[current_node]:
            dfs_recursive(graph, neighbor, visited)

# Example usage:
if __name__ == "__main__":
    # Example graph represented as an adjacency list
    graph = {
        1: [2, 3],
        2: [4],
        3: [5],
        4: [],
        5: []
    }

    start_node = 1
    visited_nodes = set()
    dfs_recursive(graph, start_node, visited_nodes)
