def barycentre(points):
        nbPoints = len(points)
        sX = 0
        sY = 0
        for p in points:
            sX += p[0]
            sY += p[1]
        mXf = sX / nbPoints
        mYf = sX / nbPoints

        mX = math.floor(mXf)
        mX += 1 if mXf - mX < 0.5 else 0
        mY = math.floor(mYf)
        mY += 1 if mYf - mY < 0.5 else 0
        
        return [mX, mY]

    def findClosestOnArm(cell, start: int = 0, distMin = float('inf')):
        minDist = distMin
        currentIndex = None
        for idx in range(start,len(b.occupiedCell[:-1])):
            newDist = (abs(b.occupiedCell[idx][0]-cell[0]) + abs(b.occupiedCell[idx][1]-cell[1]))
            if newDist < minDist:
                minDist = newDist
                currentIndex = idx
        return currentIndex

    def findCloserCell(cell, start: int = 0, distMin = float('inf')):
        minDist = distMin
        currentIndex = None
        for idx in range(start,len(b.occupiedCell[:-1])):
            newDist = (abs(b.occupiedCell[idx][0]-cell[0]) + abs(b.occupiedCell[idx][1]-cell[1]))
            if newDist < minDist:
                minDist = newDist
                currentIndex = idx
        return currentIndex

    def findFirstAlignWithBary():
        for i in range(len(b.occupiedCell)-1,-1,-1):
            if b.occupiedCell[i][0] == bary[0] or b.occupiedCell[i][1] == bary[1]:
                return i
        return None


    def retracePath(index):
        moves = []
        currentPos = b.occupiedCell.pop()
        for _ in range(len(b.occupiedCell) - index):
            nextPos = b.occupiedCell.pop()
            if currentPos[0] > nextPos[0]: #nextPos à gauche de currentPos
                moves.append("L")
            elif currentPos[0] < nextPos[0]:
                moves.append("R")
            elif currentPos[1] > nextPos[1]: #nextPos au dessous de currentPos
                moves.append("D")
            elif currentPos[1] < nextPos[1]:
                moves.append("U")
            currentPos = nextPos
        b.occupiedCell.append(currentPos) #On remet la derniere case enlevée sinon elle disparait
        return moves


    class Vector():
        def __init__(self, point1: list, point2: list):
            self.x = point2[0]-point1[0]
            self.y = point2[1]-point1[1]
        
        def __str__(self):
            return "({0}; {1})".format(self.x, self.y)

    def areSameSign(a: int, b: int):
        return a * b > 0
    
    def isLower(a: int, b: int):
        return abs(a) < abs(b)

    b = Arm()
    b.occupiedCell.append([4,2])
    pTaches = [[4,2],[2,2],[1,5],[6,4],[5,6],[4,4]]
    # pTaches = [[6,2],[5,11],[4,10],[8,9],[10,12],[12,8],[12,3],[11,6],[10,4],[8,5],[2,10],[2,3],[4,7],[7,7]]
    bary = barycentre(pTaches)

    baryIndex: int = None
    # print(bary)

    moves = []

    for i in range(len(pTaches)-1):
        #Todo: Algo d'optimisation des retractations
        currentPos = pTaches[i]
        nextPos = pTaches[i+1]

        BC = Vector(bary, currentPos)
        BN = Vector(bary, nextPos)

        sx: bool = areSameSign(BC.x, BN.x)
        sy: bool = areSameSign(BC.y, BN.y)
        lowx: bool = isLower(BN.x, BC.x)
        lowy: bool = isLower(BN.y, BC.y)

        if len(b.occupiedCell) == 1:
            moves += pathfinding.FindPath(currentPos, nextPos, b)
        else:
            closer = findCloserCell(nextPos, distMin=(abs(currentPos[0]-nextPos[0]) + abs(currentPos[1]-nextPos[1])))
            if closer:
                moves += retracePath(closer)
                moves += pathfinding.FindPath(b.occupiedCell[closer], nextPos, b)
            else:
                moves += pathfinding.FindPath(currentPos, nextPos, b)


        # Revoir si les différences entre les deux conditions est vraiment nécessaire
        # if not sx and not sy:
        #     print("1")

        #     if baryIndex == None:
        #         moves += pathfinding.FindPath(currentPos, bary, b)
        #         baryIndex = len(moves)
        #         moves += pathfinding.FindPath(bary, nextPos, b)
        #     else:
        #         # Todo : trouver le point le plus proche de next entre le début et barycentre 
        #         moves += retracePath(baryIndex - 1)
        #         closer = findClosestOnArm(nextPos, distMin=(abs(b.occupiedCell[baryIndex-1][0]-nextPos[0]) + abs(b.occupiedCell[baryIndex-1][1]-nextPos[1])))
        #         if closer:
        #             moves += retracePath(closer)
        #             moves += pathfinding.FindPath(b.occupiedCell[closer], nextPos, b)
        #         else:
        #             moves += pathfinding.FindPath(b.occupiedCell[baryIndex-1], nextPos, b)
        #         baryIndex = None

        #     # if len(b.occupiedCell) <= 1:
        #     #     moves += pathfinding.FindPath(currentPos, nextPos, b)
        #     # else:
        #     #     #! Ouais euh à finir
        #     #     closestPosOnArm = findClosestOnArm(nextPos) #! A completer
        #     #     moves += retracePath(closestPosOnArm)
        #     #     moves += pathfinding.FindPath(b.occupiedCell[closestPosOnArm], nextPos, b)

        # elif (sx and not sy and lowx) or (not sx and sy and lowy):
        #     print("2")

        #     if baryIndex == None:
        #         moves += pathfinding.FindPath(currentPos, bary, b)
        #         baryIndex = len(moves)
        #         moves += pathfinding.FindPath(bary, nextPos, b)
        #     else:
        #         closest = findClosestOnArm(nextPos)
        #         moves += retracePath(closest)
        #         moves += pathfinding.FindPath(b.occupiedCell[closest], nextPos, b)

        #     # if len(b.occupiedCell) <= 1:
        #     #     moves += pathfinding.FindPath(currentPos, nextPos, b)
        #     # else:
        #     #     closestPosOnArm = findClosestOnArm(nextPos) #! A completer
        #     #     moves += retracePath(closestPosOnArm)
        #     #     moves += pathfinding.FindPath(b.occupiedCell[closestPosOnArm], nextPos, b)

        # elif sx and sy and lowx and lowy:
        #     print("3")
        #     if baryIndex == None:
        #         moves += pathfinding.FindPath(currentPos, nextPos, b)
        #     else:
        #         closest = findClosestOnArm(nextPos)
        #         if closest:
        #             moves += retracePath(closest)
        #             moves += pathfinding.FindPath(b.occupiedCell[closest], nextPos, b)
        #         else:
        #             moves += pathfinding.FindPath(currentPos, nextPos, b)
        #     # moves += pathfinding.FindPath(currentPos, nextPos, b)
        
        # elif (sx and not sy and not lowx) or (not sx and sy and not lowy):
        #     print("4")
        #     if baryIndex == None:
        #         moves += pathfinding.FindPath(currentPos, bary, b)
        #         baryIndex = len(moves)
        #         moves += pathfinding.FindPath(bary, nextPos, b)
        #     else:
        #         closest = findClosestOnArm(nextPos, distMin=(abs(currentPos[0]-nextPos[0]) + abs(currentPos[1]-nextPos[1])))
        #         if closest:
        #             moves += retracePath(closest)
        #             moves += pathfinding.FindPath(b.occupiedCell[closest], nextPos, b)
        #         else:
        #             moves += pathfinding.FindPath(currentPos, nextPos, b)
        #     # lastAlignedWithBarycenter = findFirstAlignWithBary()
        #     # if lastAlignedWithBarycenter:
        #     #     moves += retracePath(lastAlignedWithBarycenter)
        #     #     moves += pathfinding.FindPath(b.occupiedCell[lastAlignedWithBarycenter], bary, b)
        #     #     moves += pathfinding.FindPath(bary, nextPos, b)
        #     # else:
        #     #     moves += pathfinding.FindPath(currentPos, nextPos, b)

        # elif (sx and sy) and ((lowx and not lowy) or (not lowx and lowy)):
        #     print("5")
        #     if baryIndex == None:
        #         moves += pathfinding.FindPath(currentPos, nextPos, b)
        #     else:
        #         closest = findClosestOnArm(nextPos, (abs(currentPos[0]-nextPos[0]) + abs(currentPos[1]-nextPos[1])))
        #         if closest:
        #             moves += retracePath(closest)
        #             moves += pathfinding.FindPath(b.occupiedCell[closest], nextPos, b)
        #         else:
        #             moves += pathfinding.FindPath(currentPos, nextPos, b)

        # elif sx and sy and not lowx and not lowy:
        #     print("6")
        #     moves += pathfinding.FindPath(currentPos, nextPos, b)
        # else:
        #     print("arg")
        moves.append("\n")

    print("longueur : " + str(len(moves)))
    for m in moves:
        print(m)