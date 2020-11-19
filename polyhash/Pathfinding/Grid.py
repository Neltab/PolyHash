from polyhash.Pathfinding.Node import Node
from polyhash.Pathfinding import settings as S
import copy


def apply_points_to_grid(g, p):  # retourne une grille ayant des 1 aux emplacements des points de montage et 0 sinon
    numberOfPoints = len(p) / 2
    newGrid = copy.deepcopy(g)
    n = 1
    i = 0
    while n <= numberOfPoints:  # Pour chaque point, et a chaque boucle on incrémente de 2
        newGrid[p[i]][p[i + 1]] = 1
        n += 1
        i += 2
    return newGrid

def GenerateNodeGrid(grid): #on créé une grille remplie de nodes, de la même taille que la grid.
    newGrid = copy.deepcopy(grid) #on la calque dessus pour etre sur d'avoir les bonnes dimensions
    for x in range(0, S.lines):
        for y in range(0, S.columns):
            if grid[x][y] == 0:
                newGrid[x][y] = Node(True, x, y)
            else:
                newGrid[x][y] = Node(False, x, y)

    return newGrid


#returns all the neighbour nodes from a given node
def GetNeighbours(node: Node):
    neighbours = []

    #exécuter ça 4 fois pour les 4 cases autour de la Node en question
    #1st
    checkX: int = node.gridX - 1
    checkY: int = node.gridY

    if checkX >= 0 and checkX < S.lines and checkY >= 0 and checkY < S.columns :
        neighbours.append(S.nodeGrid[checkX][checkY])

    # 2nd
    checkX: int = node.gridX + 1
    checkY: int = node.gridY

    if checkX >= 0 and checkX < S.lines and checkY >= 0 and checkY < S.columns:
        neighbours.append(S.nodeGrid[checkX][checkY])

    #3rd
    checkX: int = node.gridX
    checkY: int = node.gridY - 1

    if checkX >= 0 and checkX < S.lines and checkY >= 0 and checkY < S.columns:
        neighbours.append(S.nodeGrid[checkX][checkY])

    #4th
    checkX: int = node.gridX
    checkY: int = node.gridY + 1

    if checkX >= 0 and checkX < S.lines and checkY >= 0 and checkY < S.columns:
        neighbours.append(S.nodeGrid[checkX][checkY])

    return neighbours


def GetArms(bras: list):
    tab: list
    for i in bras:
        tab.append(i.pm[0]); tab.append(i.pm[1]) #on créé une liste de coordonnées regroupant les coords de tout les points de montage
    return tab