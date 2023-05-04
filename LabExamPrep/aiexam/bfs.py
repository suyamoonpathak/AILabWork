def bfs(graph, start, goal): 
    queue = [[start]]
    visited = set()
    while queue:
        path = queue.pop(0)
        node = path[-1]
        if node not in visited:
            visited.add(node)
            if node == goal:
                return path
            for adjacent in graph.get(node, []):
                new_path = list(path)
                new_path.append(adjacent)
                queue.append(new_path)
    return None
graph = {'A': ['B', 'C'],
         'B': ['A', 'D', 'E'],
         'C': ['A', 'F'],
         'D': ['B'],
         'E': ['B', 'F'],
         'F': ['C', 'E']}

start = input("Enter start node: ")
goal = input("Enter goal node: ")

result = bfs(graph, start, goal)
if result:
    print("Shortest path:", result)
else:
    print("No path found!")