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
