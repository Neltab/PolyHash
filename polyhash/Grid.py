from polyhash import Node
from polyhash import settings as S

def apply_points_to_grid(g, p):  # retourne une grille ayant des 1 aux emplacements des points de montage et 0 sinon
    numberOfPoints = len(p) / 2
    newGrid = g
    n = 1
    i = 0
    while n <= numberOfPoints:  # Pour chaque point, et a chaque boucle on incrémente de 2
        newGrid[p[i]][p[i + 1]] = 1
        n += 1
        i += 2
    return newGrid

#returns all the neighbour nodes from a given node
def GetNeighbours(node: Node) :
    neighbours: Node = []
    for x in range (-1, 1):
        for y in range (-1, 1):
            if x == 0 and y == 0:
                continue
            checkX = node.GridX + x
            checkY = node.gridY + y

            if checkX >= 0 and checkX < S.lines and checkY >= 0 and checkY < S.columns :
                neighbours.append(S.grid)
    return neighbours


