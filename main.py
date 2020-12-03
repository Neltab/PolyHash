#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import math

from Input2 import GRILLE, BRAS, NBPTDEMONT, NBTACHES, NBETAPES, LPOINTDEMONT, LTASK, Tache

from polyhash.Pathfinding.Grid import apply_points_to_grid
from polyhash.Pathfinding.Grid import GenerateNodeGrid, GetArms
from polyhash.Pathfinding import settings as S, pathfinding
from polyhash.polyhutils.groupBy.Arm import Arm

from polyhash import groupBy

from polyhash.taskOptimization import movementsCreation as mc

from output import CreateFile

if __name__ == "__main__":

    #####################
    # Partie d'Aurélien #
    #####################

    bras = groupBy.rendement(LTASK, LPOINTDEMONT, BRAS, NBETAPES)

    # for b in bras:
    #     print(b.taches[0].coordtask[0], b.taches[1].coordtask[0], b.taches[2].coordtask[0])

    ####################
    # Partie d'Anthime #
    ####################

    #génération de la grille remplie de zéros
    S.grid = [[0 for j in range (S.columns)] for i in range (S.lines)]
    # points = GetArms(bras)
    points = []

    pointsGrid = apply_points_to_grid(S.grid, points)  # c'est la grille qui contient les positions de collisions
    S.nodeGrid = GenerateNodeGrid(pointsGrid)

    #Re Aurelien ##############################
    debug = 0
    for b in bras:
        mc.moveToFirstTask(b)
        mc.createMoves(b)
        debug += 1

    # print(bras[-1].pm)
    # print(bras[-1].taches[0].coordtask)
    # print(bras[-1].movements)
    # print(len(bras[-1].occupiedCell))

    def get_pos_from_dir(move: str, cell: list):
        if move == "L":
            return [cell[0]-1,cell[1]]
        elif move == "R":
            return [cell[0]+1, cell[1]]
        elif move == "D":
            return [cell[0], cell[1]-1]
        elif move == "U":
            return [cell[0], cell[1]+1]
        else:
            return cell

    occupiedCellGrid = [[0 for _ in range(GRILLE[1])] for _ in range(GRILLE[0])]

    for pm in LPOINTDEMONT:
        occupiedCellGrid[pm[0]][pm[1]] = -1

    #Reset des cases occupées
    for arm in bras:
        arm.occupiedCell = [arm.pm]
        arm.nextMoves = arm.movements.pop(0)

    def checkForNextMove(b: Arm) -> bool:
        if b.nextMoves == []:
            if b.isDoingTask:
                # Ajouter les mouvements de la taches aux mouvements à output
                b.movementsDone += b.currentMovements
                b.currentMovements = []
                # Ajouter la tache a la liste des taches terminées
                b.taskDone.append(b.taches.pop(0))
                # On signale qu'on a finit la tache

                b.isDoingTask = False

                # if b.movements[0] != []:
                #     b.isDoingTask = False
                #     checkForNextMove(b)
                # else:
                #     b.movements.pop(0)
            else:
                b.isDoingTask = True
                # if b.movements[0] != []:
                #     b.isDoingTask = True
                #     checkForNextMove(b)
                # else:
                #     b.movements.pop(0)
            # Ajouter les prochains mouvements (ceux de la tache ou pour aller à la prochaine) à b.nextMoves
            if len(b.movements) >= 1:
                b.nextMoves = b.movements.pop(0)
                return True
            checkForNextMove(b)
        return False

    conflit = 0
    for t in range(NBETAPES):
        for i in range(len(bras)):
            if i == 28:
                print("debug")
            b = bras[i]
            
            done = checkForNextMove(b)

            if not done:
                move = b.nextMoves.pop(0)
                newPos = get_pos_from_dir(move, b.occupiedCell[-1])

                if occupiedCellGrid[newPos[0]][newPos[1]] == 0:
                    b.occupiedCell.append(newPos)
                    S.nodeGrid[newPos[0]][newPos[1]].walkable = False
                    occupiedCellGrid[newPos[0]][newPos[1]] = i + 1 
                    b.currentMovements.append(move)
                elif occupiedCellGrid[newPos[0]][newPos[1]] == i + 1:
                    oldPos = b.occupiedCell.pop()
                    S.nodeGrid[oldPos[0]][oldPos[1]].walkable = True
                    occupiedCellGrid[oldPos[0]][oldPos[1]] = 0
                    b.currentMovements.append(move)
                else:
                    conflit +=1
                    # # Gere le conflit
                    # b.currentMovements.append("W")
                    # b.nextMoves.insert(0,move)
    print(conflit)


    # ###########################################

    # print("Grille : 0=vide et 1=point de montage")
    # print(pointsGrid)

    
    # for b in bras:
    #     pathfinding.CompleteArmTask(b)

    ####################
    # Partie de Lucas #
    ####################
    
    CreateFile(bras)
