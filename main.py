#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from polyhash.Node import Node
from polyhash.Grid import apply_points_to_grid

if __name__ == "__main__":

    #points de montage à vérifier
    target = [0,0]
    #Lignes et colonnes de la grille
    lines,columns = 4,5

    #génération de la grille remplie de zéros
    grid = [[0 for j in range (columns)] for i in range (lines)]
    print(grid)
    points = [0,2,3,4]

    pointsGrid = apply_points_to_grid(grid, points)  # c'est la grille qui contient les positions de collisions
    print(pointsGrid)