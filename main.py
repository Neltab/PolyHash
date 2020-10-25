#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from polyhash.Node import Node
from polyhash.Grid import apply_points_to_grid
from polyhash import settings as S

if __name__ == "__main__":

    #points de montage à vérifier
    target = [0,0]

    #génération de la grille remplie de zéros
    grid = [[0 for j in range (S.columns)] for i in range (S.lines)]
    print(S.grid)
    points = [0,2,3,4]

    pointsGrid = apply_points_to_grid(S.grid, points)  # c'est la grille qui contient les positions de collisions
    print(pointsGrid)