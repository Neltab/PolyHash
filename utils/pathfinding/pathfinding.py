#Utilisé pour appeler les fonctions de pathfinding

from .Node import Node
from .Grid import GetNeighbours
from . import settings as S
from ..group.Arm import Arm
import copy


def FindPath(startPos: [], targetPos: [], arm: Arm):
    """Methode principale, suivant le principe de pathfinding de l'algorithme A*. Trouve le chemin le plus court entre deux points.

    :param startPos : Point de départ, au format [x,y]
    :param targetPos : Point d'arrivée, au format [x,y]
    :param arm : Le bras sur lequel on effectue les opérations
    """


    startNode = Node(True,  startPos[0],  startPos[1])
    targetNode = Node(True, targetPos[0], targetPos[1])

    #exception si on ne doit pas bouger de case, dans le cas d'une double éxecution de tache en un tour unique.
    if startPos == targetPos:
        return None

    openSet = [] #liste des nodes que l'on doit analyser à chaque tour de boucle
    closedSet = [] #liste des nodes analysées
    openSet.append(startNode)

    #On initialise une grille de Nodes, et pour chaque node, on lui assigne les valeurs de gCost et hCost correspondantes
    nodeGrid = copy.deepcopy(S.nodeGrid) #cette copie est une copie de la grille par défaut initialisée dans le main
    for x in range(0, S.lines):
        for y in range(0, S.columns):
            nodeGrid[x][y].gCost = GetDistance(nodeGrid[x][y], startNode)
            nodeGrid[x][y].hCost = GetDistance(nodeGrid[x][y], targetNode)

    while len(openSet) > 0 : #tant qu'on a au moins une node à vérifier
        currentNode: Node = openSet[0]
        for i in range(1,len(openSet)): # dans cette boucle on cherche la node la plus intéressante du point de vue de son cout, et on l'assigne à currentnode.
            if openSet[i].fCost() <= currentNode.fCost():
                if openSet[i].hCost < currentNode.hCost: #dans le cas ou les fCost sont égaux, on prend celle avec le hCost le plus faible.
                    currentNode = openSet[i]

        openSet.remove(currentNode) #la node est maintenant vérifiée
        closedSet.append(currentNode)



        ####################################
        #   CONDITION DE FIN DE FONCTION   #
        ####################################

        if currentNode.gridX == targetNode.gridX and currentNode.gridY == targetNode.gridY: #on est rendus à la node de fin, on appelle la fonction qui écrit les mouvements
            targetNode.parent = currentNode.parent
            return RetracePath(startNode, targetNode, arm)

        #GetNeighbours retourne un tableau que l'on parcourt ici
        for neighbour in GetNeighbours(currentNode):
            if (not neighbour.walkable) or neighbour in closedSet:
                continue

            newCostToNeighbour : int = currentNode.gCost + GetDistance(currentNode, neighbour) #dans certains cas, le cout initial de la Node n'est pas le même, car un chemin peut être le meilleur à un instant t, mais pas forcément à t+1
            if (newCostToNeighbour < neighbour.gCost) or (not neighbour in openSet):
                neighbour.gCost = newCostToNeighbour
                neighbour.hCost = GetDistance(neighbour, targetNode)
                neighbour.parent = currentNode

                if not neighbour in openSet:
                    openSet.append(neighbour)


def GetDistance(nodeA: Node, nodeB: Node):
    """retourne à combien de mouvements se trouve une case d'une autre
        on ne prend pas en compte les diagonales ici car on ne peut bouger que dans 4 directions
        ici le *10 dépend du cout de chaque mouvement, dans un algo qui gère les diagonales c'est important,
        mais dans notre cas on peut lui donner n'importe quelle valeur
    """

    return 10*(abs(nodeA.gridX-nodeB.gridX) + abs(nodeA.gridY-nodeB.gridY))


def RetracePath(startNode, endNode, arm: Arm):
    """Cette foncction retrace le chemin final pris par l'algorithme, il part de la node de fin endNode, et remonte
        en suivant les parents consécutifs. Une fois arrivé à la node de départ startNode, on renvoie un tableau de
        lettres, donnant les déplacements effectués par le bras entre les deux points. A chaque node successive, on appelle
        la fonction GetDirection() qui retourne la position de deux nodes en terme de lettre.

        :param startNode : node de départ
        :param endNode : node de fin
        :param arm : le bras sur lequel on effectue les mouvements
    """
    pathLetter = [] #contient les lettres de direction
    currentNode: Node = endNode #on part de la fin
    i = 0

    #Ici on prend les coordonnées des nodes une à une et on modifie la node à cet emplacement en mettant la valeur de walkable sur False
    #On ajoute ensuite les variable de position utilisée au bras en question
    while not currentNode == startNode :
        #path.append(currentNode)
        pathLetter.append(GetDirection(currentNode.parent, currentNode))

        #Occupation des cases
        S.nodeGrid[currentNode.gridX][currentNode.gridY].walkable = False #cette case est désormais un obstacle
        i+=1

        currentNode = currentNode.parent

    pathLetter.reverse()

    return pathLetter


def GetDirection(n1: Node, n2: Node):
    """ retourne la position en lettre (droite, gauche, haut, bas) de la node 2 par rapport à la 1
    """
    if n1.gridX > n2.gridX: #2 a gauche de 1
        return "L"
    if n1.gridX < n2.gridX:
        return "R"
    if n1.gridY > n2.gridY: #2 au dessous de 1
        return "D"
    if n1.gridY < n2.gridY:
        return "U"


def CompleteArmTask(arm : Arm):
    """Fonction qui appelle la fonction FindPath() pour toutes les taches d'un bras.

    :param arm : bras que l'on traite
    """

    startPoint = arm.pm #le point de départ de l'algo, au début c'est le point de montage, mais il change après chaque path complété comme le bras ne repart pas du pm
    # arm.taches est au format [[x1, y1],[x2,y2]...]

    for tache in arm.taches: #pour chaque tache
        for coord in tache.coordtask:
            targetPos = coord #position à aller chercher
            arm.movements += FindPath(startPoint, targetPos, arm)

            startPoint = targetPos # on change le point de départ comme expliqué plus haut