from polyhash.polyhutils.groupBy.Arm import Arm
from polyhash.Pathfinding import settings as S, pathfinding

def moveToFirstTask(bras: Arm):
    bras.occupiedCell.append(bras.pm)
    bras.movements.append(pathfinding.FindPath(bras.pm, bras.taches[0].coordtask[0], bras))

def createMoves(bras: Arm):
    for t in range(len(bras.taches)):
        tache = bras.taches[t]
        firstCell = tache.coordtask[0]
        if len(tache.coordtask) > 1:
            moves = pathfinding.FindPath(tache.coordtask[0], tache.coordtask[1], bras)

            for i in range(1,len(tache.coordtask)-1):
                currentPos = tache.coordtask[i]
                nextPos = tache.coordtask[i+1]

                closer = findCloserCell(nextPos, dist(currentPos, nextPos), bras)
                if closer != None:
                    moves += retracePath(closer, bras)
                    moves += pathfinding.FindPath(bras.occupiedCell[closer], nextPos, bras)
                else:
                    moves += pathfinding.FindPath(currentPos, nextPos, bras)

            idx = indexCellInArm(firstCell, bras)
            movesToNextTask = None
            if idx:
                moves += retracePath(idx, bras)
                if t + 1 < len(bras.taches):
                    movesToNextTask = pathfinding.FindPath(bras.occupiedCell[idx], bras.taches[t+1].coordtask[0], bras)
                # TODO: ajouter les mouvements depuis idx jusqu'à la prochaine tache
            else:
                # Todo: ajouter les mouvements depuis bras.occupiedCell[-1] jusqu'à la prochaine tache
                if t + 1 < len(bras.taches):
                    movesToNextTask = pathfinding.FindPath(bras.occupiedCell[-1], bras.taches[t+1].coordtask[0], bras)

            bras.movements.append(moves)
            if movesToNextTask != None:
                bras.movements.append(movesToNextTask)

        elif t+1< len(bras.taches):
            movesToNextTask = pathfinding.FindPath(bras.occupiedCell[-1], bras.taches[t+1].coordtask[0], bras)
            bras.movements.append([])
            bras.movements.append(movesToNextTask)
        
def retracePath(index: int, b: Arm):
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

def findCloserCell(cell: list, distMin: int, b: Arm) -> int:
        minDist = distMin
        currentIndex = None
        for idx in range(len(b.occupiedCell[:-1])):
            newDist = dist(b.occupiedCell[idx], cell)
            if newDist < minDist:
                minDist = newDist
                currentIndex = idx
        return currentIndex

def dist(x: list, y: list) -> int:
    return abs(x[0]-y[0])+ abs(x[1]-y[1])

def indexCellInArm(cell: list, b: Arm):
    for i in range(len(b.occupiedCell)):
        if b.occupiedCell[i] == cell:
            return i
    return None