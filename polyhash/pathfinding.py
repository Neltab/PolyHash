grid = []
lines = 0
columns = 0
#Récupérer les coordonnées depuis le fichier de gaetan

lines,columns = 4,5

#génération de la grille remplie de zéros
grid = [[0 for j in range (columns)] for i in range (lines)]
print(grid)
points = [2,0,2,3,4]

def apply_points_to_grid(g, p):
    numberOfPoints = p[0]
    newGrid = g
    n = 1
    i = 1
    while n <= numberOfPoints : #Pour chaque point, et a chaque boucle on incrémente de 2
        newGrid[p[i]][p[i+1]] = 1
        n+=1
        i+=2
    return newGrid


grid2 = apply_points_to_grid(grid, points)
print(grid2)