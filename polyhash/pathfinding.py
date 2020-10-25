#Utilisé pour appeler les fonctions de pathfinding

from polyhash.Node import Node
from polyhash import settings as S

def FindPath(startPos, targetPos):
    startNode: Node = S.grid[startPos[0]][startPos[1]] #On assigne 0 ou 1 à la valeur de startNode
    targetNode: Node = S.grid[targetPos[0]][targetPos[1]]

    openSet: Node =[]
    closedSet: Node = []
    openSet.append(startPos)

    while len(openSet) > 0 :
        currentNode = openSet[0]
        for i in range(1,len(openSet)):
            if(openSet[i].fCost < currentNode.fCost or openSet[i].fCost == currentNode.fCost and openSet[i].hCost < currentNode.hCost):
                currentNode = openSet[i]

        openSet.remove(currentNode)
        closedSet.append(currentNode)

        if currentNode == targetNode : #on a trouvé le chemin YES
            return