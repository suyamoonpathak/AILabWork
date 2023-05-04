graph = {
    'A': [['B', 1], ['C', 2], ['E', 3]],
    'B': [['A', 1]],
    'C': [['A', 2], ['E', 4], ['D', 5]],
    'E': [['A', 3], ['C', 4], ['D', 6], ['F', 7]],
    'D': [['C', 5], ['E', 6], ['F', 3]],
    'G': [['F', 1]],
    'F': [['G', 1], ['E', 7], ['D', 8]],
}

heuristic = {
    'A': 25,
    'B': 2,
    'C': 30,
    'D': 7,
    'E': 6,
    'F': 8,
    'G': 0
}

startstate = 'A'
goalstate = 'C'

queue = [[startstate, 0]]

def order_by_cost(queue):
    sortedValues= sorted(queue, key=lambda x: x[1] + heuristic[x[0][-1]])
    print(sortedValues)
    return sortedValues

while queue:
 
    currpath, currcost = queue.pop(0)
    if currpath[-1] == goalstate:
        print(f"Success \nPath: {currpath} (Cost = {currcost})")
        break
    for node, cost in graph[currpath[-1]]:
        if node in currpath:
            continue
        queue.append([currpath + node, currcost + cost])
    queue = order_by_cost(queue)