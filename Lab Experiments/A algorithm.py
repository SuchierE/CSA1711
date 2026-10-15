import heapq


def astar(graph, heuristic, start, goal):
    open_list = [(heuristic[start], 0, start, [start])]
    visited = set()

    while open_list:
        f, g, node, path = heapq.heappop(open_list)

        if node == goal:
            print("Shortest Path:", " -> ".join(path))
            print("Total Cost:", g)
            return

        if node in visited:
            continue

        visited.add(node)

        for neighbor, cost in graph[node].items():
            if neighbor not in visited:
                new_g = g + cost
                new_f = new_g + heuristic[neighbor]
                heapq.heappush(
                    open_list,
                    (new_f, new_g, neighbor, path + [neighbor])
                )

    print("No path found")


graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'D': 5, 'E': 1},
    'C': {'D': 1},
    'D': {'G': 3},
    'E': {'G': 5},
    'G': {}
}

heuristic = {
    'A': 7,
    'B': 6,
    'C': 4,
    'D': 3,
    'E': 5,
    'G': 0
}

astar(graph, heuristic, 'A', 'G')
