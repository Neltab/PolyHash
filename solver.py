#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import math

from utils import Arm
from utils.group import groupBy
from utils.pathfinding import settings as S
from utils.pathfinding.Grid import GenerateNodeGrid, apply_points_to_grid

if __name__ == "__main__":

    # bras = groupBy.rendement(LTASK, LPOINTDEMONT, BRAS, NBETAPES)
    bras = groupBy.rendement(LTASK, LPOINTDEMONT, 1, NBETAPES)

    #génération de la grille remplie de zéros
    S.grid = [[0 for j in range (S.columns)] for i in range (S.lines)]

    points = []
    for pm in LPOINTDEMONT:
        S.grid[pm[0]][pm[1]] = 1

    pointsGrid = apply_points_to_grid(S.grid, points)  # c'est la grille qui contient les positions de collisions
    S.nodeGrid = GenerateNodeGrid(pointsGrid)

    for b in bras:
        mc.moveToFirstTask(b)
        mc.createMoves(b)

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
                if b.taches == []:
                    return True
                b.taskDone.append(b.taches.pop(0))
                # On signale qu'on a finit la tache

                b.isDoingTask = False

            else:
                b.isDoingTask = True

            # Ajouter les prochains mouvements (ceux de la tache ou pour aller à la prochaine) à b.nextMoves
            if b.movements == []:
                return True
            b.nextMoves = b.movements.pop(0)
            checkForNextMove(b)
        return False

    for t in range(NBETAPES):
        for i in range(len(bras)):
            b = bras[i]
            
            done = checkForNextMove(b)

            if not done:
                move = b.nextMoves.pop(0)
                newPos = get_pos_from_dir(move, b.occupiedCell[-1])

                if occupiedCellGrid[newPos[0]][newPos[1]] == 0:
                    b.occupiedCell.append(newPos)
                    S.nodeGrid[newPos[0]][newPos[1]].walkable = False
                    occupiedCellGrid[newPos[0]][newPos[1]] = -i - 1 
                    b.currentMovements.append(move)
                elif occupiedCellGrid[newPos[0]][newPos[1]] == -i - 1:
                    oldPos = b.occupiedCell.pop()
                    S.nodeGrid[oldPos[0]][oldPos[1]].walkable = True
                    occupiedCellGrid[oldPos[0]][oldPos[1]] = 0
                    b.currentMovements.append(move)
                else:
                    # Gere le conflit 
                    b.currentMovements.append("W")
                    b.nextMoves.insert(0,move)

    # Du fait de notre gestion de conflits inéxistante, on retire les bras
    # n'ayant pas pu effectuer leurs taches
    for i in range(len(bras)):
        if bras[i].taskDone == []:
            del bras[i]
    
    CreateFile(bras)
