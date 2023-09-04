from collections import defaultdict, deque

def bfs(graph, start_node):
    visited = set()
    queue = deque([start_node])
    visited.add(start_node)

    while queue:
        current_node = queue.popleft()
        print(current_node)  # You can process the node here instead of just printing it

        for neighbor in graph[current_node]:
            if neighbor not in visited:
                queue.append(neighbor)
                visited.add(neighbor)

# Example usage:
if __name__ == "__main__":
    # Example graph represented as an adjacency list
    graph = defaultdict(list)
    graph[1] = [2, 3]
    graph[2] = [4]
    graph[3] = [5]
    graph[4] = []
    graph[5] = []

    start_node = 1
    bfs(graph, start_node)
