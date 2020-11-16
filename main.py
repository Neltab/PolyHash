#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from polyhash.Pathfinding.Grid import apply_points_to_grid
from polyhash.Pathfinding.Grid import GenerateNodeGrid
from polyhash.Pathfinding import settings as S, pathfinding
from polyhash.polyhutils.groupBy.Arm import Arm

from polyhash import groupBy

if __name__ == "__main__":

    #points de montage à vérifier
    target = [0,0]

    #génération de la grille remplie de zéros
    S.grid = [[0 for j in range (S.columns)] for i in range (S.lines)]
    points = [0,0,2,0]
    #Cibles a atteindre avecl'algorithme
    arm = Arm
    arm.taches = [[3,1],[3,0],[2,1]]
    arm.pm = [0,0]

    pointsGrid = apply_points_to_grid(S.grid, points)  # c'est la grille qui contient les positions de collisions
    S.nodeGrid = GenerateNodeGrid(pointsGrid)

    # print("Grille : 0=vide et 1=point de montage")
    # print(pointsGrid)

    #Donner à la fonction un Bras (Arm) et la fonction va modifier les parametres du bras en question pour lui donner la liste des mouvements
    pathfinding.CompleteArmTask(arm)
    print(arm.movements)