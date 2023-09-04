_from collections import deque

def water_jug_bfs(jug1_capacity, jug2_capacity, target):
    def get_next_states(current_state):
        a, b = current_state
        next_states = []

        # Possible actions: fill jug1, fill jug2, empty jug1, empty jug2,
        # pour from jug1 to jug2, and pour from jug2 to jug1.
        actions = [(jug1_capacity, b), (a, jug2_capacity),
                   (0, b), (a, 0),
                   (min(a + b, jug1_capacity), max(0, a + b - jug1_capacity)),
                   (max(0, a + b - jug2_capacity), min(a + b, jug2_capacity))]
        
        for action in actions:
            if action not in visited:
                next_states.append(action)
                visited.add(action)
        
        return next_states

    start_state = (0, 0)
    queue = deque([start_state])
    visited = set([start_state])

    while queue:
        current_state = queue.popleft()
        if current_state[0] == target or current_state[1] == target:
            return current_state

        for next_state in get_next_states(current_state):
            queue.append(next_state)

    return None  # Target not reachable

# Example usage:
if __name__ == "__main__":
    jug1_capacity = 5
    jug2_capacity = 3
    target = 4

    result = water_jug_bfs(jug1_capacity, jug2_capacity, target)

    if result:
        print(f"Target {target} liters can be achieved with {result[0]} liters in Jug 1 and {result[1]} liters in Jug 2.")
    else:
        print(f"Target {target} liters cannot be achieved using the given jug capacities.")
