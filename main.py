#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from polyhash.Node import Node
from polyhash.Grid import apply_points_to_grid
from polyhash.Grid import GenerateNodeGrid
from polyhash import settings as S
from polyhash import pathfinding

if __name__ == "__main__":

    #points de montage à vérifier
    target = [0,0]

    #génération de la grille remplie de zéros
    S.grid = [[0 for j in range (S.columns)] for i in range (S.lines)]
    print(S.grid)
    points = [0,2,3,4]

    pointsGrid = apply_points_to_grid(S.grid, points)  # c'est la grille qui contient les positions de collisions
    S.nodeGrid = GenerateNodeGrid(S.grid)

    pathfinding.FindPath([0,2], [1,3])