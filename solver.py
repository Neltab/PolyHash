#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import math

from utils import Input_global, Tache
from utils import Arm, groupBy
from utils import settings as S
from utils import GenerateNodeGrid, apply_points_to_grid
from utils import createMoves
from utils import gest_conflits
from utils import CreateFile

if __name__ == "__main__":

    # textInput = input("Indiquez le nom du fichier que vous vous utiliser : ")
    # textOutput = input("Indiquez le nom du fichier de sortie : ")

    textInput = "a_example"
    textOutput = "Test"

    # Input
    input_values = Input_global(textInput)


    # Initialisation des bras
    bras = groupBy.rendement(input_values["Ltsk"], input_values["Lpointdemont"], input_values["Bras"])


    #Initialisation du pathfinding
    S.grid = [[0 for j in range (input_values["Grille"][1])] for i in range (input_values["Grille"][0])] # génération de la grille remplie de zéros

    points = [] # On laisse cette valeur nulle car nous n'avons pas implémenté de gestion des conflits
    for pm in input_values["Lpointdemont"]:
        S.grid[pm[0]][pm[1]] = 1

    pointsGrid = apply_points_to_grid(S.grid, points)  # c'est la grille qui contient les positions de collisions
    S.nodeGrid = GenerateNodeGrid(pointsGrid)


    # Création des premiers mouvements
    for b in bras:
        createMoves(b)

    print(" ")
    # Gestion des conflits et créations des mouvements finaux
    gest_conflits(bras, input_values)
    

    # Ecriture du fichier de sortie
    CreateFile(bras, textOutput)

    print("Votre fichier c'est bien généré")
