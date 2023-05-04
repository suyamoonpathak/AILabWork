import copy
import time 

startstate =[[1, 8, 2], ['_', 4, 3], [7, 6, 5]]
goalstate = [[1, 2, 3], [4, 5, 6], [7, 8, '_']]

visited = []
queue  = [startstate]

def getNext(node):
    nextStates = []
    for row in range(0, len(node)):
        for col in range(0, len(node[row])):
            if(node[row][col]=='_'):
                if(row==0 or row==1):
                    a = copy.deepcopy(node)
                    a[row][col], a[row+1][col] = a[row+1][col], a[row][col]
                    nextStates.append(a)

                if(row==1 or row==2):
                    a = copy.deepcopy(node)
                    a[row][col], a[row-1][col] = a[row-1][col], a[row][col]
                    nextStates.append(a)
                
                if(col==0 or col==1):
                    a = copy.deepcopy(node)
                    a[row][col], a[row][col+1] = a[row][col+1], a[row][col]
                    nextStates.append(a)

                if(col==1 or col==2):
                    a = copy.deepcopy(node)
                    a[row][col], a[row][col-1] = a[row][col-1], a[row][col]
                    nextStates.append(a)

    return nextStates

start = time.time()
while(queue):
    node = queue.pop(0)
    neighbours = getNext(node)
    if node not in visited:
        print(node, end = " ")
        if(node == goalstate):
            break
        print('\n\n Next State\n')
        visited.append(node)
        for neighbour in neighbours:
            queue.append(neighbour)

end = time.time()

print("\n\nTotal Time Taken: ", end - start)