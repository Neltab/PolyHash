grid = []
lines = 0
columns = 0
#Récupérer les coordonnées depuis le fichier de gaetan

lines,columns = 4,5

#génération de la grille remplie de zéros
grid = [[0 for j in range (columns)] for i in range (lines)]
print(grille)

points = [2,1,2,3,5]

def apply_points_to_grid(grid, points):
    numberOfPoints = points[0]
    newGrid = grid
    for i in range(numberOfPoints): #Pour chaque point
        #modify new gfrid depending on points[]