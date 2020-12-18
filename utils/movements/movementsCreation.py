from ..group.Arm import Arm
from ..pathfinding import settings as S, pathfinding
from ..input.Tache import Tache
from typing import List, NewType

Coordinates = List[int]

def moveToFirstTask(bras: Arm):
    """Initialise les mouvements entre le point de montage et la premiere tache

    :param bras : Bras à initialiser
    """
    bras.occupiedCell.append(bras.pm)
    bras.movements.append(pathfinding.FindPath(bras.pm, bras.taches[0].coordtask[0], bras))

def createMoves(bras: Arm):
    """Ajoute les mouvements que le bras devras faire pour résoudre les taches

    La méthode employée ici est très basique: pour chaque nouveau déplacement,
    on regarde si un point du bras est plus proche que l'extrémité\n
    Si c'est le cas on fait se rétracter le bras et on part de ce point\n
    Sinon le bras va directement au point suivant\n

    :param bras : Bras pour lequel on va déterminer ses déplacements
    """

    moveToFirstTask(bras)

    # On va déterminer les mouvements initiaux du bras (sans gestion des conflits)
    # pour toutes les taches du bras, même si elles ne pourront pas forcément être
    # effectuées par la suite
    for t in range(len(bras.taches)):
        tache = bras.taches[t]
        firstCell = tache.coordtask[0]

        # Notre premiere condition pour déterminer les mouvements est le nombre
        # de points à parcourir pour effectuer la tache
        if len(tache.coordtask) > 1:
            moves = inTaskMovements(bras, tache)

            idx = indexCellInArm(firstCell, bras)

            if idx != None:
                moves += retracePath(idx, bras)
                movesToNextTask = betweenTasksMovements(bras, t, idx)
            else:
                movesToNextTask = betweenTasksMovements(bras, t)

            bras.movements.append(moves)
            bras.movements.append(movesToNextTask)

        # Si la tache contient 1 seule case
        elif t+1 < len(bras.taches):
            bras.movements.append([]) #Pas de mouvements à faire pour la tache

            # On cherche si un point déjà occupé par le bras est plus proche de la prochaine
            # case afin de minimiser le nombre de cases occupées par le bras.
            # Si c'est le cas, on se rétracte avant de se déplacer jusqu'à la prochaine case
            # Sinon on se déplace directement
            closer = findCloserCell(bras.taches[t+1].coordtask[0], dist(bras.occupiedCell[-1], bras.taches[t+1].coordtask[0]), bras)
            if closer != None:
                movesToNextTask = retracePath(closer, bras)
                if bras.occupiedCell[closer] != bras.taches[t+1].coordtask[0]:
                    movesToNextTask += pathfinding.FindPath(bras.occupiedCell[closer], bras.taches[t+1].coordtask[0], bras)
                bras.movements.append(movesToNextTask)
            else:
                movesToNextTask = pathfinding.FindPath(bras.occupiedCell[-1], bras.taches[t+1].coordtask[0], bras)
                if movesToNextTask == None:
                    bras.movements.append([]) #Pas de mouvements pour aller à la tache suivante
                else:
                    bras.movements.append(movesToNextTask)


def inTaskMovements(bras: Arm, tache: Tache) -> List[str]:
    """Cherche les déplacements à effectuer pour se déplacer entre les cases de la tache

    :param bras: Bras effectuant la tache
    :param tache: Tache en cours
    :return : Liste des mouvements à effectuer
    """

    # On inialise les mouvements en effectuant le déplacements entre
    # les deux premieres cases de la tache
    moves = pathfinding.FindPath(tache.coordtask[0], tache.coordtask[1], bras)

    if moves == None:
        moves = []
    
    # On détermine les déplacements pour le reste des cases à parcourir
    for i in range(1,len(tache.coordtask)-1):
        currentPos = tache.coordtask[i]
        nextPos = tache.coordtask[i+1]

        # On cherche si un point déjà occupé par le bras est plus proche de la prochaine
        # case afin de minimiser le nombre de cases occupées par le bras.
        # Si c'est le cas, on se rétracte avant de se déplacer jusqu'à la prochaine case
        # Sinon on se déplace directement
        closer = findCloserCell(nextPos, dist(currentPos, nextPos), bras)
        if closer != None:
            moves += retracePath(closer, bras)

            # Avant de se déplacer, on vérifie tout de même que la prochaine case n'était pas
            # celle sur laquelle on vient de se rétracter
            if nextPos != bras.occupiedCell[closer]:
                moves += pathfinding.FindPath(bras.occupiedCell[closer], nextPos, bras)

        else:
            moves += pathfinding.FindPath(currentPos, nextPos, bras)

    return moves


def betweenTasksMovements(bras: Arm, t: int, firstCellIdx: int = -1) -> List[str]:
    """Cherche les déplacements à effectuer pour se déplacer entre deux taches

    :param bras: Bras effectuant la tache
    :param t: Indice de la tache en cours dans la liste des taches du bras
    :param firstCellIdx: Indice de la premiere case de la tache en cours dans la liste des cases occupées 
    :return : Liste des mouvements à effectuer
    """

    movesToNextTask = []

    # On regarde s'il existe une prochaine tache
    if t + 1 < len(bras.taches):
        closer = findCloserCell(bras.taches[t+1].coordtask[0], dist(bras.occupiedCell[firstCellIdx], bras.taches[t+1].coordtask[0]), bras)

        # Si un point déjà occupé par le bras est plus proche de la premiere case
        # de la prochaine tache que l'extrémité du bras, on rétracte le bras
        # puis on se déplace jusqu'à la prochaine tache
        # Sinon on se déplace directement
        if closer != None:
            movesToNextTask = retracePath(closer, bras)
            if bras.occupiedCell[closer] != bras.taches[t+1].coordtask[0]:
                movesToNextTask += pathfinding.FindPath(bras.occupiedCell[closer], bras.taches[t+1].coordtask[0], bras)
        else:
            movesToNextTask = pathfinding.FindPath(bras.occupiedCell[firstCellIdx], bras.taches[t+1].coordtask[0], bras)
    
    return movesToNextTask


def retracePath(index: int, b: Arm) -> List[str]:
    """Renvoie la suite de mouvements pour se rétracter jusqu'à une certaine case

    :param index : Indice de la case jusqu'à laquelle le bras doit se rétracter
    :param b: Bras devant se rétracter
    :return : Liste des mouvements à effectuer
    """
    moves = []
    currentPos = b.occupiedCell.pop()
    for _ in range(len(b.occupiedCell) - index):
        nextPos = b.occupiedCell.pop()

        # La ligne suivante est désactivée car il n'y pas de gestion de conflits implémentée
        # S.nodeGrid[currentPos[0]][currentPos[1]].walkable = True
        
        if currentPos[1] > nextPos[1]: #nextPos au dessous de currentPos
            moves.append("D")
        elif currentPos[1] < nextPos[1]:
            moves.append("U")
        elif currentPos[0] > nextPos[0]: #nextPos à gauche de currentPos
            moves.append("L")
        elif currentPos[0] < nextPos[0]:
            moves.append("R")
        currentPos = nextPos
    b.occupiedCell.append(currentPos) #On remet la derniere case enlevée sinon elle disparait

    # La ligne suivante est désactivée car il n'y pas de gestion de conflits implémentée
    # S.nodeGrid[currentPos[0]][currentPos[1]].walkable = False

    return moves

def findCloserCell(cell: Coordinates, distMin: int, b: Arm) -> int:
    """Cherche la case occupée par le bras la plus proche de la case d'arrivée

    :param cell : Case que l'on cherche à atteindre
    :param distMin: Distance entre la case à atteindre et l'extrémité du bras
    :param b: Bras effectuer la tache
    :return : Indice de la case la plus proche (None si aucune n'est plus proche)
    """
    minDist = distMin + 1 # + 1 pour faire comme un "<=" mais uniquement pour la valeur en entrée
    currentIndex = None
    for idx in range(len(b.occupiedCell[:-1])):
        newDist = dist(b.occupiedCell[idx], cell)
        if newDist < minDist:
            minDist = newDist
            currentIndex = idx
    return currentIndex

def dist(x: Coordinates, y: Coordinates) -> int:
    """Calcule la distance entre deux points

    :param x : Coordonnées du premier point
    :param y: Coordonnées du deuxieme point

    :return : Distance entre les deux points
    """

    return abs(x[0]-y[0])+ abs(x[1]-y[1])

def indexCellInArm(cell: Coordinates, b: Arm) -> int:
    """Cherche l'indice de la premiere case d'une tache dans la liste des cases occupées par le bras

    :param cell: Coordonnées de la case
    :param b: Bras effectuant la tache

    :return : Indice, s'il existe, de la case dans la liste des cases occupées
    """

    for i in range(len(b.occupiedCell)):
        if b.occupiedCell[i] == cell:
            return i
    return None