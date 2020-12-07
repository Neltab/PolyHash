#Utilisé pour appeler les fonctions de pathfinding

from polyhash.Pathfinding.Node import Node
from polyhash.Pathfinding.Grid import GetNeighbours
from polyhash.Pathfinding import settings as S
from polyhash.polyhutils.groupBy.Arm import Arm
import copy


#Methode principale, on lui donne un point de départ et d'arrivée, ainsi qu'un objet ARM, celui dont on va modifier les coordonnées
def FindPath(startPos: [], targetPos: [], arm: Arm):
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
                if openSet[i].hCost < currentNode.hCost:
                    currentNode = openSet[i]

        openSet.remove(currentNode) #la node est maintenant vérifiée
        closedSet.append(currentNode)



        ####################################
        #   CONDITION DE FIN DE FONCTION   #
        ####################################

        if currentNode.gridX == targetNode.gridX and currentNode.gridY == targetNode.gridY: #on est rendus à la node de fin, on appelle la fonction qui écrit les mouvements
            targetNode.parent = currentNode.parent
            return RetracePath(startNode, targetNode, arm)



        '''#GetNeighbours retourne un tableau que l'on parcourt ici                 TEST JE NE PENSE PAS QUE CE SOIT UTILE COMME ON A PAS DE DIAGONALES
        for neighbour in GetNeighbours(currentNode):
            if (not neighbour.walkable) or neighbour in closedSet:
                continue

            newCostToNeighbour : int = currentNode.gCost + GetDistance(currentNode, neighbour)
            if (newCostToNeighbour < neighbour.gCost) or (not neighbour in openSet):
                neighbour.gCost = newCostToNeighbour
                neighbour.hCost = GetDistance(neighbour, targetNode)
                neighbour.parent = currentNode

                if not neighbour in openSet:
                    openSet.append(neighbour)'''

#retourne à combien de mouvements se trouve une case d'une autre
#on ne prend pas en compte les diagonales ici car on ne peut bouger que dans 4 directions
#ici le *10 dépend du cout de chaque mouvement dans l'alorithme A*
def GetDistance(nodeA: Node, nodeB: Node):
    return 10*(abs(nodeA.gridX-nodeB.gridX) + abs(nodeA.gridY-nodeB.gridY))


def RetracePath(startNode, endNode, arm: Arm):
    #path = []
    pathLetter = [] #contient les lettres de direction
    currentNode: Node = endNode #on part de la fin
    tab = [] #le tableau contenant les cases occupées par un bras, pour l'algo d'Aurelien
    i = 0

    #Ici on prend les coordonnées des nodes une à une et on modifie la node à cet emplacement en mettant la valeur de walkable sur False
    #On ajoute ensuite les variable de position utilisée au bras en question
    while not currentNode == startNode :
        #path.append(currentNode)
        pathLetter.append(GetDirection(currentNode.parent, currentNode))

        #Occupation des cases
        S.nodeGrid[currentNode.gridX][currentNode.gridY].walkable = False #cette case est désormais un obstacle
        tab[i] = [currentNode.gridX,currentNode.gridY]
        i+=1

        currentNode = currentNode.parent

    tab.reverse()
    arm.occupiedCell += tab

    pathLetter.reverse()
    #path.reverse()
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
    print(startPoint)
    targets = arm.taches #au format [[x1, y1],[x2,y2]...]

    for tache in arm.taches: #pour chaque tache
        for coord in tache.coordtask:
            targetPos = coord #position à aller chercher
            pathLetters = FindPath(startPoint, targetPos, arm)

            if pathLetters:
                for n in pathLetters: # on additionne les lettres (mouvements) une a une au tableau contenant tous les mouvements du bras
                    arm.movements.append(n)

            startPoint = targetPos # on change le point de départ comme expliqué plus haut
        print(startPoint)