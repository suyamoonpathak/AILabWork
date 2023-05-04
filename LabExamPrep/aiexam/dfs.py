def allPath(graph, start, end, arr=[]):
    arr = arr + [start]
    if start == end:
        return [arr]

    paths = []
    for node in graph[start]:
        if node not in arr:
            newpaths = allPath(graph, node, end, arr)
            for newpath in newpaths:
                paths.append(newpath)

    allPhath = paths
    return paths


def shortpath(graph, start, end, arr=[]):
    arr = allPath(graph, start, end, arr)
    small = arr[0]

    for i in range(len(arr)):
        if (len(arr[i]) < len(small)):
            small = arr[i]

    print("All possible paths: ", arr)
    print("Shortest path: ", small)


graph = {
    'A': ['B', 'C', 'D'],
    'B': ['A', 'D'],
    'C': ['A', 'E'],
    'D': ['A', 'E', 'B'],
    'E': ['C', 'D'],
}
start = input("Start node: ")
end = input("Goal node: ")

shortpath(graph,start,end)