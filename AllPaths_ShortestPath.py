def find_shortest_path(graph, start, end, path=[]):
    path = path + [start]
    if start == end:
        return path
    shortest = None
    for node in graph[start]:
        if node not in path:
            newpath = find_shortest_path(graph, node, end, path)
            if newpath:
                if not shortest or len(newpath) < len(shortest):
                    shortest = newpath
    return shortest
    
def find_all_paths(graph, start, end, path=[]):
    path = path + [start]
    if start == end:
        return [path]

    paths = []
    for node in graph[start]:
        if node not in path:
            newpaths = find_all_paths(graph, node, end, path)
            for newpath in newpaths:
                paths.append(newpath)
    return paths

graph={
    'A':['B','E'],
    'B':['E','C','A'],
    'C':['B','D'],
    'D':['E','C'],
    'E':['A','B','D']
}

start='A'
goal='D'
print("The paths are : ",find_all_paths(graph,start,goal))
print("The shortest path is : ",find_shortest_path(graph,start,goal))