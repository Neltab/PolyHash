#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from Input2 import GRILLE, BRAS, NBPTDEMONT, NBTACHES, NBETAPES, LPOINTDEMONT, LTASK

from polyhash.Pathfinding.Grid import apply_points_to_grid
from polyhash.Pathfinding.Grid import GenerateNodeGrid
from polyhash.Pathfinding import settings as S, pathfinding

from polyhash import groupBy

if __name__ == "__main__":

    #####################
    # Partie d'Aurélien #
    #####################

    bras = groupBy.rendement(LTASK, LPOINTDEMONT, BRAS)
    for b in bras:
        print(b)


    ####################
    # Partie d'Anthime #
    ####################

    #points de montage à vérifier
    target = [0,0]

    #génération de la grille remplie de zéros
    S.grid = [[0 for j in range (S.columns)] for i in range (S.lines)]
    points = [0,0,2,0]
    #Cibles a atteindre avecl'algorithme
    targets = [3,0,3,1]

    pointsGrid = apply_points_to_grid(S.grid, points)  # c'est la grille qui contient les positions de collisions
    S.nodeGrid = GenerateNodeGrid(pointsGrid)

    # print("Grille : 0=vide et 1=point de montage")
    # print(pointsGrid)

    #Donner un tableau de liste de points, et faire l'algorithme qui parcourt tous ces points
    pathfinding.CompleteTask(targets, [0, 0])