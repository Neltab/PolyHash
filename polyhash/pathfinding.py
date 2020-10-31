#Utilisé pour appeler les fonctions de pathfinding

from polyhash.Node import Node
from polyhash.Grid import GetNeighbours
from polyhash import settings as S
import copy

def FindPath(startPos: [], targetPos: []):
    startNode = Node(True,  startPos[0],  startPos[1])
    targetNode = Node(True, targetPos[0], targetPos[1])

    openSet = []
    closedSet = []
    openSet.append(startNode)

    #On initialise une grille de Nodes, et pour chaque node, on lui assigne les valeurs de gCost et hCost correspondantes
    nodeGrid = copy.deepcopy(S.nodeGrid)
    for x in range(0, S.lines):
        for y in range(0, S.columns):
            nodeGrid[x][y].gCost = GetDistance(nodeGrid[x][y], startNode)
            nodeGrid[x][y].hCost = GetDistance(nodeGrid[x][y], targetNode)
            #print(nodeGrid[x][y].gCost,nodeGrid[x][y].hCost) #print toutes les valeurs de gCost et hCost de la grille

    while len(openSet) > 0 :
        #print(openSet)
        currentNode: Node = openSet[0]
        for i in range(1,len(openSet)):
            if openSet[i].fCost() <= currentNode.fCost():
                if openSet[i].hCost < currentNode.hCost:
                    currentNode = openSet[i]

        openSet.remove(currentNode)
        closedSet.append(currentNode)

        if currentNode.gridX == targetNode.gridX and currentNode.gridY == targetNode.gridY: #on a trouvé le chemin YES
            targetNode.parent = currentNode.parent
            RetracePath(startNode, targetNode)
            return

        #GetNeighbours retourne un tableau que l'on parcourt ici
        for neighbour in GetNeighbours(currentNode):
            if (not neighbour.walkable) or neighbour in closedSet:
                continue

            newCostToNeighbour : int = currentNode.gCost + GetDistance(currentNode, neighbour)
            if (newCostToNeighbour < neighbour.gCost) or (not neighbour in openSet):
                neighbour.gCost = newCostToNeighbour
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
    pathLetter = []
    currentNode: Node = endNode #on part de la fin

    while not currentNode == startNode :
        path.append(currentNode)
        pathLetter.append(GetDirection(currentNode.parent, currentNode))
        currentNode = currentNode.parent

    pathLetter.reverse()
    path.reverse()
    print(pathLetter)


def GetDirection(n1: Node, n2: Node): #retourne la position de la node 2 par rapport à la 1
    if n1.gridX > n2.gridX: #2 a gauche de 1
        return "L"
    if n1.gridX < n2.gridX:
        return "R"
    if n1.gridY > n2.gridY: #2 au dessous de 1
        return "D"
    if n1.gridY < n2.gridY:
        return "U"


def CompleteTask(targets, startPoint):
    for i in range(0, len(targets), 2):
        if i == 0:
            pass
            FindPath(startPoint, [targets[i],targets[i+1]])
        else:
            FindPath([targets[i-2], targets[i - 1]], [targets[i],targets[i+1]])
