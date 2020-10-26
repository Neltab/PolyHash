#Utilisé pour appeler les fonctions de pathfinding

from polyhash.Node import Node
from polyhash.Grid import GetNeighbours
from polyhash import settings as S

def FindPath(startPos: [], targetPos: []):
    startNode = Node(True,  startPos[0],  startPos[1])
    targetNode = Node(True, targetPos[0], targetPos[1])

    openSet = []
    closedSet = []
    openSet.append(startNode)

    while len(openSet) > 0 :
        currentNode: Node = openSet[0]
        for i in range(1,len(openSet)):
            if(openSet[i].fCost < currentNode.fCost or openSet[i].fCost == currentNode.fCost and openSet[i].hCost < currentNode.hCost):
                currentNode = openSet[i]

        openSet.remove(currentNode)
        closedSet.append(currentNode)

        if currentNode == targetNode : #on a trouvé le chemin YES
            RetracePath(startNode, targetNode)
            return

        #GetNeighbours retourne un tableau que l'on parcourt ici
        for neighbour in GetNeighbours(currentNode):
            if (not neighbour.walkable) or neighbour in closedSet:
                continue

            newMovementCostToNeighbour: int = currentNode.gCost + GetDistance(currentNode, neighbour)
            if (newMovementCostToNeighbour < neighbour.gCost) or (not neighbour in openSet):
                neighbour.gCost = newMovementCostToNeighbour
                neighbour.hCost = GetDistance(neighbour, targetNode)
                neighbour.parent = currentNode

                if not neighbour in openSet:
                    openSet.append(neighbour)

#retourne à combien de mouvements se trouve une case d'une autre
#on ne prend pas en compte les diagonales ici car on ne peut bouger que dans 4 directions
#ici le *10 dépend du cout de chaque mouvement dans l'alorithme A*, dans notre cas 10
def GetDistance(nodeA: Node, nodeB: Node):
    return 10*abs(nodeA.gridX-nodeB.gridX + nodeA.gridY-nodeB.gridY)


def RetracePath(startNode, endNode):
    path = []
    currentNode: Node = endNode #on part de la fin

    while not currentNode == startNode :
        path.append(currentNode)
        currentNode = currentNode.parent

    path.reverse()
    print(path)