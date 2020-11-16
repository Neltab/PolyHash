#Utilisé pour appeler les fonctions de pathfinding

from polyhash.Pathfinding.Node import Node
from polyhash.Pathfinding.Grid import GetNeighbours
from polyhash.Pathfinding import settings as S
from polyhash.polyhutils.groupBy.Arm import Arm
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
            return RetracePath(startNode, targetNode)

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
    return pathLetter #retourne un tableau de lettres


def GetDirection(n1: Node, n2: Node): #retourne la position de la node 2 par rapport à la 1
    if n1.gridX > n2.gridX: #2 a gauche de 1
        return "L"
    if n1.gridX < n2.gridX:
        return "R"
    if n1.gridY > n2.gridY: #2 au dessous de 1
        return "D"
    if n1.gridY < n2.gridY:
        return "U"


def CompleteArmTask(arm : Arm): #targets est une liste de Taches (objet). Il faut donc récupérer les coordonnées de chacune des tâches

    startPoint = arm.pm #le point de départ de l'algo, au début c'est le point de montage, mais il change après chaque path complété comme le bras ne repart pas du pm
    targets = arm.taches #au format [[x1, y1],[x2,y2]...]

    for i in range(0, len(targets)): #pour chaque target
        targetPos = targets[i] #position à aller chercher
        pathLetters = FindPath(startPoint, targetPos)

        for i in pathLetters: # on additionne les lettres (mouvements) une a une au tableau contenant tous les mouvements du bras
            arm.movements.append(i)

        startPoint = targetPos # on change le point de départ comme expliqué plus haut