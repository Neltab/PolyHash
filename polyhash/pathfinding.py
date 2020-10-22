#Utilisé pour appeler les fonctions de pathfinding et pour établir la grille

from polyhash import Node

#points de montage à vérifier
target = [0,0]
#Lignes et colonnes de la grille
lines,columns = 4,5

#génération de la grille remplie de zéros
grid = [[0 for j in range (columns)] for i in range (lines)]
print(grid)
points = [0,2,3,4]

def apply_points_to_grid(g, p):
    numberOfPoints = len(p)/2
    newGrid = g
    n = 1
    i = 0
    while n <= numberOfPoints : #Pour chaque point, et a chaque boucle on incrémente de 2
        newGrid[p[i]][p[i+1]] = 1
        n+=1
        i+=2
    return newGrid

collisionGrid = apply_points_to_grid(grid, points) #c'est la grille qui contient les positions de collisions
print(collisionGrid)

def FindPath(startOos, targetPos):
