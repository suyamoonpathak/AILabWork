import time

def ham(ls1,ls2):
    dis = 0
    for i in range(len(ls1)):
        if (ls1[i]!=ls2[i]):
            dis+=1
    return dis

def swap(move,curVal,ind):
    if (move == "up"):
        nextInd = ind-3
        curVal[ind],curVal[nextInd] = curVal[nextInd],curVal[ind]
        return curVal
    if (move == "down"):
        nextInd = ind+3
        curVal[ind],curVal[nextInd] = curVal[nextInd],curVal[ind]
        return curVal
    if (move == "left"):
        nextInd = ind-1
        curVal[ind],curVal[nextInd] = curVal[nextInd],curVal[ind]
        return curVal
    if (move == "right"):
        nextInd = ind+1
        curVal[ind],curVal[nextInd] = curVal[nextInd],curVal[ind]
        return curVal


def best(cur,completed):
    moves = {
        "up" : [3,4,5,6,7,8],
        "down" : [0,1,2,3,4,5],
        "left" : [1,2,4,5,7,8],
        "right" : [0,1,3,4,6,7]
    }

    ind0 = cur.index(0)

    possibleMoves = []
    possibleMoves.append("up" if ind0 in moves["up"] else "-")
    possibleMoves.append("down" if ind0 in moves["down"] else "-")
    possibleMoves.append("left" if ind0 in moves["left"] else "-")
    possibleMoves.append("right" if ind0 in moves["right"] else "-")

    print(f"possibleMoves: {possibleMoves}")

    possiblePaths = []

    print("Position of '0' : ", ind0)
    print("CUR in best : ", cur)
    if "up" in possibleMoves:
        copyCurUp = cur.copy()
        copyCurUp = swap("up",copyCurUp,ind0)
        print("Possible Move Up: ")
        printLs(copyCurUp)
        h = ham(initial,copyCurUp)
        g = ham(copyCurUp,goal)
        f = h+g
        print("F,G,H :", f,g,h)
        if (copyCurUp == goal):
            completed = True
        possiblePaths.append((f,"up"))
        if (copyCurUp not in visited):
            bfsQueue.append((copyCurUp, f))
        else:
            print("not adding this because already visited!!!")

    if "down" in possibleMoves:
        copyCurDown = cur.copy()
        copyCurDown = swap("down",copyCurDown,ind0)
        print("Possible Move Down: ")
        printLs(copyCurDown)
        h = ham(initial, copyCurDown)
        g = ham(copyCurDown,goal)
        f = h+g
        print("F,G,H :", f,g,h)
        if (copyCurDown == goal):
            completed = True
        possiblePaths.append((f,"down"))
        if (copyCurDown not in visited):
            bfsQueue.append((copyCurDown, f))
        else:
            print("not adding this because already visited!!!")
    
    if "left" in possibleMoves:
        copyCurLeft = cur.copy()
        copyCurLeft = swap("left",copyCurLeft,ind0)
        print("Possible Move Left: ")
        printLs(copyCurLeft)
        h = ham(initial, copyCurLeft)
        g = ham(copyCurLeft,goal)
        f = h+g
        print("F,G,H :", f,g,h)
        if (copyCurLeft == goal):
            completed = True
        possiblePaths.append((f,"left"))
        if (copyCurLeft not in visited):
            bfsQueue.append((copyCurLeft, f))
        else:
            print("not adding this because already visited!!!")

    if "right" in possibleMoves:
        copyCurRight = cur.copy()
        copyCurRight = swap("right",copyCurRight,ind0)
        print("Possible Move Right: ")
        printLs(copyCurRight)
        h = ham(initial, copyCurRight)
        g = ham(copyCurRight,goal)
        f = h+g
        print("F,G,H :", f,g,h)
        if (copyCurRight == goal):
            completed = True
        possiblePaths.append((f,"right"))
        if (copyCurRight not in visited):
            bfsQueue.append((copyCurRight, f))
        else:
            print("not adding this because already visited!!!")
    
    print(f"possiblePaths and their values : {possiblePaths}")

    # No Not Move logic required

    # notMove = ""
    # if (lastMove != ""):
        # if (lastMove in ["up","down"]):
        #     notMove = "up" if lastMove == "down" else "down"
        # elif (lastMove in ["left","right"]):
        #     notMove = "left" if lastMove == "right" else "right"
        # print("Last Move : ", lastMove)
        # print("Not Move : ", notMove)
        # print("Thus removing compliment of LastMove from possiblePaths...")
        # for i in possiblePaths:
            # if i[1] == notMove:
                # possiblePaths.remove(i)
    # print(f"possiblePaths and their values : {possiblePaths}")

    
    # Not taking this minPath value instead Using BFS

    # minPath = min(possiblePaths)
    # print(f"Min : {minPath}")
    # if (minPath[1] == "up"):
    #     return copyCurUp,"up"
    # if (minPath[1] == "down"):
    #     return copyCurDown,"down"
    # if (minPath[1] == "left"):
    #     return copyCurLeft,"left"
    # if (minPath[1] == "right"):
    #     return copyCurRight,"right"

    # BFS
    return bfsQueue[0][0],completed


def printLs(ls):
    for i in range(len(ls)):
        print("{:<5}".format(ls[i]), end=" ")
        if (i == 2 or i == 5 or i == 8): print('\n')


if __name__ == "__main__":
    goal = [
        1,2,3,
        4,5,6,
        7,8,0
    ]
    initial = [
        1,2,3,
        5,0,6,
        4,7,8
    ]
    
    bfsQueue = []
    visited = [initial]
    cur = initial
    steps = 20
    completed = False
    start = time.time()
    while (True):
    # while (steps):
        print("\n\n")
        print("CUR : ")
        printLs(cur)
        cur,completed = best(cur,completed)
        print("Completed : ", completed)
        bfsQueue.pop(0)
        if (completed):
            print("\n\n")
            print("SOLUTION : ")
            printLs(bfsQueue[len(bfsQueue)-1][0])
            break
        steps -= 1
    stop = time.time() - start
    print(f"TIME : {stop}")